import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Bots of discord Python API", # Replace with your own username
    version="0.0.1",
    author="eraters",
    author_email="ryangray1207@gmail.com",
    description="The Bots Of Discord Python Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bots-Of-Discord/BOD-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
