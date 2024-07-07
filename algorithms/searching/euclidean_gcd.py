def euclideanGCD_recursive(a, b):
    if b == 0:
        return a

    return euclideanGCD_recursive(b, a % b)


def euclideanGCD_iterative(a, b):
    while b != 0:
        a, b = b, a % b

    return a


result_recursive = euclideanGCD_recursive(282, 78)
print(result_recursive)

result_iterative = euclideanGCD_iterative(282, 78)
print(result_iterative)
