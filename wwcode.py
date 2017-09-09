from corpus import *

# this function produces 'ww' 'L' list
def i_produce_who(raw_seq_dead):
    who_seq = list()
    for index, item in enumerate(raw_seq_dead):
        if item == 'TURNED' or item == 'PROTECTED':
            who_seq.insert(index, item)
        elif item.endswith('-w'):
            who_seq.insert(index, 'ww')
        elif item.endswith('-wb'):
            who_seq.insert(index, 'wb')
        elif item.endswith('-l'):
            who_seq.insert(index, 'L')
        elif item.endswith('-lb'):
            who_seq.insert(index, 'LB')
    return who_seq

# this function produces just names list, no who
def i_produce_seq_dead(raw_seq_dead):
    seq_dead = list()
    for index, item in enumerate(raw_seq_dead):
        if item == 'TURNED' or item == 'PROTECTED':
            seq_dead.insert(index, item)
        elif item.endswith('-w'):
            seq_dead.insert(index, item[:-2])
        elif item.endswith('-wb'):
            seq_dead.insert(index, item[:-3])
        elif item.endswith('-l'):
            seq_dead.insert(index, item[:-2])
        elif item.endswith('-lb'):
            seq_dead.insert(index, item[:-3])
    return seq_dead

# this function looks at dead people and people in cult and checks if they
# have a role, if not then they are a villager
# produces a dictionary with keys as names and values as 'villager'
def who_is_villager(seq_dead, seq_cult_leader, roles_dict):
    villagers_dict = {}
    for index, item in enumerate(seq_dead):
        if item == 'TURNED' or item == 'PROTECTED':
            pass
        elif item not in roles_dict and item not in villagers_dict:
            villagers_dict[item] = 'villager'
        elif item in roles_dict or item in villagers_dict:
            pass
        else:
            raise Exception('unaccounted item in SEQ_DEAD')
    for index, item in enumerate(seq_cult_leader):
        if item not in roles_dict and item not in villagers_dict:
            villagers_dict[item] = 'villager'
        elif item in roles_dict or item in villagers_dict:
            pass
        else:
            raise Exception('unaccounted item or empty list in SEQ_CULT_LEADER')
    return villagers_dict

#  so this function counts days/nights correctly, produces a list
def classifier_of_time(seq_who):
    sorted_seq_of_time = list()
    d = 1
    n = 1
    for index, item in enumerate(seq_who):
        if item == 'TURNED' or item == 'PROTECTED' or item == 'ww' or item == 'wb':
            sorted_seq_of_time.insert(index, 'night, %r' % n)
            if sorted_seq_of_time[index - 1].startswith('day'):
                d += 1
            if sorted_seq_of_time[index - 1].startswith('night'):
                sorted_seq_of_time[index] = sorted_seq_of_time[index - 1]
        elif item == 'L' or item == 'LB' or item == 'time&out' or item == 'no&one':
            sorted_seq_of_time.insert(index, 'day, %r' % d)
            if sorted_seq_of_time[index - 1].startswith('night'):
                n += 1
            if sorted_seq_of_time[index - 1].startswith('day'):
                sorted_seq_of_time[index] = sorted_seq_of_time[index - 1]
        else:
            print item + ' is unaccounted for or you started with DAY'
    return sorted_seq_of_time

def final_dict_of_roles(dict_roles, villagers_dict):
    final_dict = {}
    for key, value in dict_roles.items():
        final_dict[key] = value
    for key, value in villagers_dict.items():
        final_dict[key] = value
    return final_dict

def report_writer(final_dict, seq_dead, day_night_seq):
    report = {}
    g = 0
    for key, value in final_dict.items():
        if key in seq_dead: #if person is dead, get the night/day they died on
            report[key] = '%s, %s' % (value, day_night_seq[seq_dead.index(key)])
        elif key not in seq_dead:
            report[key] = '%s, survived, survived' % (value)
    return report

def unpacker(game_items, report):
    for key, value in report.items():
        report[key] = '%s, %s, %s, %s' % (game_items[0], game_items[1], game_items[2], value)
    return report

def make_a_file_name(unpacker_report):
    files = {}
    for key, value in unpacker_report.items():
        files[key] = '%s.txt' % key
    return files

