
def guess(num) -> int: 
    pass 


def guessNumber(n) -> int:
    """Guess the number using the Binary Search 

    Args:
        n (int): the number is between the 0 to the n 

    Returns:
        int: the exact number 
    """
    left = 0 
    right = n 
    while left <= right:
        mid = (left + right) // 2

        if guess(mid)== 0:
            return mid
        elif guess(mid) == 1: # the number is less so we will have to change the left to higher value 
            left = mid + 1
        else:
            right = mid - 1

    return -1



