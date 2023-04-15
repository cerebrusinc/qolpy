import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="qol",
    version="0.1.0",
    description="A suite of random but useful functions that are aimed at giving you 'piece of cake' level comfortability",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lewisjr/py-qol.git",
    project_urls={
        "Bug Tracker": "https://github.com/lewisjr/py-qol/issues",
    },
    author = "Cerebrus Inc | Lewis Mosho Jr",
    author_email = "lewis@cerebrus.dev",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "Typing :: Typed"
    ],
    packages=["qol", "qol.colour", "qol.date", "qol.number", "qol.string"],
    include_package_data=True,
    install_requires=["typing"],
    package_dir={"": "qol"},
    python_requires=">=3.0",
)