from setuptools import setup
setup(name='some-name',

entry_points = {
                   'console_scripts': [
                       'command-name = package.module:main_func_name',
                   ],
               },
)