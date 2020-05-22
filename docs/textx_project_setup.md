# TextX Project Setup

We give a guide to create a simple
command line tool to load and validate a
model and to generate some artifact.

In this example, we propose different models for
the __meta model structure__ (grammar), the __scoping__,
and the __ artifact generation__. Moreover, a 
__main__ and a __setup__ script are added to control
the software.

For this example we use Python 3. You need to install 

  * TextX (see [references](references.md)).
  * Arpeggio (see TextX in [references](references.md))
  * pytest (for unittests)

Using pip you can:

    ::shell
    pip3 install --upgrade textx arpeggio pytest

## File structure

Although everything can be packed within one file
(see ["TextX Intro"](textx_intro.md)), the code
is better structured into different modules 
with individual responsibilities into different files.

::shellcmd:: tree docs/examples/textx/simple_project|tail -n +2|head -n -2

We have chosen a distribution as follows:

 * setup.py is the standard python project configuration
 * simple_dsl contain all dsl related logic:
    * codegen.py: code generation.
    * metamodel.py: the meta model (grammar, scoping and validation config;
      the user classes are also stored here but could be moved
      elsewhere for more complex projects.   
    * validation.py: validation logic.
    * console/*.py: console programs (configured in setup.py).
    * \_\_init\_\_.py represent module entry points.
  * tests contains unittests.

### File: ::namedref::{textx_meta_model:metamodel.py}

Here, we define the grammar. We allocate the scope providers to
individual elements, and register validation code.

::shellcmd-start:: 
echo "::python"
cat docs/examples/textx/simple_project/simple_dsl/metamodel.py
::shellcmd-end:: 

### File: ::namedref::{textx_validation:validation.py}

This file contains validation functions registered in the meta model.

::shellcmd-start:: 
echo "::python"
cat docs/examples/textx/simple_project/simple_dsl/validation.py
::shellcmd-end:: 

### File: tests/test_validation.py

This file is a unittest using the metamodel 
(exposed via \_\_init\_\_.py) and checks the
correct functionality of the validation code.

::shellcmd-start:: 
echo "::python"
cat docs/examples/textx/simple_project/tests/test_validation.py
::shellcmd-end:: 

The two model files used in this tests are shown in the following 
subsections.

#### Model: tests/models/model_ok.dsl

::shellcmd-start:: 
echo "::java"
cat docs/examples/textx/simple_project/tests/models/model_not_ok.dsl
::shellcmd-end:: 

#### Model: tests/models/model_not_ok.dsl

::shellcmd-start:: 
echo "::java"
cat docs/examples/textx/simple_project/tests/models/model_ok.dsl
::shellcmd-end:: 

## Edit, Run and Test

Use an appropriate IDE (e.g., PyCharm) to run the tests and, thus, test and debug your 
new language.

## Install/Uninstall the Language

After all tests passed you can try to install your language.
Do not forget to adapt setup.py:

::shellcmd-start:: 
echo "::python"
cat docs/examples/textx/simple_project/setup.py
::shellcmd-end:: 

The registered console command (validate.py) contains:

::shellcmd-start:: 
echo "::python"
cat docs/examples/textx/simple_project/simple_dsl/console/validate.py
::shellcmd-end:: 

### Installation
__Install__ the software __permanently for all users__ (change directory
to the folder with the setup.py file):

    ::shell
    sudo -H pip3 install --upgrade .

You can now start the new commands defined in the setup.py: 

    ::shell
    simple_dsl_validate --help

### Uninstallation
__Uninstall__ the software:

    ::shell
    sudo -H pip3 uninstall simple_dsl


