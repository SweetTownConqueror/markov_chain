import numpy as np

def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])
    yield (corpus[len(corpus)-1], '')
        
def create_dict(pairs):
	word_dict = {}
	for word_1, word_2 in pairs:
	    if word_1 in word_dict.keys():
	        word_dict[word_1].append(word_2)
	    else:
	        word_dict[word_1] = [word_2]
	return word_dict

def show_words(dict_proposals):
	n_words = 10
	chain = []
	for i in range(len(dict_proposals)):
		if i < n_words:
			chain.append(dict_proposals[i])
	print('\033[93m'+' '.join(chain)+'\033[0m')
#generate_phrase()
messages = ""
msg_input = ""
while msg_input != "quit_pg":
	msg_input = input("Enter messages and hit enter when you want to have a prediction on the last word typed (quit_pg, clear_message)\r\n>>") 
	if msg_input == "clear_message":
		messages = ""
		msg_input = ""
	messages = messages+" "+msg_input
	with open("dict.txt", "a") as myfile:
		myfile.write(msg_input+"\r\n")
	mssgs = open('dict.txt', encoding='utf8').read()
	corpus = mssgs.split()
	pairs = make_pairs(corpus)
	dictionnary = create_dict(pairs)
	if len(msg_input.split()) > 0:
		last_word = msg_input.split()[-1]
		print('\033[92m'+messages+'\033[0m')
		show_words(dictionnary[last_word])
