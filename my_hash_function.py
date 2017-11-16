class MyHash:
	def __init__(self):
		self.my_array = [None] * 26

	def put(self, key, value):
		index = self.my_hash_function(key)
		self.my_array[index] = value

	def get(self, key):
		index = self.my_hash_function(key)
		return self.my_array[index]

	def my_hash_function(self, inputValue):
		alphabet = 'abcdefghijklmnopqrstuvwxyz'
		first_letter = inputValue[0]
		return alphabet.index(first_letter)

h = MyHash()

h.put('first_name', 'Bob')
print h.get('first_name')