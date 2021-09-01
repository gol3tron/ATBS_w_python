# coin flip streaks programming exercise from atbs w/ python

import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # code that creates a list of 100 'heads' or 'tails' values
    newSequence = ''

    for flip in range(100):
        headsOrTails = random.randint(0,1)
        if headsOrTails == 0: #tails is zero
            newSequence += 'T'
        else:
            newSequence += 'H'

    # code that checks if there is a streak of 6 heads or tails in a row
    headStreak = 'H' * 6
    tailStreak = 'T' * 6

#    if headStreak in newSequence:
#        numberOfStreaks += 1
#        print(newSequence + ' <--- streak found ' + headStreak)
#    elif tailStreak in newSequence:
#        numberOfStreaks += 1
#        print(newSequence + ' <--- streak found ' + tailStreak)
#    else:
#        print(newSequence)

    if (headStreak or tailStreak) in newSequence:
        numberOfStreaks += 1
        #print(newSequence + ' <--- streak found')


print('Chance of streak: %s%%' % (numberOfStreaks / 100))
print(numberOfStreaks)
