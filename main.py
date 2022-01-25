
print("What is an average age of your family members?")
age = input("Write down all ages.\nUse a space to spearate ages, and give an integer numbers.: ").split()

for n in range(0, len(age)):
  age[n] = int(age[n])

total_age = sum(age)
amount_of_members = len(age)

average = round(total_age/amount_of_members)
print(f"The average age in your family is {average} years, counting {amount_of_members} mentioned members.")


