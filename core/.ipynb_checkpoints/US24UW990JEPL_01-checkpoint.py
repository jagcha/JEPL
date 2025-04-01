################################################ Import modules ########################################################
import json
import os
import pandas as pd
import sys
import time

################################################## Module body #########################################################

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
        self.mapf4 = None
        self.mapf5 = None

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

    def TargetPath(self, target_file):
        """
        Function returns path that directs to a target file. File must be unique.
        :param target_file: the unique file you are looking in your data directory.
        :return: The path that directs to the file.
        """
        for dir_path, dir_names, file_names in os.walk(self.s):
            if target_file in file_names:
                return os.path.join(dir_path, target_file)

    def SavePath(self, extension, dirct='data'):
        """
        Takes the extension and returns the path where file must be saved.
        According to `dirct`, path is created in 'core' or 'data'.
        :param extension: one example is 'whatever.txt1'
        :param dirct: 'core' or 'data'. Default is 'data'.
        :return: the full path to save data.
        """
        assert dirct in ['core', 'data'], f"Invalid directory type: {dirct}. Expected 'core' or 'data'."
        if dirct == 'data':
            pth = self.sp
        else:
            pth = self.pp
        fn = self.cn + ['_impl_', '_test_'][self.t] + extension
        return os.path.join(pth, fn)
    

    def Save_PDF_as_TXT(self, pandas_df, extension):
        """
        Takes a pandas dataframe and an extension and save the pandas in the saving path with a name defined as the
        current file name, the testing mode, and the extension.
        :param pandas_df: pandas dataframe.
        :param extension: extension. Must ent in '.txt'
        :return: None
        """
        pth = self.SavePath(extension)
        with open(pth, 'w') as f:
            for _, row in pandas_df.iterrows():
                concat_str = ''.join(row.astype(str))
                f.write(concat_str + '\n')

    def GetFormatMap(self):
        """
        Reads mapping file for each format file. Stores mapping data in initialized object.
        :return: None
        """
        f4_map_path = os.path.join(self.s, 'US24UW990JEPL.01.02.03.f4map.json')
        f5_map_path = os.path.join(self.s, 'US24UW990JEPL.01.02.02.f5map.json')
        with open(f4_map_path) as f4:
            mapf4 = json.load(f4)
        with open(f5_map_path) as f5:
            mapf5 = json.load(f5)
        self.mapf4 = mapf4
        self.mapf5 = mapf5

    @staticmethod
    def Index_Handler(idx):
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

    def TXT_reader(self, target_path, format_file):
        """
        Takes a target path where txt file to be read is stored, and a map json file.
        Using the map, chops the line while reading. It creates a list of list that is then parsed as pandas dataframe.
        :param target_path: path where the txt file to be read is located.
        :param format_file: 4 or 5 w/o exception. According to that, is the mapping file.
        :return:
        """
        assert format_file in [4, 5]

        if self.mapf4 is None or self.mapf5 is None:
            self.GetFormatMap()

        ll = []
        if format_file == 4:
            map_f = self.mapf4
        else:
            map_f = self.mapf5

        with open(target_path, 'r') as fi:
            for l in fi:
                ll.append(self.Line_Chopper(l, map_f))

        return pd.DataFrame(ll, columns=list(map_f.keys()))
    
    def TXT_reader2(self, target_path):
        if self.mapf4 is None or self.mapf5 is None:
            self.GetFormatMap()
        
        ll4 = []
        ll5 = []
        kn = 2+3+12+8 # nchar X3 + X4 + X5 + X35
        with open(target_path, 'r') as fi:
            for l in fi:
                l4 = l[:709]
                l5 = l[(710+kn):]
                ll4.append(self.Line_Chopper(l4, self.mapf4))
                ll5.append(self.Line_Chopper(l5, self.mapf5))
        
        pdf4 = pd.DataFrame(ll4, columns=['f4' + key for key in self.mapf4.keys()])
        pdf5 = pd.DataFrame(ll5, columns=['f5' + key for key in self.mapf5.keys()])
        return pd.concat([pdf4, pdf5], axis=1)
                

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

class DataContainer:
    """
    A flexible container for storing and managing multiple pandas DataFrames.
    This class allows dynamic assignment of datasets, visualization of stored datasets,
    and creation of unique keys based on specified columns.
    """
    def __init__(self, **datasets):
        """
        Initializes the DataContainer with named pandas DataFrames.
        :param datasets: Arbitrary keyword arguments where keys are dataset names (str) and values are pandas DataFrames.
        """
        for name, df in datasets.items():
            setattr(self, name, df)

    def Show_Datasets(self):
        """
        Displays all datasets stored in the container, including their names, types, and shapes.
        :return: None
        """
        for attr, value in self.__dict__.items():
            print(f'{attr}: {type(value)} with shape {value.shape} \n')

    def SetKey(self, dataset_names, key_columns):
        """
        Adds a 'Key' column to the specified datasets by concatenating key_columns.
        :param dataset_names: List of dataset names (strings) to which the key column should be added.
        :param key_columns: List of column names (strings) that will be concatenated to form the key.
        :return: None
        """
        for name in dataset_names:
            df = getattr(self, name, None)
            if df is not None and all(col in df.columns for col in key_columns):
                df['Key'] = df[key_columns].astype(str).agg(''.join, axis=1)
            else:
                missing_cols = [col for col in key_columns if df is not None and col not in df.columns]
                print(f"Warning: Missing columns {missing_cols} in DataFrame {name}.")
                raise AssertionError("Please..., use columns that are in your dataset. \n")
                
    
