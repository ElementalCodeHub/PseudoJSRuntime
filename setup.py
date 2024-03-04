from setuptools import setup, find_packages

VERSION = '0.1.0' 
DESCRIPTION = 'PSeudoJSRuntime'
LONG_DESCRIPTION = 'Javascript functions implemented in Python'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="PseudoJSRuntime", 
        version=VERSION,
        author="Debaditya Malakar",
        author_email="debadityamalakar@outlook.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["colorama>=0.4.6"], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 1 - Alpha",
            "Programming Language :: Python :: 3",
        ]
)