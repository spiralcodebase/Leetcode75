
# mine solution 
def mergeAlternately(word1: str, word2: str) -> str:
    result = []
    if len(word1) > len(word2):
        i = 0 
        while i < len(word2): 
            result.append(word1[i])
            result.append(word2[i])
            i+=1 
        result.append(word1[len(word2):])
          
    elif len(word1) < len(word2): 
        i = 0 
        while i < len(word1): 
            result.append(word1[i])
            result.append(word2[i])
            i+=1 
        result.append(word2[len(word1):])
    else : 
        for i in range(len(word1)): 
            result.append(word1[i])
            result.append(word2[i]) 
    return "".join(result)

word1 = "ab"
word2 = "pqrs"       
x = mergeAlternately(word1, word2)
print(x)
