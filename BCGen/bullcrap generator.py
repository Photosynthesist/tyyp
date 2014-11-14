import random, os, string, re

loops = 5
'''
These are word banks.
However, with passages, I wanted to get unique sentence frames each time.
To do this, I had to state the amount of passages and use an if statement
in the getSentence function.
'''
passage_list = []
passages_file = open('passages.db')
for line in passages_file:
	passage_list.append(line)
#0 = imperative, 1 = present, 2 = continuous, 3 = perfect, 4 = perfect passive participle
verbs_file = open('verbs.db')
nouns_file = open('nouns.db')
adjectives_file = open('adjectives.db')
adverbs_file = open('adverbs.db')
#The above lines open files for wordbanks.
verbs = []
nouns = []
adjectives = []
adverbs = []
for line in verbs_file:
	temp = []
	for word in line.strip().split():
		temp.append(word)
	verbs.append(temp)
for line in nouns_file:
	temp = []
	for word in line.strip().split():
		temp.append(word)
	nouns.append(temp)
for line in adjectives_file:
	adjectives.append(line.strip())
for line in adverbs_file:
	adverbs.append(line.strip())
#These for loops will append each set of words to their appropriate lists declared above.
verbs_file.close()
nouns_file.close()
adjectives_file.close()
adverbs_file.close()
#These close the files, because they are not needed anymore.
passages = 7 #Set to number of passages in the getSentence function.

'''
These get functions will return a random word.

In the case of verbs, a tense argument is required to give tense.
For a random tense, just use getVerb(random.randrange(3))
0 is imperative or base word, 1 is present for singular noun,
2 is continuous, 3 is past perfect, and 4 is perfect passive participle.

For nouns, an argument of number is needed.
0 for singular, 1 for plural. For a random number, just use
getNoun(random.randrange(1))
'''

def getVerb(tense):
        return(random.choice(verbs)[tense])	

def getNoun(number):
        return(random.choice(nouns)[number])

def getAdjective():
        return(random.choice(adjectives))

def getAdverb():
        return(random.choice(adverbs))

def getSentence():
	out = []
	for word in random.choice(passage_list).split():
		if word[-1:] in string.punctuation:
			stripped_word = word[:-1]
			punctuation = word[-1:]
		else:
			stripped_word = word
			punctuation = ''
		if '::' in stripped_word:
			identifier = stripped_word.split('::')[0]
			number = stripped_word.split('::')[1]
			number = [int(x) for x in number.split(',')]
			number = random.choice(number)
			if identifier == 'verb':
				out.append(getVerb(number)+punctuation)
			if identifier == 'noun':
				out.append(getNoun(number)+punctuation)
		else:
			if stripped_word == 'verb':
				out.append(getVerb(random.randrange(5))+punctuation)
			elif stripped_word == 'noun':
				out.append(getVerb(random.randrange(2))+punctuation)
			elif stripped_word == 'adverb':
				out.append(getAdverb()+punctuation)
			elif stripped_word == 'adjective':
				out.append(getAdjective()+punctuation)
			else:
				out.append(word)
	return(re.sub('_',' ',' '.join(out)))

#print("The",getNoun(random.randrange(1)),getAdverb(),getVerb(3),"the",getNoun(random.randrange(1)) + ".")
while True:
	for i in range(loops):
		sentence = getSentence()
		if 'overdosing primeminister' in sentence:
			cotop = open('the_chronicles_of_the_overdosed_prime_minister.txt','a')
			cotop.write(sentence + '\n')
			cotop.close()
		print(sentence)
	print()
	print("Press any key to redraw.")
	os.system('pause>nul')
	os.system('cls')