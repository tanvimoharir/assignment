def isAllowed(binary):
    ''' Gets a number in binary and returns whether number of consecutive 0s exceed or equal 4'''
    consecutive_zeroes = 0
    count = 0
    for char in binary:
        if char == '0':
            count += 1
            consecutive_zeroes = max(consecutive_zeroes, count)
        else:
            count = 0
    return consecutive_zeroes < 4

def getCombinations(n):
    ''' Gets all n digit binary numbers'''
    result = []
    for i in range(1 << n):
        result.append(bin(i).replace('0b', '').rjust(n, '0'))
    return result

def getProbability(n):
    ''' Returns string representation of fraction of probablity that a student witll miss graduation'''
    # As per problem we cannot allow any student to miss more than or equal to 4 consecutive days which means that when n is less that 4, there is no way a student would miss his/her graduation
    # we can represent this using binary representation of number having n digits
    # for n = 5, we have the following combinations 00000, 00001...11111 which is nothing but all the possible 5 digit binary numbers
    # when the student is absent at the graduation ceremony itself that means we need to check whether the last digit is 0 which can be obtained by the formula 2 ** (n - 1) for when n < 4
    
    if n == 0:
        return "Invalid input value, must be greater than or equal to 1"
    if  n < 4:
        return str(2 ** (n - 1)) + '/' + str(2 ** n)
    leaves = 0
    graduation_day = 0 # count of combinations with last digit 0
    record = getCombinations(n)
    for value in record:
        if isAllowed(value):
            if value[-1] == '0':
                graduation_day += 1
            leaves += 1
    return str(graduation_day) + "/" + str(leaves)


if __name__ == "__main__":
    # tests
    assert getProbability(5) == '14/29'
    assert getProbability(10) == '372/773'
    print("Basic tests passed")
    assert getProbability(1) == '1/2'
    assert getProbability(2) == '2/4'
    assert getProbability(3) == '4/8'
    assert getProbability(0) == "Invalid input value, must be greater than or equal to 1"
    print("Additional tests passed")
