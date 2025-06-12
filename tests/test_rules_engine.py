from rules_engine import validate_plan
import json

def test_validate_plan():
    with open("plan_configs/sample_plan_A.json") as f:
        plan = json.load(f)
    
    errors=validate_plan(plan)
    assert errors == []