"""
Create a code where the user can play the different type of musical chords
the user can save a song (multiple chords) and play the song

What is a chord?
A chord is basically a group of notes played at the same time and sound harmoniously,
there are many kind of chords, major, minor, augmented etc 

To create a chord we follow a formula: 
major:     base note + 4semitones + 3semitones
minor:     base note + 3semitones + 4semitones
augmented: base note + 4semitones + 4semitones
 
Example
We have all the notes 
all_notes = ["do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"]

If I want to play "do major" (base note + 4semitones + 3semitones)
My base note is "do" the second note is the 4th note next to my base note "mi", and from there the 3rd note next to my second note "sol"

do major
do mi sol

If I want to play "la# minor" (base note + 3semitones + 4semitones) 
My base note is "la#" the second note is the 3rd note next to my base note "do#" (if the array of notes is not enough, start again from the beginning) and from there the 4th note next to my second note "fa"

la minor
la# do# fa

sol augemneted
sol si re#


Execution Example:  (loop, the user can play many chords, save and play songs until write exit to finish the program )     
play chord do major             (user input)
["do","mi","sol"]               (code output)

play chord re minor             (user input)
["re", "fa", "la"]              (code output)
.......

save song my_first_song         (user input)
> re minor                      (user input first chord)
> la augmented                  (user input second chord)
> sol# major                    (user input third chord)
> do major                      (user input fourth chord)
> end                           (user input end of the song)
my_first_song saved             (output)

play song my_first_song
["re", "fa", "la"]              (code output + 1 sleep second)
["la", "do#", "fa"]             (code output + 1 sleep second)
["sol#","do", "re#"]            (code output + 1 sleep second)
["do", "mi", "sol"]             (code output + 1 sleep second)

exit                            (user input to exit the program)

"""

"""
To create a chord we follow a formula: 
major:     base note + 4semitones + 3semitones
minor:     base note + 3semitones + 4semitones
augmented: base note + 4semitones + 4semitones
"""

from time import sleep


all_notes = ["do", "do#", "re", "re#", "mi",
             "fa", "fa#", "sol", "sol#", "la", "la#", "si"]

notelists = []

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
            print("found:", song_name)
            print("id: ", song_id)
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
    print(songs)


def play_notes(save):
    note = ""
    concat = []
    notelists = []
    while (note != "end"):
        concat = []
        note = input("Which note do you want me to play? " if save ==
                     0 else "Write note to save to song: ")
        try:
            if len(note) > 4:
                notes = note.split()
                note1 = notes[0]
                modifier = notes[1]
                initial_index = int(all_notes.index(note1))
                print(note1, modifier, initial_index)
                concat.append(note1)
                print(get_correct_index(initial_index, get_semitones1(modifier)))
                note2 = all_notes[get_correct_index(
                    initial_index, get_semitones1(modifier))]
                concat.append(note2)
                print(get_correct_index(get_correct_index(initial_index,
                      get_semitones1(modifier)), get_semitones2(modifier)))
                note3 = all_notes[get_correct_index(get_correct_index(
                    initial_index, get_semitones1(modifier)), get_semitones2(modifier))]
                concat.append(note3)
                print(concat)

                if save == 1:
                    notelists.append(concat)
                    print(notelists)
            else:
                try:
                    print(all_notes[all_notes.index((note.strip()))])
                    if save == 1:
                        notelists.append(
                            all_notes[all_notes.index((note.strip()))])
                        print(notelists)
                except Exception as e:
                    print("This does not exist", str(e))
        except Exception as e:
            print("This does not exist. ", str(e))

    if save == 1:
        print("Song will be saved")
        save_song_dict(input("What's the song's name will be?: "), notelists)


def save_song():
    print("\n*****This is save Song*****\nType end to SAVE THE SONG")
    play_notes(1)


def play_song():
    print("\n*****This is play song*****\n")
    search = input("Which song do you want to play?\n")
    if is_in_use(search, 2) is not False:
        for item in songs[is_in_use(search, 2)]['notes']: #loops through the songx key of the name found in the notes value
            print(item)
            sleep(1)
    else:
        print(search, "does not exist, please try with another song or save it.")


def general_menu():
    option = ""
    while (option != "4"):
        option = input(
            "What do you want me to do?\n1.-Chord Player\n2.-Song Saver\n3.-Song Player\n4.-Exit\n")
        if option == "1":
            play_notes()
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
