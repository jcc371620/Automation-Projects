import pytest

@pytest.fixture
def login_user():
    print("\n[前置准备]：模拟用户登录，获取 Token")
    return "admin_token"

def test_delete_order(login_user):
    # 函数参数里写了 login_user，pytest 就会先运行上面的 fixture
    print(f"正在使用 {login_user} 删除订单...")
    assert True