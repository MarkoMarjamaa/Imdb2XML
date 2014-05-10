Imdb2XML
========

 Fetching Imdb movie metadata to XML files

http://flow-morewithless.blogspot.fi/2014/04/fetching-imdb-movie-metadata-to-xml.html


Building executable:
python pyinstaller.py -F Imdb2XML.py
Open file \PyInstaller-2.1\Imdb2XML\build\Imdb2XML\out00-Analysis.toc

and replace line (depending where your Python is ) 
 [('include\\pyconfig.h', 'C:\\Python27\\include\\pyconfig.h', 'DATA'), ('Include\\pyconfig.h', 'C:\\Python27\\Include\\pyconfig.h', 'DATA')],
with 
 [('include\\pyconfig.h', 'C:\\Python27\\include\\pyconfig.h', 'DATA')],
then run bulid again:
python pyinstaller.py -F Imdb2XML.py
