def calculator():
    print("Select an Operation - \n" \
            "1.Add\n"\
            "2.Subtract\n"\
            "3.Multiply\n"\
            "4.Divide\n")
    ans=int(input("What do you want(use numbers)?"))
    num1=int(input("First Number?"))
    num2=int(input("second Number?"))
    if ans==1:   
        print("Sum is: "+str(num1+num2))
    elif ans==2:
        print("Answer is: "+str(num1-num2))
    elif ans==3:
        print("Answer is: "+str(num1*num2))
    elif ans==4:
        print("Answer is: "+str(num1/num2))
    else:
        print(".... Nah....")
        print(ans)
        
calculator()