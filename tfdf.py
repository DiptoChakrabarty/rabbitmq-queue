
import numpy as np
import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer



def compute(filename):
    sentences = list()
    with open(filename) as file:
        for line in file:
            for l in re.split(r"\.\s|\?\s|\!\s|\n",line):
                if l:
                    sentences.append(l)
    cov = CountVectorizer(stop_words='english', min_df=3, max_df=0.5, ngram_range=(1,2))
    sf = cov.fit_transform(sentences)


    transform = TfidfTransformer()
    transform_weights = transform.fit_transform(sf)
    weights = np.asarray(transform_weights.mean(axis=0)).ravel().tolist()
    weights_df = pd.DataFrame({'term': cov.get_feature_names(), 'weight': weights})
    return weights_df.sort_values(by='weight', ascending=False).head(10)

