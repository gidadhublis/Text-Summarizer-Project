import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
    
__version__ = '0.0.0'
SRC_REPO="textSummarizer"
REPO_NAME="Text-Summarizer-Project"
AUTHOR="gidadhublis"
AUTHOR_EMAIL="sachin.gdadhubli@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author={AUTHOR},
    author_email={AUTHOR_EMAIL},
    description="Text Summarizer Project for NLP Application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{AUTHOR}/{REPO_NAME}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"]
    )
