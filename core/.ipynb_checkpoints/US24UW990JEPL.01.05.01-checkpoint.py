################################################ Import modules ########################################################

import json
import os
import matplotlib.pyplot as plt
import pandas as pd
import time

############################################### Modify if needed #######################################################
t = 0
pl_show = 0

##################################################### Main objectives ##################################################
# Merge f4 and f5.
# As merging criteria, I will use ID + Calving Date.

##################################################### Notes ############################################################
# According to result `US24UW990JEPL.01.04.01_implement_FreqYearX35f5.svg`, a lot of lines do not have Calving Day.

################################################## Specific objectives #################################################
# I need to understand the merging criteria.
# I am concerned that duplications may complicate the merging step.

# Format 4 and 5 have Animal Identification Information (ID) in X3, X4, X5.
# Then ID is the concatenation of X3 + X4 + X5.

# Format 4 and 5 have Calving Date (YYYYMMDD) in X35.

# I will concatenate X3 + X4 + X5 + X35 to create a key.

# f4 and f5 will be divided in 2:
# f4s1/f5s1: with lines spanning a key without duplications.
# f4c1/f5c1: with lines not in f4s1/f5s1.

# From there, working with f4s1/f5s1 would be safe, while f4c1/f5c1 will require more work.

# In a perfect world, most of the data will be in f4s1/f5s1 (finger crossed!).

# You must clearly record the proportion of data in each step.
###################################################### Initialization ##################################################

print(f'Initialization: \n')
ini = time.time()
time_tuple = time.localtime(ini)
formatted_time = time.strftime("%m-%d-%Y at %I:%M %p", time_tuple)
CN = os.path.splitext(os.path.basename(__file__))[0]
p = '/blue/mateescu/agustinchasco/Projects/reprojersey/core'
s = '/blue/mateescu/agustinchasco/Projects/reprojersey/data'


print(f'Code {CN + ".py"} starts. \n'
      f'Codes executed when testing is {t}. \n'
      f'Reading data in {s}. \n'
      f'Running program in {p}. \n'
      f'Saving data in {s}. \n'
      f'Time profiling starts. Program executed on {formatted_time} \n')

######################################## Create folder if not present ##################################################

print('\n Create folders if not present.')
if CN not in os.listdir():
    os.makedirs(CN)

f1 = 'test'
f2 = 'implement'
if f1 not in os.listdir(CN):
    os.makedirs(os.path.join(CN, f1))

if f2 not in os.listdir(CN):
    os.makedirs(os.path.join(CN, f2))

print('Define `path_to_save_plot`.')
def path_to_save_plot(extension, test=t, branch_test=f1, branch_implement=f2, cn=CN, root=p):
    if test:
        branch = branch_test
        set_extension = cn + '_test_' + extension
    else:
        branch = branch_implement
        set_extension = cn + '_implement_' + extension
    path = os.path.join(root, cn, branch, set_extension)
    return path

print('Define `path_to_save`.')
def path_to_save_data(extension, test=t, cn=CN, root=s):
    if test:
        file_name = cn + '_babytest' + extension
    else:
        file_name = cn + '_babyimpl' + extension
    path = os.path.join(root, file_name)
    return path

print('Define `plot_show`.')
def plot_show(showing=pl_show):
    if showing:
        plt.show()

#################################################### Generic Functions #################################################

print(f'\n Defining general functions: \n'
      f'Define `tp`.')

