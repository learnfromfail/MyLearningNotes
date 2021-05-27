try:
    number = "1234" + 1 # 10/0
    print(number)
except ZeroDivisionError:
    print ("you get divide by 0")
except ValueError as err:
    print(err)
except: #every
    print("wrong")