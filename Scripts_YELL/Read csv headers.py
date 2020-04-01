import os, glob, re, sys, csv

inDir = r"T:\Restoration\Stream & Wetland Restoration\SCI_Riparian\Prisoners' Wetland\Well Data\Final Output"

csvFiles = glob.glob(inDir + os.sep + "*.csv")

for file in csvFiles:
	# print("{} Reading headers for {}".format("-"*10, file))

	f = open(file, 'r')
	reader = csv.reader(f)
	headers = next(reader, None)
	h_cat = []
	for h in headers:
		h_strip = h.strip()
		# print(h_strip)
		h_cat.append(h_strip)
	print(", ".join(h_cat))

	# print(headers)