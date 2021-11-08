def isAllowed(binary):
    """
    Gets a number in binary and returns whether number of consecutive 0s exceed or equal 4
    """
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
    """
     Gets all n digit binary numbers
    """
    record = []
    for i in range(1 << n):
        record.append(bin(i).replace('0b', '').rjust(n, '0'))
    return record

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
    if  n < 4:
        return str(1 << (n - 1)) + '/' + str(1 << n)
    leaves = 0
    graduation_day = 0 # count of combinations with last digit 0
    records = getCombinations(n)
    for record in records:
        if isAllowed(record):
            if record[-1] == '0':
                graduation_day += 1
            leaves += 1
    return str(graduation_day) + "/" + str(leaves)

