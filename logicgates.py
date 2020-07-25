def AND(*args):
	for argument in args:
		if argument:
			continue
		else:
			return False
	else:
		return True

def OR(*args):
	for argument in args:
		if argument:
			return True
		else:
			continue
	else:
		return False

def NOT(arg):
	return not arg
