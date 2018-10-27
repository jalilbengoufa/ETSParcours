# ETSParcours 

### Installation

require:
- python (2.7? 3.5?)

Python packages:
- camelot
- camelot's dependencies, if needed

### Usage

First, run the script to parse the pdf files into a csv files :
```
 python parsePDFToCSV.py
```

Look into the `cs_files/generated` directory to make sure that the parsed files looks fine

After that, run the second script that will filter and merge the generated csv file into a cleaner output:
```
python filter.py
```
