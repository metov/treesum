from distutils.core import setup

setup(
    name="treesum",
    version="0.3.1",
    description="Utility and library for summarizing trees.",
    author="Azat Akhmetov",
    author_email="azatinfo@yandex.com",
    classifiers=["Development Status :: 3 - Alpha"],
    install_requires=[
        "docopt",
    ],
    entry_points={
        "console_scripts": ["treesum=treesum.cli:main"],
    },
)
