# Takes all csv files in a folder and strips out the junk at the header of the file.
# Puts them all int a new folder named by the well name and the date of the folder.
# It's important to have the files in a YYYY_MM format so the script can pull that 
# and attach it to the file name. 

import os, glob, re, sys

site = "CHIS" 

if site == "YELL":
	basePath = r"C:\Temp\Yellowstone wetland\PilotWells_YELL NR wells" 
	pattern = re.compile(r"(NR-)(\w{2}\d+)")

elif site == "CHIS":
	basePath = r"T:\Restoration\Stream & Wetland Restoration\SCI_Riparian\Prisoners' Wetland\Well Data" 
	pattern = re.compile(r"PH\d+")


inPath = basePath + os.sep + "Site Data"
outPath = basePath + os.sep + "Processed Data"
searchFiles = (".csv") 


def walk_dir(dir_):
    """
    A directory walking generator. 
	Use: files = walk_dir(some_dir)
	Then for loop over files.
    """
    for root, dirs, files in os.walk(dir_):
        files = [ fi for fi in files if fi.endswith(searchFiles)]
        for file in files:
        	yield os.path.join(root, file)

files = walk_dir(inPath)

for file in files:
	if "BaroMerge" in file:
		print("Found valid csv file: " + file)
		wellSearch = re.search(pattern, file)

		well = wellSearch.group()
		print("Well: {}".format(well))
		# fileDate = file.split("\\")[-2]

		outFile = outPath + os.sep + well + "_" + fileDate + ".csv"

		print("Processing: " + outFile)

		# Open a csv, start writing output when it hits "Date and Time,Seconds"
		with open(file, 'r') as infile, open(outFile, 'w') as outfile:
		    # Read the file line by line...
		    for line in iter(infile.readline, ''):
		        if "Date and Time,Seconds" in line:
		            outfile.write(line)
		            outfile.write(infile.read())
		            break
