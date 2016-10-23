import re

NOUNS = '(NN|NNS|NNP|NNPS)'
VERBS = '(VB|VBD|VBG|VBN|VBP|VBZ)'
NN_VB = '(NN|NNS|NNP|NNPS|VB|VBD|VBG|VBN|VBP|VBZ)'
NN_ADJ = '(NN|NNS|NNP|NNPS|JJ|JJR|JJS)'
PR_VB = '(PRP|PRP\$|VB|VBD|VBG|VBN|VBP|VBZ)'
PR_ADJ = '(PRP|PRP\$|JJ|JJR|JJS)'
PR_NN = '(PRP|PRP\$|NN|NNS|NNP|NNPS)'
PR_NN_VB = '(PRP|PRP\$|NN|NNS|NNP|NNPS|VB|VBD|VBG|VBN|VBP|VBZ)'
PR_NN_ADJ = '(PRP|PRP\$|NN|NNS|NNP|NNPS|JJ|JJR|JJS)'
PRONOUN = '(PRP|PRP\$)'
ADJ = '(JJ|JJR|JJS)'

PR_SYN = {	'he' : set(['he','him','his','himself']),
			'him' : set(['he','him','his','himself']),
			'his' : set(['he','him','his','himself']),
			'himself' : set(['he','him','his','himself']),
			'she' : set(['she','her','hers','herself']),
			'her' : set(['she','her','hers','herself']),
			'hers' : set(['she','her','hers','herself']),
			'herself' : set(['she','her','hers','herself']),
			'it' : set(['she','her','hers','herself']),
			'its' : set(['she','her','hers','herself']),
			'itself' : set(['she','her','hers','herself']),
			'they' : set(['they','them','their','theirs', 'themselves']),
			'them' : set(['they','them','their','theirs', 'themselves']),
			'their' : set(['they','them','their','theirs', 'themselves']),
			'theirs' : set(['they','them','their','theirs', 'themselves']),
			'themselves' : set(['they','them','their','theirs', 'themselves']) }

def checkIfUnambigous(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	result = False
	try:
		check1 = checkNVNAndNV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
		check2 = checkNVNAndVN(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
		check3 = checkPVPAndPV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
		check4 = checkPVPAndVP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
		check5 = checkPVNAndPV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
		check6 = checkPVNAndVP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
		check7 = checkNVPAndPV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
		check8 = checkNVPAndVP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
		check9 = checkNVNAndNA(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
		check10 = checkNVNAndAN(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
		check11 = checkPVPAndPA(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
		check12 = checkPVPAndAP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
		check13 = checkPVNAndPA(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
		check14 = checkPVNAndAP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
		check15 = checkNVPAndPA(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
		check16 = checkNVPAndAP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
		result = check1 or check2 or check3 or check4 or check5 or check6 or check7 or check8 or check9 or check10 or check11 or check12 or check13 or check14 or check15 or check16	
	except Exception as e:
		print ">>Exception :", e
	
	return result
	
def checkNVNAndNV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):

	sentence1Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS +'(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*'+ VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		nounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(NOUNS, " ".join(sentence1POSs)).group(0))]
		
		multiple = [1 for i in sentence1Words if nounWordinSentence2.strip() == i.strip()]
		if len(multiple) == 1:
			return True
			
	return False
	
def checkNVNAndVN(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		nounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(NOUNS, " ".join(sentence1POSs)).group(0))]
		
		multiple = [1 for i in sentence1Words if nounWordinSentence2.strip() == i.strip()]
		if len(multiple) == 1:
			return True

	return False

def checkPVPAndPV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		nounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(PRONOUN, " ".join(sentence1POSs)).group(0))]
		
		multiple = [1 for i in sentence1Words if nounWordinSentence2.strip() in PR_SYN[ i.strip() ] ]
		if len(multiple) == 1:
			return True

	return False

def checkPVPAndVP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		pronounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(PRONOUN, " ".join(sentence1POSs)).group(0))]
		
		multiple = [1 for i in sentence1Words if pronounWordinSentence2.strip() in PR_SYN[ i.strip() ] ]
		if len(multiple) == 1:
			return True

	return False

def checkPVNAndPV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		pronounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(PRONOUN, " ".join(sentence1POSs)).group(0))]
		
		multiple = [1 for i in sentence1Words if pronounWordinSentence2.strip() in PR_SYN[ i.strip() ] ]
		if len(multiple) == 1:
			return True

	return False

def checkPVNAndVP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' +  VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		pronounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(PRONOUN, " ".join(sentence1POSs)).group(0))]
		
		multiple = [1 for i in sentence1Words if pronounWordinSentence2.strip() in PR_SYN[ i.strip()] ]
		if len(multiple) == 1:
			return True

	return False

