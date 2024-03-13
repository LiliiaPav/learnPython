# def is_palindrome(teststr):
#     abc=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     teststr=teststr.lower()
#     testlist=[]
#     for i in teststr:
#         if i in abc:
#             testlist.append(i)
#     teststr=''.join(testlist)
#     teststrRev = teststr[::-1]
#     print(teststr, teststrRev)
#     return teststr==teststrRev


def is_palindrome(teststr):
    teststr=teststr.lower()
    testlist=[]
    for i in teststr:
        if i.isalpha():   #The isalpha() method returns True if all the characters are alphabet letters (a-z).
            testlist.append(i)
    teststr=''.join(testlist)
    teststrRev = teststr[::-1] #start at the end of the string and end at position 0, move with the step -1, negative one, which means one step backwards.

    return teststr==teststrRev


test_words = ["Hello World!","Radar","Mama?","Madam, I'm Adam.", "Race car!"]
for word in test_words:
    print(is_palindrome(word))