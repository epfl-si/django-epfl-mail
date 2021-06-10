# (c) ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, DSI, 2021.

import io

import setuptools

long_description = io.open("README.md", encoding="utf-8").read()
version = __import__("django_epflmail").__version__
source_url = "https://github.com/epfl-si/django-epfl-mail"

setuptools.setup(
    name="django-epfl-mail",
    version=version,
    url=source_url,
    author="William Belle",
    author_email="william.belle@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=[],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    zip_safe=False,
    project_urls={
        "Changelog": source_url + "/blob/main/CHANGELOG.md",
        "Source": source_url,
        "Tracker": source_url + "/issues",
    },
    classifiers=[],
)
