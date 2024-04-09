def GoalsToWin(previousGame, currentGame, host):

    aHome = previousGame[0]

    aGuest = currentGame[0]

    bHome = currentGame[1]

    bGuest = previousGame[1]
    
    if host==2:
        aHome, aGuest = aGuest,aHome
        bHome, bGuest = bGuest,bHome

    if aHome + aGuest > bGuest + bHome:

        return 0

    equalizer = 0

    if aHome + aGuest < bGuest + bHome:

        equalizer = bGuest + bHome - aGuest - aHome

        if host == 1: aGuest += equalizer

        else: aHome += equalizer

    if aGuest > bGuest: return equalizer

    else: return equalizer + 1

 

p = list(map(int, input().split(":")))

c = list(map(int, input().split(":")))

host = int(input())

print(GoalsToWin(p, c, host))