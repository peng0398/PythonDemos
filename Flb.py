class Flb(object):
	def __init__(self):
		self.a,self.b = 0,1
	
	def __iter__(self):
		return self

	def __next__(self):
		self.a,self.b = self.b,self.a+self.b
		if self.a > 100000:
			raise StopIteration()
		return self.a
	
	def __getitem__(self,n):
		a,b = 0,1
		for x in range(n):
			a,b = b,a+b
		return a
