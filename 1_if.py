 #Categories of BMI
# BMI >= 30 - "Obesity"
# 25 <= BMI => 29 - "overweight"
# 18.5 <= BMI =< 25 - "Normal"
# BMI < 18.5 - "underweight"

Weight = float(input("Enter your weight in kg: "))
Height = float(input("Enter your height in meters"))

#formula to find BMI = weight/(height)2
Your_BMI = Weight/Height**2 

# displaying result
print(f"your BMI according to your given details is{Your_BMI: .2f} kg per meter square")

#using if-else-elif to decide the category of BMI
if Your_BMI >= 30:
    print("You are in the category of Obesity")
elif 25 <= Your_BMI <= 29:
    print("You are in the category of Overweight")
elif 18.5 <= Your_BMI < 25:
    print("You are in the category of Normal")
else:  # bmi < 18.5
    print("You are in the category of Underweight")