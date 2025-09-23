from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "Predicting emergent phenotypes from single cell populations using CELLECTION"

# Read requirements
def read_requirements():
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(requirements_path):
        with open(requirements_path, 'r') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name="cellection",
    version="0.1.2",
    author="Hongru Hu",
    author_email="hrhu.compbio@gmail.com",
    description="Predicting emergent phenotypes from single cell populations using CELLECTION",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/quon-titative-biology/CELLECTION",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
        ],
        "full": [
            "scanpy>=1.10.0",
            "anndata>=0.10.0",
            "scvi-tools>=0.20.0",
        ],
    },
    keywords="deep-learning, bioinformatics, machine-learning, multiple-instance-learning, pointnet",
    project_urls={
        "Bug Reports": "https://github.com/quon-titative-biology/CELLECTION/issues",
        "Source": "https://github.com/quon-titative-biology/CELLECTION",
        "Documentation": "https://github.com/quon-titative-biology/CELLECTION#readme",
    },
) 