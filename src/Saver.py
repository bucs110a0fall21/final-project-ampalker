import pickle

class Saver:
	def __init__(self, file_name, location):
		self.file_name = file_name
		self.location = location
	def save(self, data):
		new_data = open(self.location+'/'+self.file_name, 'wb')
		pickle.dump(data, new_data)
	def load(self):
		new_data = open(self.location+'/'+self.file_name, 'rb')
		data = pickle.load(new_data)
		return data
