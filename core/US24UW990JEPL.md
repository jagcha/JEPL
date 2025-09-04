# Project: Jersey Pregnancy Loses

```angular2html
Author: Javier Agustín Chasco
Email: agustin.chasco@wisc.edu or agustinchasco@gmail.com
Cellphone number: +1 (608) 556-6910
Involved: Francisco Peñagaricano, Guillermo Martínez Boggio 
```
```angular2html
Computer sciences is no more about computers than astronomy is about telescopes, biology is about microscopes or 
chemistry is about beakers and test tubes. Science is not about tools. It is about how we use them, and what we find
out when we do.

Edsger W. Dijkstra
```

The current markdown shows all steps I did while developing this project. <br>
The file may contain dead-ends and erroneous approaches. <br>
This file is not intended to be a perfect README file. <br>
Instead, file is used to record all steps, and eventually compile everything in a unified and refined documentation.
Code descriptions often times done with chatGPT/Copilot, and reviewed/edited by myself.

Data is in the following path:
```angular2html
blue/mateescu/fpenagaricano/Jersey0405
```

Files are
```
Agritech-Analytics.zip
DRMS-Penagaricano-2021-2022-July-2023.zip
DRMS-Penagaricano-July-2023.zip
```
Unzipped files hold the following.
* `Agritech-Analytics.zip`
  * `Jersey_Format_4_2009_2022.CM1`
  * `__MACOSX/._Jersey_Format_4_2009_2022.CM1`
  * `Jersey_Format_5_20110101_20151231.FM5`
  * `__MACOSX/._Jersey_Format_5_20110101_20151231.FM5`
  * `Jersey_Format_5_20160101_20200509.FM5`
  * `__MACOSX/._Jersey_Format_5_20160101_20200509.FM5`
```angular2html
[agustinchasco@login9 Jersey0405]$ unzip -l Agritech-Analytics.zip 
Archive:  Agritech-Analytics.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
2699646204  05-12-2022 02:35   Jersey_Format_4_2009_2022.CM1
      368  05-12-2022 02:35   __MACOSX/._Jersey_Format_4_2009_2022.CM1
1995533524  05-22-2022 11:17   Jersey_Format_5_20110101_20151231.FM5
      268  05-22-2022 11:17   __MACOSX/._Jersey_Format_5_20110101_20151231.FM5
3870219117  05-23-2022 01:11   Jersey_Format_5_20160101_20200509.FM5
      212  05-23-2022 01:11   __MACOSX/._Jersey_Format_5_20160101_20200509.FM5
---------                     -------
8565399693                     6 files
```

* `DRMS-Penagaricano-2021-2022-July-2023.zip`
  * `Pengaricano_2021-2022.4`
  * `Pengaricano_2021-2022.5`
```angular2html
[agustinchasco@login9 Jersey0405]$ unzip -l DRMS-Penagaricano-2021-2022-July-2023.zip 
Archive:  DRMS-Penagaricano-2021-2022-July-2023.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
158317492  07-05-2023 14:52   Pengaricano_2021-2022.4
 73470740  07-05-2023 15:04   Pengaricano_2021-2022.5
---------                     -------
231788232                     2 files
```

* `DRMS-Penagaricano-July-2023.zip`
  * `Penagaricano.4_thru2020`
  * `Penagaricano.5_thru2020`
```angular2html
[agustinchasco@login9 Jersey0405]$ unzip -l DRMS-Penagaricano-July-2023.zip 
Archive:  DRMS-Penagaricano-July-2023.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
1012083490  06-28-2023 16:36   Penagaricano.4_thru2020
424501798  06-28-2023 17:44   Penagaricano.5_thru2020
---------                     -------
1436585288                     2 files
```

Guillermo Martínez (GM) and Rodrigo Vivian Paradizo have been working with these files.

According to GM, they were able to compile all data in a single file. 

2 options:
- Carry on from where GM finished (pro: win time, cons: potentially overlook something).
- Revisit work made by GM (pro: start from the source, cons: slow).

## Objective:

### Output:
**1/5 Horcruxes: 1/5 Papers for my PhD** <br/>
Achieve the goal of having one published paper within 8 months (from September 1st, 2024; to April 30th, 2025).

### Tasks
* Stage 1: from September 1st, 2025; to December 24th, 2024: data analyses. `duration 4 months`
* Stage 2 (potentially overlapped with stage 1): writing stage must end by 28th February (follow GM and FP advices). `duration 2 months`
* Stage 3 (potentially overlapped with Stage 2): review stage must be finished by March 15th. `duration 1/2 month`
* Stage 4: publish. Must be accomplished by the end of April. `duration 1 to 2 month`


### Outcome:
Master pipeline-development, mapped into publications. <br>
Become one of the top PhD students at UW-Madison by publishing 4 high-impact papers in Animal Sciences, 1 in Plant Science, and maintaining a strong GPA in core courses (STAT, MATH, COMPSCI, GENETICS). <br>
Take full advantage of the 3.5-year PhD journey by working hard, acquiring deep learning, and applying it in practice. <br>
Ultimately, use this expertise to develop cutting-edge solutions that maximize food production efficiency, producing more with fewer resources, driving agriculture towards true sustainability.

# Stage 1: data analyses
* s1.1: Understand data-structure (codes `US24UW990JEPL.01`).
* s1.2: Merge data (codes `US24UW990JEPL.02`).
* s1.3: Visualize data (codes `US24UW990JEPL.03`).
* s1.4: Model response variable (codes `US24UW990JEPL.04`).
* s1.5: Conclude project (codes `US24UW990JEPL.05`).

# Stage 1.1 (codes `US24UW990JEPL.01`)

## `US24UW990JEPL.01.01.nn.py`
Works in `Agritech-Analytics.zip`. Understand its content.

## `US24UW990JEPL.01.02.nn.py`
Works in `DRMS-Penagaricano-2021-2022-July-2023.zip`. Understand its content.

## `US24UW990JEPL.01.03.nn.py`
Works in `DRMS-Penagaricano-July-2023.zip`. Understand its content.

# 09/11/2024

## US24UW990JEPL.01.01.01.py

