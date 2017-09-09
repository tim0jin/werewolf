game1_date = 'Apr-09'
game1_number = '1'
game1_victory = 'villagers'
game1_roles = {'Sartaj': 'seer', 'Muuo': 'villager', 'Platter': 'werewolf',
    'Frederick': 'villager', 'Andrew': 'cult leader', 'Lazar': 'villager',
    'Dave': 'werewolf', 'John': 'villager', 'Darwin': 'bodyguard',
    'Amanda': 'werewolf'}
game1_raw_seq_dead = ('Lazar-w', 'John-l', 'TURNED', 'Dave-l', 'PROTECTED',
    'Frederick-l', 'PROTECTED', 'Platter-l', 'PROTECTED', 'Amanda-l')
game1_cult_leader = ('Amanda', 'Frederick', 'Platter', 'Sartaj', 'Muuo')
game1_treated_who = ['ww', 'L', 'TURNED', 'L', 'PROTECTED', 'L', 'PROTECTED',
    'L', 'PROTECTED', 'L']
game1_treated_seq_dead = ['Lazar', 'John', 'TURNED', 'Dave', 'PROTECTED',
    'Frederick', 'PROTECTED', 'Platter', 'PROTECTED', 'Amanda']
game1_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4', 'night, 5', 'day, 5']
game1_items = (game1_date, game1_number, game1_victory, game1_roles,
    game1_raw_seq_dead, game1_cult_leader, game1_treated_who,
    game1_treated_seq_dead, game1_day_time_seq)

game2_date = 'Apr-09'
game2_number = '2'
game2_victory = 'villagers'
game2_roles = {'Muuo': 'werewolf', 'John': 'seer', 'Frederick': 'bodyguard',
    'Andrew': 'villager', 'Dave': 'werewolf', 'Darwin': 'cursed',
    'Amanda': 'cult leader', 'Platter': 'villager'}
game2_raw_seq_dead = ('PROTECTED', 'Dave-l', 'John-w', 'Platter-l', 'PROTECTED',
    'Amanda-l', 'PROTECTED', 'Muuo-l')
game2_cult_leader = ('Frederick', 'Darwin', 'Andrew')
game2_treated_who = ['PROTECTED', 'L', 'ww', 'L', 'PROTECTED', 'L', 'PROTECTED',
    'L']
game2_treated_seq_dead = ['PROTECTED', 'Dave', 'John', 'Platter', 'PROTECTED',
    'Amanda', 'PROTECTED', 'Muuo']
game2_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4']
game2_items = (game2_date, game2_number, game2_victory, game2_roles,
    game2_raw_seq_dead, game2_cult_leader, game2_treated_who,
    game2_treated_seq_dead, game2_day_time_seq)

game3_date = 'Apr-23'
game3_number = '1'
game3_victory = 'villagers'
game3_roles = {'Sartaj': 'villager', 'Muuo': 'bodyguard', 'Peter': 'villager',
    'Ruben': 'villager', 'Amanda': 'villager', 'Sohrab': 'seer',
    'Frederick': 'cursed', 'Jess': 'lycan', 'Dave': 'werewolf',
    'Darwin': 'cub', 'Physics': 'werewolf'}
game3_raw_seq_dead = ('Amanda-w', 'Peter-l', 'PROTECTED', 'Dave-l', 'Ruben-w',
    'Frederick-l', 'PROTECTED', 'Darwin-l', 'Jess-w', 'Sartaj-w', 'Physics-l')
game3_cult_leader = ()
game3_treated_who = ['ww', 'L', 'PROTECTED', 'L', 'ww', 'L', 'PROTECTED', 'L',
    'ww', 'ww', 'L']
game3_treated_seq_dead = ['Amanda', 'Peter', 'PROTECTED', 'Dave', 'Ruben',
    'Frederick', 'PROTECTED', 'Darwin', 'Jess', 'Sartaj', 'Physics']
game3_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4', 'night, 5', 'night, 5', 'day, 5']
game3_items = (game3_date, game3_number, game3_victory, game3_roles,
    game3_raw_seq_dead, game3_cult_leader, game3_treated_who,
    game3_treated_seq_dead, game3_day_time_seq)

game4_date = 'Apr-23'
game4_number = '2'
game4_victory = 'werewolves'
game4_roles = {'Sartaj': 'cursed', 'Muuo': 'cult leader', 'Darwin': 'cub',
    'Ruben': 'werewolf', 'Amanda': 'villager', 'Sohrab': 'seer',
    'Frederick': 'villager', 'Jess': 'bodyguard', 'Dave': 'lycan',
    'Peter': 'villager', 'Jamal': 'villager', 'Platter': 'werewolf',
    'Physics': 'villager'}
game4_raw_seq_dead = ('Dave-w', 'Amanda-l', 'PROTECTED', 'Platter-l',
    'Sohrab-w', 'Physics-l', 'Peter-w', 'Muuo-l', 'Frederick-w')
game4_cult_leader = ('Frederick', 'Peter', 'Jamal', 'Darwin')
game4_treated_who = ['ww', 'L', 'PROTECTED', 'L', 'ww', 'L', 'ww', 'L', 'ww']
game4_treated_seq_dead = ['Dave', 'Amanda', 'PROTECTED', 'Platter', 'Sohrab',
    'Physics', 'Peter', 'Muuo', 'Frederick']
game4_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4', 'night, 5']
game4_items = (game4_date, game4_number, game4_victory, game4_roles,
    game4_raw_seq_dead, game4_cult_leader, game4_treated_who,
    game4_treated_seq_dead, game4_day_time_seq)

game5_date = 'Apr-23'
game5_number = '3'
game5_victory = 'werewolves'
game5_roles = {'Sartaj': 'villager', 'Muuo': 'seer', 'Peter': 'werewolf',
    'Navid': 'cult leader', 'Ruben': 'werewolf', 'Frederick': 'villager',
    'Dave': 'lycan', 'Jamal': 'cub', 'Darwin': 'cursed', 'Amanda': 'bodyguard',
    'Platter': 'villager'}
game5_raw_seq_dead = ('Sartaj-w', 'Darwin-l', 'Muuo-w', 'Platter-l',
    'Frederick-w', 'Navid-l')
game5_cult_leader = ('Sartaj', 'Jamal', 'Dave')
game5_treated_who = ['ww', 'L', 'ww', 'L', 'ww', 'L']
game5_treated_seq_dead = ['Sartaj', 'Darwin', 'Muuo', 'Platter', 'Frederick',
    'Navid']
game5_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3']
game5_items = (game5_date, game5_number, game5_victory, game5_roles,
    game5_raw_seq_dead, game5_cult_leader, game5_treated_who,
    game5_treated_seq_dead, game5_day_time_seq)

game6_date = 'Apr-23'
game6_number = '4'
game6_victory = 'villagers'
game6_roles = {'Sartaj': 'cub', 'Muuo': 'lycan', 'Darwin': 'cursed',
    'Yonis': 'villager', 'Navid': 'villager', 'Ruben': 'cult leader',
    'Peter': 'villager', 'Frederick': 'villager', 'Elvira': 'bodyguard',
    'Jess': 'villager', 'Dave': 'werewolf', 'Platter': 'werewolf',
    'Amanda': 'seer'}
game6_raw_seq_dead = ('TURNED', 'Darwin-l', 'Jess-w', 'Dave-l', 'Peter-w',
    'Navid-l', 'Muuo-w', 'Ruben-l', 'Yonis-w', 'Platter-l', 'PROTECTED')
game6_cult_leader = ('Peter', 'Frederick', 'Navid', 'Platter')
game6_treated_who = ['TURNED', 'L', 'ww', 'L', 'ww', 'L', 'ww', 'L', 'ww', 'L',
    'PROTECTED']
game6_treated_seq_dead = ['TURNED', 'Darwin', 'Jess', 'Dave', 'Peter', 'Navid',
    'Muuo', 'Ruben', 'Yonis', 'Platter', 'PROTECTED']
game6_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4', 'night, 5', 'day, 5', 'night, 6']
game6_items = (game6_date, game6_number, game6_victory, game6_roles,
    game6_raw_seq_dead, game6_cult_leader, game6_treated_who,
    game6_treated_seq_dead, game6_day_time_seq)

game7_date = 'Apr-30'
game7_number = '1'
game7_victory = 'werewolves'
game7_roles = {'Muuo': 'villager', 'Caroline': 'seer', 'Darwin': 'villager',
    'Frederick': 'werewolf', 'Dave': 'lycan', 'Krystal': 'bodyguard',
    'Peter': 'werewolf'}
game7_raw_seq_dead = ('Darwin-w', 'Dave-l', 'Krystal-w', 'Frederick-l',
    'Caroline-w', 'Muuo-l')
game7_cult_leader = ()
game7_treated_who = ['ww', 'L', 'ww', 'L', 'ww', 'L']
game7_treated_seq_dead = ['Darwin', 'Dave', 'Krystal', 'Frederick', 'Caroline',
    'Muuo']
game7_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3']
game7_items = (game7_date, game7_number, game7_victory, game7_roles,
    game7_raw_seq_dead, game7_cult_leader, game7_treated_who,
    game7_treated_seq_dead, game7_day_time_seq)

game8_date = 'Apr-30'
game8_number = '2'
game8_victory = 'villagers'
game8_roles = {'Muuo': 'bodyguard', 'Peter': 'villager', 'Physics': 'villager',
    'Sohrab': 'seer', 'Frederick': 'werewolf', 'Dave': 'villager',
    'Krystal': 'werewolf', 'Darwin': 'cursed', 'Amanda': 'lycan'}
game8_raw_seq_dead = ('Peter-w', 'Physics-l', 'PROTECTED', 'Krystal-l',
    'Sohrab-w', 'Dave-l', 'Muuo-w', 'TURNED', 'Darwin-l', 'Amanda-w',
    'Frederick-l')
game8_cult_leader = ()
game8_treated_who = ['ww', 'L', 'PROTECTED', 'L', 'ww', 'L', 'ww', 'TURNED',
    'L', 'ww', 'L']
game8_treated_seq_dead = ['Peter', 'Physics', 'PROTECTED', 'Krystal', 'Sohrab',
    'Dave', 'Muuo', 'TURNED', 'Darwin', 'Amanda', 'Frederick']
game8_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'night, 4', 'day, 4', 'night, 5', 'day, 5']
game8_items = (game8_date, game8_number, game8_victory, game8_roles,
    game8_raw_seq_dead, game8_cult_leader, game8_treated_who,
    game8_treated_seq_dead, game8_day_time_seq)

game9_date = 'Apr-30'
game9_number = '3'
game9_victory = 'villagers'
game9_roles = {'Muuo': 'werewolf', 'Peter': 'lycan', 'Caroline': 'villager',
    'Navid': 'villager', 'Samantha': 'cursed', 'Sohrab': 'werewolf',
    'Frederick': 'villager', 'Andrew': 'werewolf', 'Dave': 'villager',
    'Krystal': 'seer', 'Darwin': 'bodyguard', 'Platter': 'villager'}
