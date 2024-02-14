from setuptools import setup, find_packages
with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="inspeqai",
    version="1.0.5",
    packages=find_packages(include=["inspeq*"]),
    license="Apache 2.0",
    author="Inspeq",
     install_requires=[
        'requests', 
            # Specify dependencies if any
    ],
    description="Inspeq AI SDK",
    long_description=long_description,  # Assign the content of your README to long_description
    long_description_content_type='text/markdown',  # Specify the type of content (markdown)

    python_requires=">=3.10",  
    project_urls={
        # "Documentation": "",
        "Source": "https://github.com/inspeq/inspeq-py-sdk",
    },
)
