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

path1=list(Path('/Users/hannahsmacbook/Test_folder').glob('*dis1*'))
path2=list(Path('/Users/hannahsmacbook/Test_folder').glob('*dis2*'))
path3=list(Path('/Users/hannahsmacbook/Test_folder').glob('*dis3*'))
path4=list(Path('/Users/hannahsmacbook/Test_folder').glob('*dis4*'))
path5=list(Path('/Users/hannahsmacbook/Test_folder').glob('*dis5*'))

# Define centroid analysis
def centroid (path):
    sound_file_paths = [f for f in path]
    res_list = []
    for sound_file_path in sound_file_paths:
        sound = slab.Binaural(sound_file_path)
        cen = statistics.mean(sound.spectral_feature(feature='centroid'))
        res_list.append(cen)
    return res_list

res_list_1=centroid(path1)
res_list_2=centroid(path2)
res_list_3=centroid(path3)
res_list_4=centroid(path4)
res_list_5=centroid(path5)

'''
c_1 = (statistics.mean(res_list_1))
c_sd_1 = (statistics.stdev(res_list_1))

c_2 = (statistics.mean(res_list_2))
c_sd_2 = (statistics.stdev(res_list_2))

c_3 = (statistics.mean(res_list_3))
c_sd_3 = (statistics.stdev(res_list_3))

c_4 = (statistics.mean(res_list_4))
c_sd_4 = (statistics.stdev(res_list_4))

c_5 = (statistics.mean(res_list_5))
c_sd_5 = (statistics.stdev(res_list_5))

# Final list with averaged centroid values for each distance
final_list_mean = [c_1, c_2, c_3, c_4, c_5]
print(final_list_mean)

# Standard deviation for each distance
print("Standard deviation for each distance:")
final_list_stdev = [c_sd_1, c_sd_2, c_sd_3, c_sd_4, c_sd_5]
print(final_list_stdev)

# Relative centroid values compared to dis_1
print("Relative centroids:")
rel_cen = [x / c_1 for x in final_list_mean]
print(rel_cen)
'''

# Creating boxplot
# Overall list with all values for each distance
overall_list = [res_list_1, res_list_2, res_list_3, res_list_4, res_list_5]


fig = plt.figure()
fig.suptitle('Centroid over distance categories', fontsize=10)

ax = fig.add_subplot(111)
ax.boxplot(overall_list)

ax.set_xlabel('Distance category')
ax.set_ylabel('Centroid')

plt.show()