import os
import ast
import sys

class ConstructorAnalyser:
	'''
	Custom Static Analysis: Parse the python files and highlight classes which have no constructor(init) function defined
	'''

	def __init__(self):
		self.module = None
		self.class_definitions = []
		self.function_definitions = []

	def parse(self,infile):
		with open(infile) as fd:
			file_contents = fd.read()
		try:
			self.module = ast.parse(file_contents)
		except:
			return None

	def check_for_constructor(self,infile):
		self.parse(infile)
		self.class_definitions = [node for node in self.module.body if isinstance(node, ast.ClassDef)]
		if not self.class_definitions:
			return
		for c in self.class_definitions:
			self.function_definitions = [node.name for node in c.body if isinstance(node, ast.FunctionDef)]			
			if "__init__" not in self.function_definitions:
				print("No constructor defined for class {0} in {1}".format(c.name,infile))

		
if __name__ == "__main__":
	analyser = ConstructorAnalyser()
	for root,dirnames,files in os.walk(sys.argv[1]):
		for f in files:
			analyser.check_for_constructor(os.path.join(root,f))
