from setuptools import setup,find_packages

setup(name='mydsl1',
      version='0.1',
      description='another simple dsl',
      url='',
      author='YOUR NAME',
      author_email='YOUR.NAME@ADDRESS',
      license='TODO',
      packages=find_packages(),
      package_data={'': ['*.tx', '*.template', 'support_*_code/**/*']},
      install_requires=["textx","arpeggio","mydsl"],
      tests_require=[
          'pytest',
      ],
      keywords="parser meta-language meta-model language DSL",
      entry_points={
          'console_scripts': [
              'mydsl1c=mydsl1:mydsl1c',
          ]
      },
      )


# to play around without installing: do "export PYTHONPATH=."
