def ArmstrongNumber(num):
    result=0
    num=str(num)
    power = len(num)
    for i in num:
        result += (int(i)**power)
    return result
num = int(input('enter number : '))
print('Input : ',num)
print('Result : ',ArmstrongNumber(num))

if ArmstrongNumber(num) == num:
    print(num , ' is a Armstrong Number')
else:
    print(num , ' is not a Armstrong Number')
