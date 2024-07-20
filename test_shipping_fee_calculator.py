import pytest
from shipping_fee_calculator import calculate_shipping_cost

def test_calculate_shipping_cost_edges():
    # nomx with values of y
    assert calculate_shipping_cost(5, "domestic") == 3.75
    assert calculate_shipping_cost(5, "international") == 5.0
    assert calculate_shipping_cost(5, "somewhere_else") == "Invalid destination"

    # edges of x with y=domestic
    assert calculate_shipping_cost(0, "domestic") == "Invalid weight"
    assert round(calculate_shipping_cost(0.1, "domestic"), 3) == 0.075
    assert calculate_shipping_cost(5, "domestic") == 3.75
    assert calculate_shipping_cost(9, "domestic") == 6.75
    assert calculate_shipping_cost(10, "domestic") == 7.5
    assert calculate_shipping_cost(10.1, "domestic") == 4.545
    assert calculate_shipping_cost(10.5, "domestic") == 4.725
    assert calculate_shipping_cost(15, "domestic") == 6.75
    assert calculate_shipping_cost(19, "domestic") == 8.55
    assert calculate_shipping_cost(20, "domestic") == 9.0
    assert calculate_shipping_cost(21, "domestic") == "Invalid weight"
    
    # edges of x with y=international
    assert calculate_shipping_cost(0, "international") == "Invalid weight"
    assert calculate_shipping_cost(0.1, "international") == 0.1
    assert calculate_shipping_cost(5, "international") == 5.0
    assert calculate_shipping_cost(9, "international") == 9.0
    assert calculate_shipping_cost(10, "international") == 10.0
    assert calculate_shipping_cost(10.1, "international") == 6.06
    assert calculate_shipping_cost(10.5, "international") == 6.3
    assert calculate_shipping_cost(15, "international") == 9.0
    assert calculate_shipping_cost(19, "international") == 11.4
    assert calculate_shipping_cost(20, "international") == 12.0
    assert calculate_shipping_cost(21, "international") == "Invalid weight"
    
def test_calculate_shipping_cost_decision():
    # decision table testing
    assert calculate_shipping_cost(0, "domestic") == "Invalid weight"
    assert calculate_shipping_cost(21, "domestic") == "Invalid weight"
    
    assert calculate_shipping_cost(5, "somewhere_else") == "Invalid destination"
    assert calculate_shipping_cost(5, "domestic") == 3.75
    assert calculate_shipping_cost(5, "international") == 5.0
    
    assert calculate_shipping_cost(15, "somewhere_else") == "Invalid destination"
    assert calculate_shipping_cost(15, "domestic") == 6.75
    assert calculate_shipping_cost(15, "international") == 9.0