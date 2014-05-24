#!/usr/bin/env python
import os
import sys
import shutil

if len(sys.argv) < 1:
    print "Usage"
    print '  %s "Target Dir" ' % sys.argv[0]
    sys.exit(2)

strSourceDir = unicode(sys.argv[1],"UTF-8")

for root, subFolders, files in os.walk(strSourceDir):
	# Loop files 
	#print root, subFolders
	for file in files:
			fullfile = os.path.join(root,file)
			Mediafile, fileExtension = os.path.splitext(fullfile)
			if fileExtension.lower() == ".xml" : 
				if os.path.isfile(Mediafile) is True : 
					print "File %s , %s " % (fileExtension,Mediafile.encode('ascii','replace'))
					strXMLDest = Mediafile + ":MetaDirectory.xml"
					if os.path.isfile(strXMLDest) is True : 
						print "File %s already exists!" % strXMLDest
					else :
						shutil.move( fullfile,strXMLDest)
