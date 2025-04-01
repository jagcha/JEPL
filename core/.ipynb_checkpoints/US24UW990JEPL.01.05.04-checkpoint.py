################################################ Import modules ########################################################
import US24UW990JEPL_01
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

##################################################### Main objectives ##################################################
# Solve conflicts in duplicated keys.

# Take as input:
# `.../data/US24UW990JEPL.01.05.03/[***]/US24UW990JEPL.01.05.03_[***]_pdf[4/5]_nu.txt`
# `.../data/US24UW990JEPL.01.05.03/[***]/US24UW990JEPL.01.05.03_[***]_pdf[4/5]_u.txt`

# Explores conflicts in `nu_txt`.

# Report combination `key + columns_j` that most reduces the number of conflict.

# Required prerequisite to tackle the issue.

##################################################### Notes ############################################################
# Incremental programming in `US24UW990JEPL.01.05.04.ipynb`. Some visualizations on dataset.

################################################## Specific objectives #################################################

####################################################### Variables ######################################################

t = 0

###################################################### Initialization ##################################################
init = US24UW990JEPL_01.Initializer('/blue/mateescu/agustinchasco/Projects/reprojersey/data',
                                    '/blue/mateescu/agustinchasco/Projects/reprojersey/core',
                                    t)

# Creates directory if not present.
init.Directories()

# Initialize format mappers.
init.GetFormatMap()

############################################# Define variables: files to read ##########################################

print('Define variables: files to read \n')
if t:
    f4u = 'US24UW990JEPL.01.05.03_test_pdf4u.txt'
    f4nu = 'US24UW990JEPL.01.05.03_test_pdf4nu.txt'
    f5u = 'US24UW990JEPL.01.05.03_test_pdf5u.txt'
    f5nu = 'US24UW990JEPL.01.05.03_test_pdf5nu.txt'
elif t == 0:
    f4u = 'US24UW990JEPL.01.05.03_impl_pdf4u.txt'
    f4nu = 'US24UW990JEPL.01.05.03_impl_pdf4nu.txt'
    f5u = 'US24UW990JEPL.01.05.03_impl_pdf5u.txt'
    f5nu = 'US24UW990JEPL.01.05.03_impl_pdf5nu.txt'
else:
    raise AssertionError("Please brosito..., t is 0 or 1 w/o exception")
    
#################################################### Initialize paths ##################################################

print('Initializing paths. \n')
pthf4u = init.TargetPath(f4u)
pthf4nu = init.TargetPath(f4nu)
pthf5u = init.TargetPath(f5u)
pthf5nu = init.TargetPath(f5nu)

##################################################### Read txt files ###################################################

print(f'Reading data in {f4nu} ... \n')
f4nu = init.TXT_reader(pthf4nu)
print(f'Reading data in {f5nu} ... \n')
f5nu = init.TXT_reader(pthf5nu)

################################################# Allocate df in container #############################################

print('Initialize data container. \n')
pdf = US24UW990JEPL_01.DataContainer(init, f4nu=f4nu, f5nu=f5nu)
pdf.Show_Datasets()

################################################### Construction of Key ################################################

set_key = ['X3', 'X4', 'X5', 'X35']
pdf.SetKey(['f4nu', 'f5nu'], set_key)
key = 'Key'

#################################################### Create core directory #############################################

init.Directories(dirct='core')

############################################## Pairwise conflict resolution f4 #########################################

n4 = pdf.f4nu.shape[0]
f4cols = list(pdf.f4nu.columns)
f4cols.remove(key)
f4cols = [col for col in f4cols if col not in set_key]
map4l = []
trck = 0
for j in f4cols:
    cnc = pdf.f4nu[key] + pdf.f4nu[j]
    ndu = 100*int(sum(cnc.value_counts().values[cnc.value_counts().values == 1]))/n4
    map4l.append((trck, j, ndu))
    trck += 1

########################################### Save f4 potential conflict resolution ######################################

spth = init.SavePath(extension='potconff4.png', dirct='core')
print(f'Saving plot showing potential conflict resolution in {spth} ... \n')

xvals = [t[0] for t in map4l]
yvals = [t[2] for t in map4l]

plt.plot(xvals, yvals, linestyle='-', marker='o', markersize=1)
plt.scatter(xvals, yvals, color='black', s=5)

plt.xlabel('Index')
plt.ylabel('Values')

plt.savefig(spth, dpi=300)
plt.close()

################################################ Pairwise conflict resolution f5 ########################################

n5 = pdf.f5nu.shape[0]
f5cols = list(pdf.f5nu.columns)
f5cols.remove(key)
f5cols = [col for col in f5cols if col not in set_key]
map5l = []
trck = 0
for j in f5cols:
    cnc = pdf.f5nu[key] + pdf.f5nu[j]
    ndu = 100*int(sum(cnc.value_counts().values[cnc.value_counts().values == 1]))/n5
    map5l.append((trck, j, ndu))
    trck += 1

########################################### Save f5 potential conflict resolution ######################################
spth = init.SavePath(extension='potconff5.png', dirct='core')
print(f'Saving plot showing potential conflict resolution in {spth} ... \n')

xvals = [t[0] for t in map5l]
yvals = [t[2] for t in map5l]

