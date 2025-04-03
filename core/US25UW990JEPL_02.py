################################################ Import modules ########################################################
from bs4 import BeautifulSoup
import copy
import json
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import requests
import re
import seaborn as sns
import subprocess
import sys
import time
from zipfile import ZipFile

################################################## Module body #########################################################

############################################### Class DataReader #######################################################

class DataReader:
    def __init__(self, raw_data_path, data_path, code_path, files_f4, files_f5, testing):
        self.r = raw_data_path
        self.s = data_path
        self.p = code_path
        self.cn = os.path.splitext(os.path.basename(sys.argv[0]))[0]
        self.t = testing
        self.ff4 = files_f4
        self.ff5 = files_f5
        self.zf = os.listdir(path=self.r)

    def Path_save_txt(self, file_i, extension=''):
        """
        This function generates the path to save a text file based on several conditions:
        the type of file (Format 4 or Format 5), the mode (testing or implementation),
        and the file extension. It returns the appropriate file path as a string.
        :param file_i: The current file being processed, used to determine whether it belongs to Format 4 or Format 5.
        :param extension: A string representing the file extension. Default ''.
        :return: A string representing the full path where the file will be saved.
        """
        pth = os.path.join(self.s, self.cn, ['implement', 'test'][self.t])

        if file_i in self.ff4 and self.t == 1:
            return os.path.join(pth, self.cn + '_testf4' + extension + '.txt')

        elif file_i in self.ff4 and self.t == 0:
            return os.path.join(pth, self.cn + '_f4' + extension + '.txt')

        elif file_i in self.ff5 and self.t == 1:
            return os.path.join(pth, self.cn + '_testf5' + extension + '.txt')

        elif file_i in self.ff5 and self.t == 0:
            return os.path.join(pth, self.cn + '_f5' + extension + '.txt')

        else:
            print('Make sure file is in Format 4 or Format 5')
            assert False

    def ResetFiles(self):
        f4p = self.Path_save_txt(file_i=self.ff4[0])
        f5p = self.Path_save_txt(file_i=self.ff5[0])
        open(f4p, 'w').close()
        open(f5p, 'w').close()
    
    def Explore_zip_files(self, zip_file):
        """
        This function opens a specified zip file and returns a list of the names of all the files contained in it.

        :param zip_file: The name of the zip file to be explored.
        :return: A list of file names contained in the zip file.
        """
        return ZipFile(file=os.path.join(self.r, zip_file), mode='r').namelist()
    
    def Expected_length(self, zip_file, f4n=710, f5n=737):
        """
        This function takes a zip file name and returns the expected length of the files contained in it.
        The expected length is determined by the file name. If the file name is in the list of f4 files, the expected
        length is 710. If the file name is in the list of f5 files, the expected length is 737.
        """
        if zip_file in self.ff4:
            return f4n
        elif zip_file in self.ff5:
            return f5n
        else:
            print('File not expected.')
            return None
    
    def Line_standardizer(self, line, expected):
        """
        Cut or extend length of the line according to expectation given by CDCB specifications.
        """
        if len(line) == expected:
            return line
        elif len(line) < expected:
            return line + ' '*(expected - len(line))
        else:
            return line[:expected]
        
    def Line_Writer(self, zip_obj, name_file, stop=5000):
        """
        Function reads a file from a zip object, standardizes the lines, and writes them to a text file.
        :param zip_obj: A ZipFile object.
        :param name_file: The name of the file to be read from the zip object.
        :param stop: The number of lines to read before stopping if `testing` is TRUE. Default is 5000.
        :return: None
        """
        tck=None
        with zip_obj.open(name=name_file, mode='r') as file:
            for line in file:
                li = str(line, encoding='utf-8').strip()
                lis = self.Line_standardizer(line=li, expected=self.Expected_length(name_file))
                path_i = self.Path_save_txt(file_i=name_file)
                with open(path_i, 'a') as f_txt:
                    f_txt.write(lis + '\n')
                if self.t and tck is None:
                    tck = 0
                if self.t and tck < stop:
                    tck += 1
                    if tck == stop:
                        break
        
    def UnzipReadSaveRaw(self):
        """
        Fubncion reads and saves raw data from zip files.
        :param zip_obj: A ZipFile object.
        :param name_file: The name of the file to be read from the zip object.
        """
        pth = os.path.join(self.s, self.cn, ['implement', 'test'][self.t])
        if os.path.exists(pth):
            print(f'Path `{pth}` already exists. Resetting files. \n')
            self.ResetFiles()
        else:
            os.makedirs(pth) 

        for zip_i in self.zf:
            fl = self.Explore_zip_files(zip_i)
            for fl_i in fl:
                fk = ''
                buchon = None
                if fl_i in self.ff4:
                    buchon = 1
                    fk = "Format 4"
                elif fl_i in self.ff5:
                    buchon = 1
                    fk = 'Format 5'
                
                if buchon is not None:
                    print(f'{fk}: reading and saving zip file {fl_i} \n')
                    with ZipFile(file=os.path.join(self.r, zip_i), mode='r') as fzip:
                        self.Line_Writer(zip_obj=fzip, name_file=fl_i)

