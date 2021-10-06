"""
FileName: setup.py
Author: Fatpandac
Create: 2021/10/07
Description: Setup mkpng.
"""

from setuptools import setup, find_packages

setup(name='mkpng',
      version='0.0.1',
      description='A CLI tool for creating pure color images.',
      author='Fatpandac',
      author_email='tingfeizheng@gmail.com',
      license='MIT',
      py_modules=['mkpng'],
      packages=find_packages(),
      install_requires=[
        'Click',
      ],
      entry_points = """
        [console_scripts]
        mkpng = mkpng:main
      """
      )