game9_raw_seq_dead = ('Frederick-w', 'Dave-l', 'Peter-w', 'Andrew-l',
    'Platter-w', 'Sohrab-l', 'PROTECTED', 'Navid-l', 'Caroline-w', 'Muuo-l')
game9_cult_leader = ()
game9_treated_who = ['ww', 'L', 'ww', 'L', 'ww', 'L', 'PROTECTED', 'L', 'ww',
    'L']
game9_treated_seq_dead = ['Frederick', 'Dave', 'Peter', 'Andrew', 'Platter',
    'Sohrab', 'PROTECTED', 'Navid', 'Caroline', 'Muuo']
game9_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4', 'night, 5', 'day, 5']
game9_items = (game9_date, game9_number, game9_victory, game9_roles,
    game9_raw_seq_dead, game9_cult_leader, game9_treated_who,
    game9_treated_seq_dead, game9_day_time_seq)

game10_date = 'Apr-30'
game10_number = '4'
game10_victory = 'villagers'
game10_roles = {'Muuo': 'lycan', 'Darwin': 'werewolf', 'Caroline': 'villager',
    'Navid': 'seer', 'Samantha': 'villager', 'Sohrab': 'werewolf',
    'Frederick': 'werewolf', 'Andrew': 'cursed', 'Elvira': 'villager',
    'Dave': 'villager', 'Krystal': 'villager', 'Peter': 'bodyguard',
    'Platter': 'villager'}
game10_raw_seq_dead = ('Caroline-w', 'Platter-l', 'Navid-w', 'Sohrab-l',
    'Krystal-w', 'Darwin-l', 'TURNED', 'Frederick-l', 'Samantha-w', 'Dave-l',
    'Elvira-w', 'Andrew-l')
game10_cult_leader = ()
game10_treated_who = ['ww', 'L', 'ww', 'L', 'ww', 'L', 'TURNED', 'L', 'ww', 'L',
    'ww', 'L']
game10_treated_seq_dead = ['Caroline', 'Platter', 'Navid', 'Sohrab', 'Krystal',
    'Darwin', 'TURNED', 'Frederick', 'Samantha', 'Dave', 'Elvira', 'Andrew']
game10_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4', 'night, 5', 'day, 5', 'night, 6', 'day, 6']
game10_items = (game10_date, game10_number, game10_victory, game10_roles,
    game10_raw_seq_dead, game10_cult_leader, game10_treated_who,
    game10_treated_seq_dead, game10_day_time_seq)

game11_date = 'Apr-30'
game11_number = '5'
game11_victory = 'villagers'
game11_roles = {'Muuo': 'cursed', 'Darwin': 'seer', 'Caroline': 'werewolf',
    'Navid': 'lycan', 'Frederick': 'villager', 'Elvira': 'villager',
    'Dave': 'villager', 'Krystal': 'bodyguard', 'Peter': 'werewolf',
    'Amanda': 'werewolf'}
game11_raw_seq_dead = ('Frederick-w', 'Peter-l', 'Dave-w', 'Caroline-l',
    'PROTECTED', 'Navid-l', 'Elvira-w', 'Amanda-l')
game11_cult_leader = ()
game11_treated_who = ['ww', 'L', 'ww', 'L', 'PROTECTED', 'L', 'ww', 'L']
game11_treated_seq_dead = ['Frederick', 'Peter', 'Dave', 'Caroline',
    'PROTECTED', 'Navid', 'Elvira', 'Amanda']
game11_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4']
game11_items = (game11_date, game11_number, game11_victory, game11_roles,
    game11_raw_seq_dead, game11_cult_leader, game11_treated_who,
    game11_treated_seq_dead, game11_day_time_seq)

game12_date = 'Apr-30'
game12_number = '6'
game12_victory = 'werewolves'
game12_roles = {'Muuo': 'villager', 'Platter': 'werewolf',
    'Caroline': 'villager', 'Navid': 'seer', 'Peter': 'villager',
    'Frederick': 'werewolf', 'Elvira': 'cursed', 'Moustafa': 'villager',
    'Dave': 'villager', 'Krystal': 'lycan', 'Darwin': 'werewolf',
    'Amanda': 'bodyguard'}
game12_raw_seq_dead = ('Peter-w', 'Muuo-l', 'Navid-w', 'Moustafa-l', 'TURNED',
    'Platter-l', 'Dave-w', 'Darwin-l', 'Krystal-w', 'Caroline-l')
game12_cult_leader = ()
game12_treated_who = ['ww', 'L', 'ww', 'L', 'TURNED', 'L', 'ww', 'L', 'ww', 'L']
game12_treated_seq_dead = ['Peter', 'Muuo', 'Navid', 'Moustafa', 'TURNED',
    'Platter', 'Dave', 'Darwin', 'Krystal', 'Caroline']
game12_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4', 'night, 5', 'day, 5']
game12_items = (game12_date, game12_number, game12_victory, game12_roles,
    game12_raw_seq_dead, game12_cult_leader, game12_treated_who,
    game12_treated_seq_dead, game12_day_time_seq)

game13_date = 'Apr-30'
game13_number = '7'
game13_victory = 'villagers'
game13_roles = {'Muuo': 'seer', 'Platter': 'villager', 'Frederick': 'lycan',
    'Moustafa': 'werewolf', 'Dave': 'villager', 'Krystal': 'werewolf',
    'Darwin': 'bodyguard', 'Amanda': 'cursed'}
game13_raw_seq_dead = ('PROTECTED', 'Dave-l', 'PROTECTED', 'Krystal-l',
    'Frederick-w', 'Amanda-l', 'Platter-w', 'Moustafa-l')
game13_cult_leader = ()
game13_treated_who = ['PROTECTED', 'L', 'PROTECTED', 'L', 'ww', 'L', 'ww', 'L']
game13_treated_seq_dead = ['PROTECTED', 'Dave', 'PROTECTED', 'Krystal',
    'Frederick', 'Amanda', 'Platter', 'Moustafa']
game13_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4']
game13_items = (game13_date, game13_number, game13_victory, game13_roles,
    game13_raw_seq_dead, game13_cult_leader, game13_treated_who,
    game13_treated_seq_dead, game13_day_time_seq)

game14_date = 'May-07'
game14_number = '1'
game14_victory = 'villagers'
game14_roles = {'Sartaj': 'villager', 'Muuo': 'werewolf', 'Platter': 'lycan',
    'Sohrab': 'werewolf', 'Frederick': 'seer', 'Andrew': 'cub',
    'Lazar': 'teenager', 'Peter': 'villager', 'John': 'prince',
    'Amanda': 'bodyguard'}
game14_raw_seq_dead = ('Frederick-w', 'Lazar-l', 'PROTECTED', 'Peter-w',
    'Muuo-l', 'Amanda-w', 'Sohrab-l', 'Sartaj-w', 'Andrew-l')
game14_cult_leader = ()
game14_treated_who = ['ww', 'L', 'PROTECTED', 'ww', 'L', 'ww', 'L', 'ww', 'L']
game14_treated_seq_dead = ['Frederick', 'Lazar', 'PROTECTED', 'Peter', 'Muuo',
    'Amanda', 'Sohrab', 'Sartaj', 'Andrew']
game14_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'night, 2', 'day, 2',
    'night, 3', 'day, 3', 'night, 4', 'day, 4']
game14_items = (game14_date, game14_number, game14_victory, game14_roles,
    game14_raw_seq_dead, game14_cult_leader, game14_treated_who,
    game14_treated_seq_dead, game14_day_time_seq)

game15_date = 'May-07'
game15_number = '2'
game15_victory = 'villagers'
game15_roles = {'Sartaj': 'seer', 'John': 'villager', 'Darwin': 'villager',
    'Amanda': 'lycan', 'Sohrab': 'villager', 'Frederick': 'villager',
    'Elvira': 'cub', 'Lazar': 'werewolf', 'Dave': 'villager',
    'Peter': 'werewolf', 'Physics': 'bodyguard', 'Platter': 'villager',
    'Andrew': 'villager'}
game15_raw_seq_dead = ('Darwin-w', 'Peter-l', 'Dave-w', 'Platter-l', 'Andrew-w',
    'Sohrab-l', 'John-w', 'Elvira-l', 'Frederick-w', 'PROTECTED', 'Lazar-l')
game15_cult_leader = ()
game15_treated_who = ['ww', 'L', 'ww', 'L', 'ww', 'L', 'ww', 'L', 'ww',
    'PROTECTED', 'L']
game15_treated_seq_dead = ['Darwin', 'Peter', 'Dave', 'Platter', 'Andrew',
    'Sohrab', 'John', 'Elvira', 'Frederick', 'PROTECTED', 'Lazar']
game15_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4', 'night, 5', 'night, 5', 'day, 5']
game15_items = (game15_date, game15_number, game15_victory, game15_roles,
    game15_raw_seq_dead, game15_cult_leader, game15_treated_who,
    game15_treated_seq_dead, game15_day_time_seq)

game16_date = 'May-07'
game16_number = '3'
game16_victory = 'werewolves'
game16_roles = {'Sartaj': 'seer', 'Peter': 'villager', 'Physics': 'villager',
    'Sohrab': 'lycan', 'Frederick': 'villager', 'Elvira': 'bodyguard',
    'Dave': 'villager', 'Darwin': 'werewolf', 'Amanda': 'werewolf'}
game16_raw_seq_dead = ('Peter-w', 'Physics-l', 'Sartaj-w', 'Frederick-l',
    'Sohrab-w', 'Dave-l')
game16_cult_leader = ()
game16_treated_who = ['ww', 'L', 'ww', 'L', 'ww', 'L']
game16_treated_seq_dead = ['Peter', 'Physics', 'Sartaj', 'Frederick', 'Sohrab',
    'Dave']
game16_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3']
game16_items = (game16_date, game16_number, game16_victory, game16_roles,
    game16_raw_seq_dead, game16_cult_leader, game16_treated_who,
    game16_treated_seq_dead, game16_day_time_seq)

game17_date = 'May-07'
game17_number = '4'
game17_victory = 'villagers'
game17_roles = {'Sartaj': 'cursed', 'Caroline': 'cult leader',
    'Darwin': 'werewolf', 'Amanda': 'villager', 'Frederick': 'bodyguard',
    'Elvira': 'spellcaster', 'Dave': 'lycan', 'Peter': 'seer',
    'Physics': 'werewolf', 'Platter': 'villager'}
game17_raw_seq_dead = ('TURNED', 'Darwin-l', 'Amanda-w', 'Sartaj-l', 'Dave-w',
    'Platter-l', 'PROTECTED', 'Physics-l')
game17_cult_leader = ('Peter', 'Frederick', 'Dave', 'Elvira')
game17_treated_who = ['TURNED', 'L', 'ww', 'L', 'ww', 'L', 'PROTECTED', 'L']
game17_treated_seq_dead = ['TURNED', 'Darwin', 'Amanda', 'Sartaj', 'Dave',
    'Platter', 'PROTECTED', 'Physics']
