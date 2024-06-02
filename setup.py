from setuptools import setup, find_packages

setup(
    name="fastapi-helmet",
    version="0.1.0",
    description="Security middleware for FastAPI applications",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Akhilesh Thykkat",
    author_email="akhileshthykkat843@gmail.com",
    url="https://github.com/AkhileshThykkat/fastapi-helmet",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "starlette",
        "pydantic",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
