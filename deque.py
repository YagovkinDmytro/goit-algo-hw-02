from collections import deque

def parse_input(user_input):
    params = user_input.split()
    if not params:
        return print("Should not be empty.")
    if len(params) != 1:
        return print("Should be one word.")
    string = params[0]
    string = string.strip().lower()
    return string

def is_palindrome():
    pass

def main():
    print("Check if a string is a palindrome.")
    try:
        while True:
            user_input = input("Enter a string: ")
            string = parse_input(user_input)
            print(string)
    except KeyboardInterrupt:
        print("\n User termination of the program.")

if __name__ == "__main__":
    main()