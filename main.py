if __name__ == "__main__":
    x = int(input(""))
    if x > 10:
        print(x % 10)
    else:
        print(x / 2)

    for i in range(10):
        if i % 3 == 0:
            print(i, " divisible by 3")
