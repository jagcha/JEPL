################################################ Import modules ########################################################
import US25UW990JEPL_02 as JEPL

################################################## Parameters ##########################################################
t = 1

JEPL010101 = 1
JEPL010501 = 1
JEPL010502 = 1
JEPL010503 = 1
JEPL010504 = 1
JEPL010505 = 1
JEPL010601 = 1
JEPL020101 = 1
JEPL020102 = 0

############################################### Initialization ##########################################################
init = JEPL.Initializer(data_path='/blue/mateescu/agustinchasco/Projects/reprojersey/data',
                          code_path='/blue/mateescu/agustinchasco/Projects/reprojersey/core',
                          testing=t)

init.Directories()
init.Directories('core')
init.GetFormatMap()

################################################# JEPL010101 ############################################################
if JEPL010101 == 0:
    print(f'JEPL010101 activated when testing is {init.t}. \n')
    dr = JEPL.DataReader(raw_data_path='/blue/mateescu/fpenagaricano/Jersey0405', 
                         data_path='/blue/mateescu/agustinchasco/Projects/reprojersey/data',
                         code_path='/blue/mateescu/agustinchasco/Projects/reprojersey/core',
                         files_f4=['Jersey_Format_4_2009_2022.CM1', 'Pengaricano_2021-2022.4', 'Penagaricano.4_thru2020'],
                         files_f5=['Jersey_Format_5_20110101_20151231.FM5', 'Jersey_Format_5_20160101_20200509.FM5', 'Pengaricano_2021-2022.5', 'Penagaricano.5_thru2020'],
                         testing=t)
    dr.UnzipReadSaveRaw()

else:
    print(f'JEPL010101 skipped when testing is {init.t}. \n')

################################################# JEPL010501 ############################################################
if JEPL010501 == 0:
    print(f'JEPL010501 activated when testing is {init.t}. \n')
    if init.t == 1:
        f4 = 'US25UW990JEPL.02_testf4.txt'
        f5 = 'US25UW990JEPL.02_testf5.txt'
    else:
        f4 = 'US25UW990JEPL.02_f4.txt'
        f5 = 'US25UW990JEPL.02_f5.txt'
    
    tpf4 = init.TargetPath(f4)
    tpf5 = init.TargetPath(f5)

    print(f'Reading {f4} in path: \n {tpf4} \n \n')
    pdf4 = init.TXT_reader(target_path=tpf4)
    print(f'Reading {f5} in path: \n {tpf5} \n \n')
    pdf5 = init.TXT_reader(target_path=tpf5)

    print(f'Loading pdf4 and pdf5 to data container. \n')
    dc = JEPL.DataContainer(init, pdf4 = pdf4, pdf5 = pdf5)
    dc.ShowDatasets()

    print(f'Setting key. \n')
    dc.SetKey(dataset_names=['pdf4', 'pdf5'], key_columns=['X3', 'X4', 'X5', 'X35'])

    print('Spanning keys. \n')
    dc.SamplerKey(dataset_names=['pdf4', 'pdf5'], prop=0.001)
    dc.ShowDatasets()

    print('Saving. \n')
    dc.SaveContainer(ext1='010501', dataset_names=['spdf4', 'spdf5'], ext2='.txt', )

else:
    print(f'JEPL010501 skipped when testing is {init.t}. \n')


################################################# JEPL010502 ############################################################
if JEPL010502 == 0:
    print(f'JEPL010502 activated when testing is {init.t}. \n')
else:
    print(f'JEPL010502 skipped when testing is {init.t}. \n')

################################################# JEPL010503 ############################################################
if JEPL010503 == 0:
    print(f'JEPL010503 activated when testing is {init.t}. \n')
else:
    print(f'JEPL010503 skipped when testing is {init.t}. \n')

################################################# JEPL010504 ############################################################
if JEPL010504 == 0:
    print(f'JEPL010504 activated when testing is {init.t}. \n')
else:
    print(f'JEPL010504 skipped when testing is {init.t}. \n')

################################################# JEPL020101 ############################################################
if JEPL020101 == 0:
    print(f'JEPL020101 activated when testing is {init.t}. \n')
    fn = ['US25UW990JEPL.01_impl_010601pdfu.txt', 'US25UW990JEPL.01_test_010601pdfu.txt'][init.t]
    fp = init.TargetPath(fn)

    print(f'Loading file {fn} in path: \n {fp} \n \n')
    dc = JEPL.DataContainer(init, pdfu = init.TXT_reader(target_path=fp))
    dc.ShowDatasets()
    
    print(f'Activate Plot020101. \n')
    dc.Plot020101(datset_name='pdfu', pattern='Type of reproductive event code')
    
else:
    print(f'JEPL020101 skipped when testing is {init.t}. \n')

################################################# JEPL020102 ############################################################
if JEPL020102 == 0:
    print(f'JEPL020102 activated when testing is {init.t}. \n')
    fn = ['US25UW990JEPL.01_impl_010601pdfu.txt', 'US25UW990JEPL.01_test_010601pdfu.txt'][init.t]
    fp = init.TargetPath(fn)
    print(f'Loading file {fn} in path: \n {fp} \n \n')
    dc = JEPL.DataContainer(init, pdfu = init.TXT_reader(target_path=fp))
    dc.ShowDatasets()
    dc.SetKey(['pdfu'], [['f4X3', 'f4X4', 'f4X5', 'f4X35'], ['f5X3', 'f5X4', 'f5X5', 'f5X35']])

else:
    print(f'JEPL020102 skipped when testing is {init.t}. \n')
    pass

############################################### Ends Profiling ##########################################################
init.EndsProfiling()
