import pytest

# 1. 定义一个 Fixture
@pytest.fixture
def start_testing():
    print("\n--- [准备阶段]：正在连接测试环境... ---")
    yield  # 这是一道分界线：yield 之前是“测试前执行”，之后是“测试后执行”
    print("\n--- [清理阶段]：正在关闭测试连接，释放资源 ---")

# 2. 编写测试函数
# 注意：把 start_testing 作为一个参数传进函数名里
def test_age_check(start_testing):
    print("正在执行：年龄检查测试...")
    age = 20
    assert age >= 18

def test_another_one(start_testing):
    print("正在执行：另一个无关痛痒的测试...")
    assert 1 + 1 == 2