from setuptools import find_packages, setup

setup(
    name="AIMCQGenerator",
    version="0.0.1",
    author="Vaasa",
    author_email="srinivasanethiraaj@gmail.com",
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2","langchain-community"],
    packages=find_packages(),
)
