import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sklearn-nature-inspired-search-timzatko", # Replace with your own username
    version="0.0.1",
    author="Timotej Zatko",
    author_email="timi.zatko@gmail.com",
    description="Search using nature inspired algorithms over specified parameter values for an sklearn estimator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/timzatko/Sklearn-Nature-Inspired-Search",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