game17_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4']
game17_items = (game17_date, game17_number, game17_victory, game17_roles,
    game17_raw_seq_dead, game17_cult_leader, game17_treated_who,
    game17_treated_seq_dead, game17_day_time_seq)

game18_date = 'May-07'
game18_number = '5'
game18_victory = 'villagers'
game18_roles = {'Sartaj': 'spellcaster', 'Darwin': 'cursed',
    'Amanda': 'villager', 'Peter': 'villager', 'Frederick': 'werewolf',
    'Elvira': 'werewolf', 'Dave': 'lycan', 'Krystal': 'cult leader',
    'Caroline': 'werewolf', 'Physics': 'bodyguard', 'Platter': 'seer'}
game18_raw_seq_dead = ('Platter-w', 'Frederick-l', 'Peter-w', 'Elvira-l',
    'PROTECTED', 'Krystal-l', 'Sartaj-w', 'Amanda-l', 'PROTECTED', 'Caroline-l')
game18_cult_leader = ('Amanda', 'Elvira', 'Darwin')
game18_treated_who = ['ww', 'L', 'ww', 'L', 'PROTECTED', 'L', 'ww', 'L',
    'PROTECTED', 'L']
game18_treated_seq_dead = ['Platter', 'Frederick', 'Peter', 'Elvira',
    'PROTECTED', 'Krystal', 'Sartaj', 'Amanda', 'PROTECTED', 'Caroline']
game18_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4', 'night, 5', 'day, 5']
game18_items = (game18_date, game18_number, game18_victory, game18_roles,
    game18_raw_seq_dead, game18_cult_leader, game18_treated_who,
    game18_treated_seq_dead, game18_day_time_seq)

game19_date = 'May-07'
game19_number = '6'
game19_victory = 'villagers'
game19_roles = {'Sartaj': 'cult leader', 'Peter': 'werewolf',
    'Frederick': 'villager', 'Physics': 'cursed', 'Darwin': 'villager',
    'Elvira': 'werewolf', 'Dave': 'spellcaster', 'Krystal': 'werewolf',
    'Caroline': 'seer', 'Amanda': 'lycan', 'Platter': 'villager'}
game19_raw_seq_dead = ('Darwin-w', 'Physics-l', 'Frederick-w', 'Peter-l',
    'Sartaj-w', 'Elvira-l', 'Platter-w', 'Krystal-l')
game19_cult_leader = ('Elvira', 'Dave', 'Amanda')
game19_treated_who = ['ww', 'L', 'ww', 'L', 'ww', 'L', 'ww', 'L']
game19_treated_seq_dead = ['Darwin', 'Physics', 'Frederick', 'Peter', 'Sartaj',
    'Elvira', 'Platter', 'Krystal']
game19_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4']
game19_items = (game19_date, game19_number, game19_victory, game19_roles,
    game19_raw_seq_dead, game19_cult_leader, game19_treated_who,
    game19_treated_seq_dead, game19_day_time_seq)

game20_date = 'May-07'
game20_number = '7'
game20_victory = 'werewolves'
game20_roles = {'Sartaj': 'lycan', 'Peter': 'werewolf', 'Caroline': 'villager',
    'Amanda': 'seer', 'Frederick': 'spellcaster', 'Elvira': 'werewolf',
    'Dave': 'villager', 'Krystal': 'werewolf', 'Darwin': 'cursed',
    'Physics': 'bodyguard', 'Platter': 'cult leader'}
game20_raw_seq_dead = ('Sartaj-w', 'Peter-l', 'TURNED', 'Platter-l', 'Amanda-w',
    'Krystal-l', 'Frederick-w', 'Dave-l')
game20_cult_leader = ('Caroline', 'Krystal')
game20_treated_who = ['ww', 'L', 'TURNED', 'L', 'ww', 'L', 'ww', 'L']
game20_treated_seq_dead = ['Sartaj', 'Peter', 'TURNED', 'Platter', 'Amanda',
    'Krystal', 'Frederick', 'Dave']
game20_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4']
game20_items = (game20_date, game20_number, game20_victory, game20_roles,
    game20_raw_seq_dead, game20_cult_leader, game20_treated_who,
    game20_treated_seq_dead, game20_day_time_seq)

game21_date = 'May-14'
game21_number = '1'
game21_victory = 'werewolves'
game21_roles = {'Sartaj': 'spellcaster', 'Muuo': 'cub', 'Caroline': 'lycan',
    'Peter': 'cursed', 'Frederick': 'villager', 'Elvira': 'werewolf',
    'Andrew': 'bodyguard', 'Dave': 'villager', 'John': 'villager',
    'Melissa': 'villager', 'Linda': 'seer', 'Krystal': 'werewolf',
    'Darwin': 'werewolf', 'Platter': 'villager'}
game21_raw_seq_dead = ('TURNED', 'Dave-l', 'Melissa-w', 'John-l', 'Linda-w',
    'Platter-l', 'Caroline-w', 'Peter-l', 'Sartaj-w', 'Frederick-l')
game21_cult_leader = ()
game21_treated_who = ['TURNED', 'L', 'ww', 'L', 'ww', 'L', 'ww', 'L', 'ww', 'L']
game21_treated_seq_dead = ['TURNED', 'Dave', 'Melissa', 'John', 'Linda',
    'Platter', 'Caroline', 'Peter', 'Sartaj', 'Frederick']
game21_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4', 'night, 5', 'day, 5']
game21_items = (game21_date, game21_number, game21_victory, game21_roles,
    game21_raw_seq_dead, game21_cult_leader, game21_treated_who,
    game21_treated_seq_dead, game21_day_time_seq)

game22_date = 'May-14'
game22_number = '2'
game22_victory = 'villagers'
game22_roles = {'John': 'werewolf', 'Caroline': 'spellcaster', 'Peter': 'seer',
    'Dave': 'villager', 'Krystal': 'villager', 'Linda': 'werewolf',
    'Darwin': 'bodyguard', 'Amanda': 'cub', 'Platter': 'lycan'}
game22_raw_seq_dead = ('PROTECTED', 'Amanda-l', 'Dave-w', 'Krystal-w', 'John-l',
    'PROTECTED', 'Linda-w')
game22_cult_leader = ()
game22_treated_who = ['PROTECTED', 'L', 'ww', 'ww', 'L', 'PROTECTED', 'ww']
game22_treated_seq_dead = ['PROTECTED', 'Amanda', 'Dave', 'Krystal', 'John',
    'PROTECTED', 'Linda']
game22_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'night, 2', 'day, 2',
    'night, 3', 'night, 3']
game22_items = (game22_date, game22_number, game22_victory, game22_roles,
    game22_raw_seq_dead, game22_cult_leader, game22_treated_who,
    game22_treated_seq_dead, game22_day_time_seq)

game23_date = 'May-14'
game23_number = '3'
game23_victory = 'villagers'
game23_roles = {'Rachel': 'villager', 'Tim': 'lycan', 'Melissa': 'bodyguard',
    'Krystal': 'cursed', 'Caroline': 'cub', 'Sartaj': 'werewolf',
    'Muuo': 'seer', 'Darwin': 'cult leader', 'Navid': 'villager',
    'Sohrab': 'werewolf', 'Andrew': 'werewolf', 'Dave': 'spellcaster',
    'Lazar': 'villager', 'John': 'minion', 'Platter': 'villager',
    'Amanda': 'villager', 'Elvira': 'villager'}
game23_raw_seq_dead = ('Darwin-w', 'Navid-l', 'Elvira-w', 'Platter-l', 'Dave-w',
    'Caroline-l', 'John-l', 'Lazar-w', 'Andrew-l', 'Amanda-w', 'Krystal-l',
    'Muuo-w', 'Sohrab-l', 'Rachel-w', 'Sartaj-l')
game23_cult_leader = ('Sartaj')
game23_treated_who = ['ww', 'L', 'ww', 'L', 'ww', 'L', 'L', 'ww', 'L', 'ww',
    'L', 'ww', 'L', 'ww', 'L']
game23_treated_seq_dead = ['Darwin', 'Navid', 'Elvira', 'Platter', 'Dave',
    'Caroline', 'John', 'Lazar', 'Andrew', 'Amanda', 'Krystal', 'Muuo',
    'Sohrab', 'Rachel', 'Sartaj']
game23_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'day, 3', 'night, 4', 'day, 4', 'night, 5', 'day, 5', 'night, 6',
    'day, 6', 'night, 7', 'day, 7']
game23_items = (game23_date, game23_number, game23_victory, game23_roles,
    game23_raw_seq_dead, game23_cult_leader, game23_treated_who,
    game23_treated_seq_dead, game23_day_time_seq)

game24_date = 'May-14'
game24_number = '4'
game24_victory = 'villagers'
game24_roles = {'Sartaj': 'villager', 'Darwin': 'bodyguard',
    'Navid': 'werewolf', 'Elvira': 'werewolf', 'Tim': 'lycan',
    'Dave': 'spellcaster', 'John': 'cursed', 'Melissa': 'seer',
    'Krystal': 'cub', 'Caroline': 'werewolf', 'Physics': 'minion',
    'Platter': 'villager'}
game24_raw_seq_dead = ('PROTECTED', 'Krystal-l', 'Tim-w', 'Sartaj-w', 'Navid-l',
    'Platter-w', 'Elvira-l', 'Melissa-w', 'Caroline-l')
game24_cult_leader = ()
game24_treated_who = ['PROTECTED', 'L', 'ww', 'ww', 'L', 'ww', 'L', 'ww', 'L']
game24_treated_seq_dead = ['PROTECTED', 'Krystal', 'Tim', 'Sartaj', 'Navid',
    'Platter', 'Elvira', 'Melissa', 'Caroline']
game24_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'night, 2', 'day, 2',
    'night, 3', 'day, 3', 'night, 4', 'day, 4']
game24_items = (game24_date, game24_number, game24_victory,
    game24_roles, game24_raw_seq_dead, game24_cult_leader, game24_treated_who,
    game24_treated_seq_dead, game24_day_time_seq)

game25_date = 'May-21'
game25_number = '1'
game25_victory = 'villagers'
game25_roles = {'Sartaj': 'werewolf', 'Muuo': 'werewolf', 'Peter': 'lycan',
    'Navid': 'cursed', 'Physics': 'seer', 'Frederick': 'villager',
    'Darwin': 'spellcaster', 'Amanda': 'bodyguard'}
game25_raw_seq_dead = ('Peter-w', 'Sartaj-l', 'Frederick-w', 'Navid-l',
    'Amanda-w', 'Muuo-l')
game25_cult_leader = ()
game25_treated_who = ['ww', 'L', 'ww', 'L', 'ww', 'L']
game25_treated_seq_dead = ['Peter', 'Sartaj', 'Frederick', 'Navid', 'Amanda',
    'Muuo']
game25_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3']
game25_items = (game25_date, game25_number, game25_victory, game25_roles,
    game25_raw_seq_dead, game25_cult_leader, game25_treated_who,
    game25_treated_seq_dead, game25_day_time_seq)

