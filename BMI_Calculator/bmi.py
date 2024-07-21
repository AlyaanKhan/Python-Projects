def bmi_calculator():
    weight = float(input("Enter your weight in kg (kilo-grams):"))
    height_cm = float(input("Enter your height in cm (centimeters):"))
    height_m = height_cm / 100 
    weight_pounds = weight * 2.20462
    height_inches = height_m * 39.3701
    bmi = weight_pounds / (height_inches ** 2) * 703
    print(f"Your BMI is: {bmi:.2f}")
    if bmi <= 18.4:
        print("Underweight")
        print("You need to gain weight.")
    elif 18.5 <= bmi <= 24.9:
        print("Normal")
        print("Doing Good.")
    elif 25.0 <= bmi <= 39.9:
        print("Overweight")
        print("You need to lose some fat!")
    else:
        print("Obese")
        print("Need to lose a lot of weight.")

bmi_calculator()
