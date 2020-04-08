print("Importing modules")
import os, glob
import pandas as pd

inDir = r"C:\Temp\Yellowstone wetland\PilotWells_YELL NR wells\Final Output" 

outFile = inDir + os.sep +  "All_well_data_combined_YELL.csv"

csvFiles = glob.glob(inDir + os.sep + "*.csv")

print("Combining files...")
combined_csv = pd.concat([pd.read_csv(f, skipinitialspace=False) for f in csvFiles ])

print("Writing csv to " + outFile)
combined_csv.to_csv(outFile, index=True, encoding='utf-8-sig')

print("Done")