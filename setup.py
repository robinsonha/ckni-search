from setuptools import setup, find_packages

setup(
    name="ckni-search",
    version="0.1.0",
    description="Search CNKI for English drugs translated to Chinese across major pathways",
    author="Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "googletrans==4.0.0-rc1",
        "pandas"
    ],
    entry_points={
        "console_scripts": [
            "ckni-search=ckni_search.main:main"
        ]
    },
    python_requires=">=3.8"
)
