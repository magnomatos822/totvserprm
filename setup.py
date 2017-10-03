# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='totvserprm',
      version='1.0.2',
      description='API para webservices do TOTVS ERP RM.',
      url='http://github.com/grupoandrademartins/totvserprm',
      author='grupoandrademartins',
      author_email='staff@sismart.com.br',
      license='MIT',
      packages=['totvserprm'],
      install_requires=[
          'dicttoxml',
          'lxml',
          'requests',
          'zeep'
      ],
      zip_safe=False)