from setuptools import setup, find_packages

# Read requirements from requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ai_printer",
    version="0.1",
    packages=find_packages(),
    install_requires=requirements,  # Uses the list from requirements.txt
    entry_points={
        'console_scripts': [
            'ai-printer=ai_printer.main:main',
        ],
    },
    author="aaajimypickle",
    description="A project for AI-assisted printing",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gimbo8000/ai_printer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
