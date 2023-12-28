# 夏季月份
SUMMER_MONTHS = (6, 7, 8, 9)

# 用電度數分段
KWH_RANGES = (120, 330, 500, 700, 1000)

# 夏季和非夏季電費
SUMMER_FEES = (1.63, 2.38, 3.52, 4.80, 5.66, 6.41)
NON_SUMMER_FEES = (1.63, 2.10, 2.89, 3.94, 4.60, 5.03)

def get_input(prompt, input_type, validation_func=None):
    while True:
        try:
            user_input = input(prompt)
            if validation_func and not validation_func(user_input):
                raise ValueError("輸入無效！")
            return input_type(user_input)
        except ValueError as e:
            print(e)

def validate_positive_integer(value):
    return value.isdigit() and int(value) > 0

def validate_positive_number(value):
    try:
        num = float(value)
        return num > 0
    except ValueError:
        return False

def validate_month(value):
    try:
        month = int(value)
        return 1 <= month <= 12
    except ValueError:
        return False

def calculate_fee(kwh, fees):
    fee = 0
    for i in range(len(KWH_RANGES)):
        if i == 0:
            fee += min(kwh, KWH_RANGES[i]) * fees[i]
        else:
            fee += max(0, min(kwh, KWH_RANGES[i]) - KWH_RANGES[i - 1]) * fees[i]
    return fee

def calculate_remaining_usage(month, current_usage, budget):
    fees = SUMMER_FEES if month in SUMMER_MONTHS else NON_SUMMER_FEES
    fee = calculate_fee(current_usage, fees)

    remaining_usage = current_usage
    while fee < budget:
        remaining_usage += 0.01
        fee = calculate_fee(remaining_usage, fees)

    remaining_usage = max(0, remaining_usage - 0.01)
    return round(remaining_usage - current_usage, 2)

def main():
    month = get_input("月份：", int, validate_month)
    current_usage = get_input("目前使用度數：", float, validate_positive_number)
    budget = get_input("本月預算：", int, validate_positive_integer)

    remaining_usage = calculate_remaining_usage(month, current_usage, budget)
    print(f'電費 {round(calculate_fee(current_usage, SUMMER_FEES), 2)} 元 尚可用 {remaining_usage} 度')

if __name__ == "__main__":
    main()