Scraping and extraction of data tables from web pages containing format specifications for the USCDCB database. <br>
Retrieving data from specific URLs (`Format_4` and `Format_5`) and converting them into JSON format for further analysis.

The function `read_format`:
- Accepts two parameters: a `url` pointing to the source of the table data, and a `path` for saving or loading the data in JSON format.
- If the web request is successful, it parses the table, processes the rows and columns, and saves the resulting dictionary structure in a JSON file.
- If the request fails due to an `HTTPError`, it attempts to read from an existing JSON file at the given path, ensuring data availability even when online retrieval is not possible.
- The main objective is to structure the data for further steps in the project, such as merging, visualization, and modeling.

# 09/13/2024

## US24UW990JEPL.01.01.01.py

### HTML Display Format 4 and 5

#### Overview

This script generates HTML files to display the structure of column information in datasets, useful for identifying column meanings linked to original Format file.

## Components

- **HTML Template Parts**
  - `html_s1`: The beginning HTML structure including the header and table setup.
  - `html_s3`: The closing HTML structure for the table and body.

- **Function: `html_parser`**
  - **Purpose**: Converts the mapping dictionary into an HTML table format.
  - **Parameters**:
    - `format_i`: Format type identifier (e.g., 'Format 4' or 'Format 5').
    - `mapdict`: Dictionary containing column mappings and descriptions (Format 4 and 5 information).
    - `s1`: Starting HTML template (default is `html_s1`).
    - `s3`: Ending HTML template (default is `html_s3`).
    - `keyword`: Text to be replaced in the HTML title (default is 'jagcha92'). 
      - This text is used for define the extension  of the file, and name of the table.

  - **Logic**:
    1. **Extension Determination**: Sets file extension based on the format type (`.html` for Format 4 or Format 5).
    2. **HTML Generation**: Iterates through the `mapdict` to populate table rows.
    3. **File Writing**: Saves the generated HTML to a file.


## Output

The script produces HTML files `US24UW990JEPL.01.01.01.f4map.html` and `fUS24UW990JEPL.01.01.01.f5map.html` with structured tables linking column name with original Format structure.
```angular2html
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.01.01.f4map.html
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.01.01.f5map.html
```
### Update summary

Python code updated to read and process files from a zip archive containing two data formats (Format 4 and Format 5). The main functionality is split into two parts:

1. **Splitting Rows (Data Parsing)**:
   - The `idx_maper()` function maps indexes based on field input, handling both single and range-based indexes.
   - The `line_chopper()` function extracts values from each line based on the mapped indexes defined in `mapdict`. It slices the lines accordingly and returns the extracted data as a list.

2. **Reading Data from Zip Files**:
   - The `data_chopper()` function reads the content of the zip files, parsing the lines using the `line_chopper()` function. It stores successfully parsed lines and captures those that result in an `IndexError`.
   - Two dictionaries (`mapf4` and `mapf5`) are used to define how Format 4 and Format 5 data are structured and parsed. The data is extracted and stored into lists (`lol4`, `lol5`).
   - Any unparsed lines are logged for further review and stored in dictionaries (`nol4`, `nol5`).

The code loops through a list of zip files, extracting and processing Format 4 and Format 5 files while skipping unrelated files.


# 09/14/2024 to 09/16/2024

Working in `US24UW990JEPL.01.01.01.py`.
Short summary: current situation slightly far from expected situation. <br>
Lines with different length caused problems. <br>
Lines ending with `\r\n`. <br>

New approach: MAXIMIZATION OF SIMPLICITY.

# 09/17/2024
Change approach.

## US24UW990JEPL.01.01.01.py

#### Overview

This script processes data from zip files containing two formats: Format 4 and Format 5. It reads data lines, adjusts them to expected lengths, and saves them into text files.

Data saved as:

```angular2html
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.01.01_f4.txt
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.01.01_f5.txt
```

# 09/22/2024

## Refactor - US24UW990JEPL.01.02.01.py

### Script Overview

This Python script is updated to extract, simplify, and store data from Format 4 and Format 5 using web scraping techniques. It retrieves the format structures from specified URLs, parses the HTML tables, and stores the data as JSON files. Additionally, the script maps the extracted data into a simplified format and generates HTML files for easy viewing of the format structure.

#### Key Components

1. **Imports:** 
   - Essential libraries for web scraping (`BeautifulSoup`, `requests`), file handling, and time profiling.

2. **Main Functions:**
   - **`tp()`**: A utility function to calculate and display elapsed time in hh:mm:ss format.
   - **`read_format()`**: Scrapes data from the Format 4 and Format 5 webpages, parses the table, and saves the structure as a JSON file. In case of failure, it loads the data from a backup JSON file.
   - **`format_map()`**: Simplifies the extracted format data into a more readable dictionary structure.
   - **`html_parser()`**: Converts the simplified format data into an HTML table for easy viewing.

3. **Output:**
   - The script generates multiple files: 
     - JSON files storing the extracted format data (`Format4.json`, `Format5.json`).
       - ```angular2html 
         /blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.02.01.Format4.json
         /blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.02.01.Format5.json 
         ```
     - Simplified JSON mappings (`f4map.json`, `f5map.json`).
       - ```angular2html
         /blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.02.01.f4map.json
         /blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.02.01.f5map.json
         ```
     - HTML files displaying the format structure (`f4map.html`, `f5map.html`).
       - ```angular2html
         /blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.02.01.f4map.html
         /blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.02.01.f5map.html
         ```

4. **Execution:** 
   - The script logs its start time, saves profiling information, and tracks the execution duration.


## US24UW990JEPL.01.03.01.py 

### Summary of the Code

This Python script processes a Format 5 dataset related to reproductive events in cattle. Its main objectives is to generate a sample-dataset with an easy-to-visualize html format, so you understand better the data structure, as a pre-requisite to estimate the following parameters:

- **ICC**: Interval calving to calving
- **ISS**: Interval calving to service
- **ILSC**: Interval last service to calving
- **NSGP**: Number of services during the gestation period
- **TRE**: Types of reproductive events

#### Key Components:

1. **Initialization**: The script initializes paths for data storage and logs the start time of execution.

