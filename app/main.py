from app.commission_cal import calculate_commission, validate_category


def main():
    category = input("Enter category: ")

    try:
        category = validate_category(category)
    except ValueError as error:
        print(error)
        return

    try:
        weight_kg = float(input("Enter weight: "))
    except ValueError:
        print("Enter numerical value")
        return

    try:
        commission = calculate_commission(category, weight_kg)
        print(commission)
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
    