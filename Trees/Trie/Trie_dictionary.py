class Trie:
	def __init__(self):
		self.root = {}

	def insert(self,word):
		level = self.root
		for char in word:
			if char not in level:
				level[char] = {}
			level = level[char]
		level['End'] = True 
	
	def search(self,word):
		level = self.root
		for char in word:
			if char not in level:
				return False
			level = level[char]
		return 'End' in level

	def startsWith(self,prefix):
		level = self.root
		for char in prefix:
			if char not in level:
				return False
			level = level[char]
		return True

if __name__ == "__main__":
	inp = ['apple','apk']
	search = ['apple','app','ap','application']
	t = Trie()

	for word in inp:
		t.insert(word)

	for word in search:
		print( word,' -> ',t.search(word) )

	print('---------------------------------')

	for word in search:
		print( word,' -> ',t.startsWith(word) )
	

