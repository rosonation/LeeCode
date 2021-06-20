print("please input 1-100 number.")
number = int(input())

if number % 3 == 0 and number % 5 == 0:
    print("麦叔")
elif number % 3 == 0 and number % 5 != 0:
    print("麦")
elif number % 5 == 0 and number % 3 != 0:
    print("叔")
else:
    print(number)
