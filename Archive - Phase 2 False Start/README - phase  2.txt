Normalizer

# Goals for creating lookup lemmatizer # 
(basically a huge datafile of declined and conjugated forms)

1) Start with a set corpus of nouns like Huehnergard
    See how well decliner performs and catch irregulars and odd forms

2) Use those to fix the decliner until it's producing a stable collection of all noun forms
    Use that as a lookup table for any form

3) Have a simple function where given any noun form would return its lemma
    This same process should be repeated pretty easily for verbs; 
    the radical converter is already setup (i.e. iprus -> iR₁R₂uR₃)
