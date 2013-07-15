def reverse(text):
    s = []
    t = []
    for each in text:
       s.append(each)
    counter = (len(s)-1)
    while counter >= 0:
        t.append(s[counter])
        counter -= 1
    for each in t:
        return "".join(t)
    print t

user = str(raw_input("Please enter a phrase to reverse:"))
print reverse(user)