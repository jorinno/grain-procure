def commission_per_kg(rate):
    def agent_commission(weight_kg):
        return rate * weight_kg
    return agent_commission


commission_calculators = {
    "maize": commission_per_kg(100),
    "beans": commission_per_kg(150),
}


def validate_category(category):
    category = category.lower().strip()

    if category == "":
        raise ValueError("Please enter beans or maize")

    if category not in commission_calculators:
        raise ValueError("We only buy beans and maize at the moment")

    return category


def calculate_commission(category, weight_kg):
    category = validate_category(category)

    if weight_kg <= 0:
        raise ValueError("Weight must be greater than 0")

    return commission_calculators[category](weight_kg)