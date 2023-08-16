try:
    num1 = int(input('Enter a number'))
    num2 = int(input('enter a number'))
    if num1/num2 and num2 == 0:
        pass
except ZeroDivisionError:
    print('You are trying to divide a number by 0')
else:
    print('num1/num2=', num1/num2)