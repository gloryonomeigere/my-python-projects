print("WELCOME TO ONOME'S FIRST PYTHON PROJECT!")

user_name = str(input("Enter your name: ")).capitalize()
print(f"Welcome {user_name}!")

year_of_birth = int(input("Enter your year of birth: "))
current_year = int(2025)
user_age = current_year - year_of_birth
print(f"If you are born in {year_of_birth} then you are", user_age)

if user_age >= 18:
    print("You are an adult!")
elif user_age >= 13:
    print("You are a teenager!")
else:
    print("You are a baby!")

hundredth_year = year_of_birth + 100
print(f"You'll be a hundred years old in {hundredth_year}!")