from setuptools import setup, find_packages
import sys, os

version = '-'

setup(name='jemt',
      version=version,
      description="For the python course",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='AJ',
      author_email='anders.jemt@scilifelab.se',
      url='-',
      license='-',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
