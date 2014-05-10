#!/usr/bin/env python
import os
import sys
import Imdb2XML

if len(sys.argv) < 3:
    print "Usage"
    print '  %s "Target Dir" "File Types" "Keywords"' % sys.argv[0]
    sys.exit(2)

FileTypes = {}

strSourceDir = unicode(sys.argv[1],"UTF-8")

strFileTypes = sys.argv[2]
strKeywords =  None
if len(sys.argv) > 3:
	strKeywords = sys.argv[3]

aFileTypes =strFileTypes.split(',')
for i in range(len(aFileTypes)): 
	aFileTypes[i] = "." + aFileTypes[i].lower()

for root, subFolders, files in os.walk(strSourceDir):
	# Loop files 
	#print root, subFolders
	for file in files:
			fullfile = os.path.join(root,file)
			Mediafile, fileExtension = os.path.splitext(fullfile)
			if fileExtension.lower() in aFileTypes : 
				print "File %s , %s " % (fileExtension,Mediafile.encode('ascii','replace'))
				if strKeywords is not None:
					Imdb2XML.Imdb2XML(fullfile, strKeywords)
				else : 
					Imdb2XML.Imdb2XML(fullfile)

	