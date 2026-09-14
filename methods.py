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
