


def commission_per_KG(rate):
    def agent_commission(weight_kg):
        return rate * weight_kg
    return agent_commission

commission_calculators = {
        "maize": commission_per_KG(100),
        "beans": commission_per_KG(150)
    }
        
category = input("Enter category: ").lower().strip()

if category == "":
    print("Please enter beans or maize")

elif category not in commission_calculators:
    print("we only buy beans and maize at the moment")
else:    
    try:
        weight_kg = float(input("Enter weight: "))
        if weight_kg <=0:
            print("Weight must be greater than 0")   


        else:
            commission = commission_calculators[category](weight_kg)
            print(commission)
        
    except ValueError:
         print("Enter numerical value")

