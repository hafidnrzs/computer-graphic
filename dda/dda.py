def dda(x1, y1, x2, y2):
    # Calculate the difference in x and y
    delta_x = x2 - x1
    delta_y = y2 - y1

    # Determine step value
    abs_delta_x = abs(delta_x)
    abs_delta_y = abs(delta_y)
    if abs_delta_x > abs_delta_y:
        step = abs_delta_x
    else:
        step = abs_delta_y

    # Calculate the increment values
    x_inc = delta_x / step
    y_inc = delta_y / step

    # Iterate to find coordinates represented the line
    print("\nStarting to draw the line...")
    print(f"Iteration-1. Coordinate: {x1, y1}")
    iter = 1
    while not (x1 == x2 and y1 == y2):
        iter += 1
        x1 += x_inc
        y1 += y_inc
        u = round(x1)
        v = round(y1)
        print(f"Iteration-{iter}. Coordinate: {u, v}")

if __name__ == "__main__":
    print("Enter the first point (as integers)")
    x_first = int(input("Input x1 = "))
    y_first = int(input("Input y1 = "))

    print("Enter the second point (as integers)")
    x_second = int(input("Input x2 = "))
    y_second = int(input("Input y2 = "))

    dda(
        x1=x_first,
        y1=y_first,
        x2=x_second,
        y2=y_second
    )