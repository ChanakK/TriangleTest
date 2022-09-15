import math


def get_x_axis(name):
    x = int(input(f"Enter X axis for {name}: "))
    return x


def get_y_axis(name):
    y = int(input(f"Enter Y axis for {name}: "))
    return y


def get_distance(x1, x2, y1, y2):
    value_of_x = (x2 - x1)

    value_of_y = (y2 - y1)

    square_of_x = value_of_x ** 2

    square_of_y = value_of_y ** 2

    sum_of_x_and_y = square_of_x + square_of_y

    distance_value = math.sqrt(sum_of_x_and_y)

    return distance_value


def length_logger(name, value):
    distance_value = value
    print()
    print(f"Length of {name} is: {distance_value}")


def check_triangle(AB, BC, AC):
    if AB == BC == AC:
        print()
        print('This is an "equilateral triangle"')
        
    else:
        print()
        print('This is not an "equilateral triangle"')
        

    if AB == BC or BC == AC or AC == AB:
        print()
        print('This is an "isosceles triangle"')
    else:
        print()
        print('This is not an "isosceles triangle"')


def distance_square(num):
    return num ** 2


def check_right_triangle(AB, BC, AC):
    a = round(distance_square(AB))
    b = round(distance_square(BC))
    c = round(distance_square(AC))

    if (a > 0 and b > 0 and c > 0) and (a == (b + c) or b == (a + c) or c == (a + b)):
        print()
        print('This is a "right angle triangle"')
    else:
        print()
        print('This is not a "right angle triangle"')


def perimeter_calculator(AB, BC, AC):
    return AB + BC + AC


def perimeter_logger(AB, BC, AC):
    perimeter = perimeter_calculator(AB, BC, AC)
    print()
    print(f"The perimeter of the triangle is: {perimeter}")


def get_even_numbers_till_perimeter(AB, BC, AC):
    limit = perimeter_calculator(AB, BC, AC)
    limit = int(limit)

    print()
    print(f"The even numbers from 0 to value of triangle perimeter are as follows: ")
    print()
    for x in range(0, limit + 1):
        if x % 2 == 0:
            print(x)


def main():
    x_axis_for_a = get_x_axis("A")
    y_axis_for_a = get_y_axis("A")

    x_axis_for_b = get_x_axis("B")
    y_axis_for_b = get_y_axis("B")

    x_axis_for_c = get_x_axis("C")
    y_axis_for_c = get_y_axis("C")

    distance_of_ab = abs(get_distance(
        x_axis_for_a, x_axis_for_b, y_axis_for_a, y_axis_for_b))
    distance_of_bc = abs(get_distance(
        x_axis_for_b, x_axis_for_c, y_axis_for_b, y_axis_for_c))
    distance_of_ac = abs(get_distance(
        x_axis_for_a, x_axis_for_c, y_axis_for_a, y_axis_for_c))

    length_logger("AB", distance_of_ab)
    length_logger("BC", distance_of_bc)
    length_logger("AC", distance_of_ac)

    check_triangle(distance_of_ab, distance_of_bc, distance_of_ac)
    check_right_triangle(distance_of_ab, distance_of_bc, distance_of_ac)
    perimeter_logger(distance_of_ab, distance_of_bc, distance_of_ac)
    get_even_numbers_till_perimeter(
        distance_of_ab, distance_of_bc, distance_of_ac)


if __name__ == '__main__':
    main()
