import random

def main():
    # Get our word corpus read into a Python list
    word_file = open('/usr/share/dict/words','r')
    words = word_file.readlines()
    word_count = len(words)

    # Construct a 'sentence' of five random words from our corpus
    sentence = ""
    for x in range(0, 6):
        sentence += words[random.randint(0,word_count)].replace("\n"," ")
    print(sentence)

if __name__ == '__main__':
    main()
