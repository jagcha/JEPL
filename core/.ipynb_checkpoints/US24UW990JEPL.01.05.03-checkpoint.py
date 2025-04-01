################################################ Import modules ########################################################

import json
import os
import pandas as pd
import time

############################################### Modify if needed #######################################################
t = 1

##################################################### Main objectives ##################################################
# Format 4 has production data, and low frequency of recorded Abortion.
# Format 5 has reproduction data.
# By merging Format 4 and 5, the abortion can be observed in a better context.
# Potentially, by using information in both files, I can better predict early abortions per lactation.

# As merging criteria, I propose to use the key X3 + X4 + X5 + X35 (ID + Calving date).

# However, often times in a given file key is duplicated.

# Such duplications will imply conflict while merging. Such duplications are a problem when trying to combine datasets.

# We can split our datasets in 2 for each format file:
# f4 - 1) US24UW990JEPL.01.05.02_impl_uniquef4.txt
# f4 - 2) US24UW990JEPL.01.05.02_impl_nouniquef4.txt
# f5 - 1) US24UW990JEPL.01.05.02_impl_uniquef5.txt
# f5 - 2) US24UW990JEPL.01.05.02_impl_nouniquef5.txt

# Files with unique key are:
# f4 - 1) US24UW990JEPL.01.05.02_impl_uniquef4.txt
# f5 - 1) US24UW990JEPL.01.05.02_impl_uniquef5.txt

# Files with duplicated key are:
# f4 - 2) US24UW990JEPL.01.05.02_impl_nouniquef4.txt
# f5 - 2) US24UW990JEPL.01.05.02_impl_nouniquef5.txt

# Among lines in Files with duplicated keys, some of them may result in consistent or inconsistent duplications.

# 2 or more lines with consistent duplications are rows with the same key and also same records in remaining columns.
# In other words, rows that are exactly the same.

# 2 or more rows with inconsistent duplications are lines with the same key, but with something different in any of their columns.
# In other words, 2 rows with inconsistent duplicated key are not exactly the same, despite key is the same.

# Then, files with duplicated key are divided in consistent and inconsistent duplications.

# Consistent duplications can be filtered out, and unique observations can be merged to the corresponding file with unique keys.

# Inconsistent duplications can be stored in a different file for further corrections.

# The objective of this code is to:

# 1- Split US24UW990JEPL.01.05.02_impl_nouniquef4.txt/US24UW990JEPL.01.05.02_impl_nouniquef5.txt in consistent and inconsistent.
# 2- Store inconsistent in a well-defined folder. Latter I will solve this issue.
# 3- Filter out consistent duplications and merge consistent observations correspondent standardized files:

# Potential bug: if I stack files in `US24UW990JEPL.01.05.02_impl_uniquef(4/5).txt`, I will run the risk of overriding
# the file if code 010502 is executed, missing rows added by 010503.

# Rewarding memory usage, is better to avoid save similar datasets again and again.

# However, I am worried with the possibility of overriding a useful file with an incomplete one. This is why I will
# create new folder 010503 to allocate all files generated by 010503.

# Once the pipeline is set, I can combine all script in a single one, and delete intermediate steps.
# But for now, I prefer to avoid painful mistakes.

# f4 - 1) US24UW990JEPL.01.05.03_impl_uniquef4.txt
# f5 - 1) US24UW990JEPL.01.05.03_impl_uniquef5.txt

# 4- Keep track on the amount of lines that are going to each path:
# f4 - 1) US24UW990JEPL.01.05.03_impl_uniquef4.txt (crf: addition of corrected consisted duplications)
# f5 - 1) US24UW990JEPL.01.05.03_impl_uniquef5.txt (")

# f4 - 2) US24UW990JEPL.01.05.02_impl_nouniquef4.txt
# f4 - 2.1) US24UW990JEPL.01.05.03_impl_nouniquef4cns.txt
# f4 - 2.1.1) US24UW990JEPL.01.05.03_impl_nouniquef4cnsunq.txt (Show how many duplications you deleted, how many you kept)
# f4 - 2.2) US24UW990JEPL.01.05.03_impl_nouniquef4ncns.txt

# f5 - 2) US24UW990JEPL.01.05.02_impl_nouniquef5.txt
# f5 - 2.1) US24UW990JEPL.01.05.03_impl_nouniquef5cns.txt
# f5 - 2.1.1) US24UW990JEPL.01.05.03_impl_nouniquef5cnsunq.txt (Show how many duplications you deleted, how many you kept)
# f5 - 2.2) US24UW990JEPL.01.05.02_impl_nouniquef5ncns.txt

