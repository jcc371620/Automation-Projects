# 业务逻辑：满 100 减 20
def calculate_total(price, count):
    total = price * count
    if total >= 100:
        # 程序员把减 20 写成了减 50
        return total - 50 
    return total