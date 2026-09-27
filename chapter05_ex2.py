def is_triangle(a_stick, b_stick, c_stick):
    if a_stick < (b_stick + c_stick) and b_stick < (a_stick + c_stick) and c_stick < (a_stick + b_stick):
        print("Yes")
    elif a_stick == (b_stick + c_stick) or b_stick == (a_stick + c_stick) or c_stick == (a_stick + b_stick):
        print('Yes')
        print("A 'degenerate' triangle")
    else:
        print('No')