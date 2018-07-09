from setuptools import setup,find_packages

setup(name='simple_dsl',
      version='0.1',
      description='a simple model validator and artifact compiler',
      url='',
      author='YOUR NAME',
      author_email='YOUR.NAME@ADDRESS',
      license='TODO',
      packages=find_packages(),
      package_data={'': ['*.tx', '*.template', 'support_*_code/**/*']},
      install_requires=["textx","arpeggio"],
      tests_require=[
          'pytest',
      ],
      keywords="parser meta-language meta-model language DSL",
      entry_points={
          'console_scripts': [
              'simple_dsl_validate=simple_dsl.console.validate:validate',
          ]
      },
      )


# to play around without installing: do "export PYTHONPATH=."