from setuptools import find_packages, setup

with open(
    "metaflow_dep_parsers/version.py", mode="r"
) as f:
    version = f.read().splitlines()[0]

setup(
    name="metaflow-dep-parsers",
    version=version,
    description="Dependency parsers for Metaflow (to be used with Config)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="Apache Software License",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    project_urls={
        "Source": "https://github.com/romain-intel/metaflow-dep-parsers",
        "Tracker": "https://github.com/romain-intel/metaflow-dep-parsers/issues",
    },
    author="Netflix Metaflow Developers",
    author_email="metaflow-dev@netflix.com",
    packages=find_packages(),
    py_modules=[
        "metaflow_dep_parsers",
    ],
    python_requires=">=3.7.2",
    install_requires=["metaflow>=2.13", "packaging>=23.0"],
)
