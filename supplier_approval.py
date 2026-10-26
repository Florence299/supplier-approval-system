contract_value = 7500
available_budget = 10000
supplier_rating = 92
supplier_certified = False
has_violations = False

contract_accepted = False

if available_budget >= contract_value and supplier_certified and not has_violations:
    print("Contract Approved")
    contract_accepted = True
    
elif available_budget >= contract_value and supplier_rating >= 90 and not has_violations:
    print("Conditional Approval")
    contract_accepted = True

else:
    print("Contract Rejected")

if contract_accepted:
    available_budget = available_budget - contract_value

if available_budget < 3000:
    print("Low Budget Alert")