# In short: the focus of this script is to deal with these files:
# f4 - 2) US24UW990JEPL.01.05.02_impl_nouniquef4.txt
# f5 - 2) US24UW990JEPL.01.05.02_impl_nouniquef5.txt
# Then identify consistent duplications, filter out duplicated data, add data to already correct observations, and store inconsistent duplications.

##################################################### Notes ############################################################
# Input data is in:
# /blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.02/implement

# Be tidy

################################################## Specific objectives #################################################

###################################################### Initialization ##################################################

print(f'Initialization: \n')
ini = time.time()
time_tuple = time.localtime(ini)
formatted_time = time.strftime("%m-%d-%Y at %I:%M %p", time_tuple)
CN = os.path.splitext(os.path.basename(__file__))[0]
CNr = CN[:-2] + '0' + str(int(CN[-2:]) - 1)
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
    """
    Creates a folder `cn` inside `root` if it does not exist,
    along with `implement` and `test` subfolders.
    """
    cn_path = os.path.join(root, cn)
    if not os.path.exists(cn_path):
        os.makedirs(os.path.join(cn_path, 'implement'))
        os.makedirs(os.path.join(cn_path, 'test'))

print(f'Create folders `{CN}` if not present.')
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

print('Define `path_to_read`.')
def path_to_read(test=t, root=s, folder=CNr):
    if test:
        sub = 'test'
    else:
        sub = 'implement'
    return os.path.join(root, folder, sub)

print(f'Targeting files in directory {path_to_read()}')


def get_txt_files_path(idx, testing=t, path=path_to_read(), cnr=CNr):
    if idx not in [0, 1]:
        print(f'Argument `idx` must be in [0, 1]. \n'
              f'Argument {idx} not in [0, 1]. Forced error')
        assert False

    idf = ['nounique', 'unique'][idx]
    if testing:
        m = '_test_'
    elif t==0:
        m = '_impl_'
    else:
        print('Crf with variable `t`. It must be 0 or 1. Assertion forced.')
        assert False

    f4 = cnr + m + idf + 'f4.txt'
    f5 = cnr + m + idf + 'f5.txt'
    pf4 = os.path.join(path, f4)
    pf5 = os.path.join(path, f5)
    return pf4, pf5

print('Define `pdf_to_txt`.')
def pdf_to_txt(pdf, pth):
    with open(pth, 'w') as f:
        for _, row in pdf.iterrows():
            concat_str = ''.join(row.astype(str))
            f.write(concat_str + '\n')

print("\n Targeted files:\n" +
      "\n".join(get_txt_files_path(i)[z] for z in (0, 1) for i in (0, 1)))

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

############################################ Functions for Splitting rows ##############################################