2. **Data Mapping**: It reads mapping information from JSON files corresponding to Format 4 and Format 5 datasets.

3. **Row Processing**:
   - **`idx_maper`**: Converts index fields into usable integer indices.
   - **`line_chopper`**: Extracts relevant data from each line of the dataset based on the mapping.

4. **Data Reading**: The `txt_reader` function reads the specified Format 5 text file, processes it into a DataFrame.

5. **Analysis**: 
   - Identifies unique identifiers with multiple records and creates a subset of the DataFrame.
   - Converts specific columns to numeric types and sorts the DataFrame.

6. **Output**: Generates an HTML file to visualize the processed data.

7. **Execution Time**: Logs the execution time upon completion.

This code serves as a foundation for further analysis of reproductive data in Jersey.

#### Note:
Structure of the data is complex. Also, the mapper dictionary extracted from the web scrapping in code `US24UW990JEPL.01.02.01.py` does not result convenient for the proposes of this study.

### Next steps:
* Re-define the dictionary that will be used as a Format 5 map.
* Allow nested levels.
* Instead of a dataframe, work with a dictionary of dictionaries.
* Save the dictionary of dictionaries in a JSON file.


# 09/25/2024

## US24UW990JEPL.01.02.02.py
Modifies Format 4 and 5 mapping dictionary to revealed convenience.
Code updated for Format 5. Format 4 still not done.

### Format 5 - Corrections in Mapping Dictionary

#### Script Overview

This Python script processes a dictionary (`fdict5`) derived from data on the official CDCB website. It aims to correct inconsistencies in the dataset, particularly from stroke 138 onward, and to standardize the structure for various reproductive events.

##### Key Components

1. **Initialization:**
   - Creates a deep copy of the original dictionary (`fdict5`) and extracts the first reproductive event into a new dictionary (`fdict5s1`).

2. **Data Cleaning:**
   - Defines a function (`get_keys_v1`) to find keys based on their 'Field Description'.
   - Cleans up unnecessary reproductive segments from `fdict5s2` (section mapping strokes for reproductive event 1 to 20).

3. **Structure Correction:**
   - Further refines the dictionary by removing unwanted keys and organizing relevant entries into a new nested dictionary (`nest_dict`).

4. **Value Updates:**
   - Utilizes a recursive function (`update_nested_dict`) to modify specific values within the nested dictionary, adjusting byte positions by adding 30.

5. **Reproductive Events Mapping:**
   - Iterates to create mappings for reproductive events 2 to 20, copying the structure of the first event and updating byte positions accordingly.

6. **Final Assembly:**
   - Combines all components into a single dictionary (`fdict5_v2`) that reflects the updated and corrected data.

7. **Output:**
   - Saves the final corrected dictionary as a JSON file for further analysis or processing.
```angular2html
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.02.02.Format5.json
```
Smething similar must be done with Format 4. 

Next steps:
1. Improve Format 4 mapping dictionary.
2. Narrow down in results needed:
   1. Create JSON file of Format5.txt data following structure given by Format 5 mapping dictionary.
   2. Extract RAW traits before any data cleaning:
      1. ICC
      2. ICS
      3. ISS


# From 09/26/2024 to 10/15/2024

## US24UW990JEPL.01.03.02.py
Continuation of `US24UW990JEPL.01.03.02.py`. ICS and ISS is defined and plotted in full dataset. ICC and ISC has bug.

Lower amount of time invested in this project due STAT 849 first midterm.

Francisco Peñagaricano meeting:
At the end of the day, we need to finish with a dataset that has a row that ends with 0 (no abortion) or 1.

3 Different ways of measuring abortions.

**Direct:** <br>
1- Identify the label ABORT theoretically present in Format 4.

**Indirect:** <br>
2- Use intervals (Pregnancy - services) to capture plausible abortions. <br>
3- Use interval (Insemination - insemination) to capture plausible abortions. <br>

# From 09/25/2024 to 02/20/2025
STAT849 and COMPSCI540 were highly time-consuming, with a lot of HW, projects and exams. <br>
I had to invest time to pass these courses. Final result, B and B. Ordinary performance. <br>

Project of Estrus Expression (EE) linked to MS degree had to be finished. <br>
I had to retrieve milk production and estimate genetic correlations with EE traits. <br>
On 02/17/2025 the updates on my thesis chapter with new results was finished. <br>
Slow, to slow. <br>

## Reflections on the CDCB Project (Beef on Dairy)

I dedicated significant time to working on the CDCB project (Beef on Dairy).  
After obtaining my results, I was instructed to update all my labels and analyses to align with specific publications in the field.  

Several specific requests were made. Few examples below:  
- I had to include a breed representing only 2% of the total dataset (Semental).  
- I was advised to be cautious with the labeling of Semental, as it varies by continent.  
- I was required to run my analysis on the same dataset used by a collaborator.  

This raised several fundamental questions:  
- Why did I spend 3 months creating a dataset for this analysis if, in the end, I am required to replicate the results of another researcher who had already prepared a dataset?  
- Why not simply run my analysis on the other researcher’s dataset from the beginning?  
- Why not just use the other researcher’s model instead?  
- Is it truly justified to invest an additional 30% of time to include data that accounts for only 2% of the total?  
- Will this 2% of extra data genuinely lead to conclusions that provide higher value to the dairy industry?  
- Or is the inclusion of Semental animals primarily aimed at reinforcing evidence aligned with the single leading research?  

Ultimately, what does CDCB prioritize more?  
- Advancing the scientific understanding of Beef on Dairy crossbreeding?  
- Reinforcing research in alignment with USDA/AGIL publications?  
- Securing a role in genetic evaluations for Beef, as Beef genetics increasingly replace Dairy bulls in the market?

At a philosophical level:
- How I as a scientist can contribute to any of these motivations?


# 02/20/2025

Read and re-cap codes `US24UW990JEPL.01.04.01.py` and `US24UW990JEPL.01.05.01.py`.

