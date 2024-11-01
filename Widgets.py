import os
import string

class Bar:
	def __init__(self, health, maxhealth, barsize=20, showBorder=True, showPercent=True, showHealth=False):
		self.health = health
		self.maxhealth = maxhealth
		self.barsize = barsize
		self.showBorder = showBorder
		self.showPercent = showPercent
		self.showHealth = showHealth

	def compute(self):
		out = "["
		for i in range(0, self.barsize):
			if i*(self.maxhealth//self.barsize) < self.health:
				out += "="
			else:
				out += " "

		if not self.showBorder:
			out = out[1:]
		else:
			out += "]"

		if self.showHealth:
			out += f" {str(self.health)} HP"

		if self.showPercent:
			out += f"  ({str((self.health/self.maxhealth)*100)} %)"

		return out
	
	def modify(self, modify):
		self.health += modify

	def getHealth(self):
		return self.health

	def getMaxHealth(self):
		return self.maxhealth

	def getBarSize(self):
		return self.barsize

	def getBorderShown(self):
		return self.showBorder

	def getPercentShown(self):
		return self.showPercent

	def getHealthShown(self):
		return self.showHealth

	def setHealth(self, health):
		self.health = health

	def setMaxHealth(self, maxhealth):
		self.maxhealth = maxhealth

	def setBarSize(self, barsize):
		self.barsize = barsize

	def setBorderShown(self, showBorder):
		self.showBorder = showBorder

	def setPercentShown(self, showPercent):
		self.showPercent = showPercent

	def setHealthShown(self, showHealth):
		self.showHealth = showHealth

	def settings(self, health=100, maxhealth=100, barsize=20, showBorder=True, showPercent=False, showHealth=True):
		self.setHealth(health)
		self.setMaxHealth(maxhealth)
		self.setBarSize(barsize)
		self.setBorderShown(showBorder)
		self.setPercentShown(showPercent)
		self.setHealthShown(showHealth)

class BigTitle:
	def __init__(self):
		self.font = [
			["■■■■■", "■■■■■", "■■■■■", "■■■■ ", "■■■■■", "■■■■■", " ■■■ ", "■   ■", "■■■■■", "■■■■■", "■   ■", "■    ",
			 "■   ■", "■   ■", "■■■■■", "■■■■ ", "■■■■■", "■■■■ ", "■■■■■", "■■■■■", "■   ■", "■   ■", "■ ■ ■", "■   ■",
			 "■   ■", "■■■■■", "     "],
			["■   ■", "■   ■", "■    ", "■   ■", "■    ", "■    ", "■    ", "■   ■", "  ■  ", "  ■  ", "■  ■ ", "■    ",
			 "■■ ■■", "■■  ■", "■   ■", "■   ■", "■   ■", "■   ■", "■    ", "  ■  ", "■   ■", "■   ■", "■ ■ ■", " ■ ■ ",
			 " ■ ■ ", "   ■ ", "     "],
			["■   ■", "■■■■ ", "■    ", "■   ■", "■■■  ", "■■■  ", "■  ■■", "■■■■■", "  ■  ", "  ■  ", "■■   ", "■    ",
			 "■ ■ ■", "■ ■ ■", "■   ■", "■   ■", "■ ■ ■", "■■■■■", "■■■■■", "  ■  ", "■   ■", "■   ■", "■ ■ ■", "  ■  ",
			 "  ■  ", "  ■  ", "     "],
			["■■■■■", "■   ■", "■    ", "■   ■", "■    ", "■    ", "■   ■", "■   ■", "  ■  ", "  ■  ", "■ ■  ", "■    ",
			 "■   ■", "■  ■■", "■   ■", "■■■■■", "■■■■■", "■ ■■ ", "    ■", "  ■  ", "■   ■", " ■ ■ ", " ■ ■ ", " ■ ■ ",
			 "  ■  ", " ■   ", "     "],
			["■   ■", "■■■■■", "■■■■■", "■■■■ ", "■■■■■", "■    ", " ■■■ ", "■   ■", "■■■■■", "■■   ", "■   ■", "■■■■■",
			 "■   ■", "■   ■", "■■■■■", "■    ", "   ■ ", "■   ■", "■■■■■", "  ■  ", "■■■■■", "  ■  ", " ■ ■ ", "■   ■",
			 "  ■  ", "■■■■■", "     "]]

	def printFont(self, text, separator="\t"):
		alphabet = string.ascii_uppercase + " "
		out = ""
		for i in range(0, 5):
			for c in text.upper():
				out += self.font[i][alphabet.index(c)] + separator
			out += "\n"

		print(out)

	def centerFont(self, text, separator="\t"):
		alphabet = string.ascii_uppercase + " "
		out = ""
		for i in range(0, int(os.get_terminal_size()[1] / 2 - 4)):
			out += "\n"

		for i in range(0, 5):
			for c in text.upper():
				out += self.font[i][alphabet.index(c)] + separator

			out += "\n"

		for i in range(0, int(os.get_terminal_size()[1] / 2 - 4)):
			out += "\n"

		print(out)

	def debugFont(self):
		for char in self.font:
			print(char + "\n")

