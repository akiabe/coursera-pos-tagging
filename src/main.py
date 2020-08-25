import baseline
import config
import dataset

if __name__ == "__main__":
    # load train corpus
    with open(config.TRAINING_CORPUS, 'r') as f:
        training_corpus = f.readlines()

    # load vocab data
    with open(config.VOCABULARY_DATA, 'r') as f:
        voc_l = f.read().split('\n')

    # create empty vocab dictionary
    vocab = {}

    # get the idx of the corresponding words
    for i, word in enumerate(sorted(voc_l)):
        vocab[word] = i

    # load test corpus
    with open(config.TEST_CORPUS, 'r') as f:
        y = f.readlines()

    # corpus w/o tags, preprocessed
    _, prep = dataset.preprocess(vocab, config.TEST_TAG)

    # get the transition_counts, emission_counts, tag_counts dictionary
    emission_counts, transition_counts, tag_counts = baseline.create_dictionaries(training_corpus, vocab)

    # get all the pos states
    states = sorted(tag_counts.keys())
    print(states)

    print(list(emission_counts.items())[:3])
    print()
    print(list(transition_counts.items())[:3])


