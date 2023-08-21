from time import sleep


listoflists = []
lista = ["Hola1","Hola2","otro","unomas"]
lista2 = ["Hola", "viejo", "como", "estas"]
listoflists.append(lista)
listoflists.append(lista2)
print(listoflists)

notelist = [['re', 'fa#', 'la'], 're', 'do', ['fa', 'la', 'do#']]
print(notelist[0])
print(notelist[1])
print(notelist[2])
print(notelist[3])

songs = {
    'song1': {'name': 'margarita', 'notes': ['fa', 're', 'mi', 'fa', ['re', 'fa#', 'la']]},
    'song2': {'name': 'ginebra', 'notes': ['fa', 're', 'mi', 'fa', 'sol', ['sol', 'la', 'si']]},
    'song3': {'name': 'paloma', 'notes': ['fa', 're', 'mi', 'fa', ['re', 'fa#', 'la']]},
    'song4': {'name': 'perlanegra', 'notes': ['fa', 're', 'mi', 'fa', 'sol', ['sol', 'la', 'si']]},
    }

songs2 = {}

def cound_nested_dicts(d):
    count = 0
    for value in d.values():
        if isinstance(value, dict):
            count += 1 + cound_nested_dicts(value)
    return count

def is_in_use(name):
    for song_id, song_name in songs.items():
        if song_name['name'] == name:
            print("found:",song_name)
            print("id: ", song_id)
            return True

def is_in_use2(name):
    for song_id, song_name in songs.items():
        if song_name['name'] == name:
            print("found:",song_name)
            print("id: ", song_id)
            return song_id

print(songs)
print("Number of dicts: ", cound_nested_dicts(songs))
print(is_in_use('perlanegra'))
print(is_in_use2('perlanegra'))
print("\n\n", songs['song3']['notes'])

play_list = songs['song3']['notes']
print(play_list)
for item in play_list:
    print(item)
    sleep(1)
# print("Will look for perlanegra", is_in_use("perlanegra"))