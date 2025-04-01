################################################ Import modules ########################################################

import json
import os
import pandas as pd
import time

############################################### Modify if needed #######################################################
t = 0

##################################################### Main objectives ##################################################
# Merge f4 and f5.
# As merging criteria, I will use ID + Calving Date.

##################################################### Notes ############################################################
# According to result `US24UW990JEPL.01.04.01_implement_FreqYearX35f5.svg`, a lot of lines do not have Calving Date.

################################################## Specific objectives #################################################

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

#################################################### Generic Functions #################################################

print(f'\n Defining general functions: \n'
      f'Define `tp`.')
def tp(ti, tf):
    d = tf - ti
    hh = str(int(d // 60 ** 2)).zfill(2)
    d %= 60 ** 2
    mm = str(int(d // 60)).zfill(2)
    d = 60 * (d % 60)
    ss = str(int(d // 60)).zfill(2)

    return f'Elapsed time (hh:mm:ss) is {hh}:{mm}:{ss}\n'

print('Define `folder_handler`.')
def folder_handler(root=s, cn=CN):
    if cn in os.listdir(root):
        pass
    else:
        os.mkdir(os.path.join(root, cn, 'implement'))
        os.mkdir(os.path.join(root, cn, 'test'))

print(f'Create folders `{CN}` if no present.')
folder_handler()

print('Define `path_to_save`.')
def path_to_save(extension, test=t, cn=CN, root=s):
    if test:
        file_name = cn + '_test' + extension
        path = os.path.join(root, cn, 'test', file_name)

    else:
        file_name = cn + '_impl' + extension
        path = os.path.join(root, cn, 'implement', file_name)
    return path

################################################ Read Format 4 & 5 map #################################################

print('\n Read Format 4 & 5 map.')
def get_format_map(root = s):
    f4_map_path = os.path.join(root, 'US24UW990JEPL.01.02.03.f4map.json')
    f5_map_path = os.path.join(root, 'US24UW990JEPL.01.02.02.f5map.json')

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
        raise Exception("Make sure `format_file` is 4 or 5")
    return list(map_i[x].keys())[0].split('-> ')[-1]

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

################################################# Working in txt files #################################################

print('Working in Format 5 txt file \n'
      'Define `get_txt_file_path`.')
def get_txt_file_path(testing=t):
    if testing:
        path_f4 = '/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.01_babyimplf4.txt'
        path_f5 = '/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.01_babyimplf5.txt'
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

##################################################### Standardization X3 ###############################################

n = 2
pdf4['X3'] = pdf4['X3'].str.replace(' '*n, '0'*n, regex=False)
pdf5['X3'] = pdf5['X3'].str.replace(' '*n, '0'*n, regex=False)

##################################################### Standardization X4 ###############################################

n = 3
pdf4['X4'] = pdf4['X4'].str.replace(' '*n, '0'*n, regex=False)
pdf5['X4'] = pdf5['X4'].str.replace(' '*n, '0'*n, regex=False)

##################################################### Standardization X5 ###############################################

n = 12
pdf4['X5'] = pdf4['X5'].str.replace(' '*n, '0'*n, regex=False)
pdf5['X5'] = pdf5['X5'].str.replace(' '*n, '0'*n, regex=False)

##################################################### Standardization X35 ##############################################

n=8
pdf4['X35'] = pdf4['X35'].str.replace(' '*n, '0'*n, regex=False)
pdf5['X35'] = pdf5['X35'].str.replace(' '*n, '0'*n, regex=False)

######################################################### Sort by Key ##################################################

print('Sort by Key. \n Key concatenation.')
pdf4['concat_key'] = pdf4['X3'] + pdf4['X4'] + pdf4['X5'] + pdf4['X35']
pdf5['concat_key'] = pdf5['X3'] + pdf5['X4'] + pdf5['X5'] + pdf5['X35']

print('Sort `pdf4`.')
pdf4 = pdf4.sort_values(by='concat_key')
print('Sort `pdf5`.')
pdf5 = pdf5.sort_values(by='concat_key')

#################################### Split data in duplicated and non duplicated key in f4 #############################

print('Split data in duplicated and non duplicated key in f4.')
repeated_keys = pdf4['concat_key'][pdf4['concat_key'].duplicated(keep=False)]
unique_keys = pdf4['concat_key'][~pdf4['concat_key'].duplicated(keep=False)]

pdf4_unique = pdf4[pdf4['concat_key'].isin(unique_keys)]
pdf4_repeated = pdf4[pdf4['concat_key'].isin(repeated_keys)]

pdf4 = pdf4.drop(columns='concat_key')
pdf4_unique = pdf4_unique.drop(columns='concat_key')
pdf4_repeated = pdf4_repeated.drop(columns='concat_key')

print(f'\n pdf4.shape[0]: {pdf4.shape[0]} \n'
      f'pdf4_unique.shape[0]: {pdf4_unique.shape[0]} \n'
      f'pdf4_repeated.shape[0]: {pdf4_repeated.shape[0]} \n'
      f'100*pdf4_unique.shape[0]/pdf4.shape[0]: {100*pdf4_unique.shape[0]/pdf4.shape[0]} \n'
      f'100*pdf4_repeated.shape[0]/pdf4.shape[0]: {100*pdf4_repeated.shape[0]/pdf4.shape[0]} \n')

assert pdf4_unique.shape[0] + pdf4_repeated.shape[0] == pdf4.shape[0]

#################################### Split data in duplicated and non duplicated key in f5 #############################

print('Split data in duplicated and non duplicated key in f5.')
repeated_keys = pdf5['concat_key'][pdf5['concat_key'].duplicated(keep=False)]
unique_keys = pdf5['concat_key'][~pdf5['concat_key'].duplicated(keep=False)]

pdf5_unique = pdf5[pdf5['concat_key'].isin(unique_keys)]
pdf5_repeated = pdf5[pdf5['concat_key'].isin(repeated_keys)]

pdf5 = pdf5.drop(columns='concat_key')
pdf5_unique = pdf5_unique.drop(columns='concat_key')
pdf5_repeated = pdf5_repeated.drop(columns='concat_key')

print(f'\n pdf5.shape[0]: {pdf5.shape[0]} \n'
      f'pdf5_unique.shape[0]: {pdf5_unique.shape[0]} \n'
      f'pdf5_repeated.shape[0]: {pdf5_repeated.shape[0]} \n'
      f'100*pdf5_unique.shape[0]/pdf5.shape[0]: {100*pdf5_unique.shape[0]/pdf5.shape[0]} \n'
      f'100*pdf5_repeated.shape[0]/pdf5.shape[0]: {100*pdf5_repeated.shape[0]/pdf5.shape[0]} \n')

assert pdf5_unique.shape[0] + pdf5_repeated.shape[0] == pdf5.shape[0]

######################################################### Save dataset #################################################

print('Define `pdf_to_txt`.')
def pdf_to_txt(pdf, pth):
    with open(pth, 'w') as f:
        for _, row in pdf.iterrows():
            concat_str = ''.join(row.astype(str))
            f.write(concat_str + '\n')

print('Saving `pdf4_unique` in: \n', path_to_save(extension='_uniquef4.txt'))
pdf_to_txt(pdf4_unique, path_to_save(extension='_uniquef4.txt'))

print('Saving `pdf4_nounique` in: \n', path_to_save(extension='_nouniquef4.txt'))
pdf_to_txt(pdf4_repeated, path_to_save(extension='_nouniquef4.txt'))

print('Saving `pdf5_unique` in: \n', path_to_save(extension='_uniquef5.txt'))
pdf_to_txt(pdf5_unique, path_to_save(extension='_uniquef5.txt'))

print('Saving `pdf5_nounique` in: \n', path_to_save(extension='_nouniquef5.txt'))
pdf_to_txt(pdf5_repeated, path_to_save(extension='_nouniquef5.txt'))

###################################################### Finish ##########################################################

fin = time.time()
print(f'\n Execution {CN} finished when testing is {t} \n'
      f'Reading data in {s}. \n'
      f'{tp(ini, fin)}\n')