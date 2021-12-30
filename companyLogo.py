from collections import Counter

def logo (l):
    sortedL = Counter (l).most_common (3)       # list the 3 most common keys and their value
    keyList = [i [0] for i in sortedL]          # list keys in the soredL list
    valueList = [i [1] for i in sortedL]        # list values in the soredL list
    for i in range (3):
        print (keyList [i], valueList [i])

if __name__ == '__main__':
    charList = list (input ())
    charList.sort ()
    logo (charList)
    
