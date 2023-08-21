from time import sleep


all_notes = ["do", "do#", "re", "re#", "mi",
             "fa", "fa#", "sol", "sol#", "la", "la#", "si"]

song = {
    "name": "Dummy Song",
    "notes": [
        ['re', 'fa', 'la'],
        ['fa', 'la', 'do#']
    ]
}

songs = {}


def get_semitones(modifier):
    if modifier == "major":
        lista = [4, 3]
        return lista
    elif modifier == "minor":
        lista = [3, 4]
        return lista
    elif modifier == "augmented":
        lista = [4, 4]
        return lista


def get_semitones1(modifier):
    if modifier == "major":
        return 4
    elif modifier == "minor":
        return 3
    elif modifier == "augmented":
        return 4


def get_semitones2(modifier):
    if modifier == "major":
        return 3
    elif modifier == "minor":
        return 4
    elif modifier == "augmented":
        return 4


def get_correct_index(actual, adding):
    if actual + adding > 11:
        return actual + adding - 12
    else:
        return actual + adding


def cound_nested_dicts(d):
    count = 0
    for value in d.values():
        if isinstance(value, dict):
            count += 1 + cound_nested_dicts(value)
    return count


def is_in_use(name, option):
    for song_id, song_name in songs.items():
        if song_name['name'] == name:
            if option == 1:
                return True
            if option == 2:
                return song_id
    return False


def save_song_dict(name, notelists):
    while (is_in_use(name, 1) == True):
        name = input("Name " + name + " already in use, try another: ")
    # Create dict for the song
    song["name"] = name
    song["notes"] = notelists
    # Check the number of songs already saved and set new song's key to n+1
    songs["song" + str(cound_nested_dicts(songs)+1)] = song.copy() # use copy() to not change all values in songs dict
    print("Songs you have:\n",songs)


def play_notes(save):
    note = ""
    concat = []
    notelists = []
    while (note != "end"):
        concat = []
        note = input("Type 'end' to exit to menu\nWhich note do you want me to play? " if save ==
                     0 else "Write note to save to song: ")
        try:
            if len(note) > 4:
                notes = note.split()
                note1 = notes[0]
                modifier = notes[1]
                initial_index = int(all_notes.index(note1))
                concat.append(note1)
                note2 = all_notes[get_correct_index(
                    initial_index, get_semitones1(modifier))]
                concat.append(note2)
                note3 = all_notes[get_correct_index(get_correct_index(
                    initial_index, get_semitones1(modifier)), get_semitones2(modifier))]
                concat.append(note3)
                print(concat)

                if save == 1:
                    notelists.append(concat)
            else:
                try:
                    print(all_notes[all_notes.index((note.strip()))])
                    if save == 1:
                        notelists.append(
                            all_notes[all_notes.index((note.strip()))])
                except Exception as e:
                    print("This does not exist", str(e))
        except Exception as e:
            print("This does not exist. ", str(e))

    if save == 1:
        print("--Song will be saved--")
        save_song_dict(input("What's the song's name will be?: "), notelists)


def save_song():
    print("\n*****This is save Song*****\nType 'end' to SAVE THE SONG")
    play_notes(1)


def play_song():
    print("\n*****This is play song*****\n")
    search = input("Which song do you want to play?\n")
    if is_in_use(search, 2) is not False:
        for item in songs[is_in_use(search, 2)]['notes']: #loops through the songx key of the name found in the notes value
            print(item)
            sleep(1)
    else:
        print("---",search, "does not exist, please try with another song or save it.---")


def general_menu():
    option = ""
    while (option != "4"):
        option = input(
            "What do you want me to do?\n1.-Chord Player\n2.-Song Saver\n3.-Song Player\n4.-Exit\n")
        if option == "1":
            play_notes(0)
        elif option == "2":
            save_song()
        elif option == "3":
            play_song()
        elif option == "4":
            print("Goodbye")
            break
        else:
            print("Option not valid, please try again.")


def main():
    general_menu()


if __name__ == "__main__":
    main()
