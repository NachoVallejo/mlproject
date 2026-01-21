from setuptools import setup, find_packages

# Read the contents of README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def get_requirements(file_path):
    """Reads a requirements file and returns a list of dependencies."""
    with open(file_path, 'r', encoding='utf-8') as file:
        requirements = file.readlines()
    return [req.strip() for req in requirements if req.strip() and not req.startswith('#')]

setup(
    name="mlproject",
    version="0.0.1",
    author="Your Name",
    author_email="hvallejot@uqvirtual.edu.co",
    description="A machine learning project template",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NachoVallejo/mlproject",
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=get_requirements('requirements.txt'),
)