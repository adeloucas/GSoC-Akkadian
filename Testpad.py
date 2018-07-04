"""
This file tests methods in file_import.py.
"""

import os
from Importer.file_importer import FileImport  # pylint: disable =import-error

__author__ = ['Andrew Deloucas <ADeloucas@g.harvard.com>']
__license__ = 'MIT License. See LICENSE.'

text = os.path.join('texts', 'Akkadian.txt')
cdli = FileImport(text)
cdli.read_file()
final = cdli.file_lines[3042:3054]
goal = ['24. _{gesz}ma2_ dan-na-tam',
    '25. a-na be-el _{gesz}ma2_',
    '26. i-na-ad-di-in',
    '@law 236',
    '27. szum-ma a-wi-lum',
    '28. _{gesz}ma2_-szu',
    '29. a-na _ma2-lah5_',
    '30. a-na ig-ri-im',
    '31. id-di-in-ma',
    '32. _ma2-lah5_ i-gi-ma',
    '33. _{gesz}ma2_ ut,-t,e4-bi',
    '34. u3 lu uh2-ta-al-li-iq']
print(final == goal)

filepath, _ = os.path.split(cdli.filename)
print(os.listdir(_))