game26_date = 'May-21'
game26_number = '2'
game26_victory = 'villagers'
game26_roles = {'Sartaj': 'villager', 'Muuo': 'spellcaster',
    'Darwin': 'bodyguard', 'Frederick': 'lycan', 'Elvira': 'cursed',
    'Laura': 'werewolf', 'Peter': 'werewolf', 'Physics': 'seer',
    'Platter': 'werewolf'}
game26_raw_seq_dead = ('PROTECTED', 'Peter-l', 'Sartaj-w', 'PROTECTED',
    'Laura-l', 'Physics-w', 'Platter-l')
game26_cult_leader = ()
game26_treated_who = ['PROTECTED', 'L', 'ww', 'PROTECTED', 'L', 'ww', 'L']
game26_treated_seq_dead = ['PROTECTED', 'Peter', 'Sartaj', 'PROTECTED', 'Laura',
    'Physics', 'Platter']
game26_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'night, 2', 'day, 2',
    'night, 3', 'day, 3']
game26_items = (game26_date, game26_number, game26_victory, game26_roles,
    game26_raw_seq_dead, game26_cult_leader, game26_treated_who,
    game26_treated_seq_dead, game26_day_time_seq)

game27_date = 'May-21'
game27_number = '3'
game27_victory = 'not_scored'
game27_roles = {'Sartaj': 'bodyguard', 'Darwin': 'cursed',
    'Navid': 'spellcaster', 'Samantha': 'werewolf', 'Frederick': 'werewolf',
    'Elvira': 'lycan', 'Laura': 'seer', 'Platter': 'werewolf',
    'Amanda': 'villager'}
game27_raw_seq_dead = ('PROTECTED', 'Darwin-l', 'Amanda-w', 'Platter-l',
    'Elvira-w', 'time&out', 'Sartaj-w', 'Laura-l')
game27_cult_leader = ()
game27_treated_who = ['PROTECTED', 'L', 'ww', 'L', 'ww', 'ww', 'L']
game27_treated_seq_dead = ['PROTECTED', 'Darwin', 'Amanda', 'Platter', 'Elvira',
    'Sartaj', 'Laura']
game27_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'night, 3', 'day, 3']
game27_items = (game27_date, game27_number, game27_victory, game27_roles,
    game27_raw_seq_dead, game27_cult_leader, game27_treated_who,
    game27_treated_seq_dead, game27_day_time_seq)

game28_date = 'May-23'
game28_number = '1'
game28_victory = 'villagers'
game28_roles = {'Sartaj': 'villager', 'Muuo': 'cursed', 'John': 'werewolf',
    'Navid': 'seer', 'Frederick': 'villager', 'Darwin': 'bodyguard',
    'Physics': 'werewolf'}
game28_raw_seq_dead = ('Frederick-w', 'John-l', 'Sartaj-w', 'Physics-l')
game28_cult_leader = ()
game28_treated_who = ['ww', 'L', 'ww', 'L']
game28_treated_seq_dead = ['Frederick', 'John', 'Sartaj', 'Physics']
game28_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2']
game28_items = (game28_date, game28_number, game28_victory, game28_roles,
    game28_raw_seq_dead, game28_cult_leader, game28_treated_who,
    game28_treated_seq_dead, game28_day_time_seq)

game29_date = 'May-23'
game29_number = '2'
game29_victory = 'villagers'
game29_roles = {'Sartaj': 'villager', 'Muuo': 'cursed', 'John': 'werewolf',
    'Navid': 'seer', 'Frederick': 'villager', 'Darwin': 'bodyguard',
    'Physics': 'werewolf'}
game29_raw_seq_dead = ('Frederick-w', 'John-l', 'Sartaj-w', 'Physics-l')
game29_cult_leader = ()
game29_treated_who = ['ww', 'L', 'ww', 'L']
game29_treated_seq_dead = ['Frederick', 'John', 'Sartaj', 'Physics']
game29_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2']
game29_items = (game29_date, game29_number, game29_victory, game29_roles,
    game29_raw_seq_dead, game29_cult_leader, game29_treated_who,
    game29_treated_seq_dead, game29_day_time_seq)

game30_date = 'May-23'
game30_number = '3'
game30_victory = 'werewolves'
game30_roles = {'Sartaj': 'bodyguard', 'Muuo': 'cursed', 'Darwin': 'villager',
    'Navid': 'seer', 'Amanda': 'villager', 'Frederick': 'villager',
    'Dave': 'villager', 'Caroline': 'werewolf', 'Physics': 'werewolf'}
game30_raw_seq_dead = ('PROTECTED', 'Dave-l', 'Amanda-w', 'Darwin-l', 'Navid-w',
    'Muuo-l', 'Frederick-w')
game30_cult_leader = ()
game30_treated_who = ['PROTECTED', 'L', 'ww', 'L', 'ww', 'L', 'ww']
game30_treated_seq_dead = ['PROTECTED', 'Dave', 'Amanda', 'Darwin', 'Navid',
    'Muuo', 'Frederick']
game30_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4']
game30_items = (game30_date, game30_number, game30_victory, game30_roles,
    game30_raw_seq_dead, game30_cult_leader, game30_treated_who,
    game30_treated_seq_dead, game30_day_time_seq)

game31_date = 'May-23'
game31_number = '4'
game31_victory = 'villagers'
game31_roles = {'Sartaj': 'villager', 'Muuo': 'werewolf', 'John': 'villager',
    'Amanda': 'werewolf', 'Tim': 'werewolf', 'Dave': 'villager',
    'Darwin': 'bodyguard', 'Physics': 'seer'}
game31_raw_seq_dead = ('PROTECTED', 'John-l', 'Dave-w', 'Tim-l', 'PROTECTED',
    'Muuo-l', 'Sartaj-w', 'Amanda-l')
game31_cult_leader = ()
game31_treated_who = ['PROTECTED', 'L', 'ww', 'L', 'PROTECTED', 'L', 'ww', 'L']
game31_treated_seq_dead = ['PROTECTED', 'John', 'Dave', 'Tim', 'PROTECTED',
    'Muuo', 'Sartaj', 'Amanda']
game31_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4']
game31_items = (game31_date, game31_number, game31_victory, game31_roles,
    game31_raw_seq_dead, game31_cult_leader, game31_treated_who,
    game31_treated_seq_dead, game31_day_time_seq)

game32_date = 'Jun-04'
game32_number = '1'
game32_victory = 'werewolves'
game32_roles = {'Sartaj': 'villager', 'Sohrab': 'villager',
    'Frederick': 'werewolf', 'Elvira': 'villager', 'Steve': 'bodyguard',
    'Krystal': 'villager', 'Platter': 'seer', 'Physics': 'werewolf'}
game32_raw_seq_dead = ('Sohrab-w', 'Steve-l', 'Platter-w', 'Sartaj-l',
    'Krystal-w', 'Elvira-l')
game32_cult_leader = ()
game32_treated_who = ['ww', 'L', 'ww', 'L', 'ww', 'L']
game32_treated_seq_dead = ['Sohrab', 'Steve', 'Platter', 'Sartaj', 'Krystal',
    'Elvira']
game32_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3']
game32_items = (game32_date, game32_number, game32_victory, game32_roles,
    game32_raw_seq_dead, game32_cult_leader, game32_treated_who,
    game32_treated_seq_dead, game32_day_time_seq)

game33_date = 'Jun-04'
game33_number = '2'
game33_victory = 'werewolves'
game33_roles = {'Sartaj': 'villager', 'Caroline': 'bomb',
    'Philippa': 'werewolf', 'Frederick': 'villager', 'Elvira': 'villager',
    'Steve': 'seer', 'Dave': 'villager', 'Krystal': 'bodyguard',
    'Darwin': 'werewolf', 'Physics': 'villager', 'Platter': 'werewolf'}
game33_raw_seq_dead = ('Sartaj-w', 'Physics-l', 'Krystal-w', 'Elvira-l',
    'Steve-w', 'Frederick-l', 'Dave-w')
game33_cult_leader = ()
game33_treated_who = ['ww', 'L', 'ww', 'L', 'ww', 'L', 'ww']
game33_treated_seq_dead = ['Sartaj', 'Physics', 'Krystal', 'Elvira', 'Steve',
    'Frederick', 'Dave']
game33_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4']
game33_items = (game33_date, game33_number, game33_victory, game33_roles,
    game33_raw_seq_dead, game33_cult_leader, game33_treated_who,
    game33_treated_seq_dead, game33_day_time_seq)

game34_date = 'Jun-04'
game34_number = '3'
game34_victory = 'villagers'
game34_roles = {'Darwin': 'bodyguard', 'Frederick': 'villager', 'Steve': 'bomb',
    'Dave': 'seer', 'Krystal': 'villager', 'Caroline': 'werewolf',
    'Physics': 'villager', 'Platter': 'werewolf'}
game34_raw_seq_dead = ('PROTECTED', 'Frederick-l', 'Physics-w', 'Caroline-l',
    'Krystal-w', 'Platter-l')
game34_cult_leader = ()
game34_treated_who = ['PROTECTED', 'L', 'ww', 'L', 'ww', 'L']
game34_treated_seq_dead = ['PROTECTED', 'Frederick', 'Physics', 'Caroline',
    'Krystal', 'Platter']
game34_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3']
game34_items = (game34_date, game34_number, game34_victory, game34_roles,
    game34_raw_seq_dead, game34_cult_leader, game34_treated_who,
    game34_treated_seq_dead, game34_day_time_seq)

game35_date = 'Jun-04'
game35_number = '4'
game35_victory = 'werewolves'
game35_roles = {'Sartaj': 'werewolf', 'Platter': 'werewolf',
    'Caroline': 'villager', 'Sohrab': 'bomb', 'Frederick': 'seer',
    'Elvira': 'bodyguard', 'Steve': 'villager', 'Krystal': 'villager',
    'Darwin': 'cursed', 'Physics': 'villager'}
game35_raw_seq_dead = ('TURNED', 'Physics-l', 'Frederick-w', 'time&out',
    'Steve-w', 'Darwin-l', 'Krystal-w', 'Caroline-l', 'Sohrab-w')
game35_cult_leader = ()
game35_treated_who = ['TURNED', 'L', 'ww', 'ww', 'L', 'ww', 'L', 'ww']
game35_treated_seq_dead = ['TURNED', 'Physics', 'Frederick', 'Steve', 'Darwin',
    'Krystal', 'Caroline', 'Sohrab']
game35_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'night, 2', 'day, 2',
    'night, 3', 'day, 3', 'night, 4']
game35_items = (game35_date, game35_number, game35_victory, game35_roles,
    game35_raw_seq_dead, game35_cult_leader, game35_treated_who,
    game35_treated_seq_dead, game35_day_time_seq)

game36_date = 'Jun-04'
game36_number = '5'
game36_victory = 'villagers'
game36_roles = {'Sartaj': 'villager', 'Caroline': 'werewolf',
    'Frederick': 'werewolf', 'Steve': 'werewolf', 'Darwin': 'bomb',
    'Physics': 'seer'}
game36_raw_seq_dead = ('Sartaj-w', 'Frederick-l', 'PROTECTED', 'Caroline-l',
    'PROTECTED', 'Steve-l')
