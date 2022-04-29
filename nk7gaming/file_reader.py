def proper_capitalization(sentence):
    """return string in lower case"""
    lower_case = sentence.lower()
    return lower_case


def tokenization(sentence):
    """return words in sentence as a string"""
    result = []
    for words in sentence.split():
        result.append(words)
    return result


def stop_word_removal(sentence, stop_words):
    """Remove all words in sentence"""
    stop_words = stop_words.split()
    result = ""
    for word in sentence.split():
        if word not in stop_words:
            result += word + " "
        else:
            continue
    return result


def remove_punc(sentence, punctuation):
    """remove punctuation from sentence"""
    new_words = []
    words = sentence.split()
    for word in words:
        new_word = word
        while True:
            if new_word[-1] in punctuation:
                new_word = new_word[:-1]
            else:
                break
        new_words.append(new_word)
    return " ".join(new_words)


def remove_duplicate_words(sentence):
    """remove duplicate words"""
    words = sentence.split(" ")
    words = list(set(words))
    words.sort()
    duplicate_free_string = ' '.join(words)
    return duplicate_free_string


def cleaning_noise(sentence):
    """Remove noise"""
    list1 = sentence.split()
    result = ""
    badlist = []
    list2 = []
    for word in list1:
        if word.count('http') != 0:
            badlist += word + ' '
        elif word.count('\n') != 0:
            badlist += word + ' '
        elif word.count('#') != 0:
            badlist += word + ' '
        elif word.count('&amp') != 0:
            result += '&' + ' '
        elif word.count('@') != 0:
            list2.append(word)
            if list2.index(word) % 2 != 0:
                result += word + ' '
            else:
                badlist += word + ' '
        else:
            result += word + ' '
    return result


def pos(sentence):
    """clean up sentences"""
    split = sentence.split()
    result = ""
    vowel = set('aeiouyAEIOUY')

    for word in split:
        count = 0
        count_of_ies = 0
        count_of_ves = 0
        count_of_s = 0
        count_of_esses = 0
        count_of_ied = 0
        count_of_ing = 0

        while count < 1:

            if word.endswith("'s"):
                word = word.replace("'s", "")
                continue

            if word.endswith("s'"):
                word = word.replace("s'", "")
                continue

            if word.endswith('ies'):
                if count_of_ies == 0:
                    word = word.replace("ies", "i")
                    if len(word) <= 2:
                        word = word + 'es'
                        count_of_ies += 1
                        continue
                    count_of_ies += 1
                    continue

            if word.endswith('ves'):
                if count_of_ves == 0:
                    word = word.replace("ves", "f")
                    if len(word) <= 3:
                        word = word + 'e'
                        count_of_ves += 1
                        continue
                    count_of_ves += 1
                    continue

            if word.endswith('s'):
                if count_of_s == 0:
                    if (
                            len(set(word) & vowel) == 0
                            or word.endswith('us')
                            or word.endswith('ss')
                    ):
                        count_of_s += 1
                        continue

                    sec_last_char = word[-2]
                    if sec_last_char in vowel:
                        count_of_s += 1
                        continue
                    count_of_s += 1
                    word = word.removesuffix('s')
                    continue

            if word.endswith("sses"):
                if count_of_esses == 0:
                    word = word.replace('sses', 'ss')
                    count_of_esses += 1
                    continue

            if word.endswith("ied"):
                if count_of_ied == 0:
                    word = word.replace('ied', 'i')
                    if len(word) == 1:
                        word = word + 'ed'
                    if len(word) == 2:
                        word = word + 'e'
                    count_of_ied += 1
                    continue

            if word.endswith("ed"):
                word = word.replace('ed', '')
                continue

            if word.endswith('er'):
                word = word.replace('er', '')
                continue

            if word.endswith('ing'):
                if count_of_ing == 0:
                    word = word.replace('ing', '')
                    if len(word) < 3:
                        word = word + 'ing'
                        count_of_ing += 1
                        continue
                    count_of_ing += 1
                    continue

            if word.endswith('ly'):
                word = word.replace('ly', '')
                continue

            count += 1

        result += word + ' '

    return result


def tweet_analysis():
    """Analyse tweet based on user input"""

    inputfilename = input("Enter the name of the file to read: ")
    output = input("Enter the name of the file to write: ")
    stop_words = input("Enter your stopwords: ")
    punctuation = input("Enter your punctuations to remove: ")
    lines = open(inputfilename, 'r')

    for sentence in lines:
        sentence = proper_capitalization(sentence)
        sentence = stop_word_removal(sentence, stop_words)
        sentence = remove_punc(sentence, punctuation)
        sentence = remove_duplicate_words(sentence)
        sentence = cleaning_noise(sentence)
        sentence = pos(sentence)
        with open(output, 'w') as infile:
            infile.write(sentence)
    return