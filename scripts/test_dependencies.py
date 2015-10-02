import unittest
import pip

class TestDependencies(unittest.TestCase):
	def test_d1(self):
		dists = set([di.key for di in pip.get_installed_distributions()])

		assert 'codecov' in dists
		assert 'flake8' in dists
		assert 'mock' in dists
		assert 'pexpect' in dists
		assert 'pytest' in dists
		assert 'tox' in dists
		assert 'sphinx' in dists
		assert 'sphinx-pypi-upload' in dists
		assert 'gitchangelog' in dists
		assert 'awscli' in dists
		assert 'click' in dists
		assert 'configobj' in dists
		assert 'prompt-toolkit' in dists
		assert 'six' in dists
		assert 'pygments' in dists
 
if __name__ == "__main__":
	unittest.main()