import re

# filter type
filter_list = []
# 0 antiXSS for RTE
filter_list.append(re.compile("[^a-zA-Z0-9-~_]"))
# 1 antiXSS for email
filter_list.append(re.compile("^[a-zA-Z0-9-_]+@[a-zA-Z0-9-_]+(.[a-zA-Z0-9-_]+)+$"))


# filter string
def antiXSS(s, filter_type = 0):
	try:
		s + ""
	except Exception, e:
		raise e
	else:
		s_list = [i for i in s]
		for i in range(len(s_list)):
			if filter_list[filter_type].match(s_list[i]):
				s_list[i] = '-'
		s = "".join(s_list)
		return s

def isEmailAddress(s, filter_type = 1):
	try:
		s + ""
	except Exception, e:
		raise e
	else:
		return filter_list[filter_type].match(s)!=None
