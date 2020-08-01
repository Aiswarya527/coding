print("BMI Caluculator\n")
name = input("Enter your Name: ")
weight = float(input("Enter your Weight: "))
height = float(input("Enter your Height in meters: "))
bmi = weight / (height ** 2)
if bmi <25:
    print(f"{name} is underweight by {bmi} BMI")
else:
        print(f"{name} is overweight by {bmi} BMI")
