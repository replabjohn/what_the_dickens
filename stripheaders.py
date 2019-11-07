#-*- coding: utf-8 -*-

# local version of Maxwell Forbes' Gutenberg utility
# various bits of https://github.com/mbforbes/Gutenberg lumped into one file

# ORIGINAL FILE:
# gutenberg/cleanup/strip_headers.py from https://github.com/mbforbes/Gutenberg



"""Module to remove the noise from Project Gutenberg texts."""


from __future__ import absolute_import
import os

from six import u


# Gutenberg exceptions.
# originally from module gutenberg.Error

class Error(Exception):
    """Top level exception for the gutenberg library. All exceptions inherit
    from this class."""
    pass

class InvalidEtextIdException(Error):
    pass

class UnknownDownloadUriException(Error):
    pass

class UnsupportedFeatureException(Error):
    pass

class CacheAlreadyExistsException(Error):
    pass

class InvalidCacheException(Error):
    pass


# strings that mark the start and end of a Project
# Gutenberg disclaimer/header.

# originally from module 
# gutenberg._domain_model.text


TEXT_START_MARKERS = frozenset((u(_) for _ in (
    "*END*THE SMALL PRINT",
    "*** START OF THE PROJECT GUTENBERG",
    "*** START OF THIS PROJECT GUTENBERG",
    "This etext was prepared by",
    "E-text prepared by",
    "Produced by",
    "Distributed Proofreading Team",
    "Proofreading Team at http://www.pgdp.net",
    "http://gallica.bnf.fr)",
    "      http://archive.org/details/",
    "http://www.pgdp.net",
    "by The Internet Archive)",
    "by The Internet Archive/Canadian Libraries",
    "by The Internet Archive/American Libraries",
    "public domain material from the Internet Archive",
    "Internet Archive)",
    "Internet Archive/Canadian Libraries",
    "Internet Archive/American Libraries",
    "material from the Google Print project",
    "*END THE SMALL PRINT",
    "***START OF THE PROJECT GUTENBERG",
    "This etext was produced by",
    "*** START OF THE COPYRIGHTED",
    "The Project Gutenberg",
    "http://gutenberg.spiegel.de/ erreichbar.",
    "Project Runeberg publishes",
    "Beginning of this Project Gutenberg",
    "Project Gutenberg Online Distributed",
    "Gutenberg Online Distributed",
    "the Project Gutenberg Online Distributed",
    "Project Gutenberg TEI",
    "This eBook was prepared by",
    "http://gutenberg2000.de erreichbar.",
    "This Etext was prepared by",
    "This Project Gutenberg Etext was prepared by",
    "Gutenberg Distributed Proofreaders",
    "Project Gutenberg Distributed Proofreaders",
    "the Project Gutenberg Online Distributed Proofreading Team",
    "**The Project Gutenberg",
    "*SMALL PRINT!",
    "More information about this book is at the top of this file.",
    "tells you about restrictions in how the file may be used.",
    "l'authorization à les utilizer pour preparer ce texte.",
    "of the etext through OCR.",
    "*****These eBooks Were Prepared By Thousands of Volunteers!*****",
    "We need your donations more than ever!",
    " *** START OF THIS PROJECT GUTENBERG",
    "****     SMALL PRINT!",
    '["Small Print" V.',
    '      (http://www.ibiblio.org/gutenberg/',
    'and the Project Gutenberg Online Distributed Proofreading Team',
    'Mary Meehan, and the Project Gutenberg Online Distributed Proofreading',
    '                this Project Gutenberg edition.',
)))


