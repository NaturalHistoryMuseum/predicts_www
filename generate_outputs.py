#!/usr/bin/env python3
"""Generates html outputs from bib
"""
import re
import sys

from bib import load_bib, format_authors

from jinja2 import Environment, FileSystemLoader



def escape_latex(val):
    """Returns val with LaTeX replaced with html equivalents
    """
    # print(repr(val))
    val = re.sub(r'\\textit{([^}]+?)}', r'<em>\1</em>', val)
    val = re.sub(r'\\textbf{([^}]+?)}', r'<strong>\1</strong>', val)
    val = re.sub(r'\\href{([^}]+?)}{([^}]+?)}', r'<a href="\1">\2</a>', val)
    val = re.sub(r'\\textsuperscript{([^}]+?)}', r'<sup>\1</sup>', val)
    val = re.sub(r'\\sfrac{([^}]+?)}{([^}]+?)}', r'<sup>\1</sup>&frasl;<sup>\2</sup>', val)
    val = val.replace('\\%', '%')
    val = val.replace('``', '&ldquo;')
    val = val.replace("''", '&rdquo;')
    val = val.replace('---', '&ndash;')
    val = val.replace('--', '&mdash;')
    val = val.replace(r'\LaTeX', 'LaTeX')
    val = val.replace(r'\BibTeX', 'BibTeX')
    val = val.replace(r'\_', '_')
    # val = re.sub(r'([0-9])(st|nd|rd|th)', r'\1<sup>\2</sup>', val)
    # print(repr(val))
    return val


def main(args):
    print("""Title: Outputs

<!-- Altmetrics -->
<script type="text/javascript" src="https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js"></script>

## The PREDICTS database
The PREDICTS database - which will form
the basis of all our analyses – now has over 3.6 million biodiversity
records from over 32,000 sites, covering more than 50,000 species.

If you would like your data to play a part, please visit our
[contribution page]({filename}/pages/contribute.md) or more
information.

Locations from which PREDICTS currently has diversity measurements are
shown below. We will update this image regularly as the project
progresses.
records from over 29,000 sites, covering more than 50,000 species.

<a href="../images/sites.png" id="data_map">
<img src="../images/sites.png" itemprop="image"
     alt="Map of PREDICTS data sites" width="698" height="415"/>
</a>

Biomes in the above map are defined by The Nature Conservancy's
[terrestrial ecoregions of the world](http://maps.tnc.org/gis_data.html) dataset.
Circle radii are proportional to log<sub>10</sub> of the number of samples at
that location. Circles have the same degree of partial transparency.

We've also tried to make our data taxonomically representative,
rather than focus on the best-known clades. The graph below shows
(on log-log axes) how the numbers of a taxon's species that are in the
database relate to the numbers that are known to science. For many of
these taxa, we're above 1% representation (solid line),

<img src="../images/taxonomic_representativeness.png" itemprop="image"
   alt="Taxonomic representativeness of predicts data" width="698"
   height="433"/>
""")

    environment = Environment(loader=FileSystemLoader('templates'))
    environment.filters['escape_latex'] = escape_latex
    template = environment.get_template('outputs.html')
    SECTIONS = (
        ('Papers', 'papers.bib'),
        ('Posters and presentations', 'presentations.bib'),
        ('Datasets', 'data.bib')
    )
    for title, bib in SECTIONS:
        bibliography = load_bib(bib)
        for bib in bibliography:
            bib['authors'] = format_authors(bib['author'])
        print(template.render(**{'items': bibliography, 'title': title}))


if __name__ == '__main__':
    main(sys.argv[1:])
