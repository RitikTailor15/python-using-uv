
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

    users = [
        {"name": "Amit", "age": 25},
        {"name": "Priya", "age": 30},
        {"name": "Ritik", "age": 26},
    ]

    for user in users:
        print(user['name'])

if __name__ == "__main__":
    main()