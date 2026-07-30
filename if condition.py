height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)

print("BMI =", round(bmi, 2))

if bmi >= 30:
    print("Obesity")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal")
else:
    print("Underweight")
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a city name: ")

if city in australia:
    print(city, "is in Australia")
elif city in uae:
    print(city, "is in UAE")
elif city in india:
    print(city, "is in India")
else:
    print("City not found")
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city1 = input("Enter first city: ")
city2 = input("Enter second city: ")

if city1 in australia and city2 in australia:
    print("Both cities belong to Australia")
elif city1 in uae and city2 in uae:
    print("Both cities belong to UAE")
elif city1 in india and city2 in india:
    print("Both cities belong to India")
else:
    print("They do not belong to the same country")
