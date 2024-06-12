import setuptools

with open('README.md','r') as file:
	long_description=file.read


setuptools.setup(
	name='preprocess_karthikBollepalli', #this shld be unique
	version='0.0.1', #can give any number
	author='Karthik Bollepalli',
	author_email= 'karthikgoud759@gmail.com',
	description='This is prepprocessing package',
	long_description=long_description,
	long_description_content_type='text/markdown',
	packages=setuptools.find_packages(),
	classifiers=[
	'programming Language :: python :: 3',
	'License :: Osi Aproved :: MIT License',
	'Operating system :: OS Independent'],
	python_requires='>=3.5'
	)