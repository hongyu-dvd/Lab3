import price_info as price

def test_total_cost_shopping():
    cost = price.total_cost_shopping()
    assert cost == 46.75

def test_cost_of_fruits():
    cost = price.cost_of_fruits('apple', 10)
    assert cost == 12.0 
