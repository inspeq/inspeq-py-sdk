from setuptools import setup, find_packages


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()


setup(
    name="inspeqai",
    version="1.0.0",
    packages=find_packages(include=['inspeq.*','inspeq']),
    license="Apache 2.0",
    author="Inspeq",
     install_requires=[
        'requests', 
            # Specify dependencies if any
    ],
    description="Inspeq AI SDK",
    long_description=read_file(file_name="README.md"),
    python_requires=">=3.10",
      
)
