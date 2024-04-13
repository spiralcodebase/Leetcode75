def reverseWords( s: str) -> str:
    filter_string = s.strip()  # removes the traling and leading spaces 
    words = filter_string.split(' ')

    reversed_words = words[::-1]
    final_filtered_words = [x for x in reversed_words if x!=""]
    print(final_filtered_words)
    return " ".join(final_filtered_words) 

s ="a good   example"

print(reverseWords(s))