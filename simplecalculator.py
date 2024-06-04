print('This is a simple calculator.')
print('Select an oparetion')
print('1. Addtion')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
print('0. stop program')

operation=int(input('Enter your choice(1/2/3/4/0):  '))
number_1=float(input('First number:  '))
number_2=float(input('Second number:  '))


if operation==1:
    print(number_1+number_2)

elif operation==2:
    print(number_1-number_2)

elif operation==3:
    print(number_1*number_2)

elif operation==4:
    print(number_1/number_2)

elif operation==0:
    breakpoint

else:
    print('Rerun the operation')
