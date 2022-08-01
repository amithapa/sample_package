"""Some edits"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='sample_package',
    version='0.0.1',
    author='Amit Thapa',
    author_email='amithapa26@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/amithapa/sample_package',
    project_urls = {
        "Bug Tracker": "https://github.com/mike-huls/toolbox/issues"
    },
    license='MIT',
    packages=['calc'],
    install_requires=['requests', 'fastapi'],
)
