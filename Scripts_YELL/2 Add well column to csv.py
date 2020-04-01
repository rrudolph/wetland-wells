# Process first with the frist python script.
# This script takes all prepared csv files in the output folder from the first script
# and adds a new field called Well, scraping that data from the file name. 


import pandas as pd
import re, glob, os

os.chdir(r"C:\Temp\Yellowstone wetland\PilotWells_YELL NR wells\Processed Data")

outDir = r"C:\Temp\Yellowstone wetland\PilotWells_YELL NR wells\Final Output"

csv_files = glob.glob("*.csv")

for csv_file in csv_files:

    outFile = outDir + os.sep + csv_file
    print(outFile)

    pattern = re.compile(r"(NR-)(\w{2}\d+)")

    wellSearch = re.search(pattern, csv_file)
    well = wellSearch.group()

    csv_input = pd.read_csv(csv_file)

    csv_input['Well'] = well
    csv_input.to_csv(outFile, index=False)

