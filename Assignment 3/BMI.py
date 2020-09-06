w=float(input("Weight in kg :"))
h=float(input("Height in meters :"))
BMI= w/(h*h)
if BMI < 18.5:
    print("Underweight")
elif BMI>=18.5 and BMI<=24.9:
    print("Normal")
elif BMI>=25.0 and BMI<=29.9:
    print("Overweight")
else:
    print("Obese")
