import pytest

# 定义一个名为 "db_conn" 的 Fixture（模拟连接数据库）
@pytest.fixture
def db_conn():
    print("\n[前置]：正在连接数据库...")
    yield "Success"
    print("\n[后置]：正在关闭数据库连接...")

# 情况 A：这个测试用例需要数据库，所以把 db_conn 写进括号
def test_user_login(db_conn):
    print(f"执行测试：正在验证登录功能，数据库状态：{db_conn}")
    assert True

# 情况 B：这个测试用例不需要数据库，括号留空或写别的
def test_simple_math():
    print("执行测试：我只是算个 1+1，不需要连接数据库")
    assert 1 + 1 == 2