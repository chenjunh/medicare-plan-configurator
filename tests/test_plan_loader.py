from plan_loader import load_plan

def test_load_plan():
    plan = load_plan("plan_configs/sample_plan_A.json")
    assert plan["plan_id"] == "H1234-001"