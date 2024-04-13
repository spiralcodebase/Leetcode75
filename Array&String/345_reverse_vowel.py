


def reverseVowels(s: str) -> str:
    i = 0 
    j = len(s)-1 # index start from 0 so elements are from 0 to len-1 
    result = [] 
    vowel = ['a','e','i','o','u']
    vowel_cap = [x.capitalize() for x in vowel ]
    vowel.extend(vowel_cap)
    while i <len(s): 
        # increase the i value till it reaches whole string length 
        if s[i] in vowel: 
            while s[j] not in vowel: 
                #till we get the vowel 
                j-=1 
            result.append(s[j])
            j-=1

        else : 
            result.append(s[i])
        i+=1 
    return ''.join(result)


s = "leetcode"
print(reverseVowels(s))