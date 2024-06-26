from setuptools import setup, find_packages

VERSION = '0.0.1' 
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
        package_dir={"": "app"},
        packages=find_packages(where="app"),
        install_requires=['pandas', 'requests'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Researchers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
        ],
        
        python_requires='>=3'
)