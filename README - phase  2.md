# Normalizer

## Goals for creating lookup lemmatizer (basically a huge datafile of declined and conjugated forms)

### Start with a set corpus of nouns like Huehnergard

#### See how well decliner performs and catch irregulars and odd forms

### Use those to fix the decliner until it's producing a stable collection of all noun forms

#### Use that as a lookup table for any form

### Have a simple function where given any noun form would return its lemma

#### This same process should be repeated pretty easily for verbs; the radical converter already setup (i.e. iprus -> iR₁R₂uR₃)

### Willis' Akkadian

#### This section borrows CLTK's Akkadian tools; this material will be deleted and will link to the original files on Github upon creation of tool