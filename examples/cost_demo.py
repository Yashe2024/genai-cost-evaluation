from src.cost import ModelPrice, monthly_projection
from src.roi import roi

model = ModelPrice("Example-LLM", 2.50, 10.00)
projection = monthly_projection(model, 6000, 1200, 100000)
print(projection)
print(roi(25000, projection["monthly_cost"]))
