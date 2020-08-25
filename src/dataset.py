import collections
import string

def create_vocab(PATH):
    # load train corpus
    with open(PATH, 'r') as f:
        lines = f.readlines()

    # get the word from each line in the dataset
    words = [line.split('\t')[0] for line in lines]

    # define defaultdict of type 'int'
    freq = collections.defaultdict(int)

    # count frequency of ocurrence for each word in the dataset
    for word in words:
        freq[word] += 1

    # create the vocabulary by filtering the 'freq' dictionary
    # filter out words that appeared only once and newline character
    vocab = [k for k, v in freq.items() if (v > 1 and k != '\n')]

    # sort the vocabulary, changes the list directly
    vocab.sort()

    return vocab


def assign_unk(word):
    """ assign tokens to unknouwn word"""
    # punctuation characters
    punct = set(string.punctuation)

    # morphology rules used to assign unknown word token
    noun_suffix = [
        "action", "age", "ance", "cy", "dom",
        "ee", "ence", "er", "hood", "ion",
        "ism", "ist", "ity", "ling", "ment",
        "ness", "or", "ry", "scape", "ship",
        "ty"
    ]

    verb_suffix = [
         "ate", "ify", "ise", "ize"
    ]

    adj_suffix = [
          "able", "ese", "ful", "i", "ian",
          "ible", "ic", "ish", "ive", "less",
          "ly", "ous"
    ]

    adv_suffix = [
           "ward", "wards", "wise"
    ]

    # loop the characters in the word, check if any is digit
    if any(char.isdigit() for char in word):
        return  "--unk_digit--"

    # loop the characters in the word, check if any is a punctuation character
    elif any(char in punct for char in word):
        return "--unk_punct--"

    # loop the characters in the word, check if any is an upper case character
    elif any(char.isupper() for char in word):
        return "--unk_upper--"

    # check if word ends with any noun suffix
    elif any(word.endswith(suffix) for suffix in noun_suffix):
        return "--unk_noun--"

    # check if word ends with any verb suffix
    elif any(word.endswith(suffix) for suffix in verb_suffix):
        return "--unk_verb--"

    # check if word ends with any adjective suffix
    elif any(word.endswith(suffix) for suffix in adj_suffix):
        return "--unk_adj--"

    # check if word ends with any adverb suffix
    elif any(word.endswith(suffix) for suffix in adv_suffix):
        return "--unk_adv--"

    # if none of the previous criteria is met, return plain unknown
    return word


def get_word_tag(line, vocab):
    # if line is empty return placeholders for word and tag
    if not line.split():
        word = "--n--"
        tag = "--"
    else:
        # split line to separate word and tag
        word, tag = line.split()

        # check if word is not in vocabulary
        if word not in vocab:
            word = assign_unk(word)

    return word, tag


def preprocess(vocab, data_fp):
    """
    Preprocess data
    """
    orig = []
    prep = []

    # Read data
    with open(data_fp, "r") as data_file:

        for cnt, word in enumerate(data_file):

            # End of sentence
            if not word.split():
                orig.append(word.strip())
                word = "--n--"
                prep.append(word)
                continue

            # Handle unknown words
            elif word.strip() not in vocab:
                orig.append(word.strip())
                word = assign_unk(word)
                prep.append(word)
                continue

            else:
                orig.append(word.strip())
                prep.append(word.strip())

    assert(len(orig) == len(open(data_fp, "r").readlines()))
    assert(len(prep) == len(open(data_fp, "r").readlines()))

    return orig, prep



