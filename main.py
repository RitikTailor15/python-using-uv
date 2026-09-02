# main.py

# "import" brings in an external library, similar to `import requests from 'requests'` in JS
import requests

# "def" defines a function — like `function fetchUser(userId) { ... }` in JS
# The `-> dict` part is optional and just documents what type the function returns
def fetch_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    # f"..." is an f-string — Python's version of a template literal (`...${x}...`)
    # The variable goes inside curly braces instead of ${}

    response = requests.get(url)
    # This makes an HTTP GET request, like `fetch(url)` or `axios.get(url)`

    return response.json()
    # .json() parses the response body as JSON, same idea as `response.json()` in fetch


# This is the "entry point" — the code that actually runs when you execute the file
def main():
    user = fetch_user(1)
    print("Name:", user["name"])
    print("Email:", user["email"])
    # print() is Python's console.log()
    # user["name"] accesses a dictionary key — like user.name or user["name"] in JS


# This line means: "only run main() if this file is being run directly"
# (not if some other file imports this one). You'll see this at the bottom of almost every Python script.
if __name__ == "__main__":
    main()