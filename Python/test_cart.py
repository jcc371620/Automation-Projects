from shopping_cart import calculate_total

def test_discount_logic():
    # 场景：买了 2 件 60 元的东西，总价 120
    # 预期：120 满百了，应该减 20，最后得 100 元
    result = calculate_total(60, 2)
    
    print(f"\n[测试运行] 实际计算结果是: {result}")
    
    # 你的自动化断言：必须等于 100 才是对的
    assert result == 100