def tp(ti, tf):
    """
    Function takes an initial and final timing. Then return hh:mm:ss.

    :param ti: initial `time.time()`
    :param tf: final `time.time()`
    :return: elapsed time expressed as hh:mm:ss.
    """

    d = tf - ti
    hh = str(int(d // 60 ** 2)).zfill(2)
    d %= 60 ** 2
    mm = str(int(d // 60)).zfill(2)
    d = 60 * (d % 60)
    ss = str(int(d // 60)).zfill(2)

    return f'Elapsed time (hh:mm:ss) is {hh}:{mm}:{ss}\n'

################################################ Read Format 4 & 5 map #################################################

print('\n Read Format 4 & 5 map.')
def get_format_map(root = s):
    f4_map_path = os.path.join(root, 'US24UW990JEPL.01.02.03.f4map.json')
    f5_map_path = os.path.join(root, 'US24UW990JEPL.01.02.02.f5map.json') ##

    with open(f4_map_path) as f4:
        mapf4 = json.load(f4)

    with open(f5_map_path) as f5:
        mapf5 = json.load(f5)

    return mapf4, mapf5

################################################## Map column to label #################################################

print('Map column to label. Define `col_label`.')
def col_label(x, format_file):
    if format_file == 4:
        map_i = get_format_map()[0]
    elif format_file == 5:
        map_i = get_format_map()[1]
    else:
        raise Exception("Make sure `foramt_file` is 4 or 5")
    return list(map_i[x].keys())[0].split('-> ')[-1]

print('Visualize column. Define `plot_frequencies`.')
def plot_frequencies(x, df, testing=t, index='y'):
    if df.shape[1] == 314:
        ff=4
    elif df.shape[1] == 336:
        ff=5
    else:
        print('Dataframe passed as argument of `df` must have 314 (f4) or 336 (f5) columns. Execution stopped.')
        assert False


    if index == 'y':
        counts = df[x].value_counts().sort_values(ascending=False)
    elif index == 'x':
        counts = df[x].value_counts().sort_index()
    else:
        print('Check `index` is x or y')
        assert False
    print(f'Frequency distribution in {x} when `t` is {testing}: \n'
          f'{counts}')

    plt.figure(figsize=(12, 6))
    plt.bar(counts.index, counts.values, color='skyblue')

    for key_z, value_z in enumerate(counts.values):
        plt.text(counts.index[key_z], value_z + 50, str(value_z), ha='center', va='bottom')

    lab_i = col_label(x=x, format_file=ff) + ' in format ' + str(ff)
    plt.xlabel(col_label(x=x, format_file=ff))
    plt.ylabel('Counts')
    plt.title(f'Frequency Distribution in {lab_i} \n')

    plt.xticks(rotation=45)
    plt.tight_layout()
    plot_show()
    plt.savefig(path_to_save_plot(f'Freq{x}f{ff}.svg'), format='svg', dpi=300)

############################################ Functions for Splitting rows ##############################################

print('Functions for Splitting rows: \n'
      'Define function `idx_maper`.')
def idx_maper(idx_field):
    if '-' not in idx_field:
        return int(idx_field) - 1

    else:
        idx_i = int(idx_field.split('-')[0]) - 1
        idx_f = int(idx_field.split('-')[-1])
        return idx_i, idx_f


print('Define function `line_chopper`.')
def line_chopper(line_i, dict_map):
    row = []

    for key1, val1 in dict_map.items():
        idx = idx_maper(dict_map[key1][list(val1.keys())[0]])
        if isinstance(idx, tuple):
            idx_i = idx[0]
            idx_f = idx[-1]
            row.append(line_i[idx_i:idx_f])
        else:
            row.append(line_i[idx])

    return row

############################################# Working in Format 5 txt file #############################################

print('Working in Format 5 txt file \n'
      'Define `get_txt_file_path`.')
def get_txt_file_path(testing=t):
    if testing:
        path_f4 = '/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.01.01_testf4.txt'
        path_f5 = '/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.01.01_testf5.txt'
    else:
        path_f4 = '/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.01.01_f4.txt'
        path_f5 = '/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.01.01_f5.txt'

    return path_f4, path_f5

print('Define `txt_reader`.')
def txt_reader(format_file):
    ll = []
    if format_file == 4:
        ffp = get_txt_file_path()[0]
        ffm = get_format_map()[0]
    elif format_file == 5:
        ffp = get_txt_file_path()[1]
        ffm = get_format_map()[1]
    else:
        print('Parameter `format_file` accepts only integers 4 or 5. Error raised.')
        assert False

    with open(ffp, 'r') as fi:
        for l in fi:
            ll.append(line_chopper(l, ffm))

    return pd.DataFrame(ll, columns=list(ffm.keys()))

print('Reading F4 & F5 txt data!')
pdf4 = txt_reader(format_file=4)
pdf5 = txt_reader(format_file=5)

#################################################### Show Shape in both datasets #######################################
print(f'print(pdf4.shape): {pdf4.shape} \n'
      f'print(pdf5.shape): {pdf5.shape} \n')

################################################## Check ID X3, X4 in f4 and 5 #########################################

print('Check ID X3, X4 in f4 and 5')
plot_frequencies(x='X3', df=pdf4)
plot_frequencies(x='X3', df=pdf5)
plot_frequencies(x='X4', df=pdf4)
plot_frequencies(x='X4', df=pdf5)

############################################### Quantify missing X5 in f4 and 5 ########################################

print('\n Quantify missing X5 in f4 and 5 \n')
counts_f4X5 = (pdf4['X5'] == '            ') | (pdf4['X5'] == '000000000000')
counts_f4X5miss = counts_f4X5.sum()
counts_f4X5ok = pdf4.shape[0] - counts_f4X5miss
print(f'counts_f4X5miss: \n'
      f'{counts_f4X5miss} \n'
      f'counts_f4X5ok: \n'
      f'{counts_f4X5ok} \n')

counts_f5X5 = (pdf5['X5'] == '            ') | (pdf5['X5'] == '000000000000')
counts_f5X5miss = counts_f5X5.sum()
counts_f5X5ok = pdf5.shape[0] - counts_f5X5miss
print(f'counts_f5X5miss: \n'
      f'{counts_f5X5miss} \n'
      f'counts_f5X5ok: \n'
      f'{counts_f5X5ok} \n')

cats = ['f4X5miss', 'f4X5ok', 'f5X5miss', 'f5X5ok']
vals = [counts_f4X5miss, counts_f4X5ok, counts_f5X5miss, counts_f5X5ok]

plt.figure(figsize=(12, 6))
plt.bar(cats, vals, color='skyblue')

for key_i, value_i in enumerate(vals):
    plt.text(cats[key_i], value_i + 50, str(value_i), ha='center', va='bottom')

lab = col_label(x='X5', format_file=4) + ' in format 4 and 5'
plt.xlabel(col_label(x='X5', format_file=4))
plt.ylabel('Counts')
plt.title(f'Frequency Distribution in {lab} \n')

plt.xticks(rotation=45)
plt.tight_layout()
plot_show()
plt.savefig(path_to_save_plot(f'FreqX5f4&5.svg'), format='svg', dpi=300)

######################################### Sample 1% of unique keys in pdf4 and pdf5 ####################################

print('Sampling datasets')
ps = 0.005
pdf4['key'] = pdf4[['X3', 'X4', 'X5', 'X35']].astype(str).agg(''.join, axis=1)
pdf5['key'] = pdf5[['X3', 'X4', 'X5', 'X35']].astype(str).agg(''.join, axis=1)

n = pdf4['key'].nunique()
n_sample = int(n*ps) + (n*ps % 1 > 0)
unique_keys = pdf4['key'].unique()

sample_keys = pd.Series(unique_keys).sample(n=n_sample, random_state=22).tolist()
print(f'length unique keys (n) = {n} \n'
      f'n_sample = {n_sample} \n')

spdf4 = pdf4[pdf4['key'].isin(sample_keys)].drop(columns=['key'])
spdf5 = pdf5[pdf5['key'].isin(sample_keys)].drop(columns=['key'])

################################################### Save sampled datasets ##############################################

print('Saving sampled datasets')
babypath_f4 = path_to_save_data(extension='f4.txt')
babypath_f5 = path_to_save_data(extension='f5.txt')

spdf4.astype(str).agg(func=''.join, axis=1).to_csv(path_or_buf=babypath_f4, index=False, header=False)
spdf5.astype(str).agg(func=''.join, axis=1).to_csv(path_or_buf=babypath_f5, index=False, header=False)

print(f'Testing is {t}. \n'
      f'Sampled `spdf4` saved in path below: \n'
      f'{babypath_f4} \n\n'
      f'Sampled `spdf5` saved in path below: \n'
      f'{babypath_f5} \n')

###################################################### Finish ##########################################################

fin = time.time()
print(f'\n Execution {CN} finished when testing is {t} \n'
      f'Reading data in {s}. \n'
      f'{tp(ini, fin)}\n')