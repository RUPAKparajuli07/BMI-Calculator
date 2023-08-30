def calculate_bmi(w, h):
    return w / (h ** 2)

def interpret_bmi(bmi):
    """ 
    provide an interpretation 
    based on common BMI categories. 
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Normal weight"
    elif bmi <=30:
        return "Overweight"
    elif bmi >= 35 and bmi <= 40:
        return "Obese"
    
    return "سير اتعالج"



weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
interpretation = interpret_bmi(bmi)

print(f"Your BMI is: {bmi:.2f}")
print(f"Interpretation: {interpretation}")