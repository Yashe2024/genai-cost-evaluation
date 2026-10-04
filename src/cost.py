from dataclasses import dataclass

@dataclass
class ModelPrice:
    name: str
    input_per_million: float
    output_per_million: float

def request_cost(model: ModelPrice, input_tokens: int, output_tokens: int) -> float:
    return round(
        input_tokens / 1_000_000 * model.input_per_million
        + output_tokens / 1_000_000 * model.output_per_million, 8
    )

def monthly_projection(model, input_tokens, output_tokens, requests):
    per_request = request_cost(model, input_tokens, output_tokens)
    return {"cost_per_request": per_request, "monthly_cost": round(per_request * requests, 2)}