game36_cult_leader = ()
game36_treated_who = ['ww', 'L', 'PROTECTED', 'L', 'PROTECTED', 'L']
game36_treated_seq_dead = ['Sartaj', 'Frederick', 'PROTECTED', 'Caroline',
    'PROTECTED', 'Steve']
game36_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3']
game36_items = (game36_date, game36_number, game36_victory, game36_roles,
    game36_raw_seq_dead, game36_cult_leader, game36_treated_who,
    game36_treated_seq_dead, game36_day_time_seq)

game37_date = 'Jun-11'
game37_number = '1'
game37_victory = 'werewolves'
game37_roles = {'Peter': 'werewolf', 'Navid': 'bodyguard', 'Amanda': 'villager',
    'Steve': 'cursed', 'John': 'werewolf', 'Darwin': 'villager',
    'Physics': 'seer', 'Platter': 'villager'}
game37_raw_seq_dead = ('Darwin-w', 'Amanda-l', 'PROTECTED', 'Navid-l',
    'Physics-w', 'Platter-l')
game37_cult_leader = ()
game37_treated_who = ['ww', 'L', 'PROTECTED', 'L', 'ww', 'L']
game37_treated_seq_dead = ['Darwin', 'Amanda', 'PROTECTED', 'Navid', 'Physics',
    'Platter']
game37_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3']
game37_items = (game37_date, game37_number, game37_victory, game37_roles,
    game37_raw_seq_dead, game37_cult_leader, game37_treated_who,
    game37_treated_seq_dead, game37_day_time_seq)

game38_date = 'Jun-11'
game38_number = '2'
game38_victory = 'werewolves'
game38_roles = {'John': 'werewolf', 'Caroline': 'werewolf', 'Navid': 'werewolf',
    'Amanda': 'cursed', 'Sohrab': 'bomb', 'Steve': 'villager',
    'Peter': 'villager', 'Krystal': 'villager', 'Darwin': 'bodyguard',
    'Physics': 'seer', 'Platter': 'villager'}
game38_raw_seq_dead = ('Peter-w', 'John-l', 'Sohrab-w', 'Darwin-wb', 'Steve-wb',
    'Caroline-l', 'Physics-w', 'Krystal-l', 'Platter-w', 'Amanda-l')
game38_cult_leader = ()
game38_treated_who = ['ww', 'L', 'ww', 'wb', 'wb', 'L', 'ww', 'L', 'ww', 'L']
game38_treated_seq_dead = ['Peter', 'John', 'Sohrab', 'Darwin', 'Steve',
    'Caroline', 'Physics', 'Krystal', 'Platter', 'Amanda']
game38_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'night, 2', 'night, 2',
    'day, 2', 'night, 3', 'day, 3', 'night, 4', 'day, 4']
game38_items = (game38_date, game38_number, game38_victory, game38_roles,
    game38_raw_seq_dead, game38_cult_leader, game38_treated_who,
    game38_treated_seq_dead, game38_day_time_seq)

game39_date = 'Jun-11'
game39_number = '3'
game39_victory = 'villagers'
game39_roles = {'Darwin': 'bodyguard', 'Navid': 'werewolf', 'Steve': 'werewolf',
    'John': 'villager', 'Sandra': 'bomb', 'Krystal': 'seer',
    'Peter': 'werewolf', 'Physics': 'cursed'}
game39_raw_seq_dead = ('PROTECTED', 'Peter-l', 'TURNED', 'Navid-l', 'Krystal-w',
    'Steve-l', 'John-w', 'Physics-l')
game39_cult_leader = ()
game39_treated_who = ['PROTECTED', 'L', 'TURNED', 'L', 'ww', 'L', 'ww', 'L']
game39_treated_seq_dead = ['PROTECTED', 'Peter', 'TURNED', 'Navid', 'Krystal',
    'Steve', 'John', 'Physics']
game39_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4']
game39_items = (game39_date, game39_number, game39_victory, game39_roles,
    game39_raw_seq_dead, game39_cult_leader, game39_treated_who,
    game39_treated_seq_dead, game39_day_time_seq)

game40_date = 'Jun-11'
game40_number = '4'
game40_victory = 'werewolves'
game40_roles = {'John': 'bomb', 'Caroline': 'villager', 'Navid': 'bodyguard',
    'Physics': 'werewolf', 'Peter': 'villager', 'Elvira': 'werewolf',
    'Steve': 'werewolf', 'Sandra': 'villager', 'Krystal': 'villager',
    'Darwin': 'cursed', 'Amanda': 'seer'}
game40_raw_seq_dead = ('Peter-w', 'John-l', 'Sandra-lb', 'Krystal-lb',
    'Caroline-w', 'Steve-l', 'TURNED')
game40_cult_leader = ()
game40_treated_who = ['ww', 'L', 'LB', 'LB', 'ww', 'L', 'TURNED']
game40_treated_seq_dead = ['Peter', 'John', 'Sandra', 'Krystal', 'Caroline',
    'Steve', 'TURNED']
game40_day_time_seq = ['night, 1', 'day, 1', 'day, 1', 'day, 1', 'night, 2',
    'day, 2', 'night, 3']
game40_items = (game40_date, game40_number, game40_victory, game40_roles,
    game40_raw_seq_dead, game40_cult_leader, game40_treated_who,
    game40_treated_seq_dead, game40_day_time_seq)

game41_date = 'Jun-19'
game41_number = '1'
game41_victory = 'werewolves'
game41_roles = {'John': 'seer', 'Philippa': 'cursed', 'Amanda': 'villager',
    'Peter': 'villager', 'Darwin': 'villager', 'Elvira': 'villager',
    'Steve': 'werewolf', 'Sandra': 'villager', 'Platter': 'werewolf',
    'Physics': 'bodyguard', 'Navid': 'villager'}
game41_raw_seq_dead = ('Sandra-w', 'time&out', 'Darwin-w', 'Navid-l', 'Peter-w',
    'Elvira-l', 'John-w', 'Amanda-l')
game41_cult_leader = ()
game41_treated_who = ['ww', 'ww', 'L', 'ww', 'L', 'ww', 'L']
game41_treated_seq_dead = ['Sandra', 'Darwin', 'Navid', 'Peter', 'Elvira',
    'John', 'Amanda']
game41_day_time_seq = ['night, 1', 'night, 1', 'day, 1', 'night, 2', 'day, 2',
    'night, 3', 'day, 3']
game41_items = (game41_date, game41_number, game41_victory, game41_roles,
    game41_raw_seq_dead, game41_cult_leader, game41_treated_who,
    game41_treated_seq_dead, game41_day_time_seq)

game42_date = 'Jun-19'
game42_number = '2'
game42_victory = 'villagers'
game42_roles = {'Platter': 'cursed', 'Navid': 'bodyguard', 'Amanda': 'werewolf',
    'Peter': 'villager', 'Darwin': 'villager', 'Elvira': 'villager',
    'Andrew': 'villager', 'Steve': 'werewolf', 'John': 'villager',
    'Sandra': 'bomb', 'Caroline': 'werewolf', 'Physics': 'seer'}
game42_raw_seq_dead = ('Darwin-w', 'John-l', 'TURNED', 'Elvira-w', 'Peter-w',
    'Steve-l', 'Navid-w', 'Platter-l', 'Andrew-w', 'Caroline-l', 'Physics-w',
    'Amanda-l')
game42_cult_leader = ()
game42_treated_who = ['ww', 'L', 'TURNED', 'ww', 'ww', 'L', 'ww', 'L', 'ww',
    'L', 'ww', 'L']
game42_treated_seq_dead = ['Darwin', 'John', 'TURNED', 'Elvira', 'Peter',
    'Steve', 'Navid', 'Platter', 'Andrew', 'Caroline', 'Physics', 'Amanda']
game42_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'night, 2', 'night, 2',
    'day, 2', 'night, 3', 'day, 3', 'night, 4', 'day, 4', 'night, 5', 'day, 5']
game42_items = (game42_date, game42_number, game42_victory, game42_roles,
    game42_raw_seq_dead, game42_cult_leader, game42_treated_who,
    game42_treated_seq_dead, game42_day_time_seq)

game43_date = 'Jun-19'
game43_number = '3'
game43_victory = 'villagers'
game43_roles = {'Darwin': 'werewolf', 'Caroline': 'werewolf',
    'Navid': 'villager', 'Peter': 'bomb', 'Andrew': 'werewolf',
    'Steve': 'bodyguard', 'Platter': 'seer'}
game43_raw_seq_dead = ('Navid-w', 'Darwin-l', 'Steve-w', 'Peter-l',
    'Caroline-lb', 'Andrew-lb')
game43_cult_leader = ()
game43_treated_who = ['ww', 'L', 'ww', 'L', 'LB', 'LB']
game43_treated_seq_dead = ['Navid', 'Darwin', 'Steve', 'Peter', 'Caroline',
    'Andrew']
game43_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'day, 2',
    'day, 2']
game43_items = (game43_date, game43_number, game43_victory, game43_roles,
    game43_raw_seq_dead, game43_cult_leader, game43_treated_who,
    game43_treated_seq_dead, game43_day_time_seq)

game44_date = 'Jun-19'
game44_number = '4'
game44_victory = 'werewolves'
game44_roles = {'Darwin': 'bomb', 'Caroline': 'villager', 'Navid': 'werewolf',
    'Foosball': 'werewolf', 'Elvira': 'werewolf', 'Andrew': 'villager',
    'Steve': 'villager', 'Sandra': 'villager', 'John': 'bodyguard',
    'Amanda': 'villager', 'Platter': 'seer'}
game44_raw_seq_dead = ('Steve-w', 'Navid-l', 'Darwin-w', 'Platter-wb',
    'Foosball-l', 'PROTECTED', 'Amanda-l', 'Caroline-w', 'Andrew-l', 'John-w',
    'Sandra-l')
game44_cult_leader = ()
game44_treated_who = ['ww', 'L', 'ww', 'wb', 'L', 'PROTECTED', 'L', 'ww', 'L',
    'ww', 'L']
game44_treated_seq_dead = ['Steve', 'Navid', 'Darwin', 'Platter', 'Foosball',
    'PROTECTED', 'Amanda', 'Caroline', 'Andrew', 'John', 'Sandra']
game44_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'night, 2', 'day, 2',
    'night, 3', 'day, 3', 'night, 4', 'day, 4', 'night, 5', 'day, 5']
game44_items = (game44_date, game44_number, game44_victory, game44_roles,
    game44_raw_seq_dead, game44_cult_leader, game44_treated_who,
    game44_treated_seq_dead, game44_day_time_seq)

game45_date = 'Jun-19'
game45_number = '5'
game45_victory = 'villagers'
game45_roles = {'Caroline': 'werewolf', 'Navid': 'bodyguard',
    'Foosball': 'werewolf', 'Peter': 'villager', 'Andrew': 'villager',
    'Steve': 'villager', 'Darwin': 'cursed', 'Platter': 'seer'}