## US24UW990JEPL.01.04.01.py
Data visualization for `f4` and `f5` codes.
Plots are saved in:
```angular2html
/blue/mateescu/agustinchasco/Projects/reprojersey/core/US24UW990JEPL.01.04.01
```
Two folders, one for testing proposes. Another to save plots from full dataset.

## US24UW990JEPL.01.05.01.py

Merging datasets.
Proposing key as the concatenation of `X3` + `X4` + `X5` + `X35`.
Proposing files `f4s1`/`f5s1` with lines spanning a key without duplications.
Proposing files `f4c1`/`f5c1` with lines not in `f4s1`/`f5s1`.

Code is not finished.

New approach: datasets `f4` and `f5` are large and complex, and during the merging you will need to make sure things make sense. <br>
Before, you proposed as testing dataset a segment of the full dataset. The complication of this approach, is that you may not have all the records of a single ID. <br>
To make sure things make sense, it would be convenient if I could track the merging of few IDs.

Consequently, I will proceed with the creation of 2 new testing datasets, with a set if IDs in both. <br>
I am thinking of something like 1% of the total number of unique IDs present in both datasets. <br>

The current code will serve this propose.

4 outputs:
* 2 files are super-small-almost-useless (sample of samples).
```angular2html
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.01_babytestf4.txt
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.01_babytestf5.txt
```
* 2 are useful, with around 233000 rows ech, with spanned keys in both of them. Over this dataset I will develop the merger-algorithm.
```angular2html
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.01_babyimplf4.txt
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.01_babyimplf5.txt
```

These last 2 are the ones I will use for testing my merger codes.

## US24UW990JEPL.01.05.02.py
Codes runs in testing mode reading data below.
```angular2html
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.01_babyimplf4.txt
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.01_babyimplf5.txt
```
If code runs in implementing mode, it reads the whole dataset.

The objective is to separate lines where key are not duplicated, from lines with duplicated key.

If 2 or more lines are sharing the same key..., why is that happening? 
Is the record corrupted? Is there something else that should be considered?

The idea is to pinpoint this questions and anticipate oversights when merging.

Sampled files in `010501` still impractically larger. Sample size reduced.

# 02/22/2025
Adapting `010502` to the following files when testing:
```angular2html
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.01_babyimplf4.txt
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.01_babyimplf5.txt
```

These files have shared key, and they can be used to mimic a merge in the full dataset.

Update saving path:
```angular2html
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.02/(implement/test)
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.02/(implement/test)
```

## US24UW990JEPL.01.05.03.py

Modification. Adapted to read files in `.../data/US24UW990JEPL.01.05.02`.

Modification in function `get_txt_files_path()`.

I still must eliminate consistent duplications, and stack unique corrected rows to partition with unique keys.
I still need to find a solution for duplicated and inconsistent rows.

# 02/25/2025
Goals:
- Merge consistent baby datasets.
- Split inconsistent subset and locate it in a well-defined bath.
- Identify sources of inconsistency. 
- Always track number of rows.
- Expand code to large dataset.

Eventually, it would be better if I can combine codes in a singe script. \
Also..., if I find myself writing the same function across codes..., why instead you don't write it as a module?


Working on `US24UW990JEPL.01.05.03.py`.

## `US24UW990JEPL.01.05.03.py`

Code designed to read txt files in:
```angular2html
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.02/
```
If texting, codes reads `test` folder. Otherwise, `implement` folder.

Script designed to read the following files:
```angular2html
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.02/[***]/US24UW990JEPL.01.05.02_[***]_nouniquef4.txt
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.02/[***]/US24UW990JEPL.01.05.02_[***]_uniquef4.txt
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.02/[***]/US24UW990JEPL.01.05.02_[***]_nouniquef5.txt
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.02/[***]/US24UW990JEPL.01.05.02_[***]_uniquef5.txt
```

Script mainly deals with files:
```angular2html
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.02/[***]/US24UW990JEPL.01.05.02_[***]_nouniquef4.txt
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.02/[***]/US24UW990JEPL.01.05.02_[***]_nouniquef5.txt
```

In both files, I delete consistent duplications, and identify consistent reports after drop duplications.\
Such consistent lines after dropping duplications are keep. Suc lines are added to the consistent records:
```angular2html
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.02/[***]/US24UW990JEPL.01.05.02_[***]_uniquef4.txt
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.02/[***]/US24UW990JEPL.01.05.02_[***]_uniquef5.txt
```

Those rows with duplicated keys, but non-duplicated rows are saved for further analysis.

File `US24UW990JEPL.01.05.03.out` shows number of rows for each dataset.

Saved datasets:
```angular2html
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.03/[***]/US24UW990JEPL.01.05.03_[***]_pdf4nu.txt
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.03/[***]/US24UW990JEPL.01.05.03_[***]_pdf4u.txt
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.03/[***]/US24UW990JEPL.01.05.03_[***]_pdf5nu.txt
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.03/[***]/US24UW990JEPL.01.05.03_[***]_pdf5u.txt
```

Files `pdf4u.txt` and `pdf5u.txt` have records without duplicated keys.

Files `pdf4nu.txt` and `pdf5nu.txt` have records with duplicated keys. These records ,ust be explored.

Overall, I expect 45% of the records in file `pdf4u.txt` or `pdf5u.txt`.\
55% of remaining records with duplicated keys are in `pdf4nu.txt` or `pdf5nu.txt`. The question is:

Goals 0225/2025 achieved.

- Why, if the key is the same, 2 or more rows are different? Why 55% of data shows this signature? 
- Am I missing something?

Next steps:
- Identify the source of conflict in records with duplicated keys.
- Visualize a simple example.
- Can I solve something? Am I missing something?
- Take needed actions.


Meanwhile:
- With data that is not duplicated, what do you do?
- Is there any association that may contribute to the detection of early embryonic loses?
- Is there something significant worth to report?


Important and general question: \
**How can you know the path you should choose if you do not really know where you want to arrive?**

The point is: 
- what do I expect from this dataset?
- What can I conclude?
- What are the potentially useful associations?
- Why do I need to merge both files?
- Do you really know the information both of them stores?
- In a narrower sense: what is worth to report on Friday?

# 02/26/2025 - 02/27/2025
 
