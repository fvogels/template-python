# https://docs.python.org/3/distutils/setupscript.html

from setuptools import setup


def fetch_version():
      '''
      Fetches version variable from version.py
      '''
      version = {}

      with open('TODO/version.py') as f:
            exec(f.read(), version)

      return version['__version__']



setup(name='TODO',
      version=fetch_version(),
      description='TODO',
      url='TODO', # Git URL
      author='Frederic Vogels',
      author_email='frederic.vogels@ucll.be',
      license='MIT',
      packages=['TODO'], # List of packages
      entry_points = {
            'console_scripts': [
                  # Example 'command=package.module:function',
            ]
      },
      test_suite='nose.collector',
      tests_require=[ 'nose' ],
      zip_safe=False)
