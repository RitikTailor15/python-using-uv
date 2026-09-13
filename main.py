def calculate_area(length, width):
    return length * width

def power(base, exponent = 2):
    return base ** exponent

def build_profile(name, age, city="Unknown"):
    return {
        "name":name, 
        "age":age, 
        "city":city
        }

def total(*args):
    sum = 0
    for num in args:
        sum += num
    return sum
   
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print('-'*15)

def get_length(str):
    return len(str)

def filter_and_square(numbers, threshold):
    return [num ** 2 for num in numbers if num > threshold]

def describe(name, *hobbies, city="Unknown"):
     print(f"{name} from {city} enjoys: {", ".join(hobbies)}")

def main():
    #  Functions Practice

    # area = calculate_area(10, 20)
    # print(area)

    # power_ans = power(10, 20)
    # print(power_ans)

    # print(build_profile('Ritik', 27, "indore"))
    # print(build_profile(age = 27,name='Ritik'))
    # print(build_profile(age = 27,name='Ritik',city="indore"))

    # print_details(name="Pooja", age= 28)
    # print_details(nam="Prateek",room=28)
    # print_details(name="Neelam", number= 28)
    # print_details(name="Ritik", score= 28)
    
    # words = ["hi", "hello", "hey", "greetings", "sup"]
    # result = [word for word in words if get_length(word) > 3]
    # print(result)

    # numbers = list(range(1, 21))
    # print(f"number : {numbers}")
    # final_list = [num ** 2 for num in numbers if num % 2 == 0]
    # print(final_list)

    # words = ["hi", "hello", "hey", "greetings", "sup"]
    # result = {len(word): word for word in words if len(word) > 2}
    # print(result)


    # describe("Ritik","reading", 'Coding', "Gaming", city="Indore" )
    # describe("Ritik", "Nothing in particular", city="Indore" )

    # sentences = ["the quick brown fox", "python is fun", "keep learning"]

    # flat_list = [word for sentence in sentences for word in sentence.split(" ") if len(word) > 3]
    # print(flat_list)

    people = [{"name": "Amit", "age": 25}, {"name": "Priya", "age": 30}, {"name": "Ritik", "age": 26}]

    # Sort by age (youngest first)
    sorted_by_age = sorted(people, key=lambda person: person["age"])
    print("Sorted by age (youngest first):")
    print(sorted_by_age)
    print()
    
    # Sort by name (alphabetically)
    sorted_by_name = sorted(people, key=lambda person: person["name"])
    print("Sorted by name (alphabetically):")
    print(sorted_by_name)



if __name__ == "__main__":
    main()