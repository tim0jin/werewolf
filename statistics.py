from __future__ import division
from restoredCorpus import *
#game71_items = (game71_date, game71_number, game71_victory, game71_roles,
#    game71_raw_seq_dead, game71_cult_leader, game71_treated_who,
#    game71_treated_seq_dead, game71_day_time_seq)

def killing_x_on_y(person, time, list_gm_items):
    i = 0
    n = 1
    personal_stat = open('person_X_on_Y.txt', 'a')
    vil_vic = {}
    wer_vic = {}
    while i < len(list_gm_items):
        x = list_gm_items[i]
        victry = x[2]
        t_seq_ded = x[7]
        game_time = x[8]
        if person in t_seq_ded: # if person was killed
            if game_time[t_seq_ded.index(person)] == time: # if it matches the queried time,
                if victry == 'villagers': # if villagers won in that game
                    vil_vic[person] = vil_vic.get(person, 0) + 1
                elif victry == 'werewolves': # if wereolves won in that game
                    wer_vic[person] = wer_vic.get(person, 0) + 1
                else:
                    pass
            else:
                pass
        else:
            pass
        i += 1
        n += 1
    print vil_vic
    print wer_vic
    if len(vil_vic) == 0 and len(wer_vic) == 0:
        print 'never killed on %s, N/A' % (time)
        return 'N/A \n' #% (person)
    elif len(vil_vic) != 0 and len(wer_vic) == 0:
        wer_vic[person] = 0
        total_games = vil_vic[person] + wer_vic[person]
        vil_won = int(vil_vic[person]) / int(total_games)
        wer_won = int(wer_vic[person]) / int(total_games)
        return "%d \n %d" % (round(vil_won * 100, 2), total_games) #,round(wer_won * 100, 2),
    elif len(vil_vic) == 0 and len(wer_vic) != 0:
        vil_vic[person] = 0
        total_games = vil_vic[person] + wer_vic[person]
        vil_won = int(vil_vic[person]) / int(total_games)
        wer_won = int(wer_vic[person]) / int(total_games)
        return "%d \n %d" % (round(vil_won * 100, 2), total_games)
    else:
        total_games = vil_vic[person] + wer_vic[person]
        vil_won = int(vil_vic[person]) / int(total_games)
        wer_won = int(wer_vic[person]) / int(total_games)
        print vil_won
        return "%d \n %d" % (round(vil_won * 100, 4), total_games)

def iterate_through_games(time, list_gm_items):
    players = ('Andrew', 'Elvira', 'John', 'Sartaj', 'Foosball', 'Peter',
    'Dave', 'Muuo', 'Platter', 'Physics', 'Darwin', 'Tim', 'Lazar', 'Caroline',
    'Amir', 'Frederick', 'Steve', 'Sohrab', 'Sandra', 'Laura', 'Linda',
    'Amanda', 'Navid', 'Krystal', 'Philippa', 'Samantha', 'Emily', 'Alexei',
    'Jess', 'Ruben', 'Moustafa', 'Jamal', 'Melissa')
    target_file = open('person_X_on_Y.txt', 'a')
    i = 0
    while i < len(players):
        zz = killing_x_on_y(players[i], time, list_gm_items)
        target_file.write('\n')
        target_file.write(str(zz).replace('(', '').replace(')', '').replace('\'', ''))
        i += 1


#kk = killing_x_on_y('John', 'day, 1', items_list)
#print kk
#j = iterate_through_games('night, 7', items_list)

#game71_items = (game71_date, game71_number, game71_victory, game71_roles,
#    game71_raw_seq_dead, game71_cult_leader, game71_treated_who,
#    game71_treated_seq_dead, game71_day_time_seq)
def graph_of_death(list_gm_items, person):
    i = 0
    personal_stat = open('person_X_on_Y.txt', 'a')
    while i < len(list_gm_items):
        x = list_gm_items[i]
        t_seq_ded = x[7]
        game_time = x[8]
        g_datex = x[0]
        g_rolesx = x[3]
        if person in x[7]:
            personal_stat.write('\n')
            personal_stat.write('%s, %s' % (x[0], game_time[t_seq_ded.index(person)]))
        elif person not in x[7] and person in x[3]:
            personal_stat.write('\n')
            personal_stat.write('%s, -1' % (x[0]))
        else:
            personal_stat.write('\n')
            personal_stat.write('%s' % (x[0]))
        i += 1

#zkn = graph_of_death(items_list, 'Philippa')

def single_game_single_line(list_gm_items, start_o):
    players = ('Andrew', 'Elvira', 'John', 'Sartaj', 'Foosball', 'Peter',
    'Dave', 'Muuo', 'Platter', 'Physics', 'Darwin', 'Tim', 'Lazar', 'Caroline',
    'Amir', 'Frederick', 'Steve', 'Sohrab', 'Sandra', 'Laura', 'Linda',
    'Amanda', 'Navid', 'Krystal', 'Philippa')
    i = 0
    one_line = list()
    personal_stat = open('person_X_on_Y.txt', 'a')
    x = list_gm_items[start_o]
    print x
    t_seq_ded = x[7]
    print "T_SEQ_DED: \n", t_seq_ded
    game_time = x[8]
    g_datex = x[0]
    g_rolesx = x[3]
    print "ROLES: \n", x[3]
    while i < len(players):
        gn = players[i]
        print gn
        if gn in t_seq_ded:
            one_line.insert(-1, '%s' % (game_time[t_seq_ded.index(gn)]))
        elif gn not in t_seq_ded:
            if gn in g_rolesx:
                one_line.insert(-1, 'Sur, -1')
        else:
            one_line.insert(-1, 'Not, 0')
        i += 1
    return one_line
    #personal_stat.write('\n')
    #personal_stat.write(str(one_line))

# ['Not, 0', 'day, 1', 'Sur, -1', 'Not, 0', 'Not, 0', 'day, 2', 'Sur, -1',
# 'day, 4', 'Not, 0', 'Sur, -1', 'Not, 0', 'night, 1', 'Not, 0', 'Not, 0',
# 'day, 3', 'Not, 0', 'Not, 0', 'Not, 0', 'Not, 0', 'Not, 0', 'day, 5',
# 'Not, 0', 'Not, 0', 'Not, 0', 'Sur, -1']

zkk = single_game_single_line(items_list, 0)
print zkk
