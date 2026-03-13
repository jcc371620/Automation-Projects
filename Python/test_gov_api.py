import requests

def test_federal_register_clippings():
    """
    业务场景：监控政府剪报 API 是否正常运行
    """
    url = "https://www.federalregister.gov/api/v1/clippings"
    
    # 1. 发送请求
    response = requests.get(url)
    
    # 2. 检查状态码 (API 是否活着)
    assert response.status_code == 200, f"API 挂了！状态码是: {response.status_code}"
    
    # 3. 检查返回内容 (数据管道是否有数据流出)
    data = response.json()
    assert len(data) > 0, "警告：API 返回了空列表，可能后台数据同步断了！"
    
    # 4. 检查具体字段 (业务逻辑是否正确)
    first_item = data[0]
    assert "title" in first_item, "错误：数据结构变了，找不到 title 字段"
    
    print(f"\n最新剪报标题: {first_item['title']}")