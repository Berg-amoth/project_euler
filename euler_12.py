def highly_divisible_triangular_number(divisors):
    triangle_number_index = 1
    triangle_number = 1
    current_divisors = 0
    while current_divisors < divisors:
        current_divisors = 0
        triangle_number_index += 1
        triangle_number += triangle_number_index
        for i in range(triangle_number):
            if triangle_number%(i+1) == 0:
                current_divisors += 1
        print(triangle_number_index, triangle_number, current_divisors)
    return triangle_number

print(highly_divisible_triangular_number(30))
