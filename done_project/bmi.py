def bmi():
    weight=float(input("What is your weight in kg?"))
    height=float(input("What is your height in meters?"))

    bmi=weight/height**2

    print("Your bmi is " +str(bmi))

bmi()