game45_raw_seq_dead = ('Peter-w', 'Foosball-l', 'Steve-w', 'Andrew-l',
    'TURNED', 'Caroline-l', 'PROTECTED', 'Navid-l', 'Platter-w', 'Darwin-l')
game45_cult_leader = ()
game45_treated_who = ['ww', 'L', 'ww', 'L', 'TURNED', 'L', 'PROTECTED', 'L',
    'ww', 'L']
game45_treated_seq_dead = ['Peter', 'Foosball', 'Steve', 'Andrew', 'TURNED',
    'Caroline', 'PROTECTED', 'Navid', 'Platter', 'Darwin']
game45_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4', 'night, 5', 'day, 5']
game45_items = (game45_date, game45_number, game45_victory, game45_roles,
    game45_raw_seq_dead, game45_cult_leader, game45_treated_who,
    game45_treated_seq_dead, game45_day_time_seq)

game46_date = 'Jun-19'
game46_number = '6'
game46_victory = 'villagers'
game46_roles = {'John': 'werewolf', 'Andrew': 'cursed', 'Elvira': 'villager',
    'Peter': 'bodyguard', 'Amanda': 'werewolf', 'Platter': 'seer'}
game46_raw_seq_dead = ('Elvira-w', 'John-l', 'Peter-w', 'Amanda-l')
game46_cult_leader = ()
game46_treated_who = ['ww', 'L', 'ww', 'L']
game46_treated_seq_dead = ['Elvira', 'John', 'Peter', 'Amanda']
game46_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2']
game46_items = (game46_date, game46_number, game46_victory, game46_roles,
    game46_raw_seq_dead, game46_cult_leader, game46_treated_who,
    game46_treated_seq_dead, game46_day_time_seq)

game47_date = 'Jun-19'
game47_number = '7'
game47_victory = 'werewolves'
game47_roles = {'John': 'bodyguard', 'Caroline': 'villager',
    'Navid': 'werewolf', 'Peter': 'villager', 'Elvira': 'villager',
    'Andrew': 'villager', 'Steve': 'cursed', 'Darwin': 'werewolf',
    'Amanda': 'seer', 'Platter': 'villager'}
game47_raw_seq_dead = ('Peter-w', 'Caroline-l', 'Amanda-w', 'time&out',
    'Elvira-w', 'Andrew-l', 'Platter-w', 'John-l')
game47_cult_leader = ()
game47_treated_who = ['ww', 'L', 'ww', 'ww', 'L', 'ww', 'L']
game47_treated_seq_dead = ['Peter', 'Caroline', 'Amanda', 'Elvira', 'Andrew',
    'Platter', 'John']
game47_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'night, 2', 'day, 2',
    'night, 3', 'day, 3']
game47_items = (game47_date, game47_number, game47_victory, game47_roles,
    game47_raw_seq_dead, game47_cult_leader, game47_treated_who,
    game47_treated_seq_dead, game47_day_time_seq)

game48_date = 'Jun-24'
game48_number = '1'
game48_victory = 'villagers'
game48_roles = {'Sartaj': 'villager', 'John': 'villager', 'Sohrab': 'seer',
    'Frederick': 'werewolf', 'Elvira': 'werewolf', 'Sandra': 'bodyguard',
    'Caroline': 'villager'}
game48_raw_seq_dead = ('Caroline-w', 'John-l', 'Sartaj-w', 'Elvira-l',
    'Sohrab-w', 'Frederick-l')
game48_cult_leader = ()
game48_treated_who = ['ww', 'L', 'ww', 'L', 'ww', 'L']
game48_treated_seq_dead = ['Caroline', 'John', 'Sartaj', 'Elvira', 'Sohrab',
    'Frederick']
game48_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3']
game48_items = (game48_date, game48_number, game48_victory, game48_roles,
    game48_raw_seq_dead, game48_cult_leader, game48_treated_who,
    game48_treated_seq_dead, game48_day_time_seq)

game49_date = 'Jun-24'
game49_number = '2'
game49_victory = 'villagers'
game49_roles = {'Sartaj': 'seer', 'Darwin': 'villager', 'Caroline': 'werewolf',
    'Sohrab': 'werewolf', 'John': 'bodyguard', 'Sandra': 'villager',
    'Peter': 'villager'}
game49_raw_seq_dead = ('John-w', 'Darwin-l', 'Sandra-w', 'Sohrab-l', 'Peter-w',
    'Caroline-l')
game49_cult_leader = ()
game49_treated_who = ['ww', 'L', 'ww', 'L', 'ww', 'L']
game49_treated_seq_dead = ['John', 'Darwin', 'Sandra', 'Sohrab', 'Peter',
    'Caroline']
game49_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3']
game49_items = (game49_date, game49_number, game49_victory, game49_roles,
    game49_raw_seq_dead, game49_cult_leader, game49_treated_who,
    game49_treated_seq_dead, game49_day_time_seq)

game50_date = 'Jul-02'
game50_number = '1'
game50_victory = 'villagers'
game50_roles = {'Sartaj': 'villager', 'Muuo': 'werewolf', 'John': 'villager',
    'Philippa': 'cursed', 'Frederick': 'seer', 'Laura': 'werewolf',
    'Darwin': 'bodyguard'}
game50_raw_seq_dead = ('PROTECTED', 'John-l', 'Sartaj-w', 'Laura-l',
    'PROTECTED', 'Muuo-l')
game50_cult_leader = ()
game50_treated_who = ['PROTECTED', 'L', 'ww', 'L', 'PROTECTED', 'L']
game50_treated_seq_dead = ['PROTECTED', 'John', 'Sartaj', 'Laura', 'PROTECTED',
    'Muuo']
game50_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3']
game50_items = (game50_date, game50_number, game50_victory, game50_roles,
    game50_raw_seq_dead, game50_cult_leader, game50_treated_who,
    game50_treated_seq_dead, game50_day_time_seq)

game51_date = 'Jul-02'
game51_number = '2'
game51_victory = 'villagers'
game51_roles = {'Sartaj': 'bodyguard', 'Muuo': 'villager', 'Darwin': 'villager',
    'Elvira': 'cub', 'John': 'villager', 'Sandra': 'werewolf',
    'Platter': 'werewolf', 'Physics': 'seer'}
game51_raw_seq_dead = ('Darwin-w', 'Muuo-l', 'PROTECTED', 'Platter-l', 'John-w',
    'Sandra-l', 'Sartaj-w', 'Elvira-l')
game51_cult_leader = ()
game51_treated_who = ['ww', 'L', 'PROTECTED', 'L', 'ww', 'L', 'ww', 'L']
game51_treated_seq_dead = ['Darwin', 'Muuo', 'PROTECTED', 'Platter', 'John',
    'Sandra', 'Sartaj', 'Elvira']
game51_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4']
game51_items = (game51_date, game51_number, game51_victory, game51_roles,
    game51_raw_seq_dead, game51_cult_leader, game51_treated_who,
    game51_treated_seq_dead, game51_day_time_seq)

game52_date = 'Jul-09'
game52_number = '1'
game52_victory = 'villagers'
game52_roles = {'Sartaj': 'villager', 'Muuo': 'villager', 'Darwin': 'villager',
    'Frederick': 'werewolf', 'Elvira': 'bodyguard', 'Sandra': 'seer',
    'Krystal': 'villager', 'John': 'werewolf', 'Physics': 'werewolf',
    'Emily': 'villager'}
game52_raw_seq_dead = ('Sartaj-w', 'John-l', 'Krystal-w', 'Physics-l',
    'Darwin-w', 'Emily-l', 'PROTECTED', 'Sandra-w', 'Muuo-l', 'PROTECTED',
    'Frederick-l')
game52_cult_leader = ()
game52_treated_who = ['ww', 'L', 'ww', 'L', 'ww', 'L', 'PROTECTED', 'ww', 'L',
    'PROTECTED', 'L']
game52_treated_seq_dead = ['Sartaj', 'John', 'Krystal', 'Physics', 'Darwin',
    'Emily', 'PROTECTED', 'Sandra', 'Muuo', 'PROTECTED', 'Frederick']
game52_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'night, 4', 'day, 4', 'night, 5', 'day, 5']
game52_items = (game52_date, game52_number, game52_victory, game52_roles,
    game52_raw_seq_dead, game52_cult_leader, game52_treated_who,
    game52_treated_seq_dead, game52_day_time_seq)

game53_date = 'Jul-09'
game53_number = '2'
game53_victory = 'villagers'
game53_roles = {'Sartaj': 'villager', 'Muuo': 'bodyguard', 'Darwin': 'villager',
    'Sohrab': 'seer', 'Frederick': 'werewolf', 'Elvira': 'villager',
    'Sandra': 'werewolf', 'Krystal': 'werewolf', 'John': 'villager',
    'Physics': 'bomb'}
game53_raw_seq_dead = ('John-w', 'Frederick-l', 'Darwin-w', 'time&out',
    'Physics-w', 'Krystal-l', 'Sartaj-w', 'Elvira-l', 'PROTECTED', 'Sandra-l')
game53_cult_leader = ()
game53_treated_who = ['ww', 'L', 'ww', 'ww', 'L', 'ww', 'L', 'PROTECTED', 'L']
game53_treated_seq_dead = ['John', 'Frederick', 'Darwin', 'Physics', 'Krystal',
    'Sartaj', 'Elvira', 'PROTECTED', 'Sandra']
game53_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'night, 2', 'day, 2',
    'night, 3', 'day, 3', 'night, 4', 'day, 4']
game53_items = (game53_date, game53_number, game53_victory, game53_roles,
    game53_raw_seq_dead, game53_cult_leader, game53_treated_who,
    game53_treated_seq_dead, game53_day_time_seq)

game54_date = 'Jul-09'
game54_number = '3'
game54_victory = 'villagers'
game54_roles = {'Sartaj': 'villager', 'Muuo': 'villager', 'Darwin': 'villager',
    'Sohrab': 'villager', 'Frederick': 'bodyguard', 'Elvira': 'seer',
    'Steve': 'cursed', 'Krystal': 'werewolf', 'John': 'werewolf',
    'Platter': 'villager'}
game54_raw_seq_dead = ('Darwin-w', 'Sartaj-l', 'Sohrab-w', 'John-l',
    'PROTECTED', 'Platter-l', 'Muuo-w', 'Krystal-l')
game54_cult_leader = ()
game54_treated_who = ['ww', 'L', 'ww', 'L', 'PROTECTED', 'L', 'ww', 'L']
game54_treated_seq_dead = ['Darwin', 'Sartaj', 'Sohrab', 'John', 'PROTECTED',
    'Platter', 'Muuo', 'Krystal']
game54_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4']
game54_items = (game54_date, game54_number, game54_victory, game54_roles,
    game54_raw_seq_dead, game54_cult_leader, game54_treated_who,
    game54_treated_seq_dead, game54_day_time_seq)

game55_date = 'Jul-16'
game55_number = '1'
game55_victory = 'villagers'
game55_roles = {'Muuo': 'villager', 'Platter': 'bodyguard',
    'Frederick': 'villager', 'Darwin': 'villager', 'Elvira': 'seer',
    'Steve': 'werewolf', 'John': 'werewolf', 'Physics': 'villager',
    'Amir': 'werewolf'}
