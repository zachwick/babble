import random

def main():
    noun_file = open('nouns.txt')
    nouns = noun_file.readlines()
    noun_count = len(nouns)

    verb_file = open('verbs.txt')
    verbs = verb_file.readlines()
    verb_count = len(verbs)

    adverbs_file = open('adverbs.txt')
    adverbs = adverbs_file.readlines()
    adverb_count = len(adverbs)

    adjectives_file = open('adjectives.txt')
    adjectives = adjectives_file.readlines()
    adjective_count = len(adjectives)

    # Construct a sentence of the form 'the noun adverb verb the adjective noun'
    sentence = "the\n"
    sentence += nouns[random.randint(0, noun_count)]
    sentence += adverbs[random.randint(0, adverb_count)]
    sentence += verbs[random.randint(0, verb_count)]
    sentence += "the\n"
    sentence += adjectives[random.randint(0, adjective_count)]
    sentence += nouns[random.randint(0, noun_count)]

    print(sentence)

if __name__ == '__main__':
    main()
