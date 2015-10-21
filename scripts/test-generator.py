import os
import ast

'''
Test generator to create new test for __init__ function in saws.py with default arguments passed
Other tests as before with the new Class Object created with default constructor args
'''

file_to_parse = "saws.py"
with open(file_to_parse) as fd:
    file_contents = fd.read()

module = ast.parse(file_contents)
class_definitions = [node for node in module.body if isinstance(node, ast.ClassDef)]
function_definitions = [node for node in class_definitions[0].body if isinstance(node, ast.FunctionDef)]
for f in function_definitions: 
	#print ast.dump(f)
	defaultargs = {}
	non_defaultargs = len(f.args.args) - len(f.args.defaults)
	for i in range(len(f.args.defaults)):
		defaultargs[f.args.args[i+non_defaultargs].id] = f.args.defaults[i].id
	newtest = ""
	if(defaultargs and f.name == "__init__"):		
		with open("test_saws2.py",'w') as fw:
			with open("test_saws.py",'r') as fd:
				for line in fd:
					if "self.saws = Saws(refresh_resources=False)" in line:
						fw.write("\t\t# creating object with default args\n")
						fw.write("\t\tself.saws = Saws({0}={1})\n".format(defaultargs.keys()[0],defaultargs[defaultargs.keys()[0]]))
					else:
						fw.write(line)
    	break