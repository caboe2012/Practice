def anti_vowel(text):
    s=[]
    if len(text) > 0:
        i = 0
        for each in user:
            if each in "aeiouAEIOU":
                i += 1
                print i
            else:
                s.append(each)
        print s
    else:
        print "You didn't enter anything!"

user = raw_input('Enter a word:')

print anti_vowel(user)


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
    word.lower()
    total = 0
    for each in word:
        total += score[each]
    return total

user = raw_input(print ("Let's tally some scores!"))

print scrabble_score(user)

##Some random changes so that I can update my Git Branch
## new code to check how "merge" feature works
## and this time I'll make the changes in the BRANCH!
## it looks like "merge" undos the benefit of a brach.
## let's see if a second branch proves it.