# Module `US24UW990JEPL_01`. 
Module is integrated by functions I always use while handling `f4` and  `f5` txt files.
Each function is well described in the module.

The `Initializer` module provides a structured way to manage script execution, data handling, and logging in Python scripts. It facilitates directory management, file path retrieval, data processing, and execution profiling.

### Features:

- **Initialization & Logging**: Captures script metadata (name, paths, and execution mode) and logs execution details.
- **Directory Management**: Ensures necessary directories exist for saving output files.
- **File Handling**:
  - Retrieves file paths within the data directory.
  - Constructs standardized save paths for output files.
  - Saves pandas DataFrames as formatted text files.
- **Data Processing**:
  - Reads and applies JSON-based mapping files to format text data.
  - Converts fixed-width text data into structured pandas DataFrames.
- **Execution Profiling**: Measures and logs the script execution time.

This module is particularly useful for structured data processing workflows where standardized input/output handling and logging are needed.

## `US24UW990JEPL.01.06.01.py` & `US24UW990.01.06.ipynb`

Basically, script is designed to take the clean datasets `f4` and `f5` without key conflict.\
It must be known that, by the current date, work still need to be done over `f4` and `f5`. 50% of their keys are duplicated.\
Nevertheless, the script is assuming that `f4` & `f5` datasets are ready to merge, and proceeds with this step.\

Basically, It just join the columns of one dataset to the columns of the other dataset.\
In other words, of dataset `f4` has $p_{f4}$ columns, and dataset `f5` has $p_{f5}$ columns. Then merged dataset has $p_{f4} + p_{f5} - 1$ columns.\
`-1` stands for the `key` column, which is repeated in both datasets.

Note: around `30` columns are supposed to be shared between both datasets. 

A quality-check would be that the information in between shared columns is supposed to be the same and should be consistent.\
This is something I will do in a different script. For today, my goal was somehow combine both datasets.

Code reads dataset with unique keys. Nowadays, such dataset is in:
```angular2html
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.03/[***]/US24UW990JEPL.01.05.03_[***]_pdf4u.txt
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.05.03/[***]/US24UW990JEPL.01.05.03_[***]_pdf5u.txt
```

Merged dataset in:
```angular2html
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US24UW990JEPL.01.06.01/[***]/US24UW990JEPL.01.06.01_[***]_merged.txt
```

Bellow, the chatGPT description of the `US24UW990JEPL.01.06.01.py` code.

### Data Merging and Processing Script

This Python script handles the merging and processing of two datasets (`pdf4` and `pdf5`). 

It includes initialization, file reading, data manipulation, and file saving steps, with profiling for execution time.

Incremental programming for this script was done in `US24UW990.01.06.ipynb`.

#### Objectives:
- **Merge Cleaner Datasets**: The primary goal is to merge two datasets (`pdf4` and `pdf5`) based on a constructed key.

#### Features:

1. **Initialization**:
   - The `Initializer` class is used to set up paths, directories, and other configuration details. 
   - The script uses different paths based on whether it’s running in testing or implementation mode.

2. **Reading Data**:
   - Reads `pdf4` and `pdf5` data files using the `TXT_reader` method, which applies a mapping from JSON files.

3. **Creating a Key**:
   - Constructs a `concat_key` from several columns (`X3`, `X4`, `X5`, and `X35`) for both `pdf4` and `pdf5`.

4. **Data Merging**:
   - Merges the two datasets using an outer join based on the `concat_key`. The resulting DataFrame (`pdf`) contains all records from both datasets, with null values where there is no match.

5. **Key Uniqueness Validation**:
   - Ensures the `concat_key` is unique in both `pdf4` and `pdf5`.

6. **Column Tagging**:
   - Tags the columns with the respective file identifiers (`f4` and `f5`) to distinguish between the two datasets in the merged DataFrame.

7. **Merge Analysis**:
   - Performs checks and calculations to assess the proportion of keys present in both datasets and in only one of the datasets.

8. **Replacing Null Values**:
   - Replaces any `None` values in the merged DataFrame with strings consisting of 'n' repeated for each column’s length.

9. **Saving the Merged Data**:
   - Saves the merged DataFrame as a text file with a standardized naming format.

10. **Profiling Execution Time**:
    - Uses the `EndsProfiling` method to display the total execution time of the script.

# 02/28/2025

## `US24990JEPL.01.07.01.ipynb`

Shows data shrinkage in each filtering step for `f4`. 

`ipynb` files have a limitation in Pycharm. They must be small.

Therefore, only `f4` in this file.

Summary graph in:
```angular2html
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US25UW990.01.07.01_f4.html
```

## `US24990JEPL.01.07.02.ipynb`

Shows data shrinkage in each filtering step for `f5`. 


Summary graph in:
```angular2html
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US25UW990.01.07.02_f5.html
```

**Meeting.**
- Kent Weigel: Duplications due non-updated records. Try to solve them.
- Kent Weigel useful comment: handling datasets is like going to the farm to collect data. It may take time, but is a fundamental stage.
- My observation: how can I be more efficient/effective/quicker preparing a large dataset? 

# 03/03/2025

Code `US24990JEPL.01.06.01.py` 3 days running. You need to solve this issue.

Objectives:
- Try to identify in which column is the conflict among duplications.
- Then, recover duplications, selecting the correct stuff, and drop what you don't need.
- Record all in code `US25UW990JEPL.01.07.[01/02].ipyng`. Show dataflow.

## `US24UW990JEPL.01.05.03.py`

Working to identify conflictive columns.

# 03/04/2025 - 03/06/2025

Pycharm is super heavy. I was kicked out from HPG.

I had to resolve the issue. Blocked on 04/04/2025. Resolved on 03/05/2025.

I had to move from PyCharm to VSCode. I hade to learn how ot tunneling VSCode, and how toopen Jupyther Hub, using UF RC services.

Working on `US24UW990JEPL.01.05.04.ipynb`.

## `US24UW990JEPL.01.05.04.ipynb`
Developing `US24UW990JEPL.01.05.04.py`. Basic explanations and steps.

## `US24UW990JEPL.01.05.04.py`

Somehow, from VSC virtual environment pandas is not being recognized.

