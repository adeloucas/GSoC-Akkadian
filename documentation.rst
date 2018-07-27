**To be added to extant Akkadian .rst file**

Read File
=========

Reads a `.txt` file and saves to memory the text in `.raw_file` and `.file_lines`.
These two instance attributes are used for the ATFConverter.

.. code-block:: python

   In[1]: import os

   In[2]: from cltk.corpus.akkadian.file_importer import FileImport

   In[3]: text_location = os.path.join('..', 'texts', 'Akkadian.txt')

   In[4]: text = FileImport(text_location)

   In[5]: text.read_file()

To access the text file, use `.raw_file` or `.file_lines`.
`.raw_file` is the file in its entirety, `.file_lines` splits the text using `.splitlines`.

File Catalog
============

This function looks at the folder storing a file and outputs its contents.

.. code-block:: python

   In[1]: import os

   In[2]: from cltk.corpus.akkadian.file_importer import FileImport

   In[3]: text_location = os.path.join('..', 'texts', 'Akkadian.txt')

   In[4]: folder = FileImport(text_location)

   In[5]: folder.file_catalog()

   Out[5]: ['Akkadian.txt', 'ARM1texts.txt', 'cdli_corpus.txt', 'Hammurabi.txt']

Ingest Text File
================

This method captures information in a text file and formats it in a clear, and disparate, manner for every text found.
It saves to memory a list of dictionaries that splits up texts by text edition, cdli number, metadata, and text, all of which are callable.

.. code-block:: python

   In[1]: Import os

   In[2]: from cltk.corpus.akkadian.cdli_corpus import CDLICorpus

   In[3]: cdli = CDLICorpus()

   In[4]: f_i = FileImport(os.path.join('..','texts', 'single_text.txt'))

   In[5]: f_i.read_file()

   In[6]: text_file = f_i.file_lines

   In[7]: cdli.ingest_text_file(text_file)

To access the text, use `.texts`.

.. code-block:: python

   In[8]: print(cdli.texts)
   Out[8]: [{'text edition': ['ARM 01, 001'], 'cdli number': ['&P254202'], 'metadata':
   [['Primary publication: ARM 01, 001', 'Author(s): Dossin, Georges', 'Publication date: 1946',
   'Secondary publication(s): Durand, Jean-Marie, LAPO 16, 0305',
   'Collection: National Museum of Syria, Damascus, Syria', 'Museum no.: NMSD —',
   'Accession no.:', 'Provenience: Mari (mod. Tell Hariri)', 'Excavation no.:',
   'Period: Old Babylonian (ca. 1900-1600 BC)', 'Dates referenced:', 'Object type: tablet',
   'Remarks:', 'Material: clay', 'Language: Akkadian', 'Genre: Letter', 'Sub-genre:',
   'CDLI comments:', 'Catalogue source: 20050104 cdliadmin', 'ATF source: cdlistaff',
   'Translation: Durand, Jean-Marie (fr); Guerra, Dylan M. (en)',
   'UCLA Library ARK: 21198/zz001rsp8x', 'Composite no.:', 'Seal no.:', 'CDLI no.: P254202']],
   'transliteration': [['&P254202 = ARM 01, 001', '#atf: lang akk', '@tablet', '@obverse',
   '1. a-na ia-ah-du-li-[im]', '2. qi2-bi2-[ma]', '3. um-ma a-bi-sa-mar#-[ma]',
   '4. sa-li-ma-am e-pu-[usz]', '5. asz-szum mu-sze-zi-ba-am# [la i-szu]',
   '6. [sa]-li#-ma-am sza e-[pu-szu]', '7. [u2-ul] e-pu-usz sa#-[li-mu-um]',
   '8. [u2-ul] sa-[li-mu-um-ma]', '$ rest broken', '@reverse', '$ beginning broken',
   "1'. isz#-tu mu#-[sze-zi-ba-am la i-szu]", "2'. a-la-nu-ia sza la is,-s,a-ab#-[tu]",
   "3'. i-na-an-na is,-s,a-ab-[tu]", "4'. i-na ne2-kur-ti _lu2_ ha-szi-[im{ki}]",
   "5'. ur-si-im{ki} _lu2_ ka-ar-ka#-[mi-is{ki}]", "6'. u3 ia-am-ha-ad[{ki}]",
   "7'. a-la-nu an-nu-tum u2-ul ih-li-qu2#", "8'. i-na ne2-kur-ti {disz}sa-am-si-{d}iszkur#-ma",
   "9'. ih-ta-al-qu2", "10'. u3 a-la-nu sza ki-ma u2-hu-ru u2-sze-zi-ib#",
   "11'. u3 na-pa-asz2-ti u2-ba-li-it,", "12'. pi2-qa-at ha-s,e-ra#-at",
   "13'. asz-szum a-la-nu-ka", "14'. u3 ma-ru-ka sza-al#-[mu]",
   "15'. [a-na na-pa]-asz2#-ti-ia i-tu-ur"]]}]


Table of Contents
=================

Prints a table of contents from which one can identify the edition and cdli number for printing purposes.

.. code-block:: python

   In[1]: Import os

   In[2]: from cltk.corpus.akkadian.cdli_corpus import CDLICorpus

   In[3]: cdli = CDLICorpus()

   In[4]: f_i = FileImport(path)

   In[5]: f_i.read_file()

   In[6]: cdli.table_of_contents()
   Out[6]: ["edition: ['ARM 01, 001']; cdli number: ['&P254202']"]

Tokenization
======

