import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lines-overlap-s528358",
    version="0.0.1",
    author="Ashish Jamuda",
    author_email="ashish.turbobit@gmail.com",
    description="lines overlap script",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ashishiit/Ashish_Jamuda_test/tree/master/Problem%20A",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)