```
[agustinchasco@c29b-s20 Projects]$ /bin/python3.11 /blue/mateescu/agustinchasco/Projects/reprojersey/core/US24UW990JEPL.01.05.04.py
Traceback (most recent call last):
  File "/blue/mateescu/agustinchasco/Projects/reprojersey/core/US24UW990JEPL.01.05.04.py", line 2, in <module>
    import US24UW990JEPL_01
  File "/blue/mateescu/agustinchasco/Projects/reprojersey/core/US24UW990JEPL_01.py", line 4, in <module>
    import pandas as pd
  File "/home/agustinchasco/.local/lib/python3.11/site-packages/pandas/__init__.py", line 19, in <module>
    raise ImportError(
ImportError: Unable to import required dependencies:
pytz: No module named 'pytz'
dateutil: No module named 'dateutil'
```
Annoying error.

Using `subproces` module in jupyter notebook to execut script from this environment.

**Problem and solution:**
I had to create an environment.
The information to set a environment where you can safely download modules is here:

```
https://help.rc.ufl.edu/doc/Managing_Python_environments_and_Jupyter_kernels
```

Modification in module `_01`. Definition `Directories` in class `Initializer` updated. One new parameter added. This for sure will make future codes crush. Eventually I will g.
Simidebularly: definition `SavePath` updated in class `Initializer`. Script 010503 will need to be debugged. Parameter must be added to the function.

# 03/07/2025


Meeting with Francisco and Kent.
Taks: define where are we going.

# 03/12/2025

Frustrating problems:
- HPG loging returning error. For example I can not diplay and test codes in Jupyter HUB
- Commiting codes: lot of conflicts. 
- f4 & f5 not merging.
- Define overall destination.

In order of importance for thso project:
1- Define overall destination.
2- f4 & f5 not merging.
3- HPG loging returning error. For example I can not diplay and test codes in Jupyter HUB
4- Commiting codes: lot of conflicts. 

What can I handle?
1- Define overall destination.
2- f4 & f5 not merging.
4- Commiting codes: lot of conflicts. 

Depends on Mateescu authorization:
3- HPG loging returning error. For example I can not diplay and test codes in Jupyter HUB

Pruning top 2 --> simplify simplify and simplify! Pick top one!
1- Define overall destination.

## Defining overall destination.
How are you going to do the analysis?

# 03/12/2025 - 03/15/2025
Show overall direction of the project.

# 03/15/2025 - 03/19/2025
Closing stuff related to STAT850. Midterm on 03/19/2025.
Solving issues related to my login in HPG.

# 03/20/2025

Recap general functionalities:
- `[**].01.05.[**].py` for cleaning stage.
- `[**].01.06.[**].py` for merging stage.
- `[**].01.07.[**].py` for summarizing cleaning stages.

Overall functionality:
- `[**].01.[**].[**].py` for prepare dataset.
- `[**].02.[**].[**].py` for analyze dataset.
- Potentially more codes.

Once you have the path, backpropagation, which means, go back, delete waste, condense all in a code, a develop a program that returns the main conclusions of this project.

Where am I?
- `[**].05.04.01.py` identifies columns source of conflict.
Done.

# 03/21/2025 - 03/25/2025
`US24UW990JEPL.01.06.01.py` I merged f4 and f5 in a single dataset.

#  03/25/2025
Centralize script in single code: `US25UW990.01.py`.

When trying to concatenate the type of reproductive events in the 20 reproductive events, I found that data did not make sense.
Then, I backtrack the issue, and discovered a painful logical bug in the module `US24UWJEPL_01.py`.
I had to correct such issue.
It was a painful and time consumming error. Is not worth it to describe this bug, the important is that is solved.
In short, I had to update the definitions of `Save_PDF_as_TXT` function in class `Initializer`.
Bassically, I had to target few columns from the f5 pandas dataframe, as information is repeated accross columns.
In other words, for row $i$, I would expect 737 characters. But when concatenating information in row $i$ in pdf5, I was obtaining 1957 characters.
Then, I was saving this 1957 characters. 
In subsequent steps, I was using the maping dictionary and the line chopper to chop 737 characters of each line with 1957 characters.
It was a reaqlly mess! and when I tried to target information, I realized things didn't make any sense....
The problem is solved, and I always solve the standard line of 737 strokes.

**More details of problems in case needed:**
Problem given by reproductive segments.

- repr s1 138-167
```
 'X37': {'Reproductive event 1 -> 0 -> Field Description -> Type of reproductive event code': '138'},
 'X38': {'Reproductive event 1 -> 1 -> Field Description -> Date of reproductive event (YYYYMMDD)': '139-146'},
 'X39': {'Reproductive event 1 -> 2 -> Field Description -> Event date origin code': '147'},
 'X40': {'Reproductive event 1 -> 3 -> Field Description -> Within event sequence number': '148-149'},
 'X41': {'Reproductive event 1 -> 4 -> Field Description -> Service sire ID type': '150'},
 'X42': {'Reproductive event 1 -> 5 -> 0 -> Field Description -> Formatting for type "R" identifications': '151-167'},
 'X43': {'Reproductive event 1 -> 5 -> 1 -> Field Description -> Breed code of service sire (alpha code only, no zeros)': '151-152'},
 'X44': {'Reproductive event 1 -> 5 -> 2 -> Field Description -> Country code of ID origin': '153-155'},
 'X45': {'Reproductive event 1 -> 5 -> 3 -> Field Description -> Identification number of animal registration, or eartag)': '156-167'},
 'X46': {'Reproductive event 1 -> 6 -> 0 -> Field Description -> Formatting for type "N" identifications (PREFERRED)': '151-167'},
 'X47': {'Reproductive event 1 -> 6 -> 1 -> Field Description -> Blanks': '151-157'},
 'X48': {'Reproductive event 1 -> 6 -> 2 -> Field Description -> NAAB code (components detailed below)': '158-167'},
 'X49': {'Reproductive event 1 -> 6 -> 3 -> Field Description -> Semen processing organization (stud number < 800)': '158-160'},
 'X50': {'Reproductive event 1 -> 6 -> 4 -> Field Description -> Breed code of ID (alpha code only, no zeros)': '161-162'},
 'X51': {'Reproductive event 1 -> 6 -> 5 -> Field Description -> Bull number assigned within processing organization': '163-167'},
```
`['X37', 'X38', 'X39', 'X40', 'X41', 'X42']`

