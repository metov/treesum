from distutils.core import setup
from pathlib import Path

setup(
    name="treesum",
    version="0.3.1.1",
    author="Azat Akhmetov",
    author_email="azatinfo@yandex.com",
    description="Utility and library for summarizing trees.",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/metov/treesum",
    classifiers=["Development Status :: 3 - Alpha"],
    install_requires=[
        "docopt",
    ],
    entry_points={
        "console_scripts": ["treesum=treesum.cli:main"],
    },
)
