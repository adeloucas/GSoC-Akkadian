# ATF Converter Week in Review

## Week 1 (April 23 - April 30)

1) Accepted work and began administrative paperwork for GSoC
2) Connected with mentors, larger community
3) Started up Github account
4) Established precedent (ATF Converter - Summer Start.ipynb) and broke out initial progress into tests
5) Moved out of Jupyter Notebook and into VSCode

## Week 2 (April 30 - May 7)

1) Familiarized myself with VSCode
2) Organized project per suggestion
3) Familiarized myself with PEP8 guideline
4) Got tests working

## Week 3 (May 7 - May 14)

1) Furthered tests: ~99.8% accurate (12,823 out of possible 12,850 lines) \
    a) 3 error lines in Hammurabi, \
    b) 24 error lines in ARM1
2) Continued to clean up project

## Week 4 (May 14 - May 21)

1) Recaptured testing group for Sumerian and Akkadian
2) Solve for last 27 lines - Completed week 5
3) Cleaned up Github Repository
4) Restructured ATFConverter per Tyler's suggestion
5) Began research for part 2 of project, normalization

## Week 5 (May 21 - May 28)

1) Begin setup for "lookup lemmatizer" - Scratched until after June 15 (Week 8)
2) Establish test for decliner based off nouns in Hammurabi and ARM1 - Scratched until after June 15 (Week 8)
3) Refine until noun forms are stable - Scratched until after June 15 (Week 8)
4) Reproduce for verbs - Scratched until after June 15 (Week 8)
---
5) Solved last 27 lines
6) Created Tokenizers for text 
7) Defined scope for next three weeks in meeting with Tyler and Willis: Refine Tokenizer and enable ATFConverter use.
8) Moved into PyCharm

## Goals for Week 6 (May 28 - June 4)

1) Refine Tokenizer
2) Adjust ATFConverter:
    a) get_number_from_sign = ignore numbers if not at the end of sign (e.g. 1(disz))
    b) convert_num = display numbers unassociated with signs ('1', '5' currently reads '', '₅')
    c) process = get to work on Tokenizer.word()
    d) determination = get to work on Tokenizer.determinatives()
