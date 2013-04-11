from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='hive',
      version=version,
      description="manmage hive table",
      long_description="""\
manage hive table""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='hive thrift',
      author='timger',
      author_email='yishenggudou@gmail.com',
      url='http://www.timger.info/about',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      data_files = [('/usr/local/etc/',['hive/hiveconf.yaml'])],
      scripts = ['scripts/hiveload.py'],
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
