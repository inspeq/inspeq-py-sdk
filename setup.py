from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="inspeqai",
    version="1.0.28",
    packages=find_packages(include=["inspeq*"]),
    package_data={'inspeq': ['config_file.json']},
    license="Apache 2.0",
    author="Inspeq",
    author_email="support@inspeq.ai",
    install_requires=[
        "requests",
    ],
    description="Inspeq AI Python SDK",
    long_description=long_description,  # Assign the content of your README to long_description
    long_description_content_type="text/markdown",  # Specify the type of content (markdown)
    python_requires=">=3.10",
    project_urls={
        "Documentation": "https://docs.inspeq.ai",
        "Source": "https://github.com/inspeq/inspeq-py-sdk",
        
    },
)

