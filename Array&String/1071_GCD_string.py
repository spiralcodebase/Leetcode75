def gcdOfStrings(str1: str, str2: str) -> str:
    # Checking if concatenating str1 and str2 in both orders gives the same result
    if str1 + str2 != str2 + str1:
            # If not, there's no common divisor, so return an empty string
            return ''

    a = len(str1)
    b = len(str2)

    # Finding the greatest common divisor (GCD)
    while b != 0:
        # Using Euclid's algorithm to find the GCD
        # Here, we're swapping the values of a and b and taking the remainder of a divided by b
        a, b = b, a % b

    # Returning a substring of str2 from index 0 to the length of the GCD
    # This substring represents the greatest common divisor of the two strings
    return str2[:a] 


# str1 = "ABCABC"
# str2 = "ABC"
str1 = "ABABAB"
str2 = "ABAB" 
# str1 = "LEET"
# str2 = "CODE"
print(gcdOfStrings(str1, str2))
