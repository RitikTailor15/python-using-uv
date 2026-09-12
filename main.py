
def main():
    # Type check
    # number_int = 900
    # print(type(number_int))
    # num_float = 4.5
    # print(type(num_float))
    # str_value = "Ritik"
    # print(type(str_value))
    # bool_value = True
    # print(type(bool_value))
    # none_value = None
    # print(type(none_value))

    # Guessing the output
    # values = [0, 1, "", "hello", None, [], [0], False, True, 0.0, "0"]

    # for v in values:
    #     if v:
    #         print(v, "→ truthy")
    #     else:
    #         print(v, "→ falsy")

    # Fixing the bug
    # cart = []

    # if cart:
    #     print("Cart has items")
    # else:
    #     print("Cart is empty")

    #  F string
    # age = 26
    # message = f"I am {age} years old"
    # print(message)

    # Reassignment
    # score = 10
    # score = "ten"
    # print(score)
    
    # sentence = "  Learning Python is fun  "
    # print(len(sentence.strip(" ").upper().split(" ")))

    # language = ["JS", "RUST", "NODE", "JAVA", "GO"]
    # print(f"First : {language[0]}")
    # print(f"last : {language[-1]}")
    # language.append("PYTHON")
    # print(language)
    # print(language[2:4])
    # print("PYTHON" in language)

    # me = {
    #     "name": "Ritik",
    #     "role": "frontend developer",
    #     "skills": ["React", "JavaScript", "Node.js"]
    # }

    # me['learning'] = "Python"
    # print(me)
    # print(me.get("salary", "Not defined!"))
    # me['skills'].append("FastAPI")
    # print(me)

    # profile = ("Ritik", "Vidisha", "Frontend Developer")
    # name, city, role = profile
    # print(name, city, role)
    # # profile[0] = 'X'
    # print(f"{name} lives in {city} with role {profile}")

    # skills_a = {"python", "react", "sql"}
    # skills_b = {"react", "docker", "python"}

    # print(skills_a & skills_b)
    # print(skills_a.intersection(skills_b))
    # print(skills_a - skills_b)
    # print(skills_a.difference(skills_b))
    # skills_a.add("fastapi")
    # print(skills_a)

    # users = [
    #     {"name": "Amit", "age": 25},
    #     {"name": "Priya", "age": 30},
    #     {"name": "Ritik", "age": 26},
    # ]

    # for user in users:
    #     print(user['name'])

    # Control flow Practice

    # 1. Grade Calculator
    # score = 82

    # if score >= 90:
    #     print("A")
    # elif score >= 75:
    #     print("B")
    # elif score >= 60:
    #     print("C")
    # else:
    #     print("D")

    # 2. FizzBuzz
    # for i in range(1,30):
    #     if i % 3 == 0 and i % 5 == 0:
    #         print('FizzBuzz')
    #     elif i % 3 == 0:
    #         print("Fizz")
    #     elif i % 5 == 0:
    #         print("Buzz")
    #     else:
    #         print(i)

    # 3. Sum and Average

    # numbers = [12, 45, 7, 89, 23, 56, 3]
    # sum  = 0
    # for num in numbers:
    #     sum += num
    # print(f"Total : {sum}, Average : {sum / len(numbers)}")

    # 4. Max in numbers

    # maxNum = numbers[0]
    # for num in numbers[1:]:
    #     if num > maxNum:
    #         maxNum = num

    # print(f"Maximum number in arr : {maxNum}")

    # 5. Enumerator Pratice
    # languages = ["Python", "JavaScript", "Go", "Rust"]
    # for idx, str in enumerate(languages):
    #     print(f"{idx + 1} : {str}")

    # 6. Dictionary loop
    # inventory = {"apples": 10, "bananas": 0, "mangoes": 5}
    # for (key, value) in inventory.items():
    #     if value > 0:
    #         print(f"{key} : in stock")
    #     else:
    #         print(f"{key} is out of stock")

    # 7. While loop function
    # count  = 10
    # while count >= 1:
    #     print(count)
    #     count -= 1

    # print("Liftoff!!")
    
    # 8. Break and continue
    
    # numbers = [3, 7, 2, 9, 4, 11, 6, 15, 1]

    # for num in numbers:
    #     if num > 5:
    #         continue
    #     elif num > 15:
    #         break
    #     else:
    #         print(num)

    # 9. Nested loops  = Multiplication Table

    # for i in range(1, 6):
    #     for j in range(1, 6):
    #         print(f"{i} x {j} = {i * j}")
    #     print("-"*15)

    users = [
        {"name": "Amit", "age": 25},
        {"name": "Priya", "age": 30},
        {"name": "Ritik", "age": 26},
    ]

    for user in users:
        if user['age'] > 25:
            print(f"{user['name']} is eligible for the program.")
        else:
            print(f"{user['name']} is not eligible for the program.")

if __name__ == "__main__":
    main()