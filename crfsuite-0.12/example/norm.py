#!/usr/bin/env python

"""
A feature extractor for normalization.
Copyright 2010,2011 Naoaki Okazaki.
"""

# Separator of field values.
separator = '\t'

# Field names of the input data.
fields = 'w pos length prefix suffix repcon alpha y'


# Attribute templates.
templates = (
    (('w', -1), ),
    (('w',  0), ),
    (('w',  1), ),
    (('pos', -1), ),
    (('pos',  0), ),
    (('pos',  1), ),
    (('length',  0), ),
    (('prefix',  0), ),
    (('suffix',  0), ),
    (('repcon',  0), ),
    (('alpha',  0), ),
    )


import crfutils

def feature_extractor(X):
    # Apply attribute templates to obtain features (in fact, attributes)
    crfutils.apply_templates(X, templates)
    if X:
    # Append BOS and EOS features manually
        X[0]['F'].append('__BOS__')     # BOS feature
        X[-1]['F'].append('__EOS__')    # EOS feature

if __name__ == '__main__':
    crfutils.main(feature_extractor, fields=fields, sep=separator)
