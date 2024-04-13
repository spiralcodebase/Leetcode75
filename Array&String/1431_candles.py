from typing import List 


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    result = [] 
    max_val = max(candies)
    for candle in candies : 
        if candle +extraCandies  >= max_val : 
            result.append(True)
        else : 
            result.append(False)
    return result 

candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies,extraCandies))