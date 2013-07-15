def count(sequence, item):
    i = 0
    for each in sequence:
        if item == each:
            i += 1
    return i
user1 = raw_input("Enter a list:")
user2 = raw_input("Enter an item to tally:")
print count(user1, user2)