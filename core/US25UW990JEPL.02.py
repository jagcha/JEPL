################################################ Import modules ########################################################
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import US25UW990JEPL_02 as JEPL

################################################## Parameters ##########################################################
t = 0

JEPL010101 = 1
JEPL010501 = 1
JEPL010502 = 1
JEPL010503 = 1
JEPL010504 = 1
JEPL010505 = 1
JEPL010601 = 1
JEPL020101 = 1
JEPL0201 = 1
JEPL0202 = 0

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

################################################### JEPL0201 ############################################################
if JEPL0201 == 0:
    print(f'JEPL0201 activated when testing is {init.t}. \n')
    fn = ['US25UW990JEPL.01_impl_010601pdfu.txt', 'US25UW990JEPL.01_test_010601pdfu.txt'][init.t]
    fp = init.TargetPath(fn)
    print(f'Loading file {fn} in path: \n {fp} \n \n')
    dc = JEPL.DataContainer(init, pdfu = init.TXT_reader(target_path=fp))
    dc.ShowDatasets()
    dc.SetKey(['pdfu'], [['f4X3', 'f4X4', 'f4X5', 'f4X35'], ['f5X3', 'f5X4', 'f5X5', 'f5X35']])
    for i in range(3):
        dc.PlotDiffs('pdfu', stp=[20,10][dc.init.t], cond=i, n=20000)
else:
    print(f'JEPL0201 skipped when testing is {init.t}. \n')

################################################### JEPL0202 ############################################################

