def roi(benefit: float, total_cost: float) -> dict:
    net = benefit - total_cost
    return {"benefit": benefit, "cost": total_cost, "net_value": net,
            "roi_pct": round((net / total_cost) * 100, 2) if total_cost else None}
