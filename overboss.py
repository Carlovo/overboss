import random

types = [
    ('forest', 'kobold'),
    ('graveyard', 'skeleton'),
    ('camp', 'orc'),
    ('cave', 'dragon'),
    ('swamp', 'witch'),
    ('castle', 'vampire'),
    ('volcano', 'elemental'),
    ('summoning circle', 'sorcerobe'),
    ('cloud island', 'harpy'),
    ('desert', 'sandworm'),
    ('tower', 'eye'),
]

print('Please choose 5 terrain/monster types from:')
for i, tile_type in enumerate(types):
    i_str = f' {i}' if i < 10 else f'{i}'
    print(f'{i_str}. {tile_type[0]} ({tile_type[1]})')

print('')

type_map = {}

for i, tile_type in enumerate(types):
    while 1 > 0:
        user_input = input(f'Would you like to play with terrain type {tile_type[0]} ({tile_type[1]})? (y/n) ')
        if user_input == 'n':
            break
        elif user_input == 'y':
            type_map[len(type_map)] = i
            break
        else:
            print('Only "y" (yes) or "n" (no) are accepted')
    if len(type_map) == 5:
        break
else:
    print('5 types are required, but less were selected, please try again')
    exit()

print('')

print('You will be playing with:')

for mapped_type in type_map.values():
    print(f'{types[mapped_type][0]} ({types[mapped_type][1]})')

print('')

tiles = [i for i in range(0, 5 * 12 + 8)]
tokens = [i for i in range(0, 5 * 10 + 5 + 6 + 7)]

random.shuffle(tiles)
random.shuffle(tokens)

tiles_taken = set()
tokens_taken = set()

while 1 > 0:
    user_input = input('Press enter to continue (input q to quit): ')
    if user_input == 'q':
        break
    elif user_input == 't':
        user_input = input('Which terrain tile would you like to return to the bag: ')
        if not user_input.isnumeric():
            print('Only numbers are accepted\n')
            continue
        input_int = int(user_input)
        if input_int > 67:
            print('Number too big\n')
        elif input_int in tiles_taken:
            tiles_taken.remove(input_int)
            tiles.append(input_int)
            random.shuffle(tiles)
            print('Done!\n')
        else:
            print('Number is not yet drawn\n')
    elif user_input == 'm':
        user_input = input('Which monster token would you like to return to the bag: ')
        if not user_input.isnumeric():
            print('Only numbers are accepted\n')
            continue
        input_int = int(user_input)
        if input_int > 67:
            print('Number too big\n')
        elif input_int in tokens_taken:
            tokens_taken.remove(input_int)
            tokens.append(input_int)
            random.shuffle(tokens)
            print('Done!\n')
        else:
            print('Number is not yet drawn\n')
    else:
        tile = tiles.pop()
        token = tokens.pop()

        tiles_taken.add(tile)
        tokens_taken.add(token)

        if tile < 5 * 12:
            type_no = tile // 12
            tile_no = tile % 12
            terrain_type = type_map[type_no]

            tile_str = f'{tile}' if tile > 9 else f' {tile}'
            type_no_str = f'{type_no}' if type_no > 9 else f' {type_no}'
            tile_no_str = f'{tile_no}' if tile_no > 9 else f' {tile_no}'

            if terrain_type == 1:
                # graveyard
                if tile_no < 3:
                    points = 3
                elif tile_no < 7:
                    points = 2
                else:
                    points = 1
                print(tile_str, type_no_str, tile_no_str, types[terrain_type][0], points)
            elif terrain_type == 2:
                # camp
                if tile_no < 2:
                    color = 'purple'
                elif tile_no < 4:
                    color = 'blue'
                elif tile_no < 6:
                    color = 'yellow'
                elif tile_no < 8:
                    color = 'orange'
                elif tile_no < 10:
                    color = 'red'
                else:
                    color = 'black'
                print(tile_str, type_no_str, tile_no_str, types[terrain_type][0], color)
            else:
                print(tile_str, type_no_str, tile_no_str, types[terrain_type][0])
        else:
            print(tile, ' -  -', 'dungeon')

        if token < 5 * 10:
            type_no = token // 10
            token_type = type_map[type_no]

            token_str = f'{token}' if token > 9 else f' {token}'
            type_no_str = f'{type_no}' if type_no > 9 else f' {type_no}'

            print(token_str, type_no_str, ' -', types[token_type][1])
        elif token < 55:
            type_no = token - 50
            token_type = type_map[type_no]

            type_no_str = f'{type_no}' if type_no > 9 else f' {type_no}'

            print(token, type_no_str, ' -', types[token_type][0], 'crystal')
        elif token < 61:
            print(token, ' -  -', 'miniboss')
        else:
            print(token, ' -  -', 'portal')

        print('')
