#!/usr/bin/env python

import imdb
import sys
import os
import string


# Main function
def Imdb2XML(strMode,strDocPathFilename, strRemovedStrings=None):

	if strRemovedStrings is not None:
		aRemovedStrings = strRemovedStrings.split(",")
	else:
		aRemovedStrings = None

	if strMode == "File":
		strXmlPathFilename = strDocPathFilename + ".xml"
	else:
		if strMode == "ADS":
			strXmlPathFilename = strDocPathFilename + ":MetaDirectory.xml"
		else:
			print "Wrong operation mode : %s" % strMode.encode(sys.stdout.encoding, 'replace')
			return(0)
		
	if os.path.isfile(strXmlPathFilename):
		print "XML File exists"
		return(0)

	__, strDocFilename = os.path.split(strDocPathFilename)
	strMovieTitle, __ = os.path.splitext(strDocFilename)

	# Remove strings
	if aRemovedStrings is not None:
		for strRemovedString in aRemovedStrings:
			strMovieTitle = strMovieTitle.replace(strRemovedString, ' ')

	def translate_non_alphanumerics(to_translate, translate_to=u'.'):
		not_letters_or_digits = u'*?"<>|:!@#$.()-'
		if isinstance(to_translate, unicode):
			translate_table = dict(
				(ord(char), unicode(translate_to))
				for char in not_letters_or_digits)
		else:
			assert isinstance(to_translate, str)
			translate_table = string.maketrans(
				not_letters_or_digits,
				translate_to * len(not_letters_or_digits))
		return to_translate.translate(translate_table)

	# Remove some non alphanumerics
	strMovieTitle = translate_non_alphanumerics(strMovieTitle, u' ')

	print "Searching title : %s" % strMovieTitle.encode(sys.stdout.encoding, 'replace')
	# Create the object that will be used to access the IMDb's database.
	ia = imdb.IMDb()

	while True:
		strNewMovieTitle = raw_input('Search Title[%s]:' % strMovieTitle.encode(sys.stdout.encoding, 'replace'))
		strMovieTitle = strNewMovieTitle or strMovieTitle

		# Search for a movie (get a list of Movie objects).
		xmlMovieResults = ia.search_movie(strMovieTitle)

		# Print the long imdb canonical title and movieID of the results.
		print 'Movies list'
		print '------------------------------------'

		print 'Index\t| Year\t| Kind \t| Title'
		for ix in range(len(xmlMovieResults)):
			xmlMovie = xmlMovieResults[ix]
			print ix, "\t|", xmlMovie.get('year', ''), "\t|", xmlMovie.get('kind', ''), "\t|", xmlMovie['title'].encode(sys.stdout.encoding, 'replace')
		print '------------------------------------'

		iSelectedMovie = -1

		while iSelectedMovie == -1:
			print "Select movie"
			print "0-99 = Selected movie"
			print "s Search again with new search string"
			print "e Create empty xml file"
			print "x Exit"
			strSelectedMovie = raw_input()
			if strSelectedMovie == "x":
				return(0)
			if strSelectedMovie == "e":
				f = open(strXmlPathFilename, 'a')
				f.write('<?xml version="1.0"?>')
				f.write('<!DOCTYPE movie SYSTEM "http://imdbpy.sf.net/dtd/imdbpy50.dtd">')
				f.write('<data></data>')
				f.close()
				return(0)
			if strSelectedMovie == "s":
				iSelectedMovie = -2
			else:
				try:
					iSelectedMovie = int(strSelectedMovie)
				except ValueError:
					print "Not a number, select again"
				if iSelectedMovie > len(xmlMovieResults) - 1:
					print "No such movie"
					iSelectedMovie = -1

		if iSelectedMovie != -2:
			break

	# Retrieves information for the result (a Movie object).
	xmlSelectedMovie = xmlMovieResults[iSelectedMovie]
	ia.update(xmlSelectedMovie)

	# Write XML file
	f = open(strXmlPathFilename, 'w')
	f.write(xmlSelectedMovie.asXML())
	f.close

# Call main
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "Only two arguments are required, third is optional:"
		print '  %s "File|ADS" "movie title" "remove strings"' % sys.argv[0]
		sys.exit(2)

	if len(sys.argv) > 3:
		Imdb2XML(sys.argv[1], sys.argv[2], sys.argv[3])
	else:
		Imdb2XML(sys.argv[1], sys.argv[2])
