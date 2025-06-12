def validate_plan(plan_data):
    errors=[]
    
    # Rule 1: Plan ID must start with 'H' or 'R'
    if not plan_data["plan_id"].startswith(("H","R")):
        errors.append("Plan ID must start with 'H' or 'R'")
        
    # Rule 2: Must contain converage fields
    required_fields=["dental","vision","drug_tier"]
    for field in required_fields:
        if field not in plan_data.get("coverage",{}):
            errors.append(f"Missing coverage field: {field}")
    
    # Rule 3: CMS code must exist for every coverage item
    for key, value in plan_data.get("coverage", {}).items():
        if isinstance(value, bool) and key not in plan_data.get("CMS_codes", {}):
            errors.append(f"Missing CMS code for coverage item: {key}")
    
    valid_tiers = ["Tier 1","Tier 2","Tier 3","Tier 4", "Specialty Tier"]
    drug_tier = plan_data.get("coverage",{}).get("drug_tier")
    if drug_tier and drug_tier not in valid_tiers:
        errors.append(f"Invalid drug tier: {drug_tier}. Must be one of {valid_tiers}")
    return errors