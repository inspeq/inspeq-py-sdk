from setuptools import setup, find_packages

# Read the content of your README file
with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='inspeqai',
    version='0.1',
    packages=find_packages(include=["inspeq*"]),
    install_requires=[
        'requests', 
            # Specify dependencies if any
    ],
    long_description=long_description,  # Assign the content of your README to long_description
    long_description_content_type='text/markdown',  # Specify the type of content (markdown)
    
    project_urls={
        'Documentation': '',  # Remove this if you want to use README as documentation
        'Source': '',
    },

    # author='Tushar Dogra, Shubam Sharma',  
)
