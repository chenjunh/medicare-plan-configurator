import json
def load_plan(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
    
if __name__ == "__main__":
    plan = load_plan("plan_configs/sample_plan_A.json")
    print("Loaded Plan Name:", plan["plan_name"])