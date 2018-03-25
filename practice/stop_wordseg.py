from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

mylang = set(stopwords.words("english"))

eg = "I am learning nltk library help me god to complete it completely"

words = word_tokenize(eg)

#print(words)

myarr = []

for i in words:
	if i not in mylang:
		myarr.append(i)

print(myarr)		#the stop words list