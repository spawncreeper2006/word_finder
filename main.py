
words = []
MIN_WORD_LENGTH = 3

def get_data():
    global words
    with open('words2.txt') as f:
        words = f.read().splitlines()
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

def format_str_list(ls: list[str]) -> str:

    new_ls = []
    for i in range(len(ls)):
        new_ls.append(f'{i + 1}. {ls[i]}')
    return '\n'.join(new_ls)

def main():
    while True:
        user_input = input('Input Letters: ')
        substrings = find_substrings(user_input)
        print (format_str_list(substrings))

if __name__ == '__main__':
    main()