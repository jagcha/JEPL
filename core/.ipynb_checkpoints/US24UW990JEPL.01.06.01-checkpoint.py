################################################ Import modules ########################################################
import numpy as np
import pandas as pd
import US24UW990JEPL_01

##################################################### Main objectives ##################################################
# Merge cleaner datasets.

##################################################### Notes ############################################################
# Incremental programming in `010601.ipynb`. Some visualizations on dataset.
# Still missing steps of standardization. But trying to advance with what I have.

################################################## Specific objectives #################################################

##################################################### Variables ########################################################
t = 0

###################################################### Initialization ##################################################
init = US24UW990JEPL_01.Initializer('/blue/mateescu/agustinchasco/Projects/reprojersey/data',
                                    '/blue/mateescu/agustinchasco/Projects/reprojersey/core',
                                    t)

# Creates directory if not present.
init.Directories()

# Initialize format mappers.
init.GetFormatMap()

########################################### Reading Files ##############################################################

print(f'Shifting file names as a function of t = {init.t} \n')
fn4_03 = None
fn5_03 = None
fn4_04 = None
fn5_04 = None

if init.t:
    fn4_03 = 'US24UW990JEPL.01.05.03_test_pdf4u.txt'
    fn5_03 = 'US24UW990JEPL.01.05.03_test_pdf5u.txt'
    fn4_04 = 'US24UW990JEPL.01.05.04_test_f4nu_u.txt'
    fn5_04 = 'US24UW990JEPL.01.05.04_test_f5nu_u.txt'
else:
    fn4_03 = 'US24UW990JEPL.01.05.03_impl_pdf4u.txt'
    fn5_03 = 'US24UW990JEPL.01.05.03_impl_pdf5u.txt'
    fn4_04 = 'US24UW990JEPL.01.05.04_impl_f4nu_u.txt'
    fn5_04 = 'US24UW990JEPL.01.05.04_impl_f5nu_u.txt'

print(f'Reading f4 data in 010503... \n')
pdf4_03 = init.TXT_reader(target_path=init.TargetPath(fn4_03),
                       format_file=4)
print(f'Reading f5 data in 010503... \n')
pdf5_03 = init.TXT_reader(target_path=init.TargetPath(fn5_03),
                       format_file=5)

print(f'Reading f4 data in 010504... \n')
pdf4_04 = init.TXT_reader(target_path=init.TargetPath(fn4_04),
                       format_file=4)
print(f'Reading f5 data in 010504... \n')
pdf5_04 = init.TXT_reader(target_path=init.TargetPath(fn5_04),
                       format_file=5)

############################################# Create Key ###############################################################
print('Constructing key. \n')
pdf4_03['key'] = pdf4_03['X3'] + pdf4_03['X4'] + pdf4_03['X5'] + pdf4_03['X35']
pdf5_03['key'] = pdf5_03['X3'] + pdf5_03['X4'] + pdf5_03['X5'] + pdf5_03['X35']

pdf4_04['key'] = pdf4_04['X3'] + pdf4_04['X4'] + pdf4_04['X5'] + pdf4_04['X35']
pdf5_04['key'] = pdf5_04['X3'] + pdf5_04['X4'] + pdf5_04['X5'] + pdf5_04['X35']

########################################### Assertion of key uniqueness ################################################
print('Asserting key uniqueness. \n')
# f4
assert pdf4_03.shape[1] == pdf4_04.shape[1]
assert not any(pdf4_03.columns != pdf4_04.columns)
assert int(pdf4_03['key'].isin(pdf4_04['key']).sum()) == 0

# f5
assert pdf5_03.shape[1] == pdf5_04.shape[1]
assert not any(pdf5_03.columns != pdf5_04.columns)
assert int(pdf5_03['key'].isin(pdf5_04['key']).sum()) == 0

############################################# Concatenation of datasets ################################################
print('Concatenating datasets. \n')
pdf4 = pd.concat([pdf4_03, pdf4_04], ignore_index=True)
pdf5 = pd.concat([pdf5_03, pdf5_04], ignore_index=True)

############################################### Record data changes ####################################################
print('Recording data changes. \n')

print(f'pdf4_03.shape[0] = {pdf4_03.shape[0]} \n'
      f'pdf4_04.shape[0] = {pdf4_04.shape[0]} \n'
      f'pdf4.shape[0] = {pdf4.shape[0]} \n\n'
      f'pdf5_03.shape[0] = {pdf5_03.shape[0]} \n'
      f'pdf5_04.shape[0] = {pdf5_04.shape[0]} \n'
      f'pdf5.shape[0] = {pdf5.shape[0]} \n\n')

####################################### Tag columns name with format file ##############################################
print('Tagging column names with file ID key. \n')
pdf4.columns = ['key' if col == 'key' else 'f4' + col for col in pdf4.columns]
pdf5.columns = ['key' if col == 'key' else 'f5' + col for col in pdf5.columns]

##################################################### Outer merge ######################################################
print('Outer merge... \n')
pdf = pd.merge(pdf4, pdf5, on='key', how='outer', indicator=True)
pdf = pdf.where(pd.notnull(pdf), None)

################################################## Check and assert ####################################################
keys4 = set(pdf4['key'])
keys5 = set(pdf5['key'])

n1 = len(keys4 & keys5)
n2 = len(keys4 - keys5)
n3 = len(keys5 - keys4)
n4 = len(keys4 | keys5)

print(f'Join data: n1 = {n1}')
print(f'Keys in pdf4 not in pdf5: n2 = {n2}')
print(f'Keys in pdf5 not in pdf4: n3 = {n3}')
print(f'Join keys, plus complement keys: n4 = {n4}')
print(f'100*n1/n4 = {100 * n1 / n4:.2f}%')
print(f'100*n2/n4 = {100 * n2 / n4:.2f}%')
print(f'100*n3/n4 = {100 * n3 / n4:.2f}%')

assert n1 + n2 == len(keys4)
assert n1 + n3 == len(keys5)
assert n1 + n2 + n3 == n4

################################################ Replace None by `n`*k #################################################
print('Replace None by string `n`*k, where k is nchar in field. \n')
# I feel safer by tracking the row in a explicit way, by adding 'nnnn' whenever missing.
ncharmap = [len(str(field)) for field in pdf.loc[int(pdf['_merge'][pdf['_merge'] == 'both'].index[0])]]

print('Replacing... \n')
for col, nchar in zip(pdf.columns, ncharmap):
    pdf[col] = pdf[col].apply(lambda x: x if x is not None else 'n' * nchar)

pdf = pdf.drop(columns=['_merge'])

################################################### Save pdf to txt ####################################################
print('Saving .. \n')
init.Save_PDF_as_TXT(pdf, 'merged.txt')

###################################################### End Profiling ###################################################
init.EndsProfiling()