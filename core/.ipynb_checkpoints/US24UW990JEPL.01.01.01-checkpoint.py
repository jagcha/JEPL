################################################ Import modules ########################################################

from zipfile import ZipFile
import os
import time

############################################### Modify if needed #######################################################
# `t=1` for testing.
# `t=0` for implementing.

t = 0

##################################################### Main objectives ##################################################
# Read line, fill to expected length, save file.
# If line is longer than expected, save in a different file.

##################################################### Notes ############################################################
# Lines not always have the same length.
# Format 4 should be composed by lines of length equal to 710.
# Format 5 should be composed by lines of length equal to 737.
# Often, lines have exactly +2 extra position.
# In sample, I observe all lines ending with `\r\n`. This characters must be eliminated.
# Often, length of the line is lower than expected.

###################################################### Initialization ##################################################

print(f'Initialization: \n')
ini = time.time()
time_tuple = time.localtime(ini)
formatted_time = time.strftime("%m-%d-%Y at %I:%M %p", time_tuple)
CN = os.path.splitext(os.path.basename(__file__))[0]
r = '/blue/mateescu/fpenagaricano/Jersey0405'
p = '/blue/mateescu/agustinchasco/Projects/reprojersey/core'
s = '/blue/mateescu/agustinchasco/Projects/reprojersey/data'

files_f4 = ['Jersey_Format_4_2009_2022.CM1',
            'Pengaricano_2021-2022.4',
            'Penagaricano.4_thru2020']

files_f5 = ['Jersey_Format_5_20110101_20151231.FM5',
            'Jersey_Format_5_20160101_20200509.FM5',
            'Pengaricano_2021-2022.5',
            'Penagaricano.5_thru2020']


print(f'Code {CN + ".py"} starts. \n'
      f'Codes executed when testing is {t}. \n'
      f'Reading data in {r}. \n'
      f'Running program in {p}. \n'
      f'Saving data in {s}. \n'
      f'Targeting Format 4 files: {files_f4} \n'
      f'Targeting Format 5 files: {files_f5} \n'
      f'Time profiling starts. Program executed on {formatted_time} \n')

#################################################### Generic Functions #################################################

print(f'Defining functions: \n\n'
      f'Define `tp`.')

