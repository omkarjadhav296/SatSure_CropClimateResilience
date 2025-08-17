from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


version = "0.1.0"

REPO_NAME = "SatSure_CropClimateResilience"
AUTHOR_USERNAME = "omkarjadhav296"
SRC_REPO = "CropClimateResilience"
AUTHOR_EMAIL = "omkarjadhav296@gmail.com"


setup(
    name=SRC_REPO,
    version=version,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for CropClimateResilience",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https//github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https//github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
)