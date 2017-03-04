def init():
	lexic = SetLexic()
	file = raw_input("Name of file to test: ") 
	test = Test(lexic, file)
	solFile = raw_input("Solution file name: ")
	accuracy = Evaluate(file,solFile)

class SetLexic():

	def __init__(self):
		self.file = "corpus.txt"
		self.exit = open("lexic.txt","w")
		self.dicc = {}
		self.lines = None
		self.setDicc()
		self.writeFile()

	def getDicc(self):
		return self.dicc

	def setDicc(self):
		with open(self.file) as f:
			for line in f:
				line = line.decode("latin_1").encode("UTF-8")
				line = line.replace("\r\n", "")
				word, typo = line.split("\t")
				word = word.lower()
				try:
					t = self.dicc[word]
					try:
						t[typo] += 1
					except KeyError, err:
						t[typo] = 1
				except KeyError, err:
					self.dicc[word] = {typo: 1}
		f.close()

	def writeFile(self):
		for key in self.dicc:
			for tag in self.dicc[key].keys():
				text = key + "\t" + tag + "\t" + str(self.dicc[key][tag]) + "\n"
				self.exit.write(text)
		self.exit.close()

class Test():

	def __init__(self,lexic,file):
		self.dicc = lexic.getDicc()
		self.file = file
		self.res = open("res_" + file, "w")
		self.lines = None
		self.setRes()

	def setRes(self):
		with open(self.file) as f:
			for line in f:
				line = line.decode("latin_1").encode("UTF-8")
				word = line.replace("\r\n", "").lower()
				try:
					types = self.dicc[word]
					types = sorted(types.items(), key=lambda t: t[1], reverse=True)
					text = word + "\t" + types[0][0] + "\n"
				except KeyError, err:
					text = word + "\t" + "NC" + "\n"
				self.res.write(text)
		f.close()
		self.res.close()

class Evaluate():
 
	def __init__(self, test,gold):
		self.testFile = open("res_" + test,"r")
		self.solFile = open(gold,"r")
		self.testLines = None
		self.solLines = None
		print "Accuracy: %.2f" % self.calcAccuracy() + "%"
 
	def read(self):
		self.testLines = self.testFile.readlines()
		self.solLines = self.solFile.readlines()
		self.solFile.close()
		self.testFile.close()
   
	def calcAccuracy(self):
		ocNumber = len(self.solLines)
		succesNumber = 0
		for test in range(len(self.testLines)):
			solWord , solTag = self.solLines[test].split("\t")
			testWord , testTag = self.testLines[test].split("\t")
			testTag = testTag.replace('\n','')
			solTag 	=  solTag.replace('\r\n','')

			if testWord.lower() == solWord.lower() and testTag == solTag:
				succesNumber += 1
		
		return (float(succesNumber)/ocNumber) * 100

init()