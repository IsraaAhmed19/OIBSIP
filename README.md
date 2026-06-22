# Oasis Infobyte Python Development Internship (OIBSIP)

Welcome to my official repository for the **Oasis Infobyte** Python Development Internship. This repository serves as a centralized hub containing all my completed tasks, structured and documented according to the highest industry standards and evaluation criteria.

---

## 🟢 Task 1: BMI Calculator
An interactive and robust command-line application built in Python that calculates the Body Mass Index (BMI) based on user weight and height. It provides accurate weight categorization according to global health standards and displays personalized health tips.

### 🎯 Key Features & Code Quality
- **Robust Input Validation:** Utilizes `while True` loops paired with `try-except` blocks to completely prevent application crashes from invalid inputs (like text strings) or illogical values (negative numbers/zeros).
- **Dynamic Category Mapping:** Automatically evaluates the BMI score against 4 distinct health tiers.
- **Personalized Health Insights:** Implements an intelligent dictionary-based mapping system (`tips`) to provide actionable health advice depending on the user's results.

### 🏗️ Code Architecture & Functions
- `get_valid_input(prompt)`: The core validation engine that ensures input weight/height are strictly positive numbers.
- `Get_User_Input()`: Handles the user interaction sequence for entering body metrics safely.
- `Calculate_BMI(height, weight)`: Computes the precise BMI score using the standard formula: $Weight / Height^2$.
- `Get_Category(bmi)`: Categorizes the score into *Underweight, Normal weight, Overweight, or Obese*.
- `Display_Result(bmi, category)`: Formats the final output cleanly, showing the BMI rounded to 2 decimal places alongside its corresponding advice.

---

## 🔵 Task 2: Random Password Generator
A highly secure, command-line utility designed to generate cryptographically strong, customizable passwords based on specific user-defined preferences (length and character types).

### 🎯 Key Features & Code Quality
- **Cryptographic Security:** Built using Python's native `secrets` module instead of the standard `random` module, ensuring that generated passwords are mathematically safe against predictability and brute-force attacks.
- **Customizable Constraints:** Gives the user full control over including lowercase letters, uppercase letters, digits, and special symbols.
- **Built-in Strength Evaluator:** Automatically analyzes the complexity and character diversity of the final password to rate its strength (Weak, Medium, Strong).

### 🏗️ Code Architecture & Functions
- `get_user_input()`: Collects and validates the password configurations, enforcing a secure minimum length of 8 characters.
- `generate_password()`: Dynamically pools character sets and builds the output efficiently using `''.join()`.
- `check_strength()`: Evaluates character distribution and complexity rules to assign a strength tier.
- `display_password()`: Neatly prints the secure password and its evaluation metrics to the console.

---

## 🛠️ Tech Stack & Requirements
- **Language:** Python 3.x
- **Standard Modules Used:** `secrets`, `string`

---

## ⚙️ How to Run the Projects

1. **Clone the repository:**
   ```bash git clone [https://github.com/IsraaAhmed19/OIBSIP]
