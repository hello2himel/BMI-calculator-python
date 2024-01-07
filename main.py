print("Which unit do you use to measure your height?")
print("[1] Centimeters")
print("[2] Feet & Inches")
unit_h = int(input("Type the unit (1 or 2): "))

if unit_h == 1:
    h = float(input("Enter the height in cm: "))
else:
    def h_feet():
        print("Enter the height in feet & inches. Separate them with a comma.")
        print("Example: 5 feet 10 inches = 5,10")
        feet, inches = map(int, input("Please enter your height (feet,inches): ").split(','))
        return (feet * 12 + inches) * 2.54

    h = h_feet()

print("Which unit do you use to measure your weight?")
print("[1] Kilograms")
print("[2] Pounds")
unit_m = int(input("Type the unit (1 or 2): "))
if unit_m == 1:
    m = float(input("Enter the mass in KG: "))
else:
    m_pounds = float(input("Enter the mass in pounds: "))
    m = m_pounds / 2.205

bmi = m / (h / 100) ** 2

rounded_bmi = round(bmi, 2)

print(f"Your BMI is {rounded_bmi}")
if rounded_bmi < 18.5:
    print("You are underweight. Please consult a doctor.")
elif 18.5 <= rounded_bmi < 24.5:
    print("Your height and weight are normal. Keep it up!")
else:
    print("You are overweight. Please consult a doctor.")