plt.plot(xvals, yvals, linestyle='-', marker='o', markersize=1)
plt.scatter(xvals, yvals, color='black', s=5)

plt.xlabel('Index')
plt.ylabel('Values')

plt.savefig(spth, dpi=300)
plt.close()

####################################### Show top 10 potential solutions f4 & f5 ########################################

map4l.sort(key=lambda i: -1*i[2])
map5l.sort(key=lambda i: -1*i[2])

print(f'map4l[:15]: \n'
      f'{map4l[:15]} \n\n'
      f'map5l[:15]: \n'
      f'{map5l[:15]} \n')

###################################################### Solve f4 ########################################################
# Visual explanation in `US24UW990JEPL.01.05.04.ipynb` if needed.

pdf.f4nu['X36'] = pd.to_numeric(pdf.f4nu['X36'], errors='coerce').fillna(0)
f4nu_u = pdf.f4nu.loc[pdf.f4nu.groupby('Key')['X36'].idxmax()]
f4nu_r = pdf.f4nu.loc[~pdf.f4nu.index.isin(f4nu_u.index)]

# Check:
assert not any(f4nu_u.index.isin(f4nu_r.index)) 
assert f4nu_u.shape[0] + f4nu_r.shape[0] == pdf.f4nu.shape[0]
assert sum(f4nu_u['Key'].duplicated()) == 0
assert sum(f4nu_r['Key'].duplicated()) > 0

########################################### Show f4 fragmentation ######################################################
print(f'pdf.f4nu.shape[0] = {pdf.f4nu.shape[0]} \n'
      f'f4nu_u.shape[0] = {f4nu_u.shape[0]} \n'
      f'f4nu_r.shape[0] = {f4nu_r.shape[0]} \n'
      f'100 * f4nu_u.shape[0]/pdf.f4nu.shape[0] = {100 * f4nu_u.shape[0]/pdf.f4nu.shape[0]} \n'
      f'100 * f4nu_r.shape[0]/pdf.f4nu.shape[0] = {100 * f4nu_r.shape[0]/pdf.f4nu.shape[0]} \n')

rnf4 = len(pdf.f4nu['Key'].unique())
unf4 = len(f4nu_u['Key'].unique())
print(f"Number of unique keys in pdf.f4nu['Key']: rnf4 = {rnf4} \n"
      f"Number of unique keys in f4nu_u (which is f4nu_u.shape[0]): unf4 = {unf4} \n"
      f"Recovered percentage: 100*unf4/rnf4 = {100*unf4/rnf4} %")

############################################# Save f4 fragmented #######################################################
f4uext = 'f4nu_u.txt'
f4rext = 'f4nu_r.txt'

print(f'Saving f4nu_u in {init.SavePath(f4uext)}')
init.Save_PDF_as_TXT(pandas_df=f4nu_u, extension=f4uext)

print(f'Saving f4nu_r in {init.SavePath(f4rext)}')
init.Save_PDF_as_TXT(pandas_df=f4nu_r, extension=f4rext)

###################################################### Solve f5 ########################################################
pdf.f5nu['X17'] = pd.to_numeric(pdf.f5nu['X17'])
f5nu_u = pdf.f5nu.loc[pdf.f5nu.groupby('Key')['X17'].idxmax()]
f5nu_r = pdf.f5nu.loc[~pdf.f5nu.index.isin(f5nu_u.index)]

assert not any(f5nu_u.index.isin(f5nu_r.index)) 
assert f5nu_u.shape[0] + f5nu_r.shape[0] == pdf.f5nu.shape[0]
assert sum(f5nu_u['Key'].duplicated()) == 0
assert sum(f5nu_r['Key'].duplicated()) > 0

########################################### Show f5 fragmentation ######################################################
print(f'pdf.f5nu.shape[0] = {pdf.f5nu.shape[0]} \n'
      f'f5nu_u.shape[0] = {f5nu_u.shape[0]} \n'
      f'f5nu_r.shape[0] = {f5nu_r.shape[0]} \n'
      f'100 * f5nu_u.shape[0]/pdf.f5nu.shape[0] = {100 * f5nu_u.shape[0]/pdf.f5nu.shape[0]} \n'
      f'100 * f5nu_r.shape[0]/pdf.f5nu.shape[0] = {100 * f5nu_r.shape[0]/pdf.f5nu.shape[0]} \n')

rnf5 = len(pdf.f5nu['Key'].unique())
unf5 = len(f5nu_u['Key'].unique())

print(f"Number of unique keys in pdf.f5nu['Key']: rnf5 = {rnf5} \n"
      f"Number of unique keys in f5nu_u (which is f5nu_u.shape[0]): unf5 = {unf5} \n"
      f"Recovered percentage: 100*unf5/rnf5 = {100*unf5/rnf5} %")

############################################# Save f5 fragmented #######################################################
f5uext = 'f5nu_u.txt'
f5rext = 'f5nu_r.txt'

print(f'Saving f5nu_u in {init.SavePath(f5uext)}')
init.Save_PDF_as_TXT(pandas_df=f5nu_u, extension=f5uext)

print(f'Saving f5nu_r in {init.SavePath(f5rext)}')
init.Save_PDF_as_TXT(pandas_df=f5nu_r, extension=f5rext)

###################################################### Finish ##########################################################
init.EndsProfiling()