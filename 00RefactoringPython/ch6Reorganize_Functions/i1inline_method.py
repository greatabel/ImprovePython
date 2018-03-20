def get_rating():
    return 2 if more_than_5_late_deliveries(10) else 1

def more_than_5_late_deliveries(number_of_late_deliveries):
    return number_of_late_deliveries > 5


print("inline method: 在函数调用点插入函数本体，然后移除函数。\
    间接性可能带来帮助，但非必要的间接性总是让人不舒服")

def get_rating():
    number_of_late_deliveries = 10
    return 2 if (number_of_late_deliveries > 5) else 1