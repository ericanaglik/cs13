# get all words from the computers dictionary 
def get_file_lines(filename='/usr/share/dict/words'):
    with open(filename) as file:
        lines = [line.strip() for line in file]
    new_set = set(lines)
    return lines

# getting all the possible permutations of the current word
def all_perms(word):
if len(word) <=1:
    return word
else:
    final_words = []
    for perm in all_perms(word[1:]):
        for i in range(len(word)):
            curr_perm = perm[:i] + word[0:1] + perm[i:]
            if curr_perm not in final_words:
                final_words.append(curr_perm)

    return final_words

# try to find the word 
def word_search(words, dictionary):
    word_found = []
    for word in words:
        if word in dictionary:
            word_found.append(word)

    return word_found


def solve_word_jumble(word_perms):
    final_words = []
    word_set = get_file_lines()
    for word in word_perms:
        all_perms = all_perms(word)
        word_found = word_search(all_perms, word_set)
        final_words.append(word_found)

    print('hello')
    return final_words

def main():
    words1 = ['TEFON', 'SOKIK', 'NIUMEM', 'SICONU']
    print(solve_word_jumble(words1))