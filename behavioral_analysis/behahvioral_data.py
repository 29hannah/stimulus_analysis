# Edit running configurations: Emulate terminal in output console
import random
import slab
import os
import pathlib
from os.path import join
import csv


# Get files
def abs_file_paths(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            if not f.startswith('.'):
                yield pathlib.Path(join(dirpath, f))


folder_path = pathlib.Path
all_file_names = [f for f in abs_file_paths("/Users/hannahsmacbook/Test_folder")]
# Randomize order of files
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
with open('test_listener_1.csv', 'w') as out:
    csv_out = csv.writer(out)
    csv_out.writerow(['sound_id', 'response_listener_1'])
    for row in sorted_result_list:
        csv_out.writerow(row)
