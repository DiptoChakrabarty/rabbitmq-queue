import math

stop_words = ["ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out", "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him", "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were", "her", "more", "himself", "this", "down", "should", "our", "their",
              "while", "above", "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them", "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", "that", "because", "what", "over", "why", "so", "can", "did", "not", "now", "under", "he", "you", "herself", "has", "just", "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t", "being", "if", "theirs", "my", "against", "a", "by", "doing", "it", "how", "further", "was", "here", "than"]


def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count/float(bowCount)
    return tfDict


def computeIDF(docList):

    idfDict = {}
    N = len(docList)

    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1

    for word, val in idfDict.items():
        idfDict[word] = math.log10(N / float(val))

    return idfDict


def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val*idfs[word]
    return tfidf


def top_words(dictionary):
    i = 0
    for k, v in sorted(dictionary.items(), key=lambda k: k[1], reverse=True):
        if(i < 10):
            print(k, v)
        i = i+1



def compute(filename):

    doc = open(filename,encoding='UTF-8').read()
    bowA = [word for word in docA.split() if word not in stop_words]
    wordSet = set(bowA).union(set(bowB)).union(set(bowC))

    wordDictA = dict.fromkeys(wordSet, 0)
    for word in bowA:
        wordDictA[word] += 1

    tfBowA = computeTF(wordDictA, bowA)
    idfs = computeIDF([wordDictA, wordDictB, wordDictC])
    tfidfBowA = computeTFIDF(tfBowA, idfs)
    print("\nTop words in Document A are")
    top_words(tfidfBowA)

