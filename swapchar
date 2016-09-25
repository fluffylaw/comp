# Author of this file: Lydia Wang!

def swapchars(string):
    s = string.lower()   
    print (string)
    print (s)
    mostCommonCharacterIndex = 0
    leastCommonCharacterIndex = 0
    mostCommonCharacter = 0
    leastCommonCharacter = len(s)

    for i in range(0, len(s)):
        if s[i] != " " and s[i] != "\'" and s.count(s[i]) > mostCommonCharacter:
            mostCommonCharacter = s.count(s[i])
            mostCommonCharacterIndex = i

    for i in range(0, len(s)):
        if s[i] != " " and s[i] != "\'" and s.count(s[i]) < leastCommonCharacter : 
            leastCommonCharacter = s.count(s[i])
            leastCommonCharacterIndex = i

    print (mostCommonCharacter)   
    print (leastCommonCharacter)   

    print (s[mostCommonCharacterIndex])  
    print (s[leastCommonCharacterIndex])  

    s1 = string.replace(s[mostCommonCharacterIndex],s[leastCommonCharacterIndex])

    print(s1)

ss ='I\'m just a chi-town coder with a nice flow.'
swapchars(ss)
