from setuptools import setup, find_packages

setup(
    name='password-generator',  # Name of the package
    version='1.0.0',  # Version of the package
    description='A secure and customizable password generator for everyday use, with advanced pattern and replacement options.',  # Catchy description
    long_description=open('README.md').read(),  # Detailed description from README.md file
    long_description_content_type='text/markdown',  # Format for the detailed description
    author='Krish foren6',  # Author's name
    author_email='kg646233@gmail.com',  # Author's email
    url="https://github.com/chris-0317/Password_Generator.git",  # GitHub link to the project
    packages=find_packages(),  # Automatically find all packages in your project
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version requirement
    entry_points={
        'console_scripts': [
            'password-generator=passwd_gen:main',  # Allow running the script from terminal using the `password-generator` command
        ],
    },
    # Add any other dependencies here if required in the future
)
