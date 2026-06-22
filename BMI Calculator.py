def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number!")
            else:
                return value
        except Exception:
            print("Invalid input. Please enter a number!")
            
def Get_User_Input():
    
    height = get_valid_input("Enter Height in meters (e.g. 1.75):\n")
    weight = get_valid_input("Enter Weight in kilograms\n")
    
    return height, weight

def Calculate_BMI(height , weight):
    
    bmi = weight / (height ** 2)
    
    return bmi

def Get_Category(bmi):
    
    if bmi < 18.5:
        category = "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        category = "Normal weight"
    elif bmi >= 25 and bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return category

def Display_Result(bmi, category):
    
    print("-" * 30)
    print(f"Your BMI is {bmi:.2f}")
    print(f"You are categorized as {category}")
    
    tips = {
        "Underweight": "You need to eat more! Focus on nutritious meals and consult a nutritionist.",
        "Normal weight": "Amazing! You're in great shape, keep up the healthy lifestyle!",
        "Overweight": "Time to take action! Regular exercise and a balanced diet will help you reach your goal.",
        "Obese": "Your health is important! Please consult a doctor for a personalized plan."
    }
    
    print(tips[category])
    
if __name__ == "__main__":
    
    print("Welcome to BMI Calculator")
    print("-" * 30)
    
    height, weight = Get_User_Input()
    bmi = Calculate_BMI(height, weight)
    category = Get_Category(bmi)
    Display_Result(bmi, category)