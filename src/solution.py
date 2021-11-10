def getProbability(n):
    """
    Returns probablity of student missing graduation for given n number of days
    """
    # As per problem we cannot allow any student to miss more than or equal to 4 consecutive days
    # which means that when n is less that 4, there is no way a student would miss his/her graduation
    # we can represent this using binary representation of number having n digits
    # for n = 5, we have the following combinations 00000, 00001...11111 which is basically all the
    # possible 5 digit binary numbers
    # when the student is absent at the graduation ceremony itself that means we need to check
    # whether the last digit is 0 (for n < 4 we can use 2 ** (n - 1))

    if n == 0:
        return "Invalid input value, must be greater than or equal to 1"
    if n < 4:
        return str(1 << (n - 1)) + "/" + str(1 << n)
    # Let f(n) be the function which determines the number of combinations
    # which are not allowed. For n < 4 there are no combinations which
    # are not allowed hence f(0),f(1),f(2) = 0 
    # for n = 4 we only have 1 combination '0000' which is not allowed
    # hence f(4) = 1, for n = 5 onwards we then use the following:
    # f(n) = (2 ** (n - 4)) + f(n - 4) + f(n - 3) + f(n - 2) + f(n - 1)
    # we use 2 ^ (n -4) since we cannot allow 4 consecutive 0s and since
    # we would also need to consider the previous iterations
    f = [0 for _ in range(n + 1)]
    f[0] = None
    f[4] = 1
    for i in range(5, n + 1):
        f[i] = (2 ** (i - 4)) + f[i - 4] + f[i - 3] + f[i - 2] + f[i - 1]
    allowed = [0 for _ in range(n + 1)]
    allowed[0] = None
    for i in range(1, n + 1):
        allowed[i] = (2 ** i) - f[i]
    graduation_miss = allowed[n] - allowed[n - 1] 
    # we do this to avoid overcounting. Suppose we did not have the constraint for 4 consecutive 0s
    # this would just be 2 ^ (n - 1)
    return str(graduation_miss) + "/" + str(allowed[n])

if __name__ == "__main__":
    assert getProbability(5) == "14/29"
    assert getProbability(10) == "372/773"
    print("Tests passed")
