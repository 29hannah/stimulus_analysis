# Edit running configurations: Emulate terminal in output console
import random
import slab
import os
import pathlib
from os.path import join
import csv

speaker_id = 1
listener = 'hannah'

# Get files

def abs_file_paths(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            if not f.startswith('.'):
                yield pathlib.Path(join(dirpath, f))

folder_path = pathlib.Path

root = '/Users/hannahsmacbook/Final_stimuli_recordings/'
folder_path = root + 'Speaker-' + str(speaker_id) + '_files' + '/Speaker-' + str(speaker_id) + '_tries/normalised'

all_file_names = [f for f in abs_file_paths(root + 'Speaker-'+str(speaker_id)+'_files/Speaker-'+str(speaker_id)+'_tries/normalised')]

'''
def play_sounds(path):
    for file in path:
        slab.Sound.play_file(file)


def training(speaker_id):
    path_1 = list(pathlib.Path(root + 'Speaker-' + str(speaker_id) + '_files' + '/Speaker-' + str(speaker_id) + '_tries/normalised').glob('*dist-1*'))
    path_2 = list(pathlib.Path(root + 'Speaker-' + str(speaker_id) + '_files' + '/Speaker-' + str(speaker_id) + '_tries/normalised').glob('*dist-2*'))
    path_3 = list(pathlib.Path(root + 'Speaker-' + str(speaker_id) + '_files' + '/Speaker-' + str(speaker_id) + '_tries/normalised').glob('*dist-3*'))
    path_4 = list(pathlib.Path(root + 'Speaker-' + str(speaker_id) + '_files' + '/Speaker-' + str(speaker_id) + '_tries/normalised').glob('*dist-4*'))
    path_5 = list(pathlib.Path(root + 'Speaker-' + str(speaker_id) + '_files' + '/Speaker-' + str(speaker_id) + '_tries/normalised').glob('*dist-5*'))

    #print("Distance_1")
    play_sounds(path_1)
    #print("Distance_2")
    play_sounds(path_2)
    #print("Distance_3")
    play_sounds(path_3)
    #print("Distance_4")
    play_sounds(path_4)
    #print("Distance_5")
    play_sounds(path_5)
training(speaker_id)
'''

def experiment(speaker_id, listener):
    random.shuffle(all_file_names)
    # Get list of sound_ids and responses
    sound_id_list = []
    response_list = []
    print("press key after sound is played")
    for file in all_file_names:
        sound_id = file.stem
        sound_id_list.append(sound_id)
        slab.Sound.play_file(file)
        with slab.key() as key:  # wait for a key press
            response = key.getch()
        if response == 49:
            response_list.append("1")
        elif response == 50:
            response_list.append("2")
        elif response == 51:
            response_list.append("3")
        elif response == 52:
            response_list.append("4")
        elif response == 53:
            response_list.append("5")

    '''
    print(sound_id_list)
    print(len(sound_id_list))
    print(response_list)
    print(len(response_list))
    '''

    # Create a list with sound_id and response
    result_list = list(zip(sound_id_list, response_list))
    print(result_list)
    # Sort list
    sorted_result_list = sorted(result_list, key=lambda tup: tup[0])
    print(sorted_result_list)

    # Write .csv file
    with open('speaker-' + str(speaker_id) + '_' + str(listener) + '.csv', 'w') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['sound_id', 'response_'+ str(listener)])
        for row in sorted_result_list:
            csv_out.writerow(row)

experiment(speaker_id, listener)