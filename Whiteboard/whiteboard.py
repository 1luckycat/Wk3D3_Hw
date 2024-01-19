# Count Palindromes
# GIven a list of strings, count the number of palindromes that occur inside of the list 
# (a palindrome is a word that is spelled the same backwards and forward).

# Example input: ['dog', 'racecar', 'wildebeest']
# Output: 1
# Explanation: 'racecar' is the only palindrome in the list

# Example input: ['kayak', 'level', 'word', 'smooth', 'detartrated']
# Output: 3
# Explanation: 'kayak', 'level', and 'detartrated' are all palindromes



def palindromes (listy):
    count = 0

    for i in listy:   
        # print (i)

        if i == i[::-1]:    # <------- list splicing 
            count += 1
            # print(count)
                
    return count


print(palindromes(['kayak', 'level', 'word', 'smooth', 'detartrated']))



