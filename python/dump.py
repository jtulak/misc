''' Debug function'''
''' Authors: Jan Tulak <jan@tulak.me>, Zoredache (http://stackoverflow.com/questions/383944/what-is-a-python-equivalent-of-phps-var-dump)'''
''' Usage: dump.var_dump(variable)'''

from pprint import pprint
class dump:
	@classmethod
	def var_print(cls,obj):
		'''Will directly print the variable'''
		print(cls.var_dump(obj))

	@classmethod
	def var_dump(cls,obj):
		'''return a string with informationis about the variable'''
		ret=""
		if isinstance(obj,str):
			ret="String ("+str(len(obj))+"): "+repr(obj)
		elif isinstance(obj,int):
			ret="Int ("+str(obj)+")"
		#elif isinstance(obj,long):
		#	ret="Long ("+str(obj)+")"
		elif isinstance(obj,float):
			ret="Float ("+str(obj)+")"
		elif isinstance(obj,complex):
			ret="Complex ("+str(obj)+")"
		elif isinstance(obj,dict):
			ret="Dict ("+str(len(obj))+"): "+repr(obj)
		elif cls.__is_sequence(obj):
			ret="Sequence ("+str(len(obj))+"): "+repr(obj)
		elif isinstance(obj,object):
			ret="Object: "+cls.__raw_dump(obj)
		else:
			ret="Not implemented... "+cls.__raw_dump(obj)
	
		return ret;

	def __is_sequence(arg):
		'''test if the variable is and list, sequence...'''
		'''author: steveha (http://stackoverflow.com/questions/1835018/python-check-if-an-object-is-a-list-or-tuple-but-not-string)'''
		return (not hasattr(arg, "strip") and
			hasattr(arg, "__getitem__") or
			hasattr(arg, "__iter__"))


	@classmethod
	def __raw_dump(cls,obj):
		'''return a printable representation of an object for debugging - do not append informations about type'''
		newobj=obj
		if '__dict__' in dir(obj):
			newobj=obj.__dict__
			if ' object at ' in str(obj) and not newobj.has_key('__type__'):
				newobj['__type__']=str(obj)
			for attr in newobj:
				newobj[attr]=dump(newobj[attr])
		return newobj
