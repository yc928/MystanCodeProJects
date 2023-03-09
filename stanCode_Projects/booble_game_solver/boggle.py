"""
File: boggle.py
Name: Ian
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	User will input 16 alphabet.
	This program will use these 16 alphabet to find the words that exactly in dictionary.
	"""
	dict_lst = read_dictionary()
	boggle_lst = []
	result_word = []
	for i in range(4):
		data = input(str(i+1) + ' row of letters: ').lower().split(' ')
		for ch in data:
			if len(ch) > 1:
				print('Illegal input')
				return
			elif not ch.isalpha():
				data.remove(ch)
		boggle_lst.append(data)
	print(boggle_lst)

	start = time.time()
	# Run all 16 chars
	for x in range(4):
		for y in range(4):
			find_words(boggle_lst, dict_lst, [], [x, y], result_word)
	print(f'There are {len(result_word)} words in total.')
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_words(boggle_lst, dict_lst, cur_ans, cur_coord, result_word):
	"""
	:boggle_lst: (list), user input 4 row char.
	:dict_lst: (list), from read_dictionary().
	:cur_ans: (list), current search step / coordinate.
	:cur_coord: (list), current coordinate.
	:result_word: (list), answer words.
	:return: no return
	"""
	# Search 8 coordinate
	search_step = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
	cur_word = char_combine(boggle_lst, cur_ans)
	if has_prefix(cur_word, dict_lst):
		if len(cur_ans) >= 4:
			if cur_word not in result_word and cur_word in dict_lst:
				print('Found ' + cur_word)
				result_word.append(cur_word)
				# Do it one more time
				for step in search_step:
					x = step[0] + cur_coord[0]
					y = step[1] + cur_coord[1]
					if (x, y) not in cur_ans and -1 < x < 4 and -1 < y < 4:
						# Choose
						cur_ans.append((x, y))
						# Explore
						find_words(boggle_lst, dict_lst, cur_ans, [x, y], result_word)
						# Un-choose
						cur_ans.pop()
		else:
			for step in search_step:
				x = step[0] + cur_coord[0]
				y = step[1] + cur_coord[1]
				# Can't out of range of boggle_lst and duplicate (x, y) coordinate.
				if (x, y) not in cur_ans and -1 < x < 4 and -1 < y < 4:
					# Choose
					cur_ans.append((x, y))
					# Explore
					find_words(boggle_lst, dict_lst, cur_ans, [x, y], result_word)
					# Un-choose
					cur_ans.pop()


def char_combine(boggle_lst, cur_ans):
	"""
	:param boggle_lst: (list), user input 4 row char.
	:param cur_ans: (list), current search step / coordinate.
	:return: (str), current word.
	"""
	chars = [boggle_lst[x][y] for x, y in cur_ans]
	cur_word = ''.join(chars)
	return cur_word


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dict_list = []
	with open(FILE, 'r') as f:
		for line in f:
			dict_list.append(line.strip())
	return dict_list


def has_prefix(sub_s, dict_lst):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dict_lst: (list), from read_dictionary().
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for words in dict_lst:
		if words.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
