# Get weight in kg from user
weight = float(input("Enter your weight in kg: "))

# Get height in meters from user
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Determine BMI category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obesity"

# Output the BMI category
print("Here is Your BMI category:", category)
