from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys

from meta import __version__, __title__, __license__, __author__


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--flakes', '--pep8', '--cov', 'ics', 'tests/test.py', 'ics/']
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name=__title__,
      version=__version__,
      description='Python icalendar (rfc5545) parser',
      long_description=readme(),
      keywords='ics icalendar calendar event todo rfc5545 parser pythonic',
      classifiers=[
                  'Development Status :: 4 - Beta',
                  'Topic :: Software Development :: Libraries',
                  'Topic :: Software Development :: Libraries :: Python Modules',
                  'Intended Audience :: Developers',
                  'Topic :: Office/Business :: Scheduling',
                  'License :: OSI Approved :: Apache Software License',
                  'Programming Language :: Python',
                  'Programming Language :: Python :: 2',
                  'Programming Language :: Python :: 2.7',
                  'Programming Language :: Python :: 3',
                  'Programming Language :: Python :: 3.3',
      ],
      url='http://github.com/C4ptainCrunch/ics.py',
      author=__author__,
      author_email='nikita.marchant@gmail.com',
      install_requires=[
          "python-dateutil",
          "arrow",
          "six",
      ],
      license=__license__,
      packages=['ics'],
      include_package_data=True,
      cmdclass={'test': PyTest},
      tests_require=['pytest', 'pytest-cov', 'pytest-flakes', 'pytest-pep8'],
      zip_safe=False
      )
