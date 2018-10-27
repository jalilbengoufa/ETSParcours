#!/usr/bin/env python
import camelot,os,pathlib
from PyPDF2 import PdfFileWriter, PdfFileReader
## tranform pdf to have one page and parse pdf to csv files 
for filename in os.listdir(os.getcwd()+'/pdf_files/'):
    if filename.endswith(".pdf"):
        inputpdf = PdfFileReader(open(os.getcwd()+'/pdf_files/'+filename, "rb"))

        for i in range(inputpdf.numPages):
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(i))
            with open(os.getcwd()+'/pdf_files/single_files/'+str(i)+filename, "wb") as outputStream:
                output.write(outputStream)
            tables = camelot.read_pdf(os.getcwd()+'/pdf_files/single_files/'+str(i)+filename)
            tables[0].to_csv(os.getcwd()+'/csv_files/generated/'+str(i)+filename[:-4]+'.csv')

