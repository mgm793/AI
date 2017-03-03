def init():
	lexit = SetLexic()

class SetLexic():
	def __init__(self):
		self.file = open("corpus.txt","r")
		self.exit = open("lexic.txt","w")
		self.dicc = {}
		self.lines = []
		self.read()
		self.setDicc()
		self.writeFile()

	def getDicc(self):
		return self.dicc

	def read(self):
		self.lines = self.file.readlines()
		self.file.close()

	def setDicc(self):
		for line in self.lines:
			line = line.decode("latin_1").encode("UTF-8")
			line = line.replace("\r\n", "")
			word, typo = line.split("\t")
			word = word.lower()
			try:
				self.dicc[word,typo] += 1
			except KeyError, err:
				self.dicc[word,typo] = 1

	def writeFile(self):
		text = ""
		for key in self.dicc:
			text += str(key[0]) + "\t" + str(key[1]) + "\t" + str(self.dicc[key]) + "\n"
		self.exit.write(text)
		self.exit.close()

init()