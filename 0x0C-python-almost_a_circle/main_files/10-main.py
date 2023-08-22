from models.square import Square

if __name__ == "__main__":
    # Create a Square instance
    s1 = Square(5)
    print(s1)        # Output: [Square] (1) 0/0 - 5
    print(s1.size)   # Output: 5

    # Update the size
    s1.size = 10
    print(s1)        # Output: [Square] (1) 0/0 - 10

    try:
        # Try setting size to a non-integer value
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
        # Output: [TypeError] width must be an integer
