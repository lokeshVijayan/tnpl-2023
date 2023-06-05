#how to check if two strings are anagrams or not!
s1=input().casefold()
s2=input().casefold()
if len(s1)==len(s2):
    if sorted(s1)==sorted(s2):
        print("its an anagram")
    else:
        print("its not an anagram")
else:
    print("length of two words are different ,it cant be anagrams")