TEXT_END_MARKERS = frozenset((u(_) for _ in (
    "*** END OF THE PROJECT GUTENBERG",
    "*** END OF THIS PROJECT GUTENBERG",
    "***END OF THE PROJECT GUTENBERG",
    "End of the Project Gutenberg",
    "End of The Project Gutenberg",
    "Ende dieses Project Gutenberg",
    "by Project Gutenberg",
    "End of Project Gutenberg",
    "End of this Project Gutenberg",
    "Ende dieses Projekt Gutenberg",
    "        ***END OF THE PROJECT GUTENBERG",
    "*** END OF THE COPYRIGHTED",
    "End of this is COPYRIGHTED",
    "Ende dieses Etextes ",
    "Ende dieses Project Gutenber",
    "Ende diese Project Gutenberg",
    "**This is a COPYRIGHTED Project Gutenberg Etext, Details Above**",
    "Fin de Project Gutenberg",
    "The Project Gutenberg Etext of ",
    "Ce document fut presente en lecture",
    "Ce document fut présenté en lecture",
    "More information about this book is at the top of this file.",
    "We need your donations more than ever!",
    "END OF PROJECT GUTENBERG",
    " End of the Project Gutenberg",
    " *** END OF THIS PROJECT GUTENBERG",
)))


LEGALESE_START_MARKERS = frozenset((u(_) for _ in (
    "<<THIS ELECTRONIC VERSION OF",
)))


LEGALESE_END_MARKERS = frozenset((u(_) for _ in (
    "SERVICE THAT CHARGES FOR DOWNLOAD",
)))



# originally from gutenberg._util.os

def reopen_encoded(fileobj, mode='r', fallback_encoding=None):
    """Makes sure that a file was opened with some valid encoding.
    Arguments:
        fileobj (file): The file-object.
        mode (str, optional): The mode in which to re-open the file.
        fallback_encoding (str, optional): The encoding in which to re-open
            the file if it does not specify an encoding itself.
    Returns:
        file: The re-opened file.
    """
    encoding = determine_encoding(fileobj.name, fallback_encoding)
    fileobj.close()
    return open(fileobj.name, mode, encoding=encoding)



def strip_headers(text):
    """Remove lines that are part of the Project Gutenberg header or footer.
    Note: this function is a port of the C++ utility by Johannes Krugel. The
    original version of the code can be found at:
    http://www14.in.tum.de/spp1307/src/strip_headers.cpp
    Args:
        text (unicode): The body of the text to clean up.
    Returns:
        unicode: The text with any non-text content removed.
    """
    lines = text.splitlines()
    #sep = str(os.linesep)
    sep = "\n"

    out = []
    i = 0
    footer_found = False
    ignore_section = False

    for line in lines:
        reset = False

        if i <= 600:
            # Check if the header ends here
            if any(line.startswith(token) for token in TEXT_START_MARKERS):
                reset = True

            # If it's the end of the header, delete the output produced so far.
            # May be done several times, if multiple lines occur indicating the
            # end of the header
            if reset:
                out = []
                continue

        if i >= 100:
            # Check if the footer begins here
            if any(line.startswith(token) for token in TEXT_END_MARKERS):
                footer_found = True

            # If it's the beginning of the footer, stop output
            if footer_found:
                break

        if any(line.startswith(token) for token in LEGALESE_START_MARKERS):
            ignore_section = True
            continue
        elif any(line.startswith(token) for token in LEGALESE_END_MARKERS):
            ignore_section = False
            continue

        if not ignore_section:
            out.append(line.rstrip(sep))
            i += 1

    return sep.join(out)


def _main():
    """Command line interface to the module.
    """
    from argparse import ArgumentParser, FileType

    parser = ArgumentParser(description='Remove headers and footers from a '
                                        'Project Gutenberg text')
    parser.add_argument('infile', type=FileType('r'))
    parser.add_argument('outfile', type=FileType('w'))
    args = parser.parse_args()

    try:
        with reopen_encoded(args.infile, 'r', 'utf8') as infile:
            text = infile.read()
            clean_text = strip_headers(text)

        with reopen_encoded(args.outfile, 'w', 'utf8') as outfile:
            outfile.write(clean_text)
    except Error as error:
        parser.error(str(error))


if __name__ == '__main__':
    _main()

