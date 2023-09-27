

words = []
common_words = []
MIN_WORD_LENGTH = 3

def get_data():
    global words, common_words
    with open('words2.txt') as f:
        words = f.read().splitlines()
    with open('common_words2.txt') as f:
        common_words = f.read().splitlines()
    words = list(filter(lambda x: len(x)>=MIN_WORD_LENGTH, words))
get_data()

def contains_letters(main_str: str, sub_str: str) -> bool:
    for char in sub_str:
        index = main_str.find(char)
        if index == -1:
            return False
        main_str = main_str[:index] + main_str[index + 1:]
    return True

def find_substrings(main_str: str) -> list[str]:
    global words
    substrings = []

    for word in words:
        if contains_letters(main_str, word):
            substrings.append(word)
    return substrings

def output_list(ls: list[str]) -> str:
    global common_words


    
    common_word_ls = []
    less_common_word_ls = ls
    for word in ls:
        if word in common_words:
            common_word_ls.append(word)
            less_common_word_ls.remove(word)


    if common_word_ls != []:
        print ('Common Words:')

        for i in range(len(common_word_ls)):
            print(f'{i + 1}. {common_word_ls[i]}')

    else:
        print ('no common words found')

    if less_common_word_ls != []:
        print ('Less Common Words:')
        for i in range(len(less_common_word_ls)):
            print(f'{i + 1}. {less_common_word_ls[i]}')

    else:
        print ('no less common words')


def main():
    while True:
        user_input = input('Input Letters: ')
        substrings = find_substrings(user_input)
        output_list(substrings)

if __name__ == '__main__':
    main()
