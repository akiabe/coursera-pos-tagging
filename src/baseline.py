import collections
import dataset

def create_dictionaries(training_corpus, vocab):
    """
    :param training_corpus: a corpus where each line has a word followed by its tag
    :param vocab: a dictionary where keys are words in vocabulary and value is an index
    :return emission_counts: a dictionary where the keys are (tag, word) and the values are the counts
    :return transition_counts: a dictionary where the keys are (prev_tag, tag) and the values are the counts
    :return tag_counts: a dictionary where the keys are the tags and the values are the counts
    """
    # initialize the dictionaries
    emission_counts = collections.defaultdict(int)
    transition_counts = collections.defaultdict(int)
    tag_counts = collections.defaultdict(int)

    # initialize prev_tag with the start state
    prev_tag = '--s--'

    # initialize the line number of corpus
    i = 0

    # each item in the train corpus contains a word and its pos tag
    # go through each word and its tag in the train corpus
    for word_tag in training_corpus:

        # increment the word_tag count
        i += 1

        # every 50,000 words, print the word count
        if i % 50000 == 0:
            print(f"word count = {i}")

        # get the word and tag
        word, tag = dataset.get_word_tag(word_tag, vocab)

        # increment the transition count for the previous word and tag
        transition_counts[(prev_tag, tag)] += 1

        # increment the emission count for the tag and word
        emission_counts[(tag, word)] += 1

        # increment the tag count
        tag_counts[tag] += 1

        # Set the previous tag to this tag (for the next iteration of the loop)
        prev_tag = tag

    return emission_counts, transition_counts, tag_counts


def predict_pos(prep, y, emission_counts, vocab, states):
    """
    :param prep: a preprocessed version of 'y'. a list with the 'word' component of the tuples
    :param y: a corpus composed of a list of tuples where each tuple consists of (word, POS)
    :param emission_counts: a dictionary where the keys are (tag, word) tuples and the value is the count
    :param vocab: a dictionary where keys are words in vocabulary and value is and index
    :param states: a sorted list of all possible tags for this assignment
    :return accuracy: number of word correctly classified times
    """
    # initialize the number of correct predictions to zero
    num_correct = 0

    all words = set(emission_counts.keys())





























