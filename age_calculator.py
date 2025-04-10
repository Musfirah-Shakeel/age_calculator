from datetime import date

#Get birthdate input
birth_day = int(input("Enter your birth day (1-31): "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_year = int(input("Enter your birth year: "))

#Get today's date
today = date.today()

# Create birth date object
birth_date = date(birth_year, birth_month, birth_day)

#Calculate age
age = today.year - birth_date.year

#Check if birthday has not occurred yet this year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

#Display the result
print("You are", age, "years old.")