def checkNVPAndPV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		pronounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(PRONOUN, " ".join(sentence1POSs)).group(0))]
		
		multiple = [1 for i in sentence1Words if pronounWordinSentence2.strip() in PR_SYN[ i.strip()] ]
		if len(multiple) == 1:
			return True

	return False

def checkNVPAndVP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' +  VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		pronounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(PRONOUN, " ".join(sentence1POSs)).group(0))]
		
		multiple = [1 for i in sentence1Words if pronounWordinSentence2.strip() in PR_SYN[ i.strip()] ]
		if len(multiple) == 1:
			return True

	return False
	
	
def checkNVNAndNA(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):

	sentence1Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS +'(IN|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*'+ ADJ + '(IN|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		nounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(NOUNS, " ".join(sentence1POSs)).group(0))]
		
		multiple = [1 for i in sentence1Words if nounWordinSentence2.strip() == i.strip()]
		if len(multiple) == 1:
			return True
			
	return False
	
def checkNVNAndAN(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + ADJ + '(IN|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		nounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(NOUNS, " ".join(sentence1POSs)).group(0))]
		
		multiple = [1 for i in sentence1Words if nounWordinSentence2.strip() == i.strip()]
		if len(multiple) == 1:
			return True

	return False

def checkPVPAndPA(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + ADJ + '(IN|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		nounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(PRONOUN, " ".join(sentence1POSs)).group(0))]
		
		multiple = [1 for i in sentence1Words if nounWordinSentence2.strip() in PR_SYN[ i.strip() ] ]
		if len(multiple) == 1:
			return True

	return False

def checkPVPAndAP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + ADJ + '(IN|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		pronounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(PRONOUN, " ".join(sentence1POSs)).group(0))]
		
		multiple = [1 for i in sentence1Words if pronounWordinSentence2.strip() in PR_SYN[ i.strip() ] ]
		if len(multiple) == 1:
			return True

	return False

def checkPVNAndPA(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + ADJ + '(IN|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		pronounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(PRONOUN, " ".join(sentence1POSs)).group(0))]
		
		multiple = [1 for i in sentence1Words if pronounWordinSentence2.strip() in PR_SYN[ i.strip() ] ]
		if len(multiple) == 1:
			return True

	return False

def checkPVNAndAP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' +  ADJ + '(IN|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		pronounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(PRONOUN, " ".join(sentence1POSs)).group(0))]
		
		multiple = [1 for i in sentence1Words if pronounWordinSentence2.strip() in PR_SYN[ i.strip()] ]
		if len(multiple) == 1:
			return True

	return False

def checkNVPAndPA(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + ADJ + '(IN|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		pronounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(PRONOUN, " ".join(sentence1POSs)).group(0))]
		
		multiple = [1 for i in sentence1Words if pronounWordinSentence2.strip() in PR_SYN[ i.strip()] ]
		if len(multiple) == 1:
			return True

	return False

def checkNVPAndAP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' +  ADJ + '(IN|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		pronounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(PRONOUN, " ".join(sentence1POSs)).group(0))]
		
		multiple = [1 for i in sentence1Words if pronounWordinSentence2.strip() in PR_SYN[ i.strip()] ]
		if len(multiple) == 1:
			return True

	return False	
	

if __name__ == "__main__":
	sentence1Words = ['kevin', 'yelled', 'at', 'john']
	sentence1POSs = ['NNP', 'VBD', 'IN', 'NN']
	sentence2Words = ['john', 'upset']
	sentence2POSs = ['NN', 'JJ']
	print checkIfUnambigous(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	
	
	sentence1Words = ['kevin', 'yelled', 'at', 'john']
	sentence1POSs = ['NNP', 'VBD', 'IN', 'NN']
	sentence2Words = ['john', 'ran']
	sentence2POSs = ['NN', 'VBD']
	print checkIfUnambigous(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	
	
	sentence1Words = ['he', 'yelled', 'at', 'him']
	sentence1POSs = ['NNP', 'VBD', 'IN', 'NN']
	sentence2Words = ['he', 'upset']
	sentence2POSs = ['NN', 'JJ']
	print checkIfUnambigous(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	
	
	sentence1Words = ['he', 'yelled', 'at', 'him']
	sentence1POSs = ['NNP', 'VBD', 'IN', 'NN']
	sentence2Words = ['he', 'ran']
	sentence2POSs = ['NN', 'VBD']
	print checkIfUnambigous(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	
