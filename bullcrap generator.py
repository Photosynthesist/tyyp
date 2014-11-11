import random

'''
These are word banks.
However, with passages, I wanted to get unique sentence frames each time.
To do this, I had to state the amount of passages and use an if statement
in the getSentence function.
'''

#0 = imperative, 1 = present, 2 = continuous, 3 = perfect
verbs = [["jump","jumps","jumping","jumped"],
		["kick","kicks","kicking","kicked"],
		["seek","seeks","seeking","sought"],
		["close","closes","closing","closed"],
		["slap","slaps","slapping","slapped"],
		["fly","flies","flying","flew"]]

#0 = singular, 1 = plural
nouns = [["dog","dogs"],
         ["sword","swords"],
         ["beard","beards"],
         ["man","men"],
		 ["boat","boats"],
		 ["fish","fish"],
		 ["dragon","dragons"]]

adjectives = ["old","silly","rusty","dissheveled","confused",
              "disoriented","intelligent","slimy","discoloured",
			  "tired","paranoid"]

adverbs = ["lovingly","carefully","cautiously","distractedly","unwittingly",
			"lazily","quickly","tiredly"]

passages = 3 #Set to number of passages in the getSentence function.


'''
These get functions will return a random word.

In the case of verbs, a tense argument is required to give tense.
For a random tense, just use getVerb(random.randrange(3))
0 is imperative or base word, 1 is present for singular noun,
2 is continuous, and 3 is past perfect.

For nouns, an argument of number is needed.
0 for singular, 1 for plural. For a random number, just use
getNoun(random.randrange(1))
'''

def getVerb(tense):
        return(verbs[random.randrange(len(verbs))][tense])	

def getNoun(number):
        return(nouns[random.randrange(len(nouns))][number])

def getAdjective():
        return(adjectives[random.randrange(len(adjectives))])

def getAdverb():
        return(adverbs[random.randrange(len(adverbs))])

def getSentence():
	picker = random.randrange(passages)
	if picker == 0:
		out = ("The " + getNoun(random.randrange(1)) + " " + getAdverb() + " " + getVerb(3) + " the " + getNoun(random.randrange(1)) + ".")
	if picker == 1:
		out = ("The " + getAdjective() + " " + getNoun(1) + " were " + getVerb(3) + " by the " + getAdjective() + " " + getNoun(random.randrange(1)) + ".")
	if picker == 2:
		out = ("Why, oh why, does the " + getAdjective() + " " + getNoun(0) + " " + getVerb(0) + "?")
	return(out)

#print("The",getNoun(random.randrange(1)),getAdverb(),getVerb(3),"the",getNoun(random.randrange(1)) + ".")

print(getSentence())
print()
input("Press enter to close.")