The Akkadian tokenizer reads ATF material and converts the data into readable, mutable tokens.
There is an option whether or not to include damage in the text.

The ATFConverter depends upon the word and sign tokenizer outputs.

**String Tokenization:**

This function is based off CLTK's line tokenizer. Use this for strings (e.g. copy-and-paste lines from a document) rather than .txt files.

.. code-block:: python

   In[1]: from cltk.tokenize.line import  Akkadian_LineTokenizer

   In[2]: line_tokenizer = Akkadian_LineTokenizer('akkadian', preserve_damage=False)

   In[3]: text = '20. u2-sza-bi-la-kum\n1. a-na ia-as2-ma-ah-{d}iszkur#\n' \
               '2. qi2-bi2-ma\n3. um-ma {d}utu-szi-{d}iszkur\n' \
               '4. a-bu-ka-a-ma\n5. t,up-pa-[ka] sza#-[tu]-sza-bi-lam esz-me' \
               '\n' '6. asz-szum t,e4#-em# {d}utu-illat-su2\n'\
               '7. u3 ia#-szu-ub-dingir sza a-na la i-[zu]-zi-im\n'

   In[4]: line_tokenizer.string_token(text)
   Out[4]: ['20. u2-sza-bi-la-kum',
            '1. a-na ia-as2-ma-ah-{d}iszkur',
            '2. qi2-bi2-ma',
            '3. um-ma {d}utu-szi-{d}iszkur',
            '4. a-bu-ka-a-ma',
            '5. t,up-pa-ka sza-tu-sza-bi-lam esz-me',
            '6. asz-szum t,e4-em {d}utu-illat-su2',
            '7. u3 ia-szu-ub-dingir sza a-na la i-zu-zi-im']

**Line Tokenization:**

Line Tokenization is for any text, from `FileImport.raw_text` to `.CDLICorpus.texts`.

.. code-block:: python

   In[1]: import os

   In[2]: from cltk.tokenize.line import  Akkadian_LineTokenizer

   In[3]: line_tokenizer = Akkadian_LineTokenizer('akkadian', preserve_damage=False)

   In[4]: text = os.path.join('..', 'texts', 'Hammurabi.txt')

   In[5]: line_tokenizer.line_token(text[3042:3054])
   Out[5]: ['20. u2-sza-bi-la-kum',
            '1. a-na ia-as2-ma-ah-{d}iszkur',
            '2. qi2-bi2-ma',
            '3. um-ma {d}utu-szi-{d}iszkur',
            '4. a-bu-ka-a-ma',
            '5. t,up-pa-ka sza-tu-sza-bi-lam esz-me',
            '6. asz-szum t,e4-em {d}utu-illat-su2',
            '7. u3 ia-szu-ub-dingir sza a-na la i-zu-zi-im']

**Word Tokenization:**

Word tokenization operates on a single line of text, returns all words in the line as a tuple in a list.

.. code-block:: python

   In[1]: import os

   In[2]: from cltk.tokenize.word import  WordTokenizer

   In[3]: word_tokenizer = WordTokenizer('akkadian')

   In[4]: line = '21. u2-wa-a-ru at-ta e2-kal2-la-ka _e2_-ka wu-e-er'

   In[5]: output = word_tokenizer.tokenize(line)
   Out[5]: [('u2-wa-a-ru', 'akkadian'), ('at-ta', 'akkadian'),
            ('e2-kal2-la-ka', 'akkadian'), ('_e2_-ka', 'sumerian'),
            ('wu-e-er', 'akkadian')]

**Sign Tokenization:**

Sign Tokenization takes a tuple (word, language) and splits the word up into individual sign tuples (sign, language) in a list.

.. code-block:: python

   In[1]: import os

   In[2]: from cltk.tokenize.word import  WordTokenizer

   In[3]: word_tokenizer = WordTokenizer('akkadian')

   In[4]: word = ("{gisz}isz-pur-ram", "akkadian")

   In[5]: word_tokenizer.tokenize_sign(word)
   Out[5]: [("gisz", "determinative"), ("isz", "akkadian"),
            ("pur", "akkadian"), ("ram", "akkadian")]

Unicode Conversion
=================

From a list of tokens, this module will return the list converted from CDLI standards to print publication standards.
`two_three` is a function allows the user to turn on and off accent marking for signs (`a₂` versus `á`).

.. code-block:: python

   In[1]: from cltk.corpus.akkadian.atf_converter import ATFConverter

   In[2]: atf = ATFConverter(two_three=False)

   In[2]: test = ['as,', 'S,ATU', 'tet,', 'T,et', 'sza', 'ASZ', "a", "a2", "a3", "be2", "bad3", "buru14"]

   In[4]: atf.process(test)

   Out[4]: ['aṣ', 'ṢATU', 'teṭ', 'Ṭet', 'ša', 'AŠ', "a", "á", "à", "bé", "bàd", "buru₁₄"]


Pretty Printing
==================

Pretty Print allows an individual to take a `.txt` file and populate it into an html file.

.. code-block:: python

   In[1]: import os

   In[2]: from cltk.corpus.akkadian.pretty_print import  PrettyPrint

   In[3]: from cltk.

   In[3]: origin = os.path.join('..', 'text', 'Akkadian.txt')

   In[4]: destination = os.path.join('..', 'PrettyPrint', 'html_file.html')

   In[5]: f_i = FileImport(path)
        f_i.read_file()
        origin = f_i.raw_file
        p_p = PrettyPrint()
        p_p.html_print(origin, destination)
        f_o = FileImport(destination)
        f_o.read_file()
        output = f_o.raw_file