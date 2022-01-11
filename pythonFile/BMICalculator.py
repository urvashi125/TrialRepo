height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg:"))

bmi = (weight / (height * height))
if bmi < 18.5:
    print(f"under {bmi} they are underweight")
elif bmi < 25:
    print("Over 18.5 but below 25 they have a normal weight")
elif bmi < 30:
    print("Over 25 but below 30 they are overweight")
elif bmi < 35:
    print("Over 30 but below 35 they are obese")
else:
    print("Above 35 they are clinically prone")