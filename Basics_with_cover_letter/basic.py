name = input("Enter your name:")
address = input("Enter your address:")
age = int(input("Enter your age:"))
skill = input("Enter your skill:")
if age <= 0:
    print("Age must be greater than zero")
else:
    cover_letter = f"""{name}
{address}

Dear Hiring Manager,

I am writing to express my interest in the position at your esteemed company.
I am {age} years old and have developed strong skills in {skill}.
I am confident that my skills and experiences make me a suitable candidate for this position.
I look forward to the opportunity to discuss how I can contribute to your team.

Sincerely,
{name}"""
    a = str(age)
    print(cover_letter)
    print(f"Length of the cover letter: {len(cover_letter)}")
    print(f"Name (sliced): {name[:len(name)]}")
    print(f"Address (sliced): {address[:len(address)]}")
    print(f"Age (sliced): {a[:len(a)]}")
    print(f"Skill (sliced): {skill[:len(skill)]}")
