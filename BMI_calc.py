# Software Testing and Quality Assurance - Assignment 3
# Name:     Karan Singh
# NetID:    kds662
# Purpose: new changes

def BMI_calc(weight_lb, feet, inches):

    weight_kg = convert_lb_to_kg(weight_lb)
    height_m = convert_feet_inch_to_m(feet, inches)
    BMI = (weight_kg / (height_m * height_m))

    return round(BMI, 1)

def BMI_calc_category(BMI):
    # [0, 18.5)
    if (BMI >= 0) and (BMI < 18.5):
        BMI_category = "Underweight"
    # [18.5, 24.9]
    elif (BMI >= 18.5) and (BMI <= 24.9):
        BMI_category = "Normal"
    # [25, 29.9]
    elif (BMI >= 25) and (BMI <= 29.9):
        BMI_category = "Overweight"
    # [30, infinity)
    elif BMI >= 30:
        BMI_category = "Obese"
    else:
        BMI_category = "Error"

    return BMI_category

def convert_lb_to_kg(weight_lb):
    weight_kg = weight_lb * 0.45
    return weight_kg

def convert_feet_inch_to_m(feet, inches):
    total_inches = (feet * 12) + inches
    height_m = total_inches * 0.025
    return height_m

def web_BMI_calc(weight_lb, height_ft, height_in):
    weight = int(weight_lb)
    feet = int(height_ft)
    inches = int(height_in)
    BMI = BMI_calc(weight, feet, inches)
    BMI_category = BMI_calc_category(BMI)
    return BMI, BMI_category

def main():
    print("Welcome to our BMI Calculator\n")
    while(1):
        weight_lb = int(input("Please enter your weight (in pounds): "))
        print("Please enter your height -")
        feet = int(input("(in feet): "))
        inches = int(input("(inches): "))
        BMI = BMI_calc(weight_lb, feet, inches)
        BMI_category = BMI_calc_category(BMI)
        print("Your BMI is: " + str(round(BMI, 2)))
        print("Your BMI category is: " + BMI_category)
        continue_loop = input("\nWould you like to continue (Y): ")
        if continue_loop != "Y":
            print("Thank you.")
            break

if __name__ == "__main__":
    main()
