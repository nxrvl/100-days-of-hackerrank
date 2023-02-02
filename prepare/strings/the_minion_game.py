#!/usr/bin/env python3

def minion_game(string):

    player = dict()
    player['Stuart'] = 0
    player['Kevin'] = 0
    for i in range(len(string)):
        if string[i] in ['A','E','I','O','U']:
            player['Kevin'] += len(string) - i
        else:
            player['Stuart'] += len(string) - i
    max_value = max(player, key=player.get)
    if player['Stuart']!=player['Kevin']:
        print(max_value,player[max_value],sep=' ')
    else:
        print('Draw')



if __name__ == '__main__':
    s = input()
    minion_game(s)
