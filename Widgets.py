import os
import string
from pynput import keyboard
import shutil
from utilities import *

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
		for i in range(0, 1):
			out += "\n"

		for i in range(0, 5):
			for c in text.upper():
				out += self.font[i][alphabet.index(c)] + separator

			out += "\n"

		for i in range(0, int(shutil.get_terminal_size().lines / 2 - 4)):
			out += "\n"

		print(out)

	def debugFont(self):
		for char in self.font:
			print(char + "\n")

class ChooseWidget:
	def __init__(self, options=[]):
		self.options = list(options)
		self.flag = {"AdaptiveIndex": False, "AllowSeveralSameOption": False}
		self.cursor = 0
		self.isEnter = False
		self.isRunning = True
		self.prefix = ""

	def add_choice(self, option):
		if option in self.options:
			if not self.flag.get("AllowSeveralSameOption"):
				raise AttributeError(
					f"Option {option} already exist in the option, you can avoid this error by turning true flag named 'AllowSeveralSameOption'")

			else:
				# raise Warning(f"Option {option} has been accepted, although her name already in the options'list")
				pass
		self.options.append(option)

	def rmv_choice(self, index=None, name=None):
		if index == None and name == None:
			raise AttributeError("You must give an index or a name")

		if not name in self.options and index == None:
			raise AttributeError(f"You probably make a mistake because {name} isn't in options'list")

		if len(self.options) <= index:
			if not self.flag.get("AdaptiveIndex"):
				raise AttributeError(
					f"Index {index} is less than options'list length {len(self.options)}, you can avoid this error by turning true flag named 'AdaptiveIndex'")
			else:
				index %= len(self.options)
				raise Warning(
					f"Index has been adapted and reduce to {index}, your original value was too big compared for size of options'list")

		if index != None:
			self.options.pop(index)

		else:
			self.options.pop(self.options.index(name))

	def rmv_all_choices(self):
		self.options.clear()

	def set_flag(self, flagname, value):
		if type(value) == bool:
			self.flag[flagname] = value

		else:
			raise AttributeError("Must be boolean")

	def on_press(self, key):
		if key == keyboard.Key.down:
			self.on_down()
			os.system("cls")
			if self.prefix != "":
				print(self.prefix)
			self.display()

		elif key == keyboard.Key.up:
			self.on_up()
			os.system("cls")
			if self.prefix != "":
				print(self.prefix)
			self.display()

		elif key == keyboard.Key.esc:
			self.on_esc()
			os.system("cls")
			if self.prefix != "":
				print(self.prefix)
			self.display()
			return False

		elif key == keyboard.Key.enter:
			self.on_enter()
			os.system("cls")
			if self.prefix != "":
				print(self.prefix)
			self.display()
			return False

		else:
			pass

	def on_down(self):
		if self.cursor + 1 == len(self.options):
			self.cursor = 0
		else:
			self.cursor += 1

	def on_up(self):
		if self.cursor == 0:
			self.cursor = len(self.options) - 1
		else:
			self.cursor -= 1

	def on_esc(self):
		self.isRunning = False

	def on_enter(self):
		self.isRunning = False
		self.isEnter = True

	def key_handler(self):
		with keyboard.Listener(on_press=self.on_press) as listener:
			while self.isRunning:
				listener.join()

			self.isRunning = True

	def display(self):
		for i in range(0, len(self.options)):
			if i == self.cursor:
				print(f"--> \t{i + 1} : {self.options[i]}")
			else:
				print(f"    \t{i + 1} : {self.options[i]}")

	def setPrefix(self, prefix):
		self.prefix = prefix

	def run(self):
		if self.prefix != "":
			print(self.prefix)
		self.display()
		self.key_handler()
		if self.isEnter:
			return self.cursor + 1

		self.cursor = 0
		self.isEnter = False
		flush_input()