if JEPL0202 == 0:
    print(f'JEPL0202 activated when testing is {init.t}. \n')
    fn = ['US25UW990JEPL.01_impl_010601pdfu.txt', 'US25UW990JEPL.01_test_010601pdfu.txt'][init.t]
    fp = init.TargetPath(fn)
    print(f'Loading file {fn} in path: \n {fp} \n \n')
    dc = JEPL.DataContainer(init, pdfu = init.TXT_reader(target_path=fp))
    # This is something that must be done upp-stream! Must be corrected and integrated.
    dc.f_X35Standardize(dataset_name='pdfu')
    dc.ShowDatasets()
    dc.CheckDirs(extension='0202')

    dc.SetKey(['pdfu'], [['f4X3', 'f4X4', 'f4X5', 'f4X35'], ['f5X3', 'f5X4', 'f5X5', 'f5X35']])
    ks = dc.GetColKey(colnames=['Calving date (YYYYMMDD)', 'Lactation number for this record', 
                                'Type of reproductive event', 'Date of reproductive event'])
    ks = ['Key'] + ks
    df = dc.pdfu[ks]

    print('Plotting frequency distribution of lactation number. \n')
    vc = df['f4X43'].value_counts()
    vc = vc.sort_index()
    plt.figure(figsize=(10, 6))
    bars = plt.bar(vc.index.astype(str), vc.values, color='skyblue')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval), ha='center', va='bottom', fontsize=9)
    plt.title(f'Counts of Unique Lactations Raw Values (N = {sum(vc):,})')
    plt.xlabel('Lactation number')
    plt.ylabel('Count')
    ext = 'JEPL0202_LACTFreq.png'
    fp = dc.init.SavePath(extension=ext, dirct='core', mode=1)
    print(f'Saving result as plot in path: \n {fp} \n \n')
    plt.savefig(fp, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"\n Proportion of nulliparous over total N: {100*sum(df['f4X43'] == '00')/df.shape[0]:.2} % \n")
    print(f'Number and proportion of Keys with reproductive events. \n'
          f"sum(df['f5X37'] != 'n') = {sum(df['f5X37'] != 'n'):,} \n"
          f"sum(df['f5X37'] == 'n') = {sum(df['f5X37'] == 'n'):,} \n"
          f"100*sum(df['f5X37'] != 'n')/df.shape[0] = {100*sum(df['f5X37'] != 'n')/df.shape[0]:.2} % \n"
          f"100*sum(df['f5X37'] == 'n')/df.shape[0] = {100*sum(df['f5X37'] == 'n')/df.shape[0]:.2} % \n")
    
    print('Among animals with reproductive data: \n Show number of ID-Lactation which reproductive sequence ends in pregnancy success.')
    k5 = [k for k in ks if '5' == k[1]]
    sk5 = [k5[i] for i in range(len(k5)) if i % 2 == 1]
    cc = df[sk5].map(str.rstrip).agg(''.join, axis=1)
    lc = cc.apply(lambda x: x[-1] if x else '')
    v_df = pd.DataFrame(lc, columns=['Last Type of Reproductive Event'])
    vc = v_df['Last Type of Reproductive Event'].value_counts().sort_values(ascending=False)
    plt.figure(figsize=(13.33, 7.5))
    bars = plt.bar(vc.index.astype(str), vc.values, color='skyblue')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval), ha='center', va='bottom', fontsize=9)
    plt.title(f'Counts of Last Type of Reproductive Event (N = {sum(vc):,})')
    plt.xlabel('Type of Reproductive Event')
    plt.ylabel('Count')
    ext = 'JEPL0202_LastTypeRepEv.png'
    fp = dc.init.SavePath(extension=ext, dirct='core', mode=1)
    print(f'Saving result as plot in path: \n {fp} \n \n')
    plt.savefig(fp, dpi=300, bbox_inches='tight')
    plt.close()

    print(f'Proportion of unique animals with one lactatiuon vs multiple lactations.')
    res = dc.MultiparousCounter(df=df)
    print(f'number of unique IDs = {res[0]:,}'
          f'Number of unique IDs with multiple lactations = {res[1]:,}'
          f'Number of unique IDs with a unique recorded lactation = {res[0]-res[1]:,}'
          f'% of unique IDs with multiples lactations = {100*res[1]/(res[0]+res[1]):.2f}'
          f'% of unique IDs single lactation = {100*res[0]/(res[0]+res[1]):.2f}')
    
    print(f'Print Getting difference between two consecutive lactation numbers (we should expect 1). \n)')
    v = dc.JEPL0202DiffSubsqLact(df)
    v_df = pd.DataFrame(v, columns=['Difference'])
    vc = v_df['Difference'].value_counts().sort_index()
    plt.figure(figsize=(13.33, 7.5))
    bars = plt.bar(vc.index.astype(str), vc.values, color='skyblue')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval), ha='center', va='bottom', fontsize=9)
    plt.title(f'Counts of Difference Between Consecutive Raw Lactation Values (N = {sum(vc):,})')
    plt.xlabel('Difference')
    plt.ylabel('Count')
    ext = 'JEPL0202_DiffSubsLacts.png'
    fp = dc.init.SavePath(extension=ext, dirct='core', mode=1)
    print(f'Saving result as plot in path: \n {fp} \n \n')
    plt.savefig(fp, dpi=300, bbox_inches='tight')
    plt.close()

    print(f'Among events with consecutive lactations: \n Get Proportion of previous events ending with P. \n')
    dc.JEPL0202CounterP(df)

    print('Among events with consecutive lactations: \n Target last recorded reproductive event that is not P and show frequency distribution of such event. \n')
    v = dc.JEPL0202TargetStrange(df)
    v_df = pd.DataFrame(v, columns=['Other Categories Different than Pregnancy Confirmation'])
    vc = v_df['Other Categories Different than Pregnancy Confirmation'].value_counts().sort_values(ascending=False)
    plt.figure(figsize=(13.33, 7.5))
    bars = plt.bar(vc.index.astype(str), vc.values, color='skyblue')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval), ha='center', va='bottom', fontsize=9)
    plt.title(f'Counts of Other Categories Different than Pregnancy Confirmation (N = {sum(vc):,})')
    plt.xlabel('Other Categories Different than Pregnancy Confirmation')
    plt.ylabel('Count')
    ext = 'JEPL0202_StrangeEnd.png'
    fp = dc.init.SavePath(extension=ext, dirct='core', mode=1)
    print(f'Saving result as plot in path: \n {fp} \n \n')
    plt.savefig(fp, dpi=300, bbox_inches='tight')
    plt.close()

    ## CRF: Chunk below causes infinite while loop. However, it has useful lines.
    # print('Among consecutive lactations: \n Interval Last reproductive event and calving. \n'
    #       '1- Show interval for those animals showing P-Calving. \n'
    #       '2- Show interval for those animals showing *-Calving. \n')
    # vp, vo = dc.JEPL0202GetInterval(df)
    # be = np.arange(min(vp)-1, max(vp)+1)
    # plt.hist(vp, bins=be, alpha=0.5, label=f'P-C (n = {len(vp)})', color='green')
    # plt.hist(vo, bins=be, alpha=0.5, label=f'*-C (n = {len(vo)})', color='red')
    # plt.legend()
    # plt.title(f"Histogram (N = {len(vp) + len(vo)})")
    # plt.xlabel("Interval Last Reproductive Event to Calving.")
    # plt.ylabel("Frequency")
    # ext = 'JEPL0202_IntervalRepCalv.png'
    # fp = dc.init.SavePath(extension=ext, dirct='core', mode=1)
    # print(f'Saving result as plot in path: \n {fp} \n \n')
    # plt.savefig(fp, dpi=300, bbox_inches='tight')
    # plt.close()

    # be = np.arange(170, 371)
    # plt.hist(vp, bins=be, alpha=0.5, label=f'P-C (n = {len(vp)})', color='green')
    # plt.hist(vo, bins=be, alpha=0.5, label=f'*-C (n = {len(vo)})', color='red')
    # plt.legend()
    # plt.title(f"Histogram (N = {len(vp) + len(vo)})")
    # plt.xlabel("Interval Last Reproductive Event to Calving.")
    # plt.ylabel("Frequency")
    # ext = 'JEPL0202_IntervalRepCalvNarrow.png'
    # fp = dc.init.SavePath(extension=ext, dirct='core', mode=1)
    # print(f'Saving result as plot in path: \n {fp} \n \n')
    # plt.savefig(fp, dpi=300, bbox_inches='tight')
    # plt.close()

else:
    print(f'JEPL0202 skipped when testing is {init.t}. \n')


############################################### Ends Profiling ##########################################################
init.EndsProfiling()
