import os
from setuptools import setup, find_packages
import glob

src_dir = os.path.dirname(__file__)


def read(filename):
    full_path = os.path.join(src_dir, filename)
    with open(full_path) as fd:
        return fd.read()


if __name__ == '__main__':
    setup(
        name='random_name',
        version='0.1.0',
        author='Michael Barrett',
        author_email='loki77@gmail.com',
        license="New BSD license",
        url="https://github.com/phobologic/random_name",
        description='Simple tool for generating random names.',
        classifiers=[
            "Intended Audience :: Developers",
            "Natural Language :: English",
            "Programming Language :: Python :: 2",
            "License :: OSI Approved :: BSD License",
            "Development Status :: 3 - Alpha"],
        packages=find_packages(),
        scripts=glob.glob(os.path.join(src_dir, 'scripts', '*')),
    )
