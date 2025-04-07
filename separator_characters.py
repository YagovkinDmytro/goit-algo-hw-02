def is_symmetric(expression):
    stack = []
    opening = "([{"
    closing = ")]}"
    matching = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return "Asymmetrical: extra closing bracket " + char
            if stack[-1] != matching[char]:
                return f"Asymmetrical: {stack[-1]} does not match {char}"
            stack.pop()
    
    if stack:
        return "Asymmetrical: brackets left opened " + "".join(stack)
    return "Symmetrically"

def main():
    print("Checking the symmetry of the brackets.\nPress Ctrl+C to exitу.")
    try:
        while True:
            expression = input("Enter the expression with brackets: ")
            result = is_symmetric(expression)
            print(result + "\n")
    except KeyboardInterrupt:
        print("\nThe program has been terminated by the user.")

if __name__ == "__main__":
    main()