list = (1, 2, 3)

def add(num):
    sum = num1 + num2
    print(sum)
    return sum

def is_even(num):
    if num % 2 == 0:
        print(True)
        return True
    else:
        print(False)
        return False

def calc_total(list):
    sum = 0
    for num in list:
        sum += num 
    return sum
print(is_even(7))