- repr s2 168-197
```
'X52': {'Reproductive event 2 -> 0 -> Field Description -> Type of reproductive event code': '168'},
 'X53': {'Reproductive event 2 -> 1 -> Field Description -> Date of reproductive event (YYYYMMDD)': '169-176'},
 'X54': {'Reproductive event 2 -> 2 -> Field Description -> Event date origin code': '177'},
 'X55': {'Reproductive event 2 -> 3 -> Field Description -> Within event sequence number': '178-179'},
 'X56': {'Reproductive event 2 -> 4 -> Field Description -> Service sire ID type': '180'},
 'X57': {'Reproductive event 2 -> 5 -> 0 -> Field Description -> Formatting for type "R" identifications': '181-197'},
 'X58': {'Reproductive event 2 -> 5 -> 1 -> Field Description -> Breed code of service sire (alpha code only, no zeros)': '181-182'},
 'X59': {'Reproductive event 2 -> 5 -> 2 -> Field Description -> Country code of ID origin': '183-185'},
 'X60': {'Reproductive event 2 -> 5 -> 3 -> Field Description -> Identification number of animal registration, or eartag)': '186-197'},
 'X61': {'Reproductive event 2 -> 6 -> 0 -> Field Description -> Formatting for type "N" identifications (PREFERRED)': '181-197'},
 'X62': {'Reproductive event 2 -> 6 -> 1 -> Field Description -> Blanks': '181-187'},
 'X63': {'Reproductive event 2 -> 6 -> 2 -> Field Description -> NAAB code (components detailed below)': '188-197'},
 'X64': {'Reproductive event 2 -> 6 -> 3 -> Field Description -> Semen processing organization (stud number < 800)': '188-190'},
 'X65': {'Reproductive event 2 -> 6 -> 4 -> Field Description -> Breed code of ID (alpha code only, no zeros)': '191-192'},
 'X66': {'Reproductive event 2 -> 6 -> 5 -> Field Description -> Bull number assigned within processing organization': '193-197'},
```

`['X52', 'X53', 'X54', 'X55', 'X56', 'X57']`

Problem when expanding information in f5 to pandas dataframe. Information between 151 to 167 stroke has multiple meanings and they are not excluyent. Then, different columns are sharing same characters from 151-167 for reproductive event 1. This hapens for rpeoductive event 1, 2 .., 20.
Then, concatenation of of elements across columns in a givne row is greater than 737. When reading this concatenated string using the map for f5 to chop the lines, problem was evident.

SOLVED.

#  03/26/2025
Pushing stuff in `US25UWJEPL.01.py`.
Pushing `010501`.
Convinient modifications in module `US24UWJEPL_01`.
Adaptations of `US25UWJEPL.01.py`.
`010501` already in `US24UWJEPL_01` and `US25UWJEPL.01.py`.
Script running. In implementing mode, would take around 2 hours.

After implementing `010501`, this files are created:
```
US25UW990JEPL.01_test_010501f4.txt
US25UW990JEPL.01_test_010501f5.txt
```

Such files were moved manually to path:
```
/blue/mateescu/agustinchasco/Projects/reprojersey/data/US25UW990JEPL.01/test
```

Pushing `010502`.
Pushed!

Pushing `010503`.

#  03/27/2025
Objectives:
Push `010503` into master script.
Push `010504` into master script.
Push `010601` into master script.


Progress:
`010503` pushed into master script.
Waiting for the script to process full dataset.

Pushing `010504`.

#  03/28/2025

Keep workin on `US25UWJEPL.01.py` and `US24UW990JEPL_01.py`


Pushing `010504` --> Pushed.
Pushing `010601` --> * I had to debug `010504`.
Pushing `010601` --> Pushed.

# Saturday 03/29/2025 

Concatenate reproductive events and show frequency distribution.


Problem with commit. 
My files suddenly dissapeaqr when trying to push work to Git repository.
Recovering 

Irrecoverable. However, good oportunity to delete all stuff that is not useful, and integrate even more my work in a single script.

Integrating construction of mapf4 joson file to module.

Module called `US25UW990JEPL_02.py`, just in case to avoid overriding.
Master code called `US25UWJEPL.02.py`, just in case to avoid overriding.

Working on `GetFormatMap`.

Doing again the master script.

Something CRITICAL is unsolved! I am gorking with git, then I MUST commit and push, otherwise I risk to lose my work.


# Sunday 03/30/2025 
Merging both map files to reade merged dataset.

Generate the result of concatenated reproductive events. Do plot.
Add `010501`, `010502`, `010503`.

Hold in `010504`, `010601`.

Multiple mistakes and bugs in mapping json file. I did all possible errors someone can do. I was like a nightmare.

Somehow, I end up with the correct mapping file. Headache.

# Monday 03/31/2025 

## Must do
- Concatenation of reproductive event types.
- Show conclusions of main categories.

## Should do
A)
- See shared columns. Identify conflicts in data.
- Somehow resolve such conflicts.
- Eliminate duplicated columns. Correct remaining columns. Reduce dimensionality of dataset.

B)
- Activate, test and make sure of functionality of `010501`, `010502`, `010503`, `010504`, `010601`.

I start with `must do`. Then proceed with `should do`.

Plot events with a recorded `P` (pregnancy record) in the middle of reproductive events. Plot and save frequency table of these events.


# Thursday 04/03/2025 

## Basic Git Workflow

### 1 Start Working (Switch to Your Branch)
```bash
# If you're already on your branch, skip this step.
git checkout my_branch

# If the branch doesn’t exist, create it and switch to it:
git checkout -b my_branch
```

### 2 Make Changes & Save Them
```bash
# Modify your files as needed.
# Check what has changed:
git statusgit

# Add specific files:
git add filename.py

# OR add all modified files:
git add .

# Commit your changes with a message:
git commit -m "Describe what you did"
```

