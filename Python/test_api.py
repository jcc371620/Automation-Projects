import pytest
import requests

# 1. 定义我们要测试的网址
@pytest.mark.parametrize("url", [
    "https://www.baidu.com",
    "https://www.bing.com",
    "https://www.google.com" # 可能会失败，取决于你的网络
])
def test_website_status(url):
    # 模拟发送请求
    response = requests.get(url, timeout=5)
    
    # 打印一下状态码（200 代表访问成功）
    print(f"\n正在请求: {url}, 状态码为: {response.status_code}")
    
    # 断言：我们预期状态码必须是 200
    assert response.status_code == 200