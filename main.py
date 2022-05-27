# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


"""
    Example 1
            !
    word1 = team
    word2 = mate
    
     !
    team

    wordMap = {
        't' : 1,
        'e' : 1,
        'a' : 1,
        'm' : 1

    }

"""

def find_anagrams(word1, word2):
    # [assignment] Add your code here
    # 1.create word map as dictionary to store letter count
    wordMap = {}

    print(f"1. wordMap {wordMap}")

    # 2.iterate through word1 and store letter count
    for letter in word1:
        if letter not in wordMap:
            wordMap[letter] = 0
        wordMap[letter] += 1
    print(f"2. wordMap {wordMap}")
    
    # 3. iterate through word2 and decrement letter count
    for letter in word2:
        if letter not in wordMap:
            return False
        wordMap[letter] -= 1
    print(f"3. wordMap {wordMap}")

    # 4. iterate through wordMap and if there is any letter that count is not 0 
    for count in wordMap.values():
        if count != 0:
            return False
    print(f"4. wordMap {wordMap}")
    return True

def main():
    print(find_anagrams("team", "meat")) # example 1 
    print(find_anagrams("nail", "lain")) # example 2 

    # print(find_anagrams("team", "meatt"))
    # print(find_anagrams("team", "meatt"))
main()