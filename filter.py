#!/usr/bin/env python

import os,csv,json
localFilesPath = os.getcwd()+'/csv_files/generated/'
localFilesPathMerged = os.getcwd()+'/csv_files/merged/'

##merge files 
os.system('sed 1d '+localFilesPath+'*LOG.csv > '+localFilesPathMerged+'LOG.csv')
os.system('sed 1d '+localFilesPath+'*CTN.csv > '+localFilesPathMerged+'CTN.csv')
os.system('sed 1d '+localFilesPath+'*ELE.csv > '+localFilesPathMerged+'ELE.csv')
os.system('sed 1d '+localFilesPath+'*GOL.csv > '+localFilesPathMerged+'GOL.csv')
os.system('sed 1d '+localFilesPath+'*MEC.csv > '+localFilesPathMerged+'MEC.csv')
os.system('sed 1d '+localFilesPath+'*GPA.csv > '+localFilesPathMerged+'GPA.csv')
os.system('sed 1d '+localFilesPath+'*SEG.csv > '+localFilesPathMerged+'SEG.csv')

header = ['sigle', 'name', 'session1','session2','session3','session4','session5']
## filter cs files by removing unwanted charters and lines
for filename in os.listdir(localFilesPathMerged):
    if filename.endswith(".csv"):
        with open(localFilesPathMerged+filename, 'r') as f:
            data = list(csv.reader(f))
        ##filter sigle 
        import collections
        counter = collections.defaultdict(int)
        for row in data:
            row[0] = row[0][-6:]
            
        ## filtre uneeded lines and characters
        writer = csv.writer(open(localFilesPathMerged+filename, 'w'))
        writer.writerow(header)  
        for rowWrite in data:
            if (rowWrite[0] != 'COURS' and rowWrite[0][0] != 'T' and rowWrite[0][0] != 'S' and rowWrite[0][0] != 'J'  
                and len(rowWrite) == 7 and  rowWrite[1] != '' ):
                writer.writerow(rowWrite)           

#Convert csv data into json 
def to_json(data, json_file, format):
    with open(json_file, "w") as f:
            f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),ensure_ascii=False))
            
##convert csv files to json objects
for filename in os.listdir(localFilesPathMerged):
    if filename.endswith(".csv"):
        csv_rows = []
        with open(localFilesPathMerged+filename) as csvfile:
            reader = csv.DictReader(csvfile)
            title = reader.fieldnames
            for row in reader:
                csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
            to_json(csv_rows, os.getcwd()+'/json_files/'+filename[:-4]+'.json', format)


