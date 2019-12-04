#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

# stub
# all actual work is done in main.py

import main
import sys, os, subprocess

VERBOSE = 0

if __name__ == "__main__":
	print "\n'What The Dickens'\n(Version: %s)\n\n" % main.__VERSION__
	main.check_for_files(VERBOSE)

	outfileName = main.run(VERBOSE)
	if os.path.isfile(outfileName):
		#try and open the PDF file... method varies with platform
		#only tested this on Windows, but the others should work...
		#see 'https://stackoverflow.com/questions/1679798/how-to-open-a-file-with-the-standard-application'
		if sys.platform.startswith('win'):
			os.startfile(outfileName)
		elif sys.platform.startswith('linux'):
			subprocess.call(["xdg-open", outfileName])
		else:
			subprocess.Popen(outfileName,shell=True)
