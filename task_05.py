from math import sqrt

def triangle_area(side_a, side_b, side_c):
    semiparameter = 1 / 2 * (side_a + side_b + side_c)
    area = sqrt(semiparameter * (semiparameter - side_a) *
            (semiparameter - side_b) * (semiparameter - side_c))
    return area

if __name__ == "__main__":
    print(triangle_area(6, 6, 6))
