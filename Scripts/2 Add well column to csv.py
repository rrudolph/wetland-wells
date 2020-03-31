# Process first with the frist python script.
# This script takes all prepared csv files in the output folder from the first script
# and adds a new field called Well, scraping that data from the file name. 


import pandas as pd
import re, glob, os

os.chdir(r"T:\Restoration\Stream & Wetland Restoration\SCI_Riparian\Prisoners' Wetland\Well Data\Processed Data")

outDir = r"T:\Restoration\Stream & Wetland Restoration\SCI_Riparian\Prisoners' Wetland\Well Data\Final Output"

csv_files = glob.glob("*.csv")

def add_well_column(csv_file):

    outFile = outDir + os.sep + csv_file
    print(outFile)

    pattern = re.compile(r"PH\d+")

    wellSearch = re.search(pattern, csv_file)
    well = wellSearch.group()

    csv_input = pd.read_csv(csv_file)

    csv_input['Well'] = well
    csv_input.to_csv(outFile, index=False)

map(add_well_column, csv_files)