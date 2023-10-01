try:
    print("""
HELLO! PLEASE PICK ONE SHAPE.""")
    shapePick = str("""
         •          • • • • • •     • • • • • • • •         • •            • • • • • • •
       •   •        •         •     •             •      •       •        •           •
      •  A  •       •    B    •     •      C      •     •    D    •      •     E     •            
     •       •      •         •     •             •      •       •      •           •
    • • • • • •     • • • • • •     • • • • • • • •         • •        • • • • • • •
      
PICK ONE OPTION (A, B, C, D, E)
    """)
    print(shapePick)
    user_input = input(">> ").lower()

    while user_input != "exit":
        if user_input == "a":
            # Triangle
            operation = input("Enter 'Per' for perimeter or 'Area' for area: ").lower()
            base = float(input("Enter the base length: "))
            height = float(input("Enter the height length: "))
            if operation == 'area':
                result = 0.5 * base * height
            elif operation == 'per':
                side1 = float(input("Enter the length of side 1: "))
                side2 = float(input("Enter the length of side 2: "))
                side3 = float(input("Enter the length of side 3: "))
                result = side1 + side2 + side3
            else:
                print("Invalid operation input")

        elif user_input == "b":
            # Square
            operation = input("Enter 'Per' for perimeter or 'Area' for area: ").lower()
            side = float(input("Enter the side length: "))
            if operation == 'area':
                result = side * side
            elif operation == 'per':
                result = 4 * side
            else:
                print("Invalid operation input")

        elif user_input == "c":
            # Rectangle
            operation = input("Enter 'Per' for perimeter or 'Area' for area: ").lower()
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            if operation == 'area':
                result = length * width
            elif operation == 'per':
                result = 2 * (length + width)
            else:
                print("Invalid operation input")

        elif user_input == "d":
            # Circle
            operation = input("Enter 'Per' for perimeter or 'Area' for area: ").lower()
            radius = float(input("Enter the radius: "))
            if operation == 'area':
                result = 3.14 * radius**2
            elif operation == 'per':
                result = 2 * 3.14 * radius
            else:
                print("Invalid operation input")

        elif user_input == "e":
            # Parallelogram
            operation = input("Enter 'Per' for perimeter or 'Area' for area: ").lower()
            base = float(input("Enter the base length: "))
            side = float(input("Enter the side length: "))
            if operation == 'area':
                result = base * side
            elif operation == 'per':
                result = 2 * (base + side)
            else:
                print("Invalid operation input")

        else:
            print("Invalid shape input")

        print(f"Result: {result}")
        user_input = input("> ").lower()

except ValueError:
    print("ERROR 404")
