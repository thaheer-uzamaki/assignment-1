num1=float(input("Enter num1 value: - "))
num2=float(input("Enter num1 value: - "))
op=input('Enter an operand from  +, -, *, /, %, **, //  :  ')
if op=='+':
    res=num1+num2
elif op=='-':
    res=abs(num1-num2)
elif op=='*':
    res=num1*num2
elif op=='/':
     print("Enter 1 for making num1 as the divisor or\nEnter 2 to make num2 as divisor")
     choice=int(input())
     if choice==1:
         res=num2/num1
     elif choice==2:
         res=num1/num2
     else:
         print("Wrong input")
elif op=='%':
     print("Enter 1 for making num1 as the divisor or\nEnter 2 to make num2 as divisor")
     choice=int(input())
     if choice==1:
         res=num2%num1
     elif choice==2:
         res=num1%num2
     else:
         print("Wrong input")
elif op=='**':
    print("Enter 1 for making num1 as the base or\nEnter 2 to make num2 as base")
    choice=int(input())
    if choice==1:
        res=pow(num1,num2)
    elif choice==2:
        res=pow(num2,num1)
    else:
        print("Wrong input")
elif op=='//':
    print("Enter 1 for making num1 as the divisor or\nEnter 2 to make num2 as divisor")
    choice=int(input())
    if choice==1:
       res=num2//num1
    elif choice==2:
        res=num1//num2
    else:
        print("Wrong input")

print("Result of your operation is: - {}".format(res))

     
    