print('\n Functions for Splitting rows: \n'
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

print('\n Working in Format 5 txt file \n'
      'Define `get_txt_files_path`.')

print('Define `txt_reader`.')
def txt_reader(format_file, target_file):
    """
    Return pandas file.
    :param format_file: 4 or 5
    :param target_file: 0 = nounique. 1 = unique
    :return: pandas dataset
    """
    assert target_file in [0, 1]
    ll = []
    if format_file == 4:
        val = 0
    elif format_file == 5:
        val = 1
    else:
        raise ValueError("Forced error. `format_file` 4 or 5 w/o exception.")
    ffp = get_txt_files_path(target_file)[val]
    ffm = get_format_map()[val]
    with open(ffp, 'r') as fi:
        for l in fi:
            ll.append(line_chopper(l, ffm))

    return pd.DataFrame(ll, columns=list(ffm.keys()))

print('Reading F4 unique!')
pdf4u01 = txt_reader(format_file=4, target_file=1)
print('Reading F4 no-unique!')
pdf4nu01 = txt_reader(format_file=4, target_file=0)
print('Reading F5 unique!')
pdf5u01 = txt_reader(format_file=5, target_file=1)
print('Reading F5 no-unique! \n')
pdf5nu01 = txt_reader(format_file=5, target_file=0)

#################################################### Show Shape in both datasets #######################################
print(f'\n Report initial number of rows for each file.\n'
      f'pdf4u01.shape[0] = {pdf4u01.shape[0]}\n'
      f'pdf4nu01.shape[0] = {pdf4nu01.shape[0]} \n'
      f'pdf5u01.shape[0] = {pdf5u01.shape[0]} \n'
      f'pdf5nu01.shape[0] = {pdf5nu01.shape[0]}\n')

###################################################### Subsets with unique data ########################################

# So far, I do not have to work in this subset. Keys are consistent and unique.
# In latter steps, corrected keys will be stacked at the bottom of this dataset.
# This is why I track the number of rows.
# Make key. Useful for check.
pdf4u01['concat_key'] = pdf4u01['X3'] + pdf4u01['X4'] + pdf4u01['X5'] + pdf4u01['X35']
pdf5u01['concat_key'] = pdf5u01['X3'] + pdf5u01['X4'] + pdf5u01['X5'] + pdf5u01['X35']

################################################### f4: solving duplications ###########################################

# Concatenate all columns. Use concatenation as Key2. Find duplicated Key2. Keep 1 of each group. Track rows. Discard redundancy.
pdf4nu02 = pdf4nu01.drop_duplicates() # Eliminate duplicated rows (key2)
pdf4nu02 = pdf4nu02.reset_index(drop=True)
n = pdf4nu01.shape[0] - pdf4nu02.shape[0]

# Quantify eliminations.
print(f'\n Number of dropped rows due duplications: \n'
      f'pdf4nu02.shape[0] = {pdf4nu02.shape[0]} \n'
      f'pdf4nu01.shape[0] - pdf4nu02.shape[0] = {n} \n'
      f'100*n/pdf4nu01.shape[0] = {100*n/pdf4nu01.shape[0]} \n')

# Identify key1 that are not duplicated anymore.
pdf4nu02['concat_key'] = pdf4nu02['X3'] + pdf4nu02['X4'] + pdf4nu02['X5'] + pdf4nu02['X35']
pdf4nu02 = pdf4nu02.sort_values(by='concat_key')

pdf4nu02_unique_keys = pdf4nu02['concat_key'][~pdf4nu02['concat_key'].duplicated(keep=False)]
pdf4nu02_unique = pdf4nu02[pdf4nu02['concat_key'].isin(pdf4nu02_unique_keys)]
pdf4nu02_repeat = pdf4nu02[~pdf4nu02['concat_key'].isin(pdf4nu02_unique_keys)]

assert pdf4nu02_unique.shape[0] + pdf4nu02_repeat.shape[0] == pdf4nu02.shape[0]
assert (pdf4nu02_unique['concat_key'].value_counts() > 1).sum() == 0
assert not pdf4nu02_unique['concat_key'].isin(pdf4u01['concat_key']).any()

# Add `pdf4nu02_unique` with consistent rows w/o duplications to the already existing `pdf4u01`
pdf4u02 = pd.concat([pdf4u01, pdf4nu02_unique], ignore_index=True)
pdf4u02.reset_index(drop=True, inplace=True)
pdf4u02 = pdf4u02.sort_values(by='concat_key')
pdf4nu02_repeat = pdf4nu02_repeat.sort_values(by='concat_key')

# Report number of rows.
print(f'\n pdf4u01.shape[0] = {pdf4u01.shape[0]} \n'
      f'pdf4nu02_unique.shape[0] = {pdf4nu02_unique.shape[0]} \n'
      f'pdf4u02.shape[0] = {pdf4u02.shape[0]} \n'
      f'pdf4nu02_repeat.shape[0] = {pdf4nu02_repeat.shape[0]} \n'
      f'100*pdf4u02.shape[0]/(pdf4u02.shape[0] + pdf4nu02_repeat.shape[0]) = '
      f'{100*pdf4u02.shape[0]/(pdf4u02.shape[0] + pdf4nu02_repeat.shape[0])} \n'
      f'100*pdf4nu02_repeat.shape[0]/(pdf4u02.shape[0] + pdf4nu02_repeat.shape[0]) = '
      f'{100*pdf4nu02_repeat.shape[0]/(pdf4u02.shape[0] + pdf4nu02_repeat.shape[0])} \n')

assert pdf4u01.shape[0] + pdf4nu02_unique.shape[0] == pdf4u02.shape[0]
assert (pdf4u02['concat_key'].value_counts() > 1).sum() == 0

################################################### f5: solving duplications ###########################################
# Same procedure than before.

pdf5nu02 = pdf5nu01.drop_duplicates() # Eliminate duplicated rows (key2)
pdf5nu02 = pdf5nu02.reset_index(drop=True)
n = pdf5nu01.shape[0] - pdf5nu02.shape[0]

# Quantify eliminations.
print(f'Number of dropped rows due duplications: \n'
      f'pdf5nu02.shape[0] = {pdf5nu02.shape[0]} \n'
      f'pdf5nu01.shape[0] - pdf5nu02.shape[0] = {n} \n'
      f'100*n/pdf5nu01.shape[0] = {100*n/pdf5nu01.shape[0]} \n')

# Identify key1 that are not duplicated anymore.
pdf5nu02['concat_key'] = pdf5nu02['X3'] + pdf5nu02['X4'] + pdf5nu02['X5'] + pdf5nu02['X35']
pdf5nu02 = pdf5nu02.sort_values(by='concat_key')

pdf5nu02_unique_keys = pdf5nu02['concat_key'][~pdf5nu02['concat_key'].duplicated(keep=False)]
pdf5nu02_unique = pdf5nu02[pdf5nu02['concat_key'].isin(pdf5nu02_unique_keys)]
pdf5nu02_repeat = pdf5nu02[~pdf5nu02['concat_key'].isin(pdf5nu02_unique_keys)]
pdf5nu02_repeat = pdf5nu02_repeat.sort_values(by='concat_key')

assert pdf5nu02_unique.shape[0] + pdf5nu02_repeat.shape[0] == pdf5nu02.shape[0]
assert (pdf5nu02_unique['concat_key'].value_counts() > 1).sum() == 0
assert not pdf5nu02_unique['concat_key'].isin(pdf5u01['concat_key']).any()

# Add `pdf5nu02_unique` with consistent rows w/o duplications to the already existing `pdf5u01`
pdf5u02 = pd.concat([pdf5u01, pdf5nu02_unique], ignore_index=True)
pdf5u02.reset_index(drop=True, inplace=True)
pdf5u02 = pdf5u02.sort_values(by='concat_key')

# Report number of rows.
print(f'\n pdf5u01.shape[0] = {pdf5u01.shape[0]} \n'
      f'pdf5nu02_unique.shape[0] = {pdf5nu02_unique.shape[0]} \n'
      f'pdf5u02.shape[0] = {pdf5u02.shape[0]} \n'
      f'pdf5nu02_repeat.shape[0] = {pdf5nu02_repeat.shape[0]} \n'
      f'100*pdf5u02.shape[0]/(pdf5u02.shape[0] + pdf5nu02_repeat.shape[0]) = '
      f'{100*pdf5u02.shape[0]/(pdf5u02.shape[0] + pdf5nu02_repeat.shape[0])} \n'
      f'100*pdf5nu02_repeat.shape[0]/(pdf5u02.shape[0] + pdf5nu02_repeat.shape[0]) = '
      f'{100*pdf5nu02_repeat.shape[0]/(pdf5u02.shape[0] + pdf5nu02_repeat.shape[0])} \n')

assert pdf5u01.shape[0] + pdf5nu02_unique.shape[0] == pdf5u02.shape[0]
assert (pdf5u02['concat_key'].value_counts() > 1).sum() == 0

###################################################### Drop key ########################################################

pdf4u02 = pdf4u02.drop(columns='concat_key')
pdf4nu02_repeat = pdf4nu02_repeat.drop(columns='concat_key')

pdf5u02 = pdf5u02.drop(columns='concat_key')
pdf5nu02_repeat = pdf5nu02_repeat.drop(columns='concat_key')

######################################################### Save dataset #################################################

print('\n Saving `pdf4u02` in: \n', path_to_save(extension='_pdf4u.txt'))
pdf_to_txt(pdf4u02, path_to_save(extension='_pdf4u.txt'))

print('\n Saving `pdf4nu02_repeat` in: \n', path_to_save(extension='_pdf4nu.txt'))
pdf_to_txt(pdf4nu02_repeat, path_to_save(extension='_pdf4nu.txt'))

print('\n Saving `pdf5u02` in: \n', path_to_save(extension='_pdf5u.txt'))
pdf_to_txt(pdf5u02, path_to_save(extension='_pdf5u.txt'))

print('\n Saving `pdf5nu02_repeat` in: \n', path_to_save(extension='_pdf5nu.txt'))
pdf_to_txt(pdf5nu02_repeat, path_to_save(extension='_pdf5nu.txt'))

###################################################### Finish ##########################################################

fin = time.time()
print(f'\n Execution {CN} finished when testing is {t} \n'
      f'Reading data in {s}. \n'
      f'{tp(ini, fin)}\n')
