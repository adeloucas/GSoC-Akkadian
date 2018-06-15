# GSoC-Akkadian

This project is being made for Google's 2018 Summer of Code on behalf of
CLTK.

## Student and Mentors

### Student

Andrew Deloucas \
email: <adeloucas@g.harvard.com>

### Mentors

Willis Monroe \
Github: https://github.com/willismonroe \
Tyler Kirby \
Github: https://github.com/TylerKirby
       
## Table of Contents

### ATFConverter

#### atf_converter.py

This is the main converter class for this project.

#### cdli_import.py

This is the main import class for this project.

#### lemmatizer.py

This is the main lemmatization class for this project.

#### pretty_print.py

This is the printing class for this project.

#### tokenizer.py

This is the main tokenizer class for this project.

### tests

#### atf_test.py

Tests that check individual parts of the atf_converter class.

#### cdli_test.py

Tests that check individual parts of the cdli_import class.

### pretty_test.py

Tests that check individual parts of the pretty_print class.

#### token_test.py

Tests that check individual parts of the tokenizer class.

### texts

#### Akkadian.txt

A text file that contains the ATF information of the publication Codex
Hammurabi. Information can be found in the file.

#### ARM1Akkadian.txt

A text file that contains the ATF information of the publication ARM 01.
Information can be found in the file.

#### Transliteration.txt

A text file that contains the ATF info for Codex Hammurabi including
translation. Information can be found in the file.

### Project Updates EOW 7.md

I will be updating weekly the development of this project, labeled as
such until final submission week.

### LICENSE and README.md

LICENCE and README.md are both supplied by Github. README.md will be
actively edited by Andrew Deloucas during the duration of GSoC 2018.

### Testpad.py

Personal scratchpad for the project.

***
### Organizations involved

#### Classical Language Tool Kit (CLTK)

GSoC Profile:
<https://summerofcode.withgoogle.com/organizations/4928035770335232/>

##### About CLTK

We develop the Classical Language Toolkit (CLTK) because we believe it
is revolutionizing the study of the ancient world. It is doing so by
removing barriers to entry for those doing natural language processing
(NLP) in Classical languages (namely, the surviving literature of the
entirety of Eurasia and north Africa, from roughly 3000 B.C. to
A.D. 1500).

Due to how academic disciplines have evolved over the past 200 years,
our earliest civilizations are often studied in isolation from one
another. This is tragic, for today we know that the ancient world –
from Rome to Mesopotamia to India to China – consisted of deeply
interconnected networks of ideas, technologies, art, and beliefs.
As a framework for multidisciplinary research, the CLTK will help
scholars discover the commonalities of what were once thought disparate
cultures.

As software, the CLTK is a suite of NLP tools suited to the special
needs of ancient languages. We have have three goals: The most basic is
to offer low-level libraries for doing NLP in particular Classical
languages (e.g., Ancient Greek, Sanskrit). Developed with an extensible
architecture, our code is easily hacked to support new languages.
Second, the CLTK offers tools for students and scholars to do
reproducible scientific research. For instance, it has
version-controlled linguistic corpora and a suite of functions for
stylometrics. Third, it is a framework for multidisciplinary language
research. With pre-trained models (such as Word2Vec for vector space
models), we provide easy-to-use tools to capture the transmission and
evolution of knowledge, from the earliest human societies to the dawn
of the modern era.

#### CDLI

GSoC Profile:
<https://summerofcode.withgoogle.com/organizations/5332375953735680/>

##### About CDLI

The mission of the Cuneiform Digital Library Initiative (CDLI) is to
collect, preserve and make available images, text and metadata of all
artifacts inscribed with the cuneiform script. It is the sole project
with this mission and we estimate that our 334,000 catalogue entries
cover some two-thirds of all sources in collections around the world.
Our data are available publicly at <https://cdli.ucla.edu> and our
audiences comprise primarily scholars and students, but with growing
numbers of informal learners.

At the heart of cdli is a group of developers, language scientists,
machine learning engineers, and cuneiform specialists who develop
software infrastructure to process and analyze curated data. To this
effect, we are actively developing two projects: Framework Update
<https://cdli.ucla.edu/?q=news/cdli-core-update> and Machine Translation
and Automated Analysis of Cuneiform Languages
<https://cdli-gh.github.io/mtaac/.> As part of these projects we are
building a natural language processing platform to empower specialists
of ancient languages for undertaking automated annotation and
translation of Sumerian language texts thus enabling data driven study
of languages, culture, history, economy and politics of the ancient
Near Eastern civilizations. As part of this platform we are focusing
on data standardization using Linked Open Data to foster best practices
in data exchange and integration with other digital humanities and
computational philology projects.

***

#### Original Proposal

