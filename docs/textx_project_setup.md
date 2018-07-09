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
(see [simple.py](examples/textx/simple/simple.py)), the code
is better structured into different modules 
with individual responsibilities into different files.

::shellcmd:: tree docs/examples/textx/simple_project|tail -n +2|head -n -2

We have chosen a distribution as follows:

 * setup.py is the standard python project configuration
 * simple_dsl contain all dsl related logic:
    * codegen.py: code generation.
    * metamodel.py: the meta model (grammar, scoping and validation config;
      the user classes are also stored herem but could be moved
      elsewhere for more complex projects.   
    * validation.py: validation logic.
    * console/*.py: console programs (configured in setup.py).
    * \_\_init\_\_.py represent module entry points.
  * tests contains unittests.

### File: metamodel.py

Here, we define the grammar. We allocate the scope providers to
individual elements, and register validation code.

::shellcmd-start:: 
echo "::python"
cat docs/examples/textx/simple_project/simple_dsl/metamodel.py
::shellcmd-end:: 

### File:: validation.py

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
