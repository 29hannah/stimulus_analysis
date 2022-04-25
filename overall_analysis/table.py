import slab
import statistics
import os
import pathlib
from os.path import join
import pandas as pd
import csv


def abs_file_paths(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            if not f.startswith('.'):
                yield pathlib.Path(join(dirpath, f))


folder_path = pathlib.Path
all_file_names = [f for f in abs_file_paths("/Users/hannahsmacbook/Pilot_stimuli_2")]


names_of_files = ['%{0}%'.format(filenames) for filenames in all_file_names]
sound_id = [elem[39:60] for elem in names_of_files]  # edit the right numbers!
pre_projected_distance = [elem[53:54] for elem in names_of_files]  # edit the right numbers!
projected_distance=[int(elem) for elem in pre_projected_distance]
# speaker_gender = [elem[71:92] for elem in names_of_files]  # edit the right numbers!
# speaker_age = [elem[71:92] for elem in names_of_files]  # edit the right numbers!

centroid_list = []
onset_slope_list = []
rolloff_list = []
flatness_list = []

for file_name in all_file_names:
    sound = slab.Binaural(file_name)
    centroid = statistics.mean(sound.spectral_feature(feature='centroid'))
    centroid_list.append(centroid)
    onset_slope = sound.onset_slope()
    onset_slope_list.append(onset_slope)
    rolloff = statistics.mean(sound.spectral_feature(feature='rolloff'))
    rolloff_list.append(rolloff)
    flatness = statistics.mean(sound.spectral_feature(feature='flatness'))
    flatness_list.append(flatness)

# features_object = dict(zip(sound_id, zip(projected_distance, speaker_gender, speaker_age, centroid_list,
#                                         onset_slope_list, rolloff_list, flatness_list)))

features_object = dict(zip(sound_id, zip(projected_distance, centroid_list, onset_slope_list, rolloff_list,
                                         flatness_list)))


# Write table without brackets
with open('Pilot_stimuli_analysis.csv', 'w+') as f:
    writer = csv.writer(f)
    for k, v in features_object.items():
        writer.writerow([k, *v])

# Add names to columns
'''
df = pd.read_csv('Pilot_stimuli_analysis.csv', header=None)
df.rename(columns={0: 'sound_id', 1: 'projected_distance', 2: 'speaker_gender', 3: 'speaker_age', 4: 'centroid',
                   5: 'onset_slope', 6: 'rolloff', 7: 'flatness'}, inplace=True)
df.to_csv('Final_Pilot_stimuli_analysis.csv', index=False)
'''

df = pd.read_csv('Pilot_stimuli_analysis.csv', header=None)
df.rename(columns={0: 'sound_id', 1: 'projected_distance', 2: 'centroid', 3: 'onset_slope', 4: 'rolloff', 5: 'flatness'}
          , inplace=True)
df.to_csv('Final_Pilot_stimuli_analysis.csv', index=False)
