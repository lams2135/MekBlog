import re
from log import write_log

# filter type
filter_list = []
# 0
filter_list.append(re.compile("[a-z]|[A-Z]|[0-9]|-|~|_"))


# filter string
def antiXSS(s, filter_type = 0):
	try:
		s + ""
	except Exception, e:
		raise e
	else:
		s_list = [i for i in s]
		for i in range(len(s_list)):
			if filter_list[filter_type].match(s_list[i]) == None:
				s_list[i] = '-'
		s = "".join(s_list)
		return s
