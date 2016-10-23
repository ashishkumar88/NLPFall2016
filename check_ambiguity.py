import re

NOUNS = '(NN|NNS|NNP|NNPS)'
VERBS = '(VB|VBD|VBG|VBN|VBP|VBZ)'
NN_VB = '(NN|NNS|NNP|NNPS|VB|VBD|VBG|VBN|VBP|VBZ)'
PR_VB = '(PRP|PRP$|VB|VBD|VBG|VBN|VBP|VBZ)'
PR_NN = '(PRP|PRP$|NN|NNS|NNP|NNPS)'
PR_NN_VB = '(PRP|PRP$|NN|NNS|NNP|NNPS|VB|VBD|VBG|VBN|VBP|VBZ)'
PRONOUN = '(PRP|PRP$)'

def checkIfUnambigous(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	check1 = checkNVNAndNV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	check2 = checkNVNAndVN(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	check3 = checkPVPAndPV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	check4 = checkPVPAndVP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	check5 = checkPVNAndPV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	check6 = checkPVNAndVP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	check7 = checkNVPAndPV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	check8 = checkNVPAndVP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	result = check1 or check2 or check3 or check4 or check5 or check6 or check7 or check8
	return result
	
def checkNVNAndNV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):

	sentence1Pattern = '^' + '[^'+ PR_VB +']*' + NOUNS + '[^' + PR_NN + ']*' + VERBS + '[^' + PR_VB + ']*' + NOUNS + '[^' + PR_NN_VB + ']*' + '$'
	sentence2Pattern = '^' + '[^'+ PR_VB +']*' + NOUNS +'[^'+ PR_NN +']*'+ VERBS + '[^' + PR_NN_VB + ']*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		nounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(NOUNS, " ".join(sentence1POSs)).group(0))]
		if nounWordinSentence2 in sentence1Words:
			return True
	return False
	
def checkNVNAndVN(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '[^'+ PR_VB +']*' + NOUNS + '[^' + PR_NN + ']*' + VERBS + '[^' + PR_VB + ']*' + NOUNS + '[^' + PR_NN_VB + ']*' + '$'
	sentence2Pattern = '^' + '[^'+ PR_NN +']*' + VERBS + '[^' + PR_VB + ']*' + NOUNS + '[^' + PR_NN_VB + ']*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		nounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(NOUNS, " ".join(sentence1POSs)).group(0))]
		if nounWordinSentence2 in sentence1Words:
			return True
	return False

def checkPVPAndPV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '[^' + NN_VB + ']*' + PRONOUN + '[^' + PR_NN + ']*' + VERBS + '[^' + NN_VB + ']*' + PRONOUN + '[^' + PR_NN_VB + ']*' + '$'
	sentence2Pattern = '^' + '[^' + NN_VB + ']*' + PRONOUN + '[^' + PR_NN + ']*' + VERBS + '[^' + PR_NN_VB + ']*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		nounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(PRONOUN, " ".join(sentence1POSs)).group(0))]
		if nounWordinSentence2 in sentence1Words:
			return True
	return False

def checkPVPAndVP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '[^' + NN_VB + ']*' + PRONOUN + '[^' + PR_NN + ']*' + VERBS + '[^' + NN_VB + ']*' + PRONOUN + '[^' + PR_NN_VB + ']*' + '$'
	sentence2Pattern = '^' + '[^' + PR_NN + ']*' + VERBS + '[^' + NN_VB + ']*' + PRONOUN + '[^' + PR_NN_VB + ']*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		nounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(PRONOUN, " ".join(sentence1POSs)).group(0))]
		if nounWordinSentence2 in sentence1Words:
			return True
	return False

def checkPVNAndPV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '[^' + NN_VB + ']*' + PRONOUN + '[^' + PR_NN + ']*' + VERBS + '[^' + PR_VB + ']*' + NOUNS + '[^' + PR_NN_VB + ']*' + '$'
	sentence2Pattern = '^' + '[^' + NN_VB + ']*' + PRONOUN + '[^' + PR_NN + ']*' + VERBS + '[^' + PR_NN_VB + ']*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		nounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(PRONOUN, " ".join(sentence1POSs)).group(0))]
		if nounWordinSentence2 in sentence1Words:
			return True
	return False

def checkPVNAndVP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '[^' + NN_VB + ']*' + PRONOUN + '[^' + PR_NN + ']*' + VERBS + '[^' + PR_VB + ']*' + NOUNS + '[^' + PR_NN_VB + ']*' + '$'
	sentence2Pattern = '^' + '[^' + PR_NN + ']*' +  VERBS + '[^' + NN_VB + ']*' + PRONOUN + '[^' + PR_NN_VB + ']*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		nounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(PRONOUN, " ".join(sentence1POSs)).group(0))]
		if nounWordinSentence2 in sentence1Words:
			return True
	return False

def checkNVPAndPV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '[^' + PR_VB + ']*' + NOUNS + '[^' + NN_VB + ']*' + VERBS + '[^'+ PR_VB +']*' + PRONOUN + '[^' + PR_NN_VB + ']*' + '$'
	sentence2Pattern = '^' + '[^' + NN_VB + ']*' + PRONOUN + '[^' + PR_NN + ']*' + VERBS + '[^' + PR_NN_VB + ']*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		nounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(PRONOUN, " ".join(sentence1POSs)).group(0))]
		if nounWordinSentence2 in sentence1Words:
			return True
	return False

def checkNVPAndVP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '[^' + PR_VB + ']*' + NOUNS + '[^' + NN_VB + ']*' + VERBS + '[^'+ PR_VB +']*' + PRONOUN + '[^' + PR_NN_VB + ']*' + '$'
	sentence2Pattern = '^' + '[^' + PR_NN + ']*' +  VERBS + '[^' + NN_VB + ']*' + PRONOUN + '[^' + PR_NN_VB + ']*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		nounWordinSentence2 = sentence2Words[sentence2POSs.index(re.search(PRONOUN, " ".join(sentence1POSs)).group(0))]
		if nounWordinSentence2 in sentence1Words:
			return True
	return False

if __name__ == "__main__":
	sentence1Words = ['man', 'ate', 'apple']
	sentence1POSs = ['NN', 'VBD', 'NN']
	sentence2Words = ['man', 'ate']
	sentence2POSs = ['NN', 'VBD']
	print checkIfUnambigous(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	
