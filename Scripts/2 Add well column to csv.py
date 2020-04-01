# Process first with the frist python script.
# This script takes all prepared csv files in the output folder from the first script
# and adds a new field called Well, scraping that data from the file name. 


import pandas as pd
import re, glob, os

site = "CHIS" 

if site == "YELL":
	basePath = r"C:\Temp\Yellowstone wetland\PilotWells_YELL NR wells" 
	pattern = re.compile(r"(NR-)(\w{2}\d+)")

elif site == "CHIS":
	basePath = r"T:\Restoration\Stream & Wetland Restoration\SCI_Riparian\Prisoners' Wetland\Well Data" 
	pattern = re.compile(r"PH\d+") 

inPath = basePath + os.sep + "Processed Data"
outDir = basePath + os.sep + "Final Output"

csv_files = glob.glob("*.csv")

for csv_file in csv_files:
	csv_file = os.path.basename(csv_file)
	
    outFile = outDir + os.sep + csv_file
    print(outFile)

    wellSearch = re.search(pattern, csv_file)
    well = wellSearch.group()

    csv_input = pd.read_csv(csv_file)

    csv_input['Well'] = well
    csv_input.to_csv(outFile, index=False)
