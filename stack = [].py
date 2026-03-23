stack = []

while True:
    print("\n1.Push")
    print("2.Pop")
    print("3.Display")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        stack.append(value)

    elif choice == 2:
        if len(stack) == 0:
            print("Stack Underflow")
        else:
            print("Removed:", stack.pop())

    elif choice == 3:
        print("Stack:", stack)

    elif choice == 4:
        break