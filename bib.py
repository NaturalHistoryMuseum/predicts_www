"""BiBTeX helpers
"""
import re

import bibtexparser

from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode


def load_bib(bib):
    """Returns list of BibDatabase objects
    """
    with open(bib) as bibtex_file:
        parser = BibTexParser()
        parser.customization = convert_to_unicode
        # Find the url field of a misc entry
        # https://github.com/sciunto-org/python-bibtexparser/issues/93
        parser.homogenise_fields = False
        bib = bibtexparser.load(bibtex_file, parser=parser)

    for entry in bib.entries:
        if 'author' in entry:
            # Fuck me
            entry['author'] = entry['author'].replace('{́i}', 'í')
    return bib.entries


def format_authors(authors, up_to=6):
    """Given a bibtex-formatted string of authors, returns a string of authors
    in form 'Initials Surname, ' of up to and including the first 'up_to'
    authors.
    """
    def format_author(author):
        try:
            surname, forenames = re.split(r',\s*', author)
        except ValueError:
            return author
        else:
            initials = ''.join(n[0].upper() for n in re.findall("\w+", forenames))
            return '{0} {1}'.format(initials, surname)

    authors = [format_author(author) for author in re.split(r'\s+and\s+', authors)]

    et_al = '\\textit{et al}.'

    if up_to < len(authors):
        # A, B, C, et al
        authors = authors[:up_to] + [et_al]
    else:
        # A, B, C
        authors = authors[:up_to]

    # A, B, C
    authors = ', '.join(authors)

    # End with a full stop
    if not authors.endswith('.'):
        authors = '{0}.'.format(authors)

    # Fix commas before and after 'et al.' and put key author in bold
    return authors.replace(
        ', {0},'.format(et_al), ' {0}'.format(et_al)
    ).replace(
        ', {0}'.format(et_al), ' {0}'.format(et_al)
    )
