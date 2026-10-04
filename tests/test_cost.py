from src.cost import ModelPrice, request_cost

def test_cost_calculation():
    model = ModelPrice("test", 2, 8)
    assert request_cost(model, 1_000_000, 1_000_000) == 10
