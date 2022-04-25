import slab
import statistics
import os
import pathlib
from os.path import join
import matplotlib.pyplot as plt
from pathlib import Path


def abs_file_paths(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            if not f.startswith('.'):
                yield pathlib.Path(join(dirpath, f))


folder_path = pathlib.Path


# Distance 1
path_1 = list(Path('/Users/hannahsmacbook/Pilot_stimuli_2').glob('*dis1*'))
sound_file_paths_dis1 = [f for f in path_1]
res_list_1 = []
for sound_file_path in sound_file_paths_dis1:
    sound = slab.Binaural(sound_file_path)
    cen = sound.onset_slope()
    res_list_1.append(cen)
c_1 = (statistics.mean(res_list_1))
c_sd_1 = (statistics.stdev(res_list_1))

# Distance 2
path_2 = list(Path('/Users/hannahsmacbook/Pilot_stimuli_2').glob('*dis2*'))
sound_file_paths_dis2 = [f for f in path_2]
res_list_2 = []
for sound_file_path in sound_file_paths_dis2:
    sound = slab.Binaural(sound_file_path)
    cen = sound.onset_slope()
    res_list_2.append(cen)
c_2 = (statistics.mean(res_list_2))
c_sd_2 = (statistics.stdev(res_list_2))


# Distance 3
path_3 = list(Path('/Users/hannahsmacbook/Pilot_stimuli_2').glob('*dis3*'))
sound_file_paths_dis3 = [f for f in path_3]
res_list_3 = []
for sound_file_path in sound_file_paths_dis3:
    sound = slab.Binaural(sound_file_path)
    cen = sound.onset_slope()
    res_list_3.append(cen)
c_3 = (statistics.mean(res_list_3))
c_sd_3 = (statistics.stdev(res_list_3))


# Distance 4
path_4 = list(Path('/Users/hannahsmacbook/Pilot_stimuli_2').glob('*dis4*'))
sound_file_paths_dis4 = [f for f in path_4]
res_list_4 = []
for sound_file_path in sound_file_paths_dis4:
    sound = slab.Binaural(sound_file_path)
    cen = sound.onset_slope()
    res_list_4.append(cen)
c_4 = (statistics.mean(res_list_4))
c_sd_4 = (statistics.stdev(res_list_4))

# Distance 5
path_5 = list(Path('/Users/hannahsmacbook/Pilot_stimuli_2').glob('*dis5*'))
sound_file_paths_dis5 = [f for f in path_5]
res_list_5 = []
for sound_file_path in sound_file_paths_dis5:
    sound = slab.Binaural(sound_file_path)
    cen = sound.onset_slope()
    res_list_5.append(cen)
c_5 = (statistics.mean(res_list_5))
c_sd_5 = (statistics.stdev(res_list_5))


# Final list with averaged centroid values for each distance
final_list_mean = [c_1, c_2, c_3, c_4, c_5]
print(final_list_mean)

# Calculate standard deviation for each distance
print("Standard deviation for each distance:")
final_list_stdev = [c_sd_1, c_sd_2, c_sd_3, c_sd_4, c_sd_5]
print(final_list_stdev)

# Relative centroid values compared to distance 1
print("Relative centroids:")
rel_cen = [x / c_1 for x in final_list_mean]
print(rel_cen)

# Overall list with all values for each distance
overall_list = [res_list_1, res_list_2, res_list_3, res_list_4, res_list_5]
'''
print(overall_list)
'''

# Creating boxplot
fig = plt.figure()
fig.suptitle('Onset slope over distance categories', fontsize=10)

ax = fig.add_subplot(111)
ax.boxplot(overall_list)

ax.set_xlabel('Distance category')
ax.set_ylabel('Onset slope')

'''
plt.show()
'''
plt.savefig("pilot2_onset_slope_overall")
