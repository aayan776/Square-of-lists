try:
    list1 = []
    count = 0
    result = 0
    while True:
        def calculate(count):
            for i in list1[:]:
                result = list1[count] ** 2
                count += 1
                print(f"Result: {result}")
        list1.append(int(input("What do you want to square: ")))
        choice = input("Do you want to square something else (Y/N): ").lower()
        if choice == "y":
            continue
        elif choice == "n":
            calculate(count)
        else:
            print("Invalid input. Try again")
            continue
except ValueError:
    print("Value Error detected")