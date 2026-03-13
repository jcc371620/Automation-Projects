import sqlite3
import pytest

# --- 模拟业务系统 (被测对象) ---

def api_register_user(name):
    """模拟 API：用户注册并存入数据库"""
    conn = sqlite3.connect(":memory:") # 创建一个内存数据库
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()
    return conn, {"code": 200, "msg": "注册成功"}

def data_pipeline_sync(conn):
    """模拟数据管道：从用户表发现新用户，并在优惠券表发一张 50 元券"""
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE coupons (user_id INTEGER, amount INTEGER)")
    
    # 管道逻辑：读取所有用户，同步到优惠券表
    cursor.execute("SELECT id FROM users")
    users = cursor.fetchall()
    for user in users:
        cursor.execute("INSERT INTO coupons VALUES (?, ?)", (user[0], 50))
    conn.commit()

# --- 自动化测试用例 ---

def test_full_business_process():
    # 1. API 测试：调用注册接口
    connection, response = api_register_user("张三")
    assert response["code"] == 200
    print("\n[OK] API 注册接口响应正常")

    # 2. 数据管道测试：运行同步程序
    data_pipeline_sync(connection)
    
    # 3. 业务流程校验：去数据库查，优惠券到底发了吗？
    cursor = connection.cursor()
    cursor.execute("SELECT amount FROM coupons WHERE user_id = 1")
    result = cursor.fetchone()
    
    assert result is not None, "错误：管道没把数据搬过来！"
    assert result[0] == 50, f"错误：优惠券金额不对，应该是 50，实际是 {result[0]}"
    
    print("[OK] 业务全链路闭环：用户注册后，优惠券已自动到账")
    connection.close()