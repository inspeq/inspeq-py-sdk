from setuptools import setup, find_packages

setup(
    name="inspeqai",
    version="1.0.0",
    packages=find_packages(),
    license="Apache 2.0",
    author="Inspeq",
     install_requires=[
        'requests', 
            # Specify dependencies if any
    ],
    description="Inspeq AI SDK",

    python_requires=">=3.10",  
)
