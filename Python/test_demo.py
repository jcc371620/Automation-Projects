def add(a, b):
    return a + b

def test_add_success():
    # 这里的 assert 就是断言，判断结果是否符合预期
    assert add(1, 2) == 3

def test_add_fail():
    # 故意写错，看看报错
    assert add(1, 2) == 5