import json

unused = "!<---unused--->!"

class Illegal_address_object(object):
	"""
		docstring for Illegal_address_object
		for Illegal operation of settings_object
	"""
	def __init__(self):
		super(Illegal_address_object, self).__init__()
	def __getattr__(self, name):
		return self
	def get(self):
		raise KeyError("Illegal address")
	def exist(self):
		return False
	def set(self, name):
		raise KeyError("Illegal address")

Illegal_address = Illegal_address_object()
		

class settings_object(object):
	"""
		docstring for settings_object
		__tree_dict__ for dynamic attribute
		__value__ for key to value
	"""
	def __init__(self):
		super(settings_object, self).__init__()
		self.__tree_dict__ = unused
		self.__value__ = unused
	def load(self, filename):
		fp = open(filename, "r")
		self.set(json.load(fp))
		fp.close()
	def save(self, filename):
		fp = open(filename, "w")
		json.dump(self.get(), fp, indent=2)
		fp.close()
	def __getattr__(self, name):
		if name not in self.__tree_dict__:
			return Illegal_address
		return self.__tree_dict__[name]
	def get(self):
		def get_travel(settings):
			if type(settings.__tree_dict__) != dict:
				if settings.__value__ != unused:
					get_dict = settings.__value__
					return get_dict
				else:
					raise KeyError("Illegal address")
			else:
				get_dict = {}
				for x,y in settings.__tree_dict__.items():
					get_dict[x] = get_travel(y)
				return get_dict
		return get_travel(self)

	def set(self, set_dict):
		def set_travel(settings, set_dict):
			if type(set_dict) != dict:
				settings.__value__ = set_dict
			else:
				settings.__tree_dict__ = {}
				for x,y in set_dict.items():
					settings.__tree_dict__.setdefault(x, settings_object())
					set_travel(settings.__tree_dict__[x], y)
			#	print settings[0].__tree_dict__
		self.__tree_dict__ = unused
		self.__value__ = unused
		set_travel(self, set_dict)
	def exist(self):
		return True

setting = settings_object()

if __name__ == "__main__":

	setting.load("test.json")
	print setting.core.db.exist()
	print setting.core.db.get()
	setting.core.db.set({"hahahah":1111})
	setting.save("tt.json")

