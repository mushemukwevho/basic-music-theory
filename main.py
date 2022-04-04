#  UMUZI
#  Mushe Mukwevho, mushemukwevho@gmail.com
#  2022

import random


def get_music_notes()->int:
    """Randomly generating two music notes and returning the the number of semitones
    between them.

    Returns:
        int: the number of semitones between notes.
    """
    ordered_list = \
        ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']
    choices = random.choices(ordered_list, k=2) #  Generate two random items from list
    
    #  If the second note is found within the first iteration
    if ordered_list.index(choices[1]) > ordered_list.index(choices[0]):      
        num_semitones = abs(ordered_list.index(choices[1])-ordered_list.index(choices[0]))
    
    #  If the second notes is found in the 2nd iteration, then
    else: 
        list_len = len(ordered_list)
        
        #  Get the first note position relative to the end of the list
        relative_note_position = list_len - ordered_list.index(choices[0])
        
        #  Get the second note position relative to the start of the list, completing a cycle
        num_semitones = relative_note_position + ordered_list.index(choices[1])
    print(f"\nNotes: '{choices[0]}' and '{choices[1]}'")
    return num_semitones



def play_game()->bool:
    """User guess how many semitones are between the notes.
    Returns:
        False: Game didn't play.
        True: Game played successful.
    """
    output = False
    while True:
        print("=========================Music Theory=========================")
        # Get music notes
        semitones=get_music_notes()
        # Get user input
        user_input = \
            input('\nGuess how many semitones are between the notes or "Give up":\n')
        
        while user_input.isnumeric():  # Check for numbers when looping
            if eval(user_input)== semitones:
                print("Correct!")
                break
            elif eval(user_input)!= semitones:
                print("Incorrect!")
                user_input = input('\nTry again or "Give up":\n')
        
        if not user_input.isnumeric():  # Check for text
            if user_input.lower() in ["give up", "giveup", "stop"]:
                print(f"Correct answer: {semitones}")
                user_input_2 = input('\nPlay again? Y/N:\n')
                if user_input_2.lower() in ["y", "yes"]:
                    continue
                if user_input_2.lower() in ["n", "no"]:
                    break
            
            else:
                print("Enter a relevant response!")
                
        output = True
                
    return output

            
if __name__=='__main__':
    """The script will run when it is the 'main' script being run.
    That is to make sure that it doesn't run within other scripts when imported.
    Only its code will be used then."""

    play_game()