def open_and_write(unpacker_report, files):
    for key, value in unpacker_report.items():
        open_key = open(files[key], 'a')
        open_key.write('\n')
        open_key.write(value)
    return open_key

def reconstruction_report(game_items, numberx):
    i = numberx
    g_date = game_items[0]
    g_nmbr = game_items[1]
    g_victory = game_items[2]
    g_roles = game_items[3]
    g_raw_seq = game_items[4]
    g_cult = game_items[5]
    treated_who = i_produce_who(g_raw_seq)
    treated_seq_dead = i_produce_seq_dead(g_raw_seq)
    villagers_are = who_is_villager(treated_seq_dead, g_cult, g_roles)
    day_time_seq = classifier_of_time(treated_who)
    everyone_is = final_dict_of_roles(g_roles, villagers_are)
    newdatafile = open('newCorpus.py', 'a')
    newdatafile.write('\n')
    newdatafile.write('\n')
    newdatafile.write('game%d_date = \'%s\'' % (i, g_date))
    newdatafile.write('\n')
    newdatafile.write('game%d_number = \'%s\'' % (i, g_nmbr))
    newdatafile.write('\n')
    newdatafile.write('game%d_victory = \'%s\'' % (i, g_victory))
    newdatafile.write('\n')
    newdatafile.write('game%d_roles = %s' % (i, everyone_is))
    newdatafile.write('\n')
    newdatafile.write('game%d_raw_seq_dead = %s' % (i, g_raw_seq))
    newdatafile.write('\n')
    newdatafile.write('game%d_cult_leader = %s' %(i, g_cult))
    newdatafile.write('\n')
    newdatafile.write('game%d_treated_who = %s' % (i, treated_who))
    newdatafile.write('\n')
    newdatafile.write('game%d_treated_seq_dead = %s' % (i, treated_seq_dead))
    newdatafile.write('\n')
    newdatafile.write('game%d_day_time_seq = %s' % (i, day_time_seq))
    newdatafile.write('\n')
    newdatafile.write('game%d_items = (game%d_date, game%d_number, \
game%d_victory, game%d_roles, game%d_raw_seq_dead, game%d_cult_leader, \
game%d_treated_who, game%d_treated_seq_dead, game%d_day_time_seq)' %
(i, i, i, i, i, i, i, i, i, i))

def everything_function(game_items):
    g_date = game_items[0]
    print "DATE: ", g_date
    g_nmbr = game_items[1]
    print "NUMBER", g_nmbr
    g_victory = game_items[2]
    print "VICTORY OF: ", g_victory
    g_roles = game_items[3]
    print "THE ROLES ARE: ", g_roles
    g_raw_seq = game_items[4]
    print "THE RAW SEQ IS: ", g_raw_seq
    g_cult = game_items[5]
    print "CULT LEADER SEQ: ", g_cult
    treated_who = i_produce_who(g_raw_seq)
    print "PROCESSED WHO: ", treated_who
    treated_seq_dead = i_produce_seq_dead(g_raw_seq)
    print "PROCESSED SEQ_DEAD: ", treated_seq_dead
    villagers_are = who_is_villager(treated_seq_dead, g_cult, g_roles)
    print "VILLAGERS ARE: ", villagers_are
    day_time_seq = classifier_of_time(treated_who)
    print "DAYTIME SEQ IS: ", day_time_seq
    everyone_is = final_dict_of_roles(g_roles, villagers_are)
    print "ROLES OF EVERYONE", everyone_is
    small_report = report_writer(everyone_is, treated_seq_dead, day_time_seq)
    print "PRELIMINARY REPORT", small_report
    unpacked = unpacker(game1_items, small_report)
    print "UNPACKING: ", unpacked
    file_directory = make_a_file_name(unpacked)
    print "DIRECTORIES: ", file_directory
    writing = open_and_write(unpacked, file_directory)
    print "WRITING:", writing
    print "analyzed %r, %r" % (g_date, g_nmbr)

def finally_doing_it(list_of_itemz):
    i = 0
    n = 1
    while i < 71:
        reconstruction_report(list_of_itemz[i], n)
        i += 1
        n += 1

omg = finally_doing_it(items_list)