game55_raw_seq_dead = ('Darwin-w', 'Frederick-l', 'Physics-w', 'Muuo-l',
    'PROTECTED', 'John-l', 'Platter-w', 'Amir-l', 'Elvira-w', 'Steve-l')
game55_cult_leader = ()
game55_treated_who = ['ww', 'L', 'ww', 'L', 'PROTECTED', 'L', 'ww', 'L', 'ww',
    'L']
game55_treated_seq_dead = ['Darwin', 'Frederick', 'Physics', 'Muuo',
    'PROTECTED', 'John', 'Platter', 'Amir', 'Elvira', 'Steve']
game55_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4', 'night, 5', 'day, 5']
game55_items = (game55_date, game55_number, game55_victory, game55_roles,
    game55_raw_seq_dead, game55_cult_leader, game55_treated_who,
    game55_treated_seq_dead, game55_day_time_seq)

game56_date = 'Jul-16'
game56_number = '2'
game56_victory = 'villagers'
game56_roles = {'John': 'werewolf', 'Caroline': 'werewolf',
    'Sohrab': 'villager', 'Frederick': 'villager', 'Elvira': 'seer',
    'Steve': 'villager', 'Darwin': 'bodyguard', 'Physics': 'werewolf',
    'Platter': 'villager', 'Amir': 'villager'}
game56_raw_seq_dead = ('Steve-w', 'Sohrab-l', 'PROTECTED', 'Amir-l',
    'Platter-w', 'John-l', 'PROTECTED', 'Caroline-l', 'Frederick-w',
    'Physics-l')
game56_cult_leader = ()
game56_treated_who = ['ww', 'L', 'PROTECTED', 'L', 'ww', 'L', 'PROTECTED', 'L',
    'ww', 'L']
game56_treated_seq_dead = ['Steve', 'Sohrab', 'PROTECTED', 'Amir', 'Platter',
    'John', 'PROTECTED', 'Caroline', 'Frederick', 'Physics']
game56_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4', 'night, 5', 'day, 5']
game56_items = (game56_date, game56_number, game56_victory, game56_roles,
    game56_raw_seq_dead, game56_cult_leader, game56_treated_who,
    game56_treated_seq_dead, game56_day_time_seq)

game57_date = 'Jul-16'
game57_number = '3'
game57_victory = 'villagers'
game57_roles = {'Platter': 'werewolf', 'Darwin': 'villager',
    'Sohrab': 'villager', 'Frederick': 'bodyguard', 'Elvira': 'villager',
    'Lazar': 'villager', 'Steve': 'werewolf', 'Caroline': 'werewolf',
    'Physics': 'seer', 'Amir': 'villager'}
game57_raw_seq_dead = ('PROTECTED', 'Platter-l', 'Physics-w', 'Steve-l',
    'Elvira-w', 'Lazar-l', 'Darwin-w', 'Amir-l', 'Sohrab-w', 'Caroline-l')
game57_cult_leader = ()
game57_treated_who = ['PROTECTED', 'L', 'ww', 'L', 'ww', 'L', 'ww', 'L', 'ww',
    'L']
game57_treated_seq_dead = ['PROTECTED', 'Platter', 'Physics', 'Steve', 'Elvira',
    'Lazar', 'Darwin', 'Amir', 'Sohrab', 'Caroline']
game57_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4', 'night, 5', 'day, 5']
game57_items = (game57_date, game57_number, game57_victory, game57_roles,
    game57_raw_seq_dead, game57_cult_leader, game57_treated_who,
    game57_treated_seq_dead, game57_day_time_seq)

game58_date = 'Jul-16'
game58_number = '4'
game58_victory = 'werewolves'
game58_roles = {'Darwin': 'villager', 'Platter': 'werewolf',
    'Caroline': 'villager', 'Sohrab': 'werewolf', 'Frederick': 'villager',
    'Elvira': 'seer', 'Lazar': 'villager', 'Steve': 'villager',
    'John': 'werewolf', 'Amir': 'bodyguard'}
game58_raw_seq_dead = ('Elvira-w', 'John-l', 'Amir-w', 'Platter-l',
    'Caroline-w', 'Darwin-l', 'Steve-w', 'time&out', 'Lazar-w', 'Frederick-l')
game58_cult_leader = ()
game58_treated_who = ['ww', 'L', 'ww', 'L', 'ww', 'L', 'ww', 'ww', 'L']
game58_treated_seq_dead = ['Elvira', 'John', 'Amir', 'Platter', 'Caroline',
    'Darwin', 'Steve', 'Lazar', 'Frederick']
game58_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'night, 4', 'day, 4']
game58_items = (game58_date, game58_number, game58_victory, game58_roles,
    game58_raw_seq_dead, game58_cult_leader, game58_treated_who,
    game58_treated_seq_dead, game58_day_time_seq)

game59_date = 'Jul-16'
game59_number = '5'
game59_victory = 'werewolves'
game59_roles = {'Caroline': 'werewolf', 'Darwin': 'villager',
    'Andrew': 'villager', 'Frederick': 'villager', 'Lazar': 'werewolf',
    'Elvira': 'villager', 'Steve': 'villager', 'John': 'villager',
    'Physics': 'seer', 'Platter': 'bodyguard', 'Amir': 'werewolf'}
game59_raw_seq_dead = ('PROTECTED', 'Lazar-l', 'Darwin-w', 'Frederick-l',
    'Physics-w', 'Amir-l', 'Elvira-w', 'Andrew-l', 'Steve-w', 'John-l')
game59_cult_leader = ()
game59_treated_who = ['PROTECTED', 'L', 'ww', 'L', 'ww', 'L', 'ww', 'L', 'ww',
    'L']
game59_treated_seq_dead = ['PROTECTED', 'Lazar', 'Darwin', 'Frederick',
    'Physics', 'Amir', 'Elvira', 'Andrew', 'Steve', 'John']
game59_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4', 'night, 5', 'day, 5']
game59_items = (game59_date, game59_number, game59_victory, game59_roles,
    game59_raw_seq_dead, game59_cult_leader, game59_treated_who,
    game59_treated_seq_dead, game59_day_time_seq)

game60_date = 'Jul-16'
game60_number = '6'
game60_victory = 'werewolves'
game60_roles = {'Darwin': 'werewolf', 'Caroline': 'bodyguard',
    'Andrew': 'werewolf', 'Steve': 'villager', 'John': 'seer',
    'Platter': 'cursed', 'Physics': 'villager', 'Amir': 'villager'}
game60_raw_seq_dead = ('John-w', 'Platter-l', 'PROTECTED', 'Amir-l',
    'Caroline-w', 'time&out', 'Physics-w', 'Steve-l')
game60_cult_leader = ()
game60_treated_who = ['ww', 'L', 'PROTECTED', 'L', 'ww', 'ww', 'L']
game60_treated_seq_dead = ['John', 'Platter', 'PROTECTED', 'Amir', 'Caroline',
    'Physics', 'Steve']
game60_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'night, 3', 'day, 3']
game60_items = (game60_date, game60_number, game60_victory, game60_roles,
    game60_raw_seq_dead, game60_cult_leader, game60_treated_who,
    game60_treated_seq_dead, game60_day_time_seq)

game61_date = 'Jul-16'
game61_number = '7'
game61_victory = 'villagers'
game61_roles = {'Darwin': 'seer', 'Elvira': 'werewolf', 'Andrew': 'bodyguard',
    'Caroline': 'villager', 'Physics': 'werewolf', 'Platter': 'villager'}
game61_raw_seq_dead = ('Platter-w', 'Physics-l', 'Caroline-w', 'time&out',
    'PROTECTED', 'Elvira-l')
game61_cult_leader = ()
game61_treated_who = ['ww', 'L', 'ww', 'PROTECTED', 'L']
game61_treated_seq_dead = ['Platter', 'Physics', 'Caroline', 'PROTECTED',
    'Elvira']
game61_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'night, 2', 'day, 2']
game61_items = (game61_date, game61_number, game61_victory, game61_roles,
    game61_raw_seq_dead, game61_cult_leader, game61_treated_who,
    game61_treated_seq_dead, game61_day_time_seq)

game62_date = 'Jul-16'
game62_number = '8'
game62_victory = 'villagers'
game62_roles = {'Platter': 'werewolf', 'Darwin': 'villager',
    'Andrew': 'werewolf', 'Elvira': 'seer', 'Steve': 'villager',
    'John': 'villager', 'Caroline': 'villager', 'Physics': 'bodyguard'}
game62_raw_seq_dead = ('Steve-w', 'Caroline-l', 'Darwin-w', 'time&out',
    'John-w', 'Platter-l', 'PROTECTED', 'Andrew-l')
game62_cult_leader = ()
game62_treated_who = ['ww', 'L', 'ww', 'ww', 'L', 'PROTECTED', 'L']
game62_treated_seq_dead = ['Steve', 'Caroline', 'Darwin', 'John', 'Platter',
    'PROTECTED', 'Andrew']
game62_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'night, 2', 'day, 2',
    'night, 3', 'day, 3']
game62_items = (game62_date, game62_number, game62_victory, game62_roles,
    game62_raw_seq_dead, game62_cult_leader, game62_treated_who,
    game62_treated_seq_dead, game62_day_time_seq)

game63_date = 'Jul-23'
game63_number = '1'
game63_victory = 'werewolves'
game63_roles = {'Darwin': 'seer', 'Navid': 'werewolf', 'Foosball': 'werewolf',
    'Sohrab': 'villager', 'Frederick': 'villager', 'Lazar': 'bodyguard',
    'John': 'villager', 'Peter': 'werewolf', 'Platter': 'villager'}
game63_raw_seq_dead = ('Darwin-w', 'John-l', 'Sohrab-w', 'Frederick-l',
    'PROTECTED', 'Platter-l')
game63_cult_leader = ()
game63_treated_who = ['ww', 'L', 'ww', 'L', 'PROTECTED', 'L']
game63_treated_seq_dead = ['Darwin', 'John', 'Sohrab', 'Frederick', 'PROTECTED',
    'Platter']
game63_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3']
game63_items = (game63_date, game63_number, game63_victory, game63_roles,
    game63_raw_seq_dead, game63_cult_leader, game63_treated_who,
    game63_treated_seq_dead, game63_day_time_seq)

game64_date = 'Jul-23'
game64_number = '2'
game64_victory = 'villagers'
game64_roles = {'Caroline': 'werewolf', 'Foosball': 'bodyguard',
    'Peter': 'villager', 'Lazar': 'werewolf', 'Steve': 'seer',
    'Platter': 'werewolf'}
game64_raw_seq_dead = ('Foosball-w', 'Lazar-l', 'Steve-w', 'Platter-l',
    'Peter-w', 'Caroline-l')
game64_cult_leader = ()
game64_treated_who = ['ww', 'L', 'ww', 'L', 'ww', 'L']
game64_treated_seq_dead = ['Foosball', 'Lazar', 'Steve', 'Platter', 'Peter',
    'Caroline']
