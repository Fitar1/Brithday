# Brithday
from datetime import datetime

def calculate_days_between_dates(birthday_str):
    # 将生日字符串转换为日期对象
    birthday = datetime.strptime(birthday_str, "%Y-%m-%d")

    # 获取当前日期
    current_date = datetime.now()

    # 计算天数差
    days_difference = (current_date - birthday).days

    return days_difference

# 输入生日日期（格式：YYYY-MM-DD）
birthday_input = input("请输入你的生日（格式：YYYY-MM-DD）：")

try:
    # 调用函数计算天数
    days_difference = calculate_days_between_dates(birthday_input)

    # 输出结果
    print(f"从你的生日到现在已经过了 {days_difference} 天！")

except ValueError:
    print("请输入正确的日期格式（YYYY-MM-DD）！")
    
