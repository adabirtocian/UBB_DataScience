if __name__ == "__main__":
    x = int(input(""))
    if x > 10:
        print(x % 10)
    else:
        print(x / 2)


    # I added some code and my colleagues need to fetch it !
    while x > 2:
        x = x / 2
    print(x)