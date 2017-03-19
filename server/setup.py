from setuptools import setup

setup(name='Proboty',
      version='0.1.0',
      author='Mikael Larsson',
      packages=['proboty'],
      test_suite='proboty.tests',
      entry_points={
          'console_scripts': [
              'proboty = proboty.__main__:main'
          ]
      },
)