### 3 Push Changes to GitHub
```bash
# Send your changes to the remote repository:
git push origin my_branch
```

### 4 Merge Changes into `master` (When Ready)
```bash
# Switch to master
git checkout master

# Update master (make sure you have the latest version)
git pull origin master

# Merge your branch into master
git merge my_branch

# Push the updated master to GitHub
git push origin master
```

### 5 Switch Back to Your Branch (Continue Working)
```bash
# If you need to continue working on your branch:
git checkout my_branch
```

### Bonus Tips
```bash
# Check branches
git branch  # Shows all local branches

# See commit history
git log --oneline --graph --all

# Undo last commit (before pushing)
git reset --soft HEAD~1

# Undo last commit (after pushing, use with caution!)
git revert HEAD
git push origin my_branch
```

This is a **basic yet powerful workflow** that works for most Git projects.

## Objective:
- Create a function that targets a subset of Keys, otherwise takes a random sample. _/
- Such function also must take a subset of columns. _/
- Function must save subseted dataset as html. _/
- The objective of this function is to visualize the data and reduce complexity. _/

- 2 approaches. 1 gives a lot of information, 2 is more story-telling.
- 1) Take two subsequent Repro events in given lactation. Concatenate event type. Define days in between. Group by concatenated event type. 
- 1.1) Pick top 3 categories. Plot histogram of differences in days.
- 1.2) Pick top 3 categories in which first type is P, and second type is some kind of insemination. (I will have to somehow triangulate stuff with the calving date to make sure such subsequent insemination is not in fact a nosense event when the animal was in fact pregnant).

- 2) Plot sequence of events in a visually catchy way. Would help to support further explanations.

Meeting 04/04/2025
- They want to see the differences in day between consecutive events.
- They want to understand the spaicing between events.

I did a function that allows the estimation of the elapsed time (days) between consecutive events.
The function is inside `PlotDiffs()` in `US25UW990JEPL_02.py` module.

Adaptation of function `PlotDiffs()`. Pulishing saving paths. Pulishing modules.

# 04/05/2025 to 04/06/2025 (Sat & Sun)
- I was eble to plot histograms showing distribution of elapsed time between two cnsecutive reproduction events.

# 04/09/2025
Few improvments:
1- Add C-R1 interval to `dc.PlotDiffs` definition. Done.

2- Next steps.
- Get proportion of nulliparous and multiparous.
- Get proportion of ID-Lact ending reproductive sequence with P
- Get proportion of animals with 1 or more lactations.
- Among animals with multiple lactations, get difference between subsequent recorded lactations. Plot barplot. We should expect all 1.
- Among animals having two sequential lactations with diff 1, get interval between date last reproductive event and subsequent calving date. We should expect 9*30

Fundational concern:
- Information in key must be sound. Spoecially calving date. For a given row, you must have a single calving date. you can not have 2 calving dates on with 'nnnnnnnn'. You need to make sure to check this.
- Latter I will correct the staff related to shared columns. They must have consistent information.
- Another potential issue.., is that key is the concatenation of raw information. Errors in YYYYDDMM may lead to differnt keys.

# 04/10/2025
- Potential structural improvements:
1- `SetKey`: If Key is present, and you do not force the override, just don't do nothing. This will smooth out the back-and-forth process when testing and developing.
2- I will be working in modules. Same code will have different modules activated. Output of one module may be importnat (print statements). It would be nice if I can allocate such print statements in a specific folder corresponding to the module. This is specially important for the module `0202`.
3- If a plot is super standard, you could define this as a function.

`JEPL0202`
I did multiple exploration:
- Number of nulliparous.
- Number of IDs with multiple lactations.
- Interval between two sequential lactations. Exploration of missing lacations.
- Percentage of Keys with recorded reproductive events (f5 has key, then key counts as recorded).
- Among keys with recorded events, show last reproductive type event. Plot frequency distribution.
- Frequency distribution of lactations.
- Among animals with sequential lactations, check if initial lactation ends ith pregnancy check. If not, show how they are labeling last reproductive event.
- Among animals with sequentiual lactations: show interval Pregnancy Calving for thos with Pregnancy check. Show Interval 'whatever' - Calving for those w/o Preg-check. (This analysis may also exclude interval in which dates are not valid).


# 04/11/2025
Important code to transfer data from remote ssh server to personal computer:
```
(base) agustinchasco@Agustins-MacBook-Air US25UW990JEPL.02.01.04 % scp -r agustinchasco@hpg2.rc.ufl.edu:'/blue/mateescu/agustinchasco/Projects/reprojersey/core/US25UW990JEPL.02/implement/impl_020104/*' "/Users/agustinchasco/Documents/UW Madison/Core/Research/reprojersey/results/US25UW990JEPL.02.01.04"
```

# 04/12/2025 - 05/01/2025
Meeting with my committee.
Finals, reports and presentations.
Reading paper related to early/late fetal losses. ref:

# 05/02/2025
Presentation/meeting. We decided that we are going to get interval service service.
We do know some services ending in pregnancy loses.
We do know sometimes this is not recorded.
We do know that whenever felat mortality occurs, interval service service gets delayed. 
Then, validate fetal mortality (0, 1) with interval service service. They m,ust be highly correlated.

End of semester: report & presentation BMI620, final exam STAT850.

# 05/07/2025 Wed
Subset these IDs where you know there are Fetal Mortality (recording O after P).
Subset random IDs where you do not know anything about FM.

Develop pipeline with this subseted data. 

## Defining reproductive types. Excluding some lavels.
Reproductive events any acttion with the intention of end up in a conception. The definition is wide, but also robust. 
Diversity in such definition will be accounted as different labels on fixed effects.
E, I and J may result as different category, but latter I will account for that adding this as fixed effect in my model.
P and O latter going to be used to flag 0 and 1.
H likelly to be used for flag 1's.
H, S, P, O, X, D not expected to be an event supposed to end up in pregnancy success.

# 05/08/2025
Enriching dataset. Preparing standardized data to proceed w/ stat analysis!

# 07/04/2025
I finished my summer internship at ABS global.
I will continue with my research in embrionic losses.git stat  
