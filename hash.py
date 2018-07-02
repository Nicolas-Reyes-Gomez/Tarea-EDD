# Hash Map

class HashMap:
	def __init__(self):
		self.size = 6
		self.map = [None] * self.size

	def _get_hash(self, mail):
		hash = 0
		for char in str(mail):
			hash += ord(char)
		return hash % self.size

	def add(self, mail, nombre, apellido, telefono):
		key_hash = self._get_hash(mail)
		key_value = [mail, nombre, apellido, telefono]

		if self.map[key_hash] is None:
			self.map[key_hash] = list([key_value])
			return True
		else:
			for pair in self.map[key_hash]:
				if pair[0] == mail:
					pair[1] = nombre
					pair[2] = apellido
					pair[3] = telefono
					return True
			self.map[key_hash].append(key_value)
			return True

	def get(self, mail):
		key_hash = self._get_hash(mail)
		if self.map[key_hash] is not None:
			for pair in self.map[key_hash]:
				if pair[0] == mail:
					return (pair[1], pair[2], pair[3])
		return None

	def delete(self, mail):
		key_hash = self._get_hash(mail)

		if self.map[key_hash] is None:
			return False
		for i in range (0, len(self.map[key_hash])):
			if self.map[key_hash][i][0] == mail:
				self.map[key_hash].pop(i)
				return True
		return False

	def print_(self):
		print('---PHONEBOOK----')
		for item in self.map:
			if item is not None:
				print(str(item))
