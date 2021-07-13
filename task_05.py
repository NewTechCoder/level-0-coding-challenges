def triangle_area(side_a, side_b, side_c):
    semiparameter = 1 / 2 * (side_a + side_b + side_c)
    area = (semiparameter * (semiparameter - side_a) * (semiparameter - side_b)
            * (semiparameter - side_c)) ** 0.5
    return area

if __name__ == "__main__":
    print(triangle_area(4, 5, 3))
