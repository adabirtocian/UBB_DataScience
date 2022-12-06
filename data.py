if __name__ == "__main__":
    x = [i for i in range(10)]
    y = [i for i in range(10, 30, 2)]

    s = 0
    for elem in x:
       s += elem
    print("Sum= ", s)

    c = 0
    for elem in y:
        c += elem+1
    print("Sum when increasing each number by one=", c)