game64_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3']
game64_items = (game64_date, game64_number, game64_victory, game64_roles,
    game64_raw_seq_dead, game64_cult_leader, game64_treated_who,
    game64_treated_seq_dead, game64_day_time_seq)

game65_date = 'Jul-23'
game65_number = '3'
game65_victory = 'villagers'
game65_roles = {'Platter': 'cursed', 'Navid': 'werewolf', 'Sohrab': 'werewolf',
    'Frederick': 'villager', 'Andrew': 'villager', 'Steve': 'bodyguard',
    'Caroline': 'seer'}
game65_raw_seq_dead = ('Frederick-w', 'Sohrab-l', 'Andrew-w', 'Navid-l')
game65_cult_leader = ()
game65_treated_who = ['ww', 'L', 'ww', 'L']
game65_treated_seq_dead = ['Frederick', 'Sohrab', 'Andrew', 'Navid']
game65_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2']
game65_items = (game65_date, game65_number, game65_victory, game65_roles,
    game65_raw_seq_dead, game65_cult_leader, game65_treated_who,
    game65_treated_seq_dead, game65_day_time_seq)

game66_date = 'Jul-23'
game66_number = '4'
game66_victory = 'villagers'
game66_roles = {'Darwin': 'bodyguard', 'Navid': 'seer', 'Lazar': 'villager',
    'Andrew': 'villager', 'Steve': 'werewolf', 'John': 'werewolf',
    'Amir': 'werewolf'}
game66_raw_seq_dead = ('PROTECTED', 'John-l', 'Lazar-w', 'Andrew-l',
    'PROTECTED', 'Steve-l', 'PROTECTED', 'Amir-l')
game66_cult_leader = ()
game66_treated_who = ['PROTECTED', 'L', 'ww', 'L', 'PROTECTED', 'L',
    'PROTECTED', 'L']
game66_treated_seq_dead = ['PROTECTED', 'John', 'Lazar', 'Andrew', 'PROTECTED',
    'Steve', 'PROTECTED', 'Amir']
game66_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4']
game66_items = (game66_date, game66_number, game66_victory, game66_roles,
    game66_raw_seq_dead, game66_cult_leader, game66_treated_who,
    game66_treated_seq_dead, game66_day_time_seq)

game67_date = 'Jul-23'
game67_number = '5'
game67_victory = 'werewolves'
game67_roles = {'Caroline': 'werewolf', 'Navid': 'villager',
    'Foosball': 'cursed', 'Sohrab': 'villager', 'Darwin': 'villager',
    'Andrew': 'bodyguard', 'Lazar': 'villager', 'Steve': 'werewolf',
    'Platter': 'seer', 'Amir': 'werewolf'}
game67_raw_seq_dead = ('Darwin-w', 'Lazar-l', 'Sohrab-w', 'Caroline-l',
    'Andrew-w', 'time&out', 'Platter-w', 'Amir-l', 'Navid-w', 'Foosball-l')
game67_cult_leader = ()
game67_treated_who = ['ww', 'L', 'ww', 'L', 'ww', 'ww', 'L', 'ww', 'L']
game67_treated_seq_dead = ['Darwin', 'Lazar', 'Sohrab', 'Caroline', 'Andrew',
    'Platter', 'Amir', 'Navid', 'Foosball']
game67_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'night, 3', 'day, 3', 'night, 4', 'day, 4']
game67_items = (game67_date, game67_number, game67_victory, game67_roles,
    game67_raw_seq_dead, game67_cult_leader, game67_treated_who,
    game67_treated_seq_dead, game67_day_time_seq)

game68_date = 'Jul-23'
game68_number = '6'
game68_victory = 'werewolves'
game68_roles = {'Darwin': 'werewolf', 'Caroline': 'villager',
    'Foosball': 'villager', 'Sohrab': 'villager', 'Lazar': 'cursed',
    'Andrew': 'seer', 'Steve': 'bodyguard', 'John': 'villager',
    'Platter': 'werewolf'}
game68_raw_seq_dead = ('Andrew-w', 'Sohrab-l', 'Foosball-w', 'time&out',
    'John-w', 'Darwin-l', 'Caroline-w', 'Lazar-l', 'Steve-w')
game68_cult_leader = ()
game68_treated_who = ['ww', 'L', 'ww', 'ww', 'L', 'ww', 'L', 'ww']
game68_treated_seq_dead = ['Andrew', 'Sohrab', 'Foosball', 'John', 'Darwin',
    'Caroline', 'Lazar', 'Steve']
game68_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'night, 2', 'day, 2',
    'night, 3', 'day, 3', 'night, 4']
game68_items = (game68_date, game68_number, game68_victory, game68_roles,
    game68_raw_seq_dead, game68_cult_leader, game68_treated_who,
    game68_treated_seq_dead, game68_day_time_seq)

game69_date = 'Jul-02'
game69_number = '3'
game69_victory = 'werewolves'
game69_roles = {'Alexei': 'villager', 'Sartaj': 'bomb', 'Platter': 'cub',
    'Philippa': 'villager', 'Frederick': 'villager', 'Elvira': 'seer',
    'Laura': 'werewolf', 'John': 'villager', 'Sandra': 'villager',
    'Darwin': 'werewolf', 'Physics': 'bodyguard'}
game69_raw_seq_dead = ('John-w', 'Darwin-l', 'Sartaj-wb', 'Sandra-wb',
    'Frederick-l', 'PROTECTED', 'Alexei-l', 'Philippa-w', 'Platter-l',
    'Physics-w', 'Elvira-w')
game69_cult_leader = ()
game69_treated_who = ['ww', 'L', 'wb', 'wb', 'L', 'PROTECTED', 'L', 'ww', 'L',
    'ww', 'ww']
game69_treated_seq_dead = ['John', 'Darwin', 'Sartaj', 'Sandra', 'Frederick',
    'PROTECTED', 'Alexei', 'Philippa', 'Platter', 'Physics', 'Elvira']
game69_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'night, 2', 'day, 2',
    'night, 3', 'day, 3', 'night, 4', 'day, 4', 'night, 5', 'night, 5']
game69_items = (game69_date, game69_number, game69_victory, game69_roles,
    game69_raw_seq_dead, game69_cult_leader, game69_treated_who,
    game69_treated_seq_dead, game69_day_time_seq)

game70_date = 'Jul-02'
game70_number = '4'
game70_victory = 'villagers'
game70_roles = {'Sartaj': 'villager', 'Muuo': 'bodyguard', 'Platter': 'seer',
    'Philippa': 'werewolf', 'Frederick': 'villager', 'Laura': 'villager',
    'John': 'werewolf', 'Physics': 'cub'}
game70_raw_seq_dead = ('Frederick-w', 'Laura-l', 'PROTECTED', 'John-l',
    'Sartaj-w', 'Physics-l', 'Muuo-w', 'Philippa-l')
game70_cult_leader = ()
game70_treated_who = ['ww', 'L', 'PROTECTED', 'L', 'ww', 'L', 'ww', 'L']
game70_treated_seq_dead = ['Frederick', 'Laura', 'PROTECTED', 'John', 'Sartaj',
    'Physics', 'Muuo', 'Philippa']
game70_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'day, 2', 'night, 3',
    'day, 3', 'night, 4', 'day, 4']
game70_items = (game70_date, game70_number, game70_victory, game70_roles,
    game70_raw_seq_dead, game70_cult_leader, game70_treated_who,
    game70_treated_seq_dead, game70_day_time_seq)

game71_date = 'Jul-02'
game71_number = '5'
game71_victory = 'villagers'
game71_roles = {'Muuo': 'werewolf', 'Platter': 'villager', 'Frederick': 'seer',
    'Elvira': 'cub', 'Laura': 'villager', 'Sandra': 'werewolf',
    'Darwin': 'villager', 'Physics': 'bodyguard'}
game71_raw_seq_dead = ('PROTECTED', 'Elvira-l', 'Physics-w', 'Darwin-w',
    'Platter-l', 'Frederick-w', 'Sandra-l', 'Laura-w', 'Muuo-l')
game71_cult_leader = ()
game71_treated_who = ['PROTECTED', 'L', 'ww', 'ww', 'L', 'ww', 'L', 'ww', 'L']
game71_treated_seq_dead = ['PROTECTED', 'Elvira', 'Physics', 'Darwin',
    'Platter', 'Frederick', 'Sandra', 'Laura', 'Muuo']
game71_day_time_seq = ['night, 1', 'day, 1', 'night, 2', 'night, 2', 'day, 2',
    'night, 3', 'day, 3', 'night, 4', 'day, 4']
game71_items = (game71_date, game71_number, game71_victory, game71_roles,
    game71_raw_seq_dead, game71_cult_leader, game71_treated_who,
    game71_treated_seq_dead, game71_day_time_seq)

Apr_09_session = (game1_items, game2_items)
Apr_23_session = (game3_items, game4_items, game5_items, game6_items)
Apr_30_session = (game7_items, game8_items, game9_items, game10_items,
    game11_items, game12_items, game13_items)
May_07_session = (game14_items, game15_items, game16_items, game17_items,
    game18_items, game19_items, game20_items)
May_14_session = (game21_items, game22_items, game23_items, game24_items)
May_21_session = (game25_items, game26_items, game27_items)
May_23_session = (game28_items, game29_items, game30_items, game31_items)
Jun_04_session = (game32_items, game33_items, game34_items, game35_items,
    game36_items)
Jun_11_session = (game37_items, game38_items, game39_items, game40_items)
Jun_19_session = (game41_items, game42_items, game43_items, game44_items,
    game45_items, game46_items, game47_items)
Jun_24_session = (game48_items, game49_items)
Jul_02_session = (game50_items, game51_items, game69_items, game70_items,
    game71_items)
Jul_09_session = (game52_items, game53_items, game54_items)
Jul_16_session = (game55_items, game56_items, game57_items, game58_items,
    game59_items, game60_items, game61_items, game62_items)
Jul_23_session = (game63_items, game64_items, game65_items, game66_items,
    game67_items, game68_items)


def allesroles(sessions):
    all_rolez = {}
    i = 0
    while i < len(sessions):
        x = sessions[i]
        print "i before: ", i
        print x[3]
        for key, value in x[3].items():
            all_rolez[key] = all_rolez.get(key, 0) + 1
        i += 1
        print "i after: ", i
    return all_rolez

def what_is_missing(sessions, restored_roles, start_n):
    """compares game_roles with sessions_dict and says what is missing"""
    i = 0
    n = start_n
    restored_roles_file = open('restored.py', 'a')
    print "SESSION LEN", len(sessions)
    while i < len(sessions):
        x = sessions[i]
        print 'SESSION %d' % (i), x[3]
        for key, value in restored_roles.items():
            if key not in x[3]:
                restored_roles_file.write('game%d_roles MISSING == \'%s\': \'villager\'' % \
                (n, key))
                restored_roles_file.write('\n')
            else:
                pass
        n += 1
        i += 1

kk = allesroles(Jul_23_session)
zz = what_is_missing(Jul_23_session, kk, 63)
