from pathlib import Path


def proper_capitalization(sentence):
    """return string in lower case"""
    return sentence.lower()


def tokenization(sentence):
    """return words in sentence as a string"""
    return list(sentence.split())


def stop_word_removal(sentence, stop_words):
    """Remove all words in sentence"""
    return "".join(f"{word} " for word in sentence.split() if word not in stop_words)


def remove_punc(sentence, punctuation):
    """remove punctuation from sentence"""
    new_words = []
    words = sentence.split()
    for word in words:
        if word[-1] in punctuation and len(word) < 1:
            new_words.append(word[:-1])
        else:
            new_words.append(word)
    return " ".join(new_words)


def remove_duplicate_words(sentence):
    """remove duplicate words"""
    words = sentence.split(" ")
    words = sorted(set(words))
    return ' '.join(words)


def cleaning_noise(sentence):
    """Remove noise"""
    list1 = sentence.split()
    result = ""
    bad_list = []
    list2 = []
    for word in list1:
        if word.count('http') != 0:
            bad_list += f'{word} '
        elif word.count('\n') != 0:
            bad_list += f'{word} '
        elif word.count('#') != 0:
            bad_list += f'{word} '
        elif word.count('&amp') != 0:
            result += '&' + ' '
        elif word.count('@') != 0:
            list2.append(word)
            if list2.index(word) % 2 != 0:
                result += f'{word} '
            else:
                bad_list += f'{word} '
        else:
            result += f'{word} '
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

            if word.endswith('ies') and count_of_ies == 0:
                word = word.replace("ies", "i")
                if len(word) <= 2:
                    word = f'{word}es'
                    count_of_ies += 1
                    continue
                count_of_ies += 1
                continue

            if word.endswith('ves') and count_of_ves == 0:
                word = word.replace("ves", "f")
                if len(word) <= 3:
                    word = f'{word}e'
                    count_of_ves += 1
                    continue
                count_of_ves += 1
                continue

            if word.endswith('s') and count_of_s == 0:
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

            if word.endswith("sses") and count_of_esses == 0:
                word = word.replace('sses', 'ss')
                count_of_esses += 1
                continue

            if word.endswith("ied") and count_of_ied == 0:
                word = word.replace('ied', 'i')
                if len(word) == 1:
                    word = f'{word}ed'
                if len(word) == 2:
                    word = f'{word}e'
                count_of_ied += 1
                continue

            if word.endswith("ed"):
                word = word.replace('ed', '')
                continue

            if word.endswith('er'):
                word = word.replace('er', '')
                continue

            if word.endswith('ing') and count_of_ing == 0:
                word = word.replace('ing', '')
                if len(word) < 3:
                    word = f'{word}ing'
                    count_of_ing += 1
                    continue
                count_of_ing += 1
                continue

            if word.endswith('ly'):
                word = word.replace('ly', '')
                continue

            count += 1

        result += f'{word} '

    return result


def read_file(current_path, file_name):
    with open(f"{current_path}/{file_name}", 'r') as file:
        return list(file.readlines())


def tweet_analysis(lines, stop_words, punctuation, current_path, output):
    """Analyse tweet based on user input"""
    result_list = []
    for sentence in lines:
        sentence = proper_capitalization(sentence)
        sentence = stop_word_removal(sentence, stop_words)
        sentence = remove_punc(sentence, punctuation)
        sentence = remove_duplicate_words(sentence)
        sentence = cleaning_noise(sentence)
        sentence = pos(sentence)
        result_list.append(sentence)
        write_file(current_path, output, sentence)

    return result_list


def write_file(current_path, file_name, sentence):
    with open(f"{current_path}/{file_name}", 'a+') as file:
        file.write(sentence)


def main():
    current_path = Path().absolute()
    input_file_name = input("Enter the name of the file to read: ")
    output = input("Enter the name of the file to write: ")
    stop_words = list(map(str, input("Enter your stopwords: ").split()))
    punctuation = input("Enter your punctuations to remove: ")

    lines = read_file(current_path, input_file_name)
    return tweet_analysis(lines, stop_words, punctuation, current_path, output)


my_words = main()
print(sorted(my_words[10].split()))
