from distutils.core import setup

try:
    longdesc = open('README').read()
except IOError:
    longdesc = ''

setup(name='dynamicloader',
      version='0.1.0',
      description='A django middleware and template loader to dynamically change template directories based on request headers',
      long_description=longdesc,
      author='Corey Oordt',
      author_email='coordt@washingtontimes.com',
      url='http://opensource.washingtontimes.com/projects/dynamicloader/',
      packages=['dynamicloader'],
      classifiers=[],
      )