### The Road to CDLI’s Corpora Integration into CLTK: an Undertaking

GSoC Profile:
<https://summerofcode.withgoogle.com/projects/#5184805973524480>

#### Abstract

This project focuses on integrating Cuneiform Digital Library Initiative
(CDLI) corpora into the Classical Language Toolkit (CLTK). Currently,
CLTK houses several functions developed by Dr. Willis Monroe; the
difficulty in utilizing these functions is due to the variables having
to be presented in a reconstructed normalized form of Akkadian, which
is not how tablets are either written traditionally or stored by CDLI.
The goal of this project is to enable CLTK to reconstruct a normalized
spelling out of CDLI’s ATF text and thus create data available for two
fundamental uses: 1) allowance of individuals to learn and practice
Akkadian with real and novel reading exercises; and 2) with further
class development, be analyzed on a mass scale.

#### The Problem

At its core, this project highlights the discrepancy between current
CTLK functions and their (in)ability to utilize the world’s largest
archive of Akkadian data: CDLI. CDLI uses ATF (ASCII Transliteration
Format), which is currently unreadable by CLTK.

#### The Landscape "There are several issues that thus must be
confronted before CLTK’s Akkadian corpus can be fleshed out: 1) CLTK
must be able to read a variety of cuneiform writing styles in ATF by
means of an ASCIIUnicode converter, 2) for writing that does not provide
full inflection, CLTK must know how to read writing conventions via
declination and lemmatization, and 3) the exposition must become
recognizable for additional classes to work. Thus, this project is
established in three parts: \
1) ASCII-Unicode conversion,
2) Normalization, and
3) Implementation, or case study.

#### ASCII-Unicode conversion

The development of an ASCII-Unicode converter shall be first established
for functions in which CLTK is familiar: the goal of this converter is
to establish a way to encode unrecognizable data into Unicode. This
process will take the established methods of typography for CDLI in
ASCII and replace the characters with Unicode. This will allow current
and proposed functions to be used. The end result of this converter will
additionally provide a ‘sign transliteration’.

#### Normalization

Because ATF-inflected data is uncommon to find, part 2 of this project
involves creating a class that, in processing typical ATF data,
references and abides by grammatical rules via lemmatization,
declension, stress, and morphology: that is to say, normalization.
By utilizing Huehnergard’s grammar, we will be able to create a class
that follows set orthographic rules. Dr. Willis Monroe has already
developed a decliner class, which establishes how Akkadian nouns, based
upon their gender, are declined by case and number, as well as a tool to
recognize radicals in a verb. Beginning with a set corpus of nouns, I
will perform declinations of (ir)regular nouns and their forms in order
to catch any inconsistencies; when corrections are made, its output will
create a “lookup table” that will aid the process of creating a function
where any noun form would return their lemma. This process will be
repeated, albeit with verbs. From such functions, a final table will
take form as a “lemmatizer.” Upon finalizing the lemmatizer, the goal
is to finalize the class such that, upon exposition of the converter
above, CLTK can normalize the provided ATF corpus and be able to operate
any additional functions.

#### Implementation

The case study of this project is composed of two exercises: 1) a
long-form analysis of a singular text and 2) a sample of a larger
corpus. This section of the project should be able to utilize parts 1
and 2 in order to become fully capable of being analyzed like any other
NLP.

#### The Dataset

Due to the scope of this project, this proposal will focus on the Old
Babylonian dialect of Akkadian, which has rules well established in Dr.
John Huehnergard’s “A Grammar of Akkadian.” The texts being used will be
the Code of Hammurapi (henceforth Codex Hammurabi) and Georges Dossin’s
'Archives Royale de Mari 1' (ARM 01).

#### Timeline

I will be dedicating 20 hours per week to this project. Below is a table
breaking down work and goals, hours dedicated, and their relation to the
Google Summer of Code schedule. Evaluations established by GSoC will be
completed outside of the allotted time mentioned.

#### GSoC Timeline Weeks Endeavors

#### Application Review Period, 27.3 – 23.4, COMPLETED

(4 weeks) \
• Learn string manipulation \
• Learn Dictionary / List Comprehension \
• Familiarize myself with collections library functions \
• Total hours = 80 hours

#### Community Bonding, 23.4 – 14.5, COMPLETED

(3 weeks) \
• Develop and Complete Part 1, Converter \
• Total hours = 60 hours

### Coding, 14.5 – 6.8, IN PROGRESS

(12 weeks) \
• Develop and Complete Parts 2 and 3, Normalization and Implementation \
• Total hours = 240 hours

#### Code Submissions and Final Evaluations, 6.8 – 18.8, not started

(2 weeks) \
• Complete Evaluations and Write Article \
• Set for Publication \
• Total hours = 40 hours
