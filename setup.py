import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_world",
    version="0.0.1",
    author="Cedd Burge",
    author_email="ceddlyburge@gmail.com",
    description="A function that returns 'world'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ceddlyburge/python_world",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["numpy==1.22.1",
        "matplotlib==3.6.2",
        "pandas==1.4.4",
        "plotly==5.10.0",
        "pytest==7.2.0",
        "scikit-learn==1.1.3",
        "scipy==1.7.3",
        "seaborn==0.12.1"]
)
