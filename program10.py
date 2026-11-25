while True:
    print("\n========MENU========")
    print("1.Check even or odd")
    print("2.Largest of three numbers")
    print("3.Multiplication table")
    print("4.Prime numbers in a range")
    print("5.Exit")
    choice = int(input("Enter your choice(1-5): "))

    if choice == 1:
        n = int(input("Enter a number: "))
        if n % 2 == 0:
            print(n,"is even.")
        else:
            print(n," is odd.")
    elif choice == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        c = int(input("Enter third number: "))
        if a >= b and a >= c:
            largest = a
        elif b >= a and b >= c:
            largest = b
        else:
            largest = c
        print(largest,"is the largest number.")

    elif choice == 3:
        n = int(input("Enter a number: "))
        for i in range(1, 11):
            print(n, "x", i, "=", n*i)

    elif choice == 4:
        lower = int(input("Enter lower limit: "))
        upper = int(input("Enter upper limit: "))
        print("Prime numbers in the range", lower, "to", upper, "are:")
        for num in range(lower, upper + 1):
            if num < 2:
                continue
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num, end=" ") 
                print()  # for new line after printing all prime numbers
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")