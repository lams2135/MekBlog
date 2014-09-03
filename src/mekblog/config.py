import json

unused = "!<---u-n-u-s-e-d--->!"
used = "!<---u-s-e-d--->!"
unknown = "!<---u-n-k-n-o-w-n--->!"

class settings_object(object):
	"""
		docstring for settings_object
		__value__ for key to value
		__state__:
				unused
				dummy
				used
	"""
	def __init__(self):
		super(settings_object, self).__init__()
		self.__value__ = unused
		self.__state__ = unused
	def load(self, filename):
		fp = open(filename, "r")
		self.set(json.load(fp))
		fp.close()
	def save(self, filename):
		fp = open(filename, "w")
		json.dump(self.get(), fp, indent=2)
		fp.close()
	def __getattr__(self, name):
		if type(self.__dict__) != dict and self.__value__ != unused:
			raise KeyError("Attribute %s isn't a dict type" % name)
		elif self.__value__ == unused:
			self.__value__ = {}
		if name not in self.__value__:
			self.__value__.setdefault(name, settings_object())
		self.__state__ = unknown
		return self.__value__[name]
	def get(self):
		def get_travel(settings):
			if settings.__state__ == unused:
				return False, None
			elif type(settings.__value__) == dict:
				# check if client set a empty dict like {}
				exist = (settings.__state__ == used)
				get_dict = {}
				for x, y in settings.__value__.items():
					exist_tmp, get_dict_tmp = get_travel(settings.__value__[x])
					if exist_tmp == True:
						get_dict[x] = get_dict_tmp
						exist = True
				if exist == True:
					settings.__state__ = used
				else:
					settings.__state__ = unused	
				return exist, get_dict
			elif settings.__value__ != unused:
				settings.__state__ = used
				return True, settings.__value__
			else:
				settings.__state__ = unused
				return False, None


		exist, get_dict = get_travel(self)
		if exist == False:
			raise KeyError("Illegal route")
		return get_dict

	def set(self, set_dict):
		def set_travel(settings, set_dict):
			settings.__state__ = used
			if type(set_dict) != dict:
				settings.__value__ = set_dict
			else:
				settings.__value__ = {}
				for x,y in set_dict.items():
					settings.__value__.setdefault(x, settings_object())
					set_travel(settings.__value__[x], y)
		self.__value__ = unused
		set_travel(self, set_dict)
	def exist(self):
		return True

setting = settings_object()

def load(fn):
	setting.load(fn)

def save(fn):
	setting.save(fn)

if __name__ == "__main__":

	setting.load("test.json")
	print setting.core.db.exist()
	print setting.core.db.get()
	setting.core.db.set({"hahahah":1111})
	setting.askdlfjh.ahjksdgf.ajksdhg.set(123)
	setting.asjkldfh.asjkdfk.akjssj.set({})
	setting.save("tt.json")

