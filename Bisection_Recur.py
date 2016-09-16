def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr=='':
        return False
    if aStr[0]==char or aStr[-1]==char:
        return True
    elif aStr[0]<char<aStr[-1]:
        k=len(aStr)/2
        if char < aStr[k]:
            print aStr[:k], aStr[k] 
            return isIn(char,aStr[:k])
        elif char > aStr[k:]:
            print aStr[k:], aStr[k] 
            return isIn(char,aStr[k:])
        elif char==aStr[k]:
            return True
    else:
        return False