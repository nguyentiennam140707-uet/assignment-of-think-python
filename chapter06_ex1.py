def hypot(a_side, b_side):
    a_squared = a_side ** 2
    b_squared = b_side ** 2
    sum_squares = a_squared + b_squared
    hypotenuse = sum_squares ** 0.5 # == math.sqrt(sum_squares)
    return hypotenuse
hypot(3, 4)