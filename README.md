# GSoC-Akkadian

This project is being made for Google's 2018 Summer of Code on behalf of CLTK.

The author is Andrew Deloucas <adeloucas@g.harvard.com>

## Table of Contents

The following items are in this repository:

1) ARM1-Akkadian.txt
2) ARM-Transliteration.txt
3) ATF Converter - Summer Start.ipynb
4) Akkadian.txt
5) LICENCE
6) README.md
7) Transliteration.txt

###### Detailed Table of Contents 

1) ARM1-Akkadian.txt
       A text file that contains the ATF information of the publication ARM 01. Information can be found in the file.

2) ARM1-Transliteration.txt
       A text file that contains the ATF info for publication ARM 01.001. Information can be found in the file.

3) ATF Converter - Summer Start.ipynb
       A python file that shows the state of this code as of 4/23/18.

4) Akkadian.txt
       A text file that contains the ATF information of the publication Codex Hammurabi. Information can be found in the file.

5) and 6) Supplied by Github. 
       README.md will be actively edited by Andrew Deloucas during the duration of GSoc 2018.

7) Transliteration.txt 
       A text file that contains the ATF info for Codex Hammurabi including translation. Information can be found in the file.

## Updates

I will be updating weekly the development of this project, labeled such (n being the next number in the folder series, x being the number of the weeks' end within the project) until final submission, dated week of August 6th:
       n) z - ATF Converter EOW x.ipynb
       n+1) z - ATF Converter EOW x+1.ipynb
       etc.

This code will follow the proposal developed by the author, seen here and reproduced below: <https://summerofcode.withgoogle.com/projects/#5184805973524480>

# The Road to CDLI’s Corpora Integration into CLTK: an Undertaking

## Abstract
This project focuses on integrating Cuneiform Digital Library Initiative (CDLI) corpora into the Classical Language Toolkit (CLTK). Currently, CLTK houses several functions developed by Dr. Willis Monroe; the difficulty in utilizing these functions is due to the variables having to be presented in a reconstructed normalized form of Akkadian, which is not how tablets are either written traditionally or stored by CDLI. The goal of this project is to enable CLTK to reconstruct a normalized spelling out of CDLI’s ATF text and thus create data available for two fundamental uses: 1) allowance of individuals to learn and practice Akkadian with real and novel reading exercises; and 2) with further class development, be analyzed on a mass scale.

## The Problem
At its core, this project highlights the discrepancy between current CTLK functions and their (in)ability to utilize the world’s largest archive of Akkadian data: CDLI. CDLI uses ATF (ASCII Transliteration Format), which is currently unreadable by CLTK.
The Landscape = "There are several issues that thus must be confronted before CLTK’s Akkadian corpus can be fleshed out: 1) CLTK must be able to read a variety of cuneiform writing styles in ATF by means of an ASCIIUnicode converter, 2) for writing that does not provide full inflection, CLTK must know how to read writing conventions via declination and lemmatization, and 3) the exposition must become recognizable for additional classes to work. Thus, this project is established in three parts: 1) ASCII-Unicode conversion, 2) Normalization, and 3) Implementation, or case study.

###### ASCII-Unicode conversion 
The development of an ASCII-Unicode converter shall be first established for functions in which CLTK is familiar: the goal of this converter is to establish a way to encode unrecognizable data into Unicode. This process will take the established methods of typography for CDLI in ASCII and replace the characters with Unicode. This will allow current and proposed functions to be used. The end result of this converter will additionally provide a ‘sign transliteration’.

###### Normalization 
Because ATF-inflected data is uncommon to find, part 2 of this project involves creating a class that, in processing typical ATF data, references and abides by grammatical rules via lemmatization, declension, stress, and morphology: that is to say, normalization. By utilizing Huehnergard’s grammar, we will be able to create a class that follows set orthographic rules. Dr. Willis Monroe has already developed a decliner class, which establishes how Akkadian nouns, based upon their gender, are declined by case and number, as well as a tool to recognize radicals in a verb. Beginning with a set corpus of nouns, I will perform declinations of (ir)regular nouns and their forms in order to catch any inconsistencies; when corrections are made, its output will create a “lookup table” that will aid the process of creating a function where any noun form would return their lemma. This process will be repeated, albeit with verbs. From such functions, a final table will take form as a “lemmatizer.” Upon finalizing the lemmatizer, the goal is to finalize the class such that, upon exposition of the converter above, CLTK can normalize the provided ATF corpus and be able to operate any additional functions.

###### Implementation  
The case study of this project is composed of two exercises: 1) a long-form analysis of a singular text and 2) a sample of a larger corpus. This section of the project should be able to utilize parts 1 and 2 in order to become fully capable of being analyzed like any other NLP.

## The Dataset  
Due to the scope of this project, this proposal will focus on the Old Babylonian dialect of Akkadian, which has rules well established in Dr. John Huehnergard’s “A Grammar of Akkadian.” The texts being used will be the Code of Hammurapi and Georges Dossin’s
'Archives Royale de Mari 1' (ARM 01).

# Timeline 
I will be dedicating 20 hours per week to this project, totaling 420 hours over the next four months. Below is a table breaking down work and goals, hours dedicated, and their relation to the Google Summer of Code schedule. Evaluations established by GSoC will be completed outside of the allotted time mentioned.

## GSoC Timeline Weeks Endeavors
###### Application Review Period, 27.3 – 23.4, COMPLETED
(4 weeks)
• Learn string manipulation
• Learn Dictionary / List Comprehension
• Familiarize myself with collections library functions
• Total hours = 80 hours

###### Community Bonding, 23.4 – 14.5, IN PROGRESS
(3 weeks)
• Develop and Complete Part 1, Converter
• Total hours = 60 hours

###### Coding, 14.5 – 6.8, IN PROGRESS
(12 weeks)
• Develop and Complete Parts 2 and 3, Normalization and Implementation
• Total hours = 240 hours

###### Code Submissions and Final Evaluations, 6.8 – 18.8, IN PROGRESS
(2 weeks)
• Complete Evaluations and Write Article
Set for Publication
• Total hours = 40 hours
