role = input("Enter role: ")
age = int(input("Enter age: "))

is_eligible = (role.lower() == "student") and (age < 21)

print(f"eligible : {is_eligible}")