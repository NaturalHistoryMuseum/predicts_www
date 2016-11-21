import unittest

from generate import format_authors


class TestBib(unittest.TestCase):
    def test_one(self):
        self.assertEqual(
            'LN Hudson.',
            format_authors('Hudson, Lawrence N')
        )

    def test_two(self):
        self.assertEqual(
            'LN Hudson, DC Reuman.',
            format_authors('Hudson, Lawrence Nicholas and Reuman, Dan C')
        )

    def test_three(self):
        authors = 'Newbold, Tim and Hudson, Lawrence N and Purvis, Andy'
        self.assertEqual(
            'T Newbold, LN Hudson, A Purvis.',
            format_authors(authors)
        )

    def test_six(self):
        authors = """Hudson, Lawrence N. and Newbold, Tim and Purves, Drew W. and
        Scharlemann, Jörn P. W. and Mace, Georgina and
        Purvis, Andy
        """
        expected = ('LN Hudson, T Newbold, DW Purves, JPW Scharlemann, '
                    'G Mace, A Purvis.')
        self.assertEqual(expected, format_authors(authors))

    def test_seven(self):
        authors = """Hudson, Lawrence N. and Newbold, Tim and Hill, Sam L L and
        Purves, Drew W. and Scharlemann, Jörn P. W. and Mace, Georgina and
        Purvis, Andy
        """
        expected = ('LN Hudson, T Newbold, SLL Hill, DW Purves, '
                    'JPW Scharlemann, G Mace \\textit{et al}.')
        self.assertEqual(expected, format_authors(authors))


if __name__ == '__main__':
    unittest.main()