def tp(i, f):
    """
    Function takes an initial and final timing. Then return hh:mm:ss.

    :param i: initial `time.time()`
    :param f: final `time.time()`
    :return: elapsed time expressed as hh:mm:ss.
    """

    d = f - i
    hh = str(int(d // 60 ** 2)).zfill(2)
    d %= 60 ** 2
    mm = str(int(d // 60)).zfill(2)
    d = 60 * (d % 60)
    ss = str(int(d // 60)).zfill(2)

    return f'Elapsed time (hh:mm:ss) is {hh}:{mm}:{ss}\n'

def path_save_txt(file_i, extension='', set_f4=None, set_f5=None, root=s, cn=CN, test=t):
    """
    This function generates the path to save a text file based on several conditions:
    the type of file (Format 4 or Format 5), the mode (testing or implementation),
    and the file extension. It returns the appropriate file path as a string.

    :param file_i: The current file being processed, used to determine whether it belongs
                   to Format 4 or Format 5.
    :param extension: A string representing the file extension. Default ''.
    :param set_f4: A list of Format 4 files. If not provided, defaults to `files_f4`.
    :param set_f5: A list of Format 5 files. If not provided, defaults to `files_f5`.
    :param root: The root directory where the file should be saved (default is `s`).
    :param cn: The name of the current script or code being executed, used as a prefix for
               the saved file (default is `CN`).
    :param test: An integer (0 or 1) that determines if the code is running in testing mode
                 (1) or implementation mode (0).
    :return: A string representing the full path where the file will be saved.
    """

    if set_f5 is None:
        set_f5 = files_f5
    if set_f4 is None:
        set_f4 = files_f4

    if file_i in set_f4 and test == 1:
        return os.path.join(root, cn + '_testf4' + extension + '.txt')

    elif file_i in set_f4 and test == 0:
        return os.path.join(root, cn + '_f4' + extension + '.txt')

    elif file_i in set_f5 and test == 1:
        return os.path.join(root, cn + '_testf5' + extension + '.txt')

    elif file_i in set_f5 and test == 0:
        return os.path.join(root, cn + '_f5' + extension + '.txt')

    else:
        print('Make sure file is in Format 4 or Format 5')
        assert False

###################################################### Get zip files ###################################################

zip_files = os.listdir(path=r)

def explore_zip_file(root, zip_file):
    """
    This function opens a specified zip file and returns a list of the names of all the files contained in it.

    :param root: The root directory where the zip file is located.
    :param zip_file: The name of the zip file to be explored.
    :return: A list of file names contained in the zip file.
    """
    rp = os.path.join(root, zip_file)
    zip_li = ZipFile(file=rp, mode='r')
    return zip_li.namelist()

print('\n Hoking files:')
for zip_i in zip_files:
    file_list = explore_zip_file(r, zip_i)
    for f_i in file_list:
        print(zip_i, ' -> ', f_i)

###################################### Define standard length of F4 and F% line ########################################
# Hardcoding the number of characters a standard line of Format 4 and 5 must have.

def expected_length(file, set_f4=None, set_f5=None, f4n = 710, f5n = 737):

    if set_f5 is None:
        set_f5 = files_f5

    if set_f4 is None:
        set_f4 = files_f4

    if file in set_f4:
        return f4n

    elif file in set_f5:
        return f5n

    else:
        return None

##################################################### Checking rows ####################################################

def line_standardizer(line, expected):
    """
    Cut of extend length of the line according to the expected length, given by CDCB specifications.
    """
    if len(line) == expected:
        return line
    elif len(line) < expected:
        return line + ' '*(expected - len(line))
    else:
        return line[:expected]

############################################ Function to save lines ####################################################

# Capture files
print('\n Working in zip files \n')

def line_writer(zip_obj, namefile, test=t, stop=5000, tck=None):

    with zip_obj.open(name=namefile, mode='r') as file:
        for line in file:
            li = str(line, encoding='utf-8').strip()
            lis = line_standardizer(line=li, expected=expected_length(namefile))
            path_i = path_save_txt(file_i=namefile)

            with open(path_i, 'a') as f_txt:
                f_txt.write(lis + '\n')

            if test and tck is None:
                tck = 0

            if test and tck < stop:
                tck += 1
                if tck == stop:
                    break

################################################## Overwrite dummy files ###############################################

def reset_files():
    # Get paths for all four files
    f4_path = path_save_txt(file_i=files_f4[0])
    f5_path = path_save_txt(file_i=files_f5[0])

    # Open and close the files in write mode ('w') to clear them
    open(f4_path, 'w').close()
    open(f5_path, 'w').close()

# Call reset_files at the start
reset_files()

###################################################### Saving lines ####################################################

for zip_i in zip_files:
    print(f'\n Working in {zip_i}')
    file_list = explore_zip_file(r, zip_i)
    for f_i in file_list:
        format_k = ''
        buchon = None
        if f_i in files_f4:
            buchon = 1
            format_k = 'Format 4'

        elif f_i in files_f5:
            buchon = 1
            format_k = 'Format 5'

        if buchon is not None:
            print(f'{format_k}: reading {f_i}')
            with ZipFile(file=os.path.join(r, zip_i), mode='r') as fzip:
                line_writer(zip_obj=fzip, namefile=f_i)

        else:
            print(f'File `{f_i} in {zip_i} skipped.')
    print()

########################################################## Finish ######################################################

fin = time.time()
print(f'Execution {CN} finished when testing is {t} \n'
      f'Reading data in {r}. \n'
      f'{tp(ini, fin)}\n')