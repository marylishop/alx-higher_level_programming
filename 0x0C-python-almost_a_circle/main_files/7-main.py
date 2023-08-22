from models.rectangle import Rectangle

if __name__ == "__main__":
    # Create a Rectangle instance
    r1 = Rectangle(10, 10, 10, 10)
    print(r1)  # Output: [Rectangle] (1) 10/10 - 10/10

    # Update only the ID
    r1.update(89)
    print(r1)  # Output: [Rectangle] (89) 10/10 - 10/10

    # Update the ID and width
    r1.update(89, 2)
    print(r1)  # Output: [Rectangle] (89) 10/10 - 2/10

    # Update the ID, width, and height
    r1.update(89, 2, 3)
    print(r1)  # Output: [Rectangle] (89) 10/10 - 2/3

    # Update the ID, width, height, x-coordinate
    r1.update(89, 2, 3, 4)
    print(r1)  # Output: [Rectangle] (89) 4/10 - 2/3

    # Update all attributes
    r1.update(89, 2, 3, 4, 5)
    print(r1)  # Output: [Rectangle] (89) 4/5 - 2/3
