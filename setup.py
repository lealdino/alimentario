from setuptools import setup, find_packages

VERSION = '0.1.0' 
DESCRIPTION = 'Python package to import survey data from LimeSurvey'
LONG_DESCRIPTION = 'This package allows you to download data from LimeSurvey surveys in form of Pandas DataFrame'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="alimentario", 
        version=VERSION,
        author=["Pedro Lealdino Filho", "Marcio Gazolla", "Cristiane Tavares Feijo"],
        author_email=["admin@dataverso.com.br"],
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['pandas', 'requests'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Researchers',
            'License :: OSI Approved :: MIT License',

            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
            'Programming Language :: Python :: 3 :: Only',
            'License :: OSI Approved :: MIT License'
        ],
        
        python_requires='>=3'
)