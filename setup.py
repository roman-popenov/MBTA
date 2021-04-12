""" The setup script. """

from setuptools import setup, find_packages

requirements = ['requests',
                'PyQt5',
                'PyQt5-stubs',
                'PyYAML',
                'iso8601']

setup_requirements = []

test_requirements = []

setup(name='MBTA',
      version='1.0',
      description='Application to query MBTA endpoint and get the predicted passages.',
      entry_points={
          'console_scripts': [
              'mbta_py=src/mbta_main_app:main',
          ],
      },
      author='Roman Popenov',
      author_email='popenov.r@gmail.com',
      packages=find_packages(include=['MBTA']),
      setup_requires=setup_requirements,
      test_suite='tests',
      tests_require=test_requirements,
      include_package_data=True,
      keywords='MBTA',
      install_requires=requirements,
      url='https://github.com/roman-popenov/MBTA',
      zip_safe=False
      )
