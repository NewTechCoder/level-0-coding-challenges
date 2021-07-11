def maximum(*arg):
    large_number = arg[0]
    for i in range(len(arg)):
        if large_number < arg[i]:
            large_number = arg[i]
    return large_number

if __name__ == "__main__":
    print(maximum(1, 22, 3, 2))
