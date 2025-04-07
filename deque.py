from collections import deque

def parse_input(user_input):
    params = user_input.strip().split()
    if not params:
        print("Should not be empty.")
        return None
    if len(params) != 1:
        print("Should be one word.")
        return None
    return params[0].lower()

def is_palindrome(string):
    string_deque = deque()
    words_count = 0
    while words_count != 2:
        for char in string:
            string_deque.append(char)
        words_count += 1
    while len(string_deque) > 1:
        if string_deque.popleft() != string_deque.pop():
            print("Not a palindrome.")
            return
    print("The string is a palindrome.")

def main():
    print("Check if a string is a palindrome.")
    try:
        while True:
            user_input = input("Enter a string: ")
            string = parse_input(user_input)
            is_palindrome(string)
    except KeyboardInterrupt:
        print("\n User termination of the program.")

if __name__ == "__main__":
    main()