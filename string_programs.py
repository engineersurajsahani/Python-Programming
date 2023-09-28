# Python String Programs

# 1) Python Program to count the total number of characters in a string

def countCharacter(s):
    count=0
    for x in s:
        if x!=" ":
            count+=1 
    print("Count of Characters :- ",count)
    
s="My name is Suraj Sahani"
countCharacter(s)

# 3) Python Program to count the total number of punctuation characters exists in a String

import string
def countPunctuations(s):
    count=0
    for x in s:
        if x in string.punctuation:
            count+=1 
    print("Count Of Punctuation :- ",count)

ss=",;!.My name is Suraj Sahani"
countPunctuations(ss)

# 4) Python Program to count the total number of vowels and consonants in a string

def countVowels(s):
    count=0
    vowels="aeiouAEIOU"
    for x in s :
        if x in vowels:
            count+=1 
    print("Count Of Vowels :- ",count)
    
def countConsonants(s):
    count=0
    consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    for x in s :
        if x in consonants:
            count+=1 
    print("Count Of Consonants :- ",count)

countVowels(s)
countConsonants(s)

# 5) Python Program to determine whether two strings are the anagram

def are_anagrams(s1,s2):
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()
    if sorted(s1)==sorted(s2):
        print("Strings are anagram.")
    else:
        print("Strings are not anagram.")

s1="SurajSahani"
s2="SahaniSuraj"
are_anagrams(s1,s2)

# 7) Python Program to find all subsets of a string

def generateSubsets(s):
    def backtrack(start,currentString):
        result.append(currentString[:])
        for i in range(start,len(s)):
            currentString.append(s[i])
            backtrack(i+1,currentString)
            currentString.pop()
    result=[]
    backtrack(0,[])
    return result
result=generateSubsets("Suraj")
print(result)

# 9) Python Program to find all the permutations of a string

from itertools import permutations

def generatePermutations(s):
    result=list(permutations(s))
    for x in result:
        print(''.join(x))
print("Permutations :- ")   
generatePermutations("Suraj")

# 10) Python Program to remove all the white spaces from a string

def removeWitheSpaces(s):
    result=""
    for x in s:
        if x !=" ":
            result+=x 
    print("Without White Spaces :- ",result)

removeWitheSpaces("My name is Suraj Sahani.")

# 11) Python Program to replace lower-case characters with upper-case and vice-versa

def changeCase(s):
    result=""
    for x in s:
        if x.isupper():
            result+=x.lower()
        elif x.islower():
            result+=x.upper()
    print("Chnage Case :- ",result)

changeCase("My name is Suraj Sahani.")

# 12) Python Program to replace the spaces of a string with a specific character

def replaceSpacesWithSpecificCharacter(s):
    result=""
    for x in s:
        if x==" ":
            result+="@"
        else:
            result+=x 
    print("replaceSpacesWithSpecificCharacter :- ",result)

replaceSpacesWithSpecificCharacter("My name is Suraj Sahani.")

# 13) Python Program to determine whether a given string is palindrome

def checkPalindrome(s):
    first=s 
    second=s[::-1]
    for i in range(len(s)):
        if first[i]!=second[i]:
            return False 
    return True 

result=checkPalindrome("suraj")
if result:
    print("String are palindrme string.")
else:
    print("String are not palindrome.")

# 16) Python Program to find Reverse of the string

def reverseString(s):
    result=""
    for i in range(len(s)-1,-1,-1):
        result+=s[i]
    print("Reverse String :- ",result)
    
reverseString("Suraj")

# 17) Python program to find the duplicate characters in a string

from collections import defaultdict

def findDuplicateCharacters(s):
    map=defaultdict()
    for x in s:
        if x in map:
            map[x]=map[x]+1 
        else:
            map[x]=1 
    print("Duplicates Characters :- ",end=" ")
    for index,key in enumerate(map):
        if map[key]>1:
            print(key," ",end=" ")

findDuplicateCharacters("surajsahani")

# 18) Python program to find the duplicate words in a string

from collections import defaultdict

def findDuplicateWords(s):
    map=defaultdict()
    word=""
    words=[]
    for x in s:
        if x==" ":
            words.append(word)
            word=""
        else:
            word+=x
    for x in words:
        if x in map:
            map[x]=map[x]+1 
        else:
            map[x]=1 
    print("Duplicates Words :- ",end=" ")
    for index,key in enumerate(map):
        if map[key]>1:
            print(key," ",end=" ")

print()
findDuplicateWords("My name is Suraj Sahani My Sahani name")

# 19) Python Program to find the frequency of characters

from collections import defaultdict

def findFrequency(s):
    map=defaultdict()
    for x in s:
        if x in map:
            map[x]=map[x]+1 
        else:
            map[x]=1 
    print("Frequency Of Characters :- ",end=" ")
    for index,key in enumerate(map):
        print(key," : ",map[key])

findFrequency("surajsahani")

# 20) Python Program to find the largest and smallest word in a string

from collections import defaultdict

def findLargestAndsmallestWord(s):
    map=defaultdict()
    word=""
    words=[]
    maxWord="a"
    minWord="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for x in s:
        if x==" ":
            words.append(word)
            word=""
        else:
            word+=x
    for x in words:
        if len(x)>len(maxWord):
            maxWord=x
    for x in words:
        if len(x)<len(minWord):
            minWord=x 
    print("Largest Word :- ",maxWord)
    print("Smallest Word :- ",minWord)

print()
findLargestAndsmallestWord("My name is Suraj Sahani My Sahani name")

# 24) Python Program to swap two string variables without using third or temp variable.

def swapString(s1,s2):
    s1,s2=s2,s1
    print("First String :- ",s1)
    print("Second String :- ",s2)
    
swapString("Suraj","Sahani")








