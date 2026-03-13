import pytest

# 1. 这是我们要测的业务逻辑
def add(a, b):
    return a + b

# 2. 这里的参数化就像是一个“循环注入机”
# "a, b, expected" 是变量名
# [ (1, 2, 3), (5, 5, 10), (10, -2, 8) ] 是我们要测试的三组数据
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),      # 第一组：1+2=3
    (5, 5, 10),     # 第二组：5+5=10
    (10, -2, 8),    # 第三组：10+(-2)=8
    (2, 2, 5),      # 第四组：故意写错一个，看看效果
])
def test_add_multi_times(a, b, expected):
    print(f"\n正在测试：{a} + {b} 是否等于 {expected}")
    assert add(a, b) == expected