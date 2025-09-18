from shopping import final_price

def test_standard_purchase():
    """Tests a typical purchase with multiple items of each fruit."""
    assert final_price(4, 7, 2) == 38

def test_zero_quantity():
    """Tests the price when buying zero items."""
    assert final_price(0, 0, 0) == 0

def test_only_one_type_of_fruit():
    """Tests the price when only one type of fruit is purchased."""
    # 10 apples * $2 = 20
    assert final_price(10, 0, 0) == 20
    # 5 bananas * $4 = 20
    assert final_price(0, 5, 0) == 20

def test_single_item_each():
    """Tests the price when buying exactly one of each fruit."""
    assert final_price(1, 1, 1) == 7
