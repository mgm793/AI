from calcvect import CalcVect
from createcorpus import CreateCorpus
def init():
	path = './dataset/'
	n = raw_input("Number of most common words: ")
	corpus = CreateCorpus(n,path)
	calcVect = CalcVect(corpus.counts,n,path)

init()

