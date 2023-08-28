from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0',
    description='Clean folder',
    author='Tsyvis Anna',
    author_email='cyvisanna@gmail.com',
    packages=find_namespace_packages(),
    entry_points={'console_scripts':['clean-folder=clean_folder.main:main']}
   )