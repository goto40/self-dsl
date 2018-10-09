from setuptools import setup,find_packages

setup(name='stduent_dsl',
      version='0.1',
      description='a simple model to manage student data',
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
              'mydslc=mydsl:myydslc',
          ]
      },
      )


# to play around without installing: do "export PYTHONPATH=."