############################################## Class Initializer #######################################################
class Initializer:
    """
    A class to handle initialization and logging information about the script execution.
    Attributes:
        p (str): Path to the directory where the code is stored.
        s (str): Path to the directory where data is stored.
        cn (str): Name of the script being executed.
        t (int): Indicator for testing mode. 1 stands for testing. 0 stand for implementing.
    """
    def __init__(self, data_path, code_path, testing):
        """
        Initializes the script execution by setting paths, capturing the script name,
        and printing a summary of execution details.
        Args:
            data_path (str): The path to the directory where data files are stored.
            code_path (str): The path to the directory where the script is located.
            testing (int): A flag indicating whether the script is in testing mode. 1 stands for testing. 0 stand for implementing.
        """
        print(f'Initialization: \n')
        ini = time.time()
        self.ini = ini
        formatted_time = time.strftime("%m-%d-%Y at %I:%M %p", time.localtime(ini))
        CN = os.path.splitext(os.path.basename(sys.argv[0]))[0]
        self.p = code_path
        self.s = data_path
        self.cn = CN
        self.t = testing
        self.pp = os.path.join(self.p, self.cn, ['implement', 'test'][self.t])
        self.sp = os.path.join(self.s, self.cn, ['implement', 'test'][self.t])
        self.vp = os.path.join(self.s, 'view')
        self.mapf4 = None
        self.mapf5 = None
        self.mapf = None

        print(f'Code {self.cn + ".py"} starts. \n'
              f'Codes executed when testing is {self.t}. \n'
              f'Running program in {self.p}. \n'
              f'Reading data in {self.s}. \n'
              f'Saving data in {self.s}. \n'
              f'Time profiling starts. Program executed on {formatted_time} EST.\n')

    def Directories(self, dirct='data'):
        """
        Checks if the folder named `cn` is in the `dir`. If not, create the folder and subfolder in `dir`.
        :param dirct: 'core' or 'data'. Default is 'data'.
        :return: None
        """
        assert dirct in ['core', 'data'], f"Invalid directory type: {dirct}. Expected 'core' or 'data'."

        if dirct == 'data':
            pth = self.sp
        else:
            pth = self.pp
        if os.path.exists(pth):
            print(f'Path `{pth}` already exists. \n')
        else:
            os.makedirs(pth) 
        if os.path.exists(self.vp):
            print(f'Path `{self.vp}` already exists. \n')
        else:
            os.makedirs(self.vp) 
        

    def TargetPath(self, target_file):
        """
        Function returns path that directs to a target file. File must be unique.
        :param target_file: the unique file you are looking in your data directory.
        :return: The path that directs to the file.
        """
        for dir_path, dir_names, file_names in os.walk(self.s):
            if target_file in file_names:
                return os.path.join(dir_path, target_file)
            
    def FileName(self, extension):
        return self.cn + ['_impl_', '_test_'][self.t] + extension

    def SavePath(self, extension, dirct='data'):
        """
        Takes the extension and returns the path where file must be saved.
        According to `dirct`, path is created in 'core' or 'data'.
        :param extension: one example is 'whatever.txt'
        :param dirct: 'core' or 'data'. Default is 'data'.
        :return: the full path to save data.
        """
        assert dirct in ['core', 'data'], f"Invalid directory type: {dirct}. Expected 'core' or 'data'."
        if dirct == 'data':
            pth = self.sp
        else:
            pth = self.pp

        fn = self.FileName(extension=extension)
        return os.path.join(pth, fn)    

    def Save_PDF_as_TXT(self, pandas_df, extension):
        """
        Takes a pandas dataframe and an extension and save the pandas in the saving path with a name defined as the
        current file name, the testing mode, and the extension.
        This function is designed to backtransform the pandas dataframe to the original txt file.
        Finction works uniquelly for standard f4 (314 columns in pdf) and f5 (336 columns in pdf) files.
        :param pandas_df: pandas dataframe.
        :param extension: extension. Must end in '.txt'
        :return: None
        """
        if pandas_df.shape[1] == 336:
            ki = ['X' + str(i+1)for i in range(36)]
            kr = []
            for i in range(20):
                ini = 37 + 15*i
                fin = 43 + 15*i
                kr += ['X' + str(k) for k in range(ini, fin)]
            f5k = ki + kr
            pdf = pandas_df[f5k]
        elif pandas_df.shape[1] == 314:
            pdf = pandas_df

        elif pandas_df.shape[1] == 650:
            f4k = ['f4X' + str(i+1) for i in range(314)]
            ki = ['f5X' + str(i+1)for i in range(36)]
            kr = []
            for i in range(20):
                ini = 37 + 15*i
                fin = 43 + 15*i
                kr += ['f5X' + str(k) for k in range(ini, fin)]
            f5k = ki + kr
            fk = f4k + f5k
            pdf = pandas_df[fk]

        else:
            print(f'Carfeul: keep constant the format of the data. Minimize unnecesary changes. \n'
                  f'Current shape of the dataframe is {pandas_df.shape}. \n'
                  f'If pandas if f4, is expected to have exactly 314 columns. \n'
                  f' If pandas is f5, is expected to have`exactly 336 columns. \n'
                  f'Execution stopped because of inconsistency in number of columns. \n')
            assert False            

        pth = self.SavePath(extension)
        with open(pth, 'w') as f:
            for _, row in pdf.iterrows():
                concat_str = ''.join(row.astype(str))
                f.write(concat_str + '\n')

    def GetFormatMap(self):
        """
        Reads mapping file for each format file. Stores mapping data in initialized object.
        :return: None
        """
        f4f = self.cn + ['_impl_', '_test_'][self.t] + 'f4map.json'
        f5f = self.cn + ['_impl_', '_test_'][self.t] + 'f5map.json'
        ff = self.cn + ['_impl_', '_test_'][self.t] + 'fmap.json'
        hf = self.cn + ['_impl_', '_test_'][self.t] + 'fmap.html'

        f4_map_path = self.SavePath(extension='f4map.json')
        f5_map_path = self.SavePath(extension='f5map.json')
        f_map_path = self.SavePath(extension='fmap.json')
        html_path = self.SavePath(extension='fmap.html')

        fmps = [f4_map_path, f5_map_path]
        
        try:
            
            with open(f4_map_path) as f4:
                mapf4 = json.load(f4)
            with open(f5_map_path) as f5:
                mapf5 = json.load(f5)

            print(f'Loading map {f4f} in pathf4_map_path: \n {f4_map_path} \n \n')
            self.mapf4 = mapf4
            print(f'Loading map {f5f} in pathf5_map_path: \n {f5_map_path} \n \n')
            self.mapf5 = mapf5

            print(f'Creation of master map {ff} in path: \n {f_map_path} \n \n')
            nmf4 = {'f4' + str(k): self.mapf4[k] for k in self.mapf4}
            nmf5 = {'f5' + str(k): copy.deepcopy(self.mapf5[k]) for k in self.mapf5}
            for k1 in nmf5:
                for k2 in nmf5[k1]:
                    v = self.Index_Handler(nmf5[k1][k2])
                    if isinstance(v, tuple):
                        l = v[0] + 710 + 1
                        u = v[1] + 710
                        vn = str(l) + '-' + str(u)
                    else:
                        vn = str(v + 710 + 1)
                    nmf5[k1][k2] = vn

            nmf = {**nmf4, **nmf5}
            self.mapf = nmf
            with open(f_map_path, "w") as ff:
                    json.dump(nmf, ff, indent=4)
            
            htmlc = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>CDCB's Format Files (4 & 5) Dictionary Table</title>
                <style>
                    table {
                        width: 50%;
                        border-collapse: collapse;
                    }
                    th, td {
                        border: 1px solid black;
                        padding: 8px;
                        text-align: left;
                    }
                    th {
                        background-color: #f2f2f2;
                    }
                </style>
            </head>
            <body>
                <h2>Dictionary Table</h2>
                <table>
                    <tr>
                        <th>Key</th>
                        <th>Ref</th>
                        <th>Idx</th>
                    </tr>

            """
            for key, subdict in nmf.items():
                for ref, idx in subdict.items():
                    htmlc += f"<tr><td>{key}</td><td>{ref}</td><td>{idx}</td></tr>\n"
            htmlc += """
               </table>
            """
            print(f'HTML map file named {hf} saved in pat: \n {html_path} \n \n')
            with open(html_path, "w") as f:
                f.write(htmlc)

        except:
            urls = ['https://redmine.uscdcb.com/projects/cdcb-customer-service/wiki/Format_4',
                    'https://redmine.uscdcb.com/projects/cdcb-customer-service/wiki/Format_5']
            print(f'Scrapping {f4f} in link: \n {urls[0]} \n \n'
                  f'Scrapping {f5f} in link: \n {urls[1]} \n \n')

            flgs1 = ['Segment #2', 'Reproductive segment #2']
            lgs2 = ['Days in milk this test day', 'Type of reproductive event code']
            prfx = ['TDI #1 ', 'RES #1 ']
            ns = [273 - 251 + 1, 167 - 138 + 1]
            for idx in range(len(urls)):
                res = requests.get(urls[idx])
                soup = BeautifulSoup(res.content, 'html.parser')
                table = soup.find('table')
                fm = {}
                i = 1
                b = False
                for row in table.find_all('tr'):
                    tds = row.find_all('td')
                    ftd = tds[0].get_text(strip=True)
                    ltd = tds[-1].get_text(strip=True)
                    if not bool(re.search(r'\d', ftd)):
                        continue
                    if flgs1[idx] in ltd:
                        break
                    if lgs2[idx] in ltd:
                        b = True
                    if b:
                        ltd = prfx[idx] + ltd
                    k = 'X' + str(i)
                    fm[k] = {ltd:ftd}
                    i += 1

                bd = {k: v for k, v in fm.items() if prfx[idx] in list(v.keys())[0]}

                ed = {}
                for i in range(2, 21):
                    for k, v in bd.items():
                        nk = f"X{int(k[1:]) + (i - 1) * len(bd)}"
                        nka = re.sub(r"#\d+", f"#{i}", prfx[idx]) 
                        nkb = list(v.keys())[0].replace(prfx[idx], '')
                        nk2 = nka + nkb
                        v = self.Index_Handler(list(v.values())[0])
                        if isinstance(v, tuple):
                            l = v[0] + ns[idx] * (i-1) + 1
                            u = v[1] + ns[idx] * (i-1)
                            nv = str(l) + '-' + str(u)
                        else:
                            nv = str(v + ns[idx] * (i-1) + 1)
                        nv2 = {nk2: nv}
                        ed[nk] = nv2   

                fm = {**fm, **ed}

                with open(fmps[idx], "w") as f:
                    json.dump(fm, f, indent=4)

            self.GetFormatMap()

    def Index_Handler(self, idx):
        """
        Handles the indexing format to return adjusted indices.
        :param idx: A string representing a single index or a range (e.g., '5' or '2-8').
        :return: Adjusted index or a tuple of adjusted start and end indices.
        """
        if '-' not in idx:
            return int(idx) - 1

        else:
            idx_i = int(idx.split('-')[0]) - 1
            idx_f = int(idx.split('-')[-1])
            return idx_i, idx_f

    def Line_Chopper(self, line_i, dict_map):
        """
        Function takes a string (row or line) from a txt file, and a mapping json file.
        Using the information in the mapping json file, splits the string.
        Returns the divided string in a list.
        :param line_i: a txt line or row
        :param dict_map: a json mapping file.
        :return: a list with N strings, each one corresponds to a meaningful category.
        """
        row = []
        for key1, val1 in dict_map.items():
            idx = self.Index_Handler(dict_map[key1][list(val1.keys())[0]])
            if isinstance(idx, tuple):
                idx_i = idx[0]
                idx_f = idx[-1]
                row.append(line_i[idx_i:idx_f])
            else:
                row.append(line_i[idx])
        return row

    def TXT_reader(self, target_path):
        """
        Takes a target path where txt file to be read is stored. According to txt file in path, map diccionary is selected.
        Using the map, chops the line while reading. It creates a list of list that is then parsed as pandas dataframe.
        :param target_path: path where the txt file to be read is located.
        :return: pandas dataframe.
        """
        if self.mapf4 is None or self.mapf5 is None or self.mapf is None:
            self.GetFormatMap()
        
        res = subprocess.run(f"awk '{{print length}}' {target_path} | sort -nu", shell=True, capture_output=True, text=True)
        ll = []
        if int(res.stdout) == 710:
            map_f = self.mapf4
        elif int(res.stdout) == 737:
            map_f = self.mapf5
        elif int(res.stdout) == (710 + 737):
            map_f = self.mapf

        else:
            print(f'File {target_path} has unexpected number of characters. \n'
                  f'Expected is 710 for f4 or 737 for f5, or sum of both. \n'
                  f'Instead, file has {int(res.stdout)} characters. \n'
                  f'Execution stopped because of inconsistency in number of characters may be due a hidden bug. \n')
            assert False

        with open(target_path, 'r') as fi:
            for l in fi:
                ll.append(self.Line_Chopper(l, map_f))

        return pd.DataFrame(ll, columns=list(map_f.keys()))

    def EndsProfiling(self):
        """
        Function takes an initial and final timing. Then return hh:mm:ss.
        :return: elapsed time expressed as hh:mm:ss.
        """
        fin = time.time()
        d = fin - self.ini
        hh = str(int(d // 60 ** 2)).zfill(2)
        d %= 60 ** 2
        mm = str(int(d // 60)).zfill(2)
        d = 60 * (d % 60)
        ss = str(int(d // 60)).zfill(2)
        print(f'\n Execution {self.cn} finished when testing is {self.t} \n'
              f'Data was read and saved in {self.s}. \n'
              f'Elapsed time (hh:mm:ss) is {hh}:{mm}:{ss}\n')

######################################### Class DataContainer ##########################################################

class DataContainer:
    """
    A flexible container for storing and managing multiple pandas DataFrames.
    This class allows dynamic assignment of datasets, visualization of stored datasets,
    and creation of unique keys based on specified columns.
    """
    def __init__(self, initializer, **datasets):
        """
        Initializes the DataContainer with named pandas DataFrames.
        :param initializer: An instance of the Initializer class.
        :param datasets: Arbitrary keyword arguments where keys are dataset names (str) and values are pandas DataFrames.
        """
        self.init = initializer
        for name, df in datasets.items():
            setattr(self, name, df)

    def ShowDatasets(self):
        """
        Displays all datasets stored in the container, including their names, types, and shapes.
        Objects that are not pandas DataFrame are shown separately.
        :return: None
        """
        for attr, value in self.__dict__.items():
            if isinstance(value, pd.DataFrame):  # Ensure it's a DataFrame before accessing shape
                print(f'{attr}: {type(value)} with shape {value.shape} \n')
            else:
                print(f'{attr}: {type(value)} (Not a DataFrame) \n')

    def SetKey(self, dataset_names, key_columns):
        """
        Adds a 'Key' column to the specified datasets by concatenating key_columns.
        :param dataset_names: List of dataset names (strings) to which the key column should be added.
        :param key_columns: List of column names (strings) that will be concatenated to form the key.
        :return: None
        """
        for name in dataset_names:
            df = getattr(self, name, None)
            b1 = all(isinstance(v, list) for v in key_columns)
            if not b1 and df is not None and (df.shape[1] == 314 or df.shape[1] == 336) and all(col in df.columns for col in key_columns):
                df['Key'] = df[key_columns].astype(str).agg(''.join, axis=1)
            
            elif (df is not None and df.shape[1] == 650 and b1 and  
                  all(col in df.columns for col in key_columns[0]) and all(col in df.columns for col in key_columns[1])):
                print(f'Setting key in merged dataset with {df.shape[1]} columns.')
                df['Key1'] = df[key_columns[0]].astype(str).agg(''.join, axis=1)
                df['Key2'] = df[key_columns[0]].astype(str).agg(''.join, axis=1)
                ms = 'n'*len(df['Key1'][0])
                assert not ((df['Key1'] == ms) & (df['Key2'] == ms)).any(), f'ERROR: Both Key1 and Key2 cannot be {ms} in the same row'
                df['Key'] = df.apply(lambda r: r['Key1'] if r['Key1'] != ms else r['Key2'], axis=1)
                df = df.sort_values('Key').reset_index(drop=True)
                df = df.drop(columns=['Key1', 'Key2'])
                setattr(self, name, df)

            else:
                raise AssertionError('Please..., Check the conditions.\n')

    def SamplerKey(self, dataset_names, prop, seed=22):
        tck = 0
        for name in dataset_names:
            df = getattr(self, name, None)
            tck += 'Key' in df.columns
        if tck == len(dataset_names):
            print(f'Key already set! Ready to go.')
        else:
            raise AssertionError('Please, define the key you want to span. Assertion error rised. \n')
        
        df1 = getattr(self, dataset_names[0], None)
        n = df1['Key'].nunique()
        ns = int(n*prop) + (n*prop % 1 > 0)
        uk = df1['Key'].unique()
        sk = pd.Series(uk).sample(n=ns, random_state=seed).tolist()
        print(f'Sampled set of unique keys from {dataset_names[0]}. \n'
              f'Number of unique keys in {dataset_names[0]} is {n}. \n'
              f'Number of unique keys sampled is {ns}. \n')
        for name in dataset_names:
            print(f'Sampling spanning Keys in {name} \n')
            df = getattr(self, name, None)
            sn = 's' + name
            sdf = df[df['Key'].isin(sk)].drop(columns='Key')
            setattr(self, sn, sdf)

    def Split010502(self, dataset_names, key_column):
        """
        Splits the datasets into unique and duplicated rows based on the specified key column.
        :param dataset_names: List of dataset names (strings) to be split.
        :param key_column: Name of the key column (string) used to determine uniqueness.
        :return: None
        """
        for name in dataset_names:
            df = getattr(self, name, None)
            if df is not None and key_column in df.columns:
                kc = df[key_column].map(df[key_column].value_counts())
                dfu = df[kc == 1]
                dfr = df[kc > 1]
                un = 'u' + name
                rn = 'r' + name
                setattr(self, un, dfu)
                setattr(self, rn, dfr)
                print(f'Dataset {name} has {df.shape[0]} rows. \n'
                      f'Dataset {un} has {dfu.shape[0]} rows. \n'
                      f'Dataset {rn} has {dfr.shape[0]} rows. \n'
                      f'100*dfu.shape[0]/df.shape[0] = {100*dfu.shape[0]/df.shape[0]} \n'
                      f'100*dfr.shape[0]/df.shape[0] = {100*dfr.shape[0]/df.shape[0]} \n')
                assert dfu.shape[0] + dfr.shape[0] == df.shape[0]
                assert (dfu[key_column].value_counts() > 1).sum() == 0
            else:
                print(f'Missing key column {key_column} in DataFrame {name}.')
                raise AssertionError('Please..., use as key something in your dataset.')
            
    def Split010503(self, datasets_rep, datasets_unq):
        """"
        Function takes pairs of pandas dataframes with unique and repeated keys.
        Deletes duplicated rows on dataframe with repeated keys.
        Then, extracts rows with unique key from dataset with repeated keys.
        Adds this set of extracted rows to corresponding dataframe with unique keys.
        Overrides the dataframe with unique keys with the newest dataframe with added keys.
        Overrides the dataframe with duplicated keys after extracting duplicated rows.
        :param datasets_rep: list of pandas dataframe (string) with repeated keys.
        :param datasets_unq: list of pandas dataframe (string) with unique keys.
        :return: None
        """

        assert len(datasets_rep) == len(datasets_unq), 'List of datasets must have the same length.'
        assert all(hasattr(self, name) for name in datasets_rep), 'All datasets must be loaded in the DataContainer.'
        assert all(hasattr(self, name) for name in datasets_unq), 'All datasets must be loaded in the DataContainer.'

        for idx in range(len(datasets_rep)):
            print(f'Loading dataset {datasets_rep[idx]} and {datasets_unq[idx]} \n')
            dfr = getattr(self, datasets_rep[idx])
            dfu = getattr(self, datasets_unq[idx])

            print(f'Initial report: \n'
                  f'Dimensions in {datasets_rep[idx]} is {dfr.shape} \n'
                  f'Dimensions in {datasets_unq[idx]} is {dfu.shape} \n')

            print(f'Dropping duplicated rows in {datasets_rep[idx]} \n')
            dfr2 = dfr.drop_duplicates()
            dfr2 = dfr2.reset_index(drop=True)

            print(f'Report number od dropped rows in {datasets_rep[idx]} \n'
                  f'Number of rows in {datasets_rep[idx]} is {dfr.shape[0]} \n'
                  f'Number of rows after dropping duplicated rows is {dfr2.shape[0]} \n'
                  f'Numb of dropped rows is {dfr.shape[0] - dfr2.shape[0]} \n')
            
            print(f'Overriding {datasets_rep[idx]} with new dataframe after dropping duplicated rows. \n')
            setattr(self, datasets_rep[idx], dfr2)

            print(f'Activate module JEPL010502. \n')
            self.Split010502(dataset_names=[datasets_rep[idx]], key_column='Key')
            un = 'u' + datasets_rep[idx]
            rn = 'r' + datasets_rep[idx]

            print(f'Combine {datasets_unq[idx]} and {un}. Override {datasets_unq[idx]} with new combined dataframe. \n')
            dfu2 = getattr(self, un)
            dfr2 = getattr(self, rn)
            assert not dfu2['Key'].isin(dfu['Key']).any(), 'Key must be unique.'
            dfu3 = pd.concat([dfu, dfu2], ignore_index=True)

            print(f'Report after activation of `Split010502`. \n'
                  f'Dimensions in {datasets_unq[idx]} is {dfu.shape} \n'
                  f'Dimensions in {un} is {dfu2.shape} \n'
                  f'Dimensions after combining is {dfu3.shape}. \n',
                  f'Dimension in {rn} is {dfr2.shape} \n')

            print('Data standardization. \n')
            dfu3.reset_index(drop=True, inplace=True)
            dfu3 = dfu3.sort_values(by='Key')
            dfr2.reset_index(drop=True, inplace=True)
            dfr2 = dfr2.sort_values(by='Key')

            print(f'Override {datasets_unq[idx]} with new combined dataframe. \n')
            setattr(self, datasets_unq[idx], dfu3)

            print(f'Override {datasets_rep[idx]} with remaining dataframe after elimination of duplicated rows. \n')
            setattr(self, datasets_rep[idx], dfr2)

            print(f'Delete attributes {un} and {rn}. \n')
            delattr(self, un)
            delattr(self, rn)
        self.ShowDatasets()
    
    def SaveContainer(self, ext1, dataset_names=None, ext2='.txt', ):
        """
        Saves pandas dataframe as standard f4 or f5 txt file.
        :param dataset_names: List of dataset names (strings) to be saved. If nothing is added, all dataframes in Container are saved.
        :param ext2: final strings on txt file (strings). By default is `.txt`. Recommended to end up in `.txt`.
        :return: None
        """
        if dataset_names is None:
            dataset_names = [name for name, value in self.__dict__.items() if isinstance(value, pd.DataFrame)]
            print(f'dataset_names: \n {dataset_names} \n \n')

        for name in dataset_names:
            df = getattr(self, name)

            if 'Key' in df.columns:
                print(f'Dropping `Key` column in {name}. \n')
                self.__dict__[name] = df.drop(columns='Key')

            ext = ext1 + name + ext2
            print(f'Saving {name} in: \n {self.init.SavePath(extension=ext)}. \n \n')
            self.init.Save_PDF_as_TXT(pandas_df=self.__dict__[name], extension=ext)

    def Pinpoint010504(self, datasets_rep, key_cols, top=10):
        k = 'Key'
        key_cols.append(k)
        for name in datasets_rep:
            assert k in self.__dict__[name].columns
            nr = self.__dict__[name].shape[0]
            cn = [c for c in self.__dict__[name].columns if c not in key_cols]
            mp = []
            idx = 0
            for j in cn:
                cc = self.__dict__[name][k] + self.__dict__[name][j]
                pr = 100*int(sum(cc.value_counts().values[cc.value_counts().values == 1]))/nr
                mp.append((idx, j, pr))
                idx += 1
            
            nn = 'cc' + name
            print(f'Insight on stage 010504 --> Showing top {top} source of conflicts in {name}: \n')
            mp.sort(key=lambda i: -1*i[2])
            for idx in mp[:top]:
                print(idx)

            print(f'\n Assign insight as {nn} in DataContainer object. \n')
            setattr(self, nn, mp)
    
    def Plot010504(self, conflict_map=None, extension=''):

        if conflict_map is None:
            nms = [n for n, v in self.__dict__.items() if 'cc' in n and isinstance(v, list)]
        
        assert len(nms) >= 1, 'Make sure `Stage010504` is activated before plot its summary. \n'
        for nm in nms:
            ex = nm + extension + '.png'
            sp = self.init.SavePath(extension=ex, dirct='core')
            print(f'Saving plot for conflict {nm} in path: \n {sp} \n \n')

            mp = self.__dict__[nm]
            mp.sort(key=lambda i: i[0])
            xs = [t[0] for t in mp]
            ys = [t[2] for t in mp]

            plt.plot(xs, ys, linestyle='-', marker='o', markersize=1)
            plt.scatter(xs, ys, color='black', s=5)

            plt.xlabel('Index')
            plt.ylabel('Values')

            plt.savefig(sp, dpi=300)
            plt.close()
    
    def Solve010504(self):
        nms = [name for name, value in self.__dict__.items() if isinstance(value, pd.DataFrame)]
        nmu = [nm for nm in nms if 'u' in nm]
        nmr = [nm for nm in nms if 'r' in nm]
        print(f'Targeting nmu = {nmu}. \nTargeting nmr = {nmr}. \n')

        for i in range(len(nmu)):
            if '4' in nmu[i] and '4' in nmr[i]:
                c = 'X36'
                n = 3
            elif '5' in nmu[i] and '5' in nmr[i]:
                c = 'X17'
                n = 8
            else:
                raise AssertionError('Careful... Pandas Dataframe in Container must be referencing f4u, f4r, f5u & f5r data. \n')
            
            print(f'Working on {nmu[i]} and {nmr[i]}. Target column is {c}. \n')
            dfu = getattr(self, nmu[i])
            dfr = getattr(self, nmr[i])

            print(f'Among duplicated Keys, keep the one with higher numeric number in column {c} (f4 --> DIM. f5 --> DATE). \n')
            dfu[c] = pd.to_numeric(dfu[c], errors='coerce')
            nu = dfu[c].isna().sum()
            dfr[c] = pd.to_numeric(dfr[c], errors='coerce')
            nr = dfr[c].isna().sum()

            print(f'{nmu[i]} has {nu} coerced errors after convert {c} from string to numeric. \n'
                  f'100*nu/dfu.shape[0] = {100*nu/dfu.shape[0]:.2f}% \n'
                  f'{nmr[i]} has {nr} coerced errors after convert {c} from string to numeric. \n'
                  f'100*nr/dfr.shape[0] = {100*nr/dfr.shape[0]:.2f}% \n')
            
            dfu[c] = dfu[c].fillna(0)
            dfr[c] = dfr[c].fillna(0)
            
            udfr = dfr.loc[dfr.groupby('Key')[c].idxmax()]
            rdfr = dfr.loc[~dfr.index.isin(udfr.index)]
            
            print(f'Assert Key uniqueness and data complmentarity. \n')
            assert udfr.shape[0] + rdfr.shape[0] == dfr.shape[0], 'Assertion of complmentarity failed. \n'
            assert sum(udfr['Key'].duplicated()) == 0, 'Assertion of Key uniqueness failed. \n'

            print(f'Show fragmentation: \n'
                  f'dfr.shape[0] = {dfr.shape[0]}. \n'
                  f'udfr.shape[0] = {udfr.shape[0]}. \n'
                  f'rdfr.shape[0] = {rdfr.shape[0]}. \n')
            
            rn = len(dfr['Key'].unique())
            un = len(udfr['Key'].unique())
            print(f'Number of unique keys in {nmr[i]}: {rn}. \n'
                  f'Number of unique keys in {nmr[i]} after accounting for `{c}`: {un}. \n'
                  f'Recovered percentage of Keys: 100*un/rn = {100*un/rn} %. \n')
            
            print(f'Combine {nmu[i]} and corrected {nmr[i]}. \n')
            assert not udfr['Key'].isin(dfu['Key']).any(), 'Assertion of Key uniqueness (2) failed. \n'
            dfu2 = pd.concat([dfu, udfr], ignore_index=True)
            assert sum(udfr['Key'].duplicated()) == 0, 'Assertion of Key uniqueness (3) failed. \n'

            print(f'Report data flow. \n'
                  f'Dimensions of {nmu[i]} is {dfu.shape}. \n'
                  f'Dimension of original {nmr[i]} is {dfr.shape}. \n'
                  f'Dimensions of {nmr[i]} after extracting filtering by max value in column {c} is {udfr.shape}. \n'
                  f'Dimensions after combining both datasets is {dfu2.shape}. \n'
                  f'Dimension of remaining {nmr[i]} is {rdfr.shape}. \n')
            
            print('Data standardization. \n')
            dfu2.reset_index(drop=True, inplace=True)
            dfu2 = dfu2.sort_values(by='Key')
            dfu2[c] = dfu2[c].apply(lambda x: str(int(x)).zfill(n))
            rdfr.reset_index(drop=True, inplace=True)
            rdfr = rdfr.sort_values(by='Key')
            rdfr[c] = rdfr[c].apply(lambda x: str(int(x)).zfill(n))

            print(f'Override {nmu[i]} with new combined dataframe. \n')
            setattr(self, nmu[i], dfu2)
            print(f'Override {nmr[i]} with remaining dataframe after filter criteria using DIM in {c}. \n')
            setattr(self, nmr[i], rdfr)
            
        self.ShowDatasets()
    
    def OuterMerge010601(self, dataset_names):
        for nm in dataset_names:
            if 'Key' not in self.__dict__[nm].columns:
                k = ['X3', 'X4', 'X5', 'X35']
                print(f'Setting columns {k} as Key in dataframe {nm}. \n')
                self.SetKey(dataset_names=[nm], key_columns=k)

        print('Outer merge... \n')
        if len(dataset_names) == 2:
            print('Setting convinient columname. \n')
            nf4, nf5 = [nm for nm in dataset_names if '4' in nm], [nm for nm in dataset_names if '5' in nm]
            self.__dict__[nf4[0]].columns = ['Key' if c == 'Key' else 'f4' + c for c in self.__dict__[nf4[0]].columns]
            self.__dict__[nf5[0]].columns = ['Key' if c == 'Key' else 'f5' + c for c in self.__dict__[nf5[0]].columns]

            print('Outer merge of 2 df with unique Key.')
            pdfu = pd.merge(self.__dict__[nf4[0]], self.__dict__[nf5[0]], on='Key', how='outer', indicator=True)
            pdfu = pdfu.where(pd.notnull(pdfu), None)

            print(f'Check and assert stage. \n')
            sk4 = set(self.__dict__[nf4[0]]['Key'])
            sk5 = set(self.__dict__[nf5[0]]['Key'])
            n1 = len(sk4 & sk5)
            n2 = len(sk4 - sk5)
            n3 = len(sk5 - sk4)
            n4 = len(sk4 | sk5)
            assert n4 == pdfu.shape[0], f'Assertion (1) failed: n4 = {n4}. pdfu.shape[0] = {pdfu.shape[0]}. \n'
            assert n1 + n2 == self.__dict__[nf4[0]].shape[0], f'Assertion (2) failed: n1 = {n1}, n2 = {n2}, . {nf4[0]}.shape[0] = {self.__dict__[nf4[0]].shape[0]}. \n'
            assert n1 + n3 == self.__dict__[nf5[0]].shape[0], f'Assertion (3) failed: n1 = {n1}, n3 = {n3}, . {nf5[0]}.shape[0] = {self.__dict__[nf5[0]].shape[0]}. \n'

            print(f'Report dataflow in stage 010601: \n'
                  f'{nf4[0]}.shape: {self.__dict__[nf4[0]].shape[0]}. \n'
                  f'{nf5[0]}.shape: {self.__dict__[nf5[0]].shape[0]}. \n'
                  f'Dataframe after Outer merge shape: {pdfu.shape}. \n'
                  f'Number of spanned keys: {n1}. \n'
                  f'Number of keys in {nf4[0]} not in {nf5[0]}: {n2}. \n'
                  f'Number of keys in {nf5[0]} not in {nf4[0]}: {n3}. \n'
                  f'Percentage spanned keys over {n4}: {100*n1/n4:.2f}%. \n'
                  f'Percentage of keys in {nf4[0]} not in {nf5[0]} over {n4}: {100*n2/n4:.2f}%. \n'
                  f'Percentage of keys in {nf5[0]} not in {nf4[0]} over {n4}: {100*n3/n4:.2f}. \n')
            
            print(f'Remove {nf4[0]} and {nf5[0]}. \n')
            delattr(self, nf4[0])
            delattr(self, nf5[0])

        else:
            print(f'Function `OuterMerge010601` so far designed to handle 2 pandas dataframe. \n'
                  f'If needed, update function to handle multiple pandas dataframes. \n')
        
        print("Replacing None's by `n`. Keep consistency in txt file. \n")
        ncm = [len(str(fd)) for fd in pdfu.loc[int(pdfu['_merge'][pdfu['_merge'] == 'both'].index[0])]]
        for col, nc in zip(pdfu.columns, ncm):
            pdfu[col] = pdfu[col].apply(lambda x: x if x is not None else 'n'*nc)
        pdfu = pdfu.drop(columns=['_merge'])

        print('Add merged data to container. \n')
        setattr(self, 'pdfu', pdfu)
        self.ShowDatasets()

    def Plot020101(self, datset_name, pattern, prop=0.8):

        extension = self.Plot020101.__name__[-6:-2]
        df = getattr(self, datset_name)
        kr = [k for k in self.init.mapf if pattern in list(self.init.mapf[k].items())[0][0]]
        cc = df[kr].astype(str).agg(''.join, axis=1)
        ns = 'n'*len(kr)
        cc = cc[cc != ns].str.lstrip()
        fc = cc.value_counts().reset_index()
        fc['prop'] = cc.value_counts(normalize=True).values
        fc['cprop'] = fc['prop'].cumsum()
        plt.figure(figsize=(10, 5))
        sns.lineplot(x=fc.index, y=fc['prop'], label='Proportion')
        sns.lineplot(x=fc.index, y=fc['cprop'], label='Cumulative Proportion')
        plt.xlabel('Index')
        plt.ylabel('Proportion')
        plt.title('Proportion and Cumulative Proportion of Categories')
        plt.legend()
        plt.grid(True)
        ex = extension + '01.png'
        fn = self.init.FileName(extension=ex)
        sp = self.init.SavePath(extension=ex, dirct='core')
        print(f'Saving plot {ex} as {fn} in path: \n {sp} \n \n')
        plt.savefig(sp, dpi=300, bbox_inches='tight')

        fcs = fc[fc['cprop'] <= prop]
        plt.figure(figsize=(12, 6))
        sns.lineplot(x=fcs['index'], y=fcs['prop'], label='Proportion')
        sns.lineplot(x=fcs['index'], y=fcs['cprop'], label='Cumulative Proportion')
        plt.xlabel("Index (Characters)", labelpad=10)
        plt.ylabel("Value")
        plt.title("Proportion and Cumulative Proportion of Categories")
        plt.xticks(rotation=90, fontsize=8)
        plt.grid(axis='y')
        plt.legend()
        ex = extension + '02.png'
        fn = self.init.FileName(extension=ex)
        sp = self.init.SavePath(extension=ex, dirct='core')
        print(f'Saving plot {ex} as {fn} in path: \n {sp} \n \n')
        plt.savefig(sp, dpi=300, bbox_inches='tight')

        mask = fc["index"].str.contains(r"P.*P", regex=True)
        fcp = fc.loc[mask].copy()
        fcp = fcp.reset_index()
        fcp['cprop'] = fcp['prop'].cumsum()
        plt.figure(figsize=(12, 6))
        sns.lineplot(x=fcp.index, y=fcp['prop'], label='Proportion')
        sns.lineplot(x=fcp.index, y=fcp['cprop'], label='Cumulative Proportion')
        plt.xlabel("Index (Characters)", labelpad=10)
        plt.ylabel("Value")
        plt.title("Proportion and Cumulative Proportion of Categories (Potential Abortion)")
        plt.grid(axis='y')
        plt.legend()
        ex = extension + '03.png'
        fn = self.init.FileName(extension=ex)
        sp = self.init.SavePath(extension=ex, dirct='core')
        print(f'Saving plot {ex} as {fn} in path: \n {sp} \n \n')
        plt.savefig(sp, dpi=300, bbox_inches='tight')

        ex = extension + '03.html'
        fn = self.init.FileName(extension=ex)
        sp = self.init.SavePath(extension=ex, dirct='core')
        print(f'Saving table {ex} as {fn} in path: \n {sp} \n \n')
        fcp = fcp.drop(columns=["level_0"])
        fcp.to_html(sp, index=False)
    
    def ColSelect(self, f4='f4', f5='f5', key=None):
        k = [] if key is None else [key]
        if f4 == 'f4':
            c4 = ['f4X' + str(i4) for i4 in range(1, 315)]
        elif isinstance(f4, int) or all(f4[i] + 1 == f4[i + 1] for i in range(len(f4) - 1)):
            if isinstance(f4, int):
                f4 = [f4]
            f4l = min(f4)
            f4u = max(f4)
            c4 = ['f4X' + str(i4) for i4 in range(f4l, f4u+1)]
        else:
            c4 = ['f4X' + str(i4) for i4 in f4]

        if f5 == 'f5':
            c5 = ['f5X' + str(i5) for i5 in range(1, 337)]
        elif isinstance(f5, int) or all(f5[i] + 1 == f5[i + 1] for i in range(len(f5) - 1)):
            if isinstance(f5, int):
                f5 = [f5]
            f5l = min(f5)
            f5u = max(f5)
            c5 = ['f5X' + str(i5) for i5 in range(f5l, f5u+1)]
        else:
            c5 = ['f5X' + str(i5) for i5 in f5]

        return c4 + c5 + k
    
    def GetKeyMask(self, dataset_name, subset_keys, lact):
        c = 17
        if lact == 'm':
            sks = [k[:c] for k in subset_keys]
            return self.__dict__[dataset_name]['Key'].str[:c].isin(sks)
        elif lact == 'u':
            return self.__dict__[dataset_name]['Key'].isin(subset_keys)
        else:
            raise AssertionError(f'Argument `lact` is {lact}. \n'
                                 f'Only `m` (multiple) or `u` (unique) lactations is allowed. \n')

    def GetSubset(self, dataset_name, colf4='f4', colf5='f5', keys=None, ext='', n=10, lact='m', seed=22):
        c = 17
        t = 25
        if 'Key' not in self.__dict__[dataset_name].columns:
            self.SetKey([dataset_name], [['f4X3', 'f4X4', 'f4X5', 'f4X35'], ['f5X3', 'f5X4', 'f5X5', 'f5X35']])
        cols = self.ColSelect(f4=colf4, f5=colf5, key='Key')
        print(f'cols are: \n {cols} \n \n')

        if keys is None:
            ks = list(set(self.__dict__[dataset_name]['Key']))
            np.random.seed(seed)
            sks = np.random.choice(ks, size=n, replace=False)
            mask = self.GetKeyMask(dataset_name=dataset_name, subset_keys=sks, lact=lact)
        else:
            nk = len(keys[0])
            assert all(len(k) == nk for k in keys), "Not all elements in parameter `keys` have the same length"
            if nk == c:
                mask = self.__dict__[dataset_name]['Key'].str[:c].isin(keys)
            elif nk == t:
                mask = self.__dict__[dataset_name]['Key'].isin(keys)
            else:
                raise AssertionError(f'Length of Key must be 17 or 25. Instead, it is {nk}. \n')
        print(f'mask.head(): \n {mask.head()} \n \n')
        sdf = self.__dict__[dataset_name].loc[mask, cols]
        setattr(self, 'sdf', sdf)
        self.ShowDatasets()
        if ext != '':
            ext = '_' + ext
        fn = self.init.cn + ext + 'html'
        fp = os.path.join(self.init.pp, self.init.cn, fn)
        sdf.to_html(fp, index=False)
        

