class EnemyBar():
	def __init__(self, health, maxhealth, barsize=20, border=True):
		self.health = health
		self.maxhealth = maxhealth
		self.barsize = barsize
		self.border = border

	def compute(self):
		percentage = int(self.health/(self.maxhealth/100))
		points = int(self.health/(self.maxhealth/self.barsize))
		displayed_percent = str(percentage)
		while len(displayed_percent) != 3:
			displayed_percent += " "

		displayed_percent += "%"
		out = f"[{displayed_percent.center(self.barsize+4, "=")}"
		if percentage > 100:
			out += f"[{'-'*((percentage-100)//(100//self.barsize))}]"

		else:
			for i in range(0, self.barsize-points):


		return out
	
	def modify(self, modify):
		self.health += modify
		
enemy = EnemyBar(1000, 1000)
print(enemy.compute())
enemy.modify(-200)
print(enemy.compute())