# 1. 这是我们要测试的“业务代码”（实际工作中可能是你的APP或网页功能）
def check_age(age):
    if age >= 18:
        return "成年"
    else:
        return "未成年"

# 2. 这是测试用例：测试成年情况
def test_is_adult():
    result = check_age(20)
    assert result == "成年"  # 断言：我们预期 20 岁应该是“成年”

# 3. 这是测试用例：测试未成年情况
def test_is_child():
    result = check_age(10)
    assert result == "未成年" # 断言：我们预期 10 岁应该是“未成年”

# 4. 这是一个故意写错的用例，用来看看报错长什么样
def test_error_example():
    assert check_age(18) == "未成年"