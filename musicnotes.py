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

all_notes = ["do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"]

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
    else: return actual + adding

def play_notes():
    #print(all_notes.index("la#"))
    note=""
    concat=[]
    steps=[]
    while(note!="end"):
        concat = []
        note = input("Which note do you want me to play? ")
        try:
            if len(note)>4:
                notes = note.split()
                note1 = notes[0]
                modifier = notes[1]
                initial_index = int(all_notes.index(note1))
                print(note1, modifier, initial_index)
                concat.append(note1)
                #steps = get_semitones(modifier)
                #print(steps[1])
                #print(type(steps))
                print(get_correct_index(initial_index, get_semitones1(modifier)))
                note2 = all_notes[get_correct_index(initial_index, get_semitones1(modifier))]
                concat.append(note2)
                print(get_correct_index(get_correct_index(initial_index, get_semitones1(modifier)), get_semitones2(modifier)))
                note3 = all_notes[get_correct_index(get_correct_index(initial_index, get_semitones1(modifier)), get_semitones2(modifier))]
                concat.append(note3)
                print(concat)
            else:
                try:
                    print(all_notes[all_notes.index((note.strip()))])
                except Exception as e:
                    print("This does not exist", str(e))
        except Exception as e:
            print("This does not exist. ", str(e))

def save_song():
    pass

def play_song():
    pass

def general_menu():
    pass

def main():
    play_notes()

if __name__ == "__main__":
    main()