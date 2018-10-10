# TextX: Model Modularization

Similar to [xtext_modularization.md](xtext_modularization.md), we 
show how to achive model modularization across files in TextX.

## Modularization within the same Meta Model

Ready to use scope providers exists to handle multiple files. See the
::namedref::(references.md#textx) documentation for details.

## Referencing Model Elements form other Meta Models

If you wish to reference model elements from other metamodels, this can be 
achieved using the multi meta model support of TextX 
(see ::namedref::(references.md#textx)).

The following example is self contained and shows how to deploy two
python packages for two DSLs, one referencing the other.

 * **mydsl**: a simple "Hello World" language
 * **mydsl1**: a language referencing Greetings from the mydsl language.

------------------------

### mydsl - a simple model of "Greetings"

#### File layout
::shellcmd:: tree docs/examples/textx/modularization/mydsl |tail -n +2|head -n -2

### Grammar MyDsl.tx
The grammar defines the structure...

::shellcmd-start:: 
echo "::antlr"
cat docs/examples/textx/modularization/mydsl/mydsl/MyDsl.tx
::shellcmd-end:: 

### metamodel.py
The metamodel is created based on the grammar...

::shellcmd-start:: 
echo "::python"
cat docs/examples/textx/modularization/mydsl/mydsl/metamodel.py
::shellcmd-end:: 

### \_\_init\_\_.py
The entry point for the DSL "compiler" (it just outputs some model data)...

::shellcmd-start:: 
echo "::python"
cat docs/examples/textx/modularization/mydsl/mydsl/__init__.py
::shellcmd-end:: 

### setup.py
The installer configuration (see 
[textx_project_setupx.md](textx_project_setup.md) for more details).

::shellcmd-start:: 
echo "::python"
echo "..."
grep "name=" docs/examples/textx/modularization/mydsl/setup.py
echo "..."
grep "entry_points=" -A4 docs/examples/textx/modularization/mydsl/setup.py
echo "..."
::shellcmd-end:: 

### Create installer

Create an installer to help pip find its dependencies:

    ::bash
    python setup.py  sdist

------------------------

### mydsl1 - a model referencing the "Greetings" from mydsl

#### File layout
::shellcmd:: tree docs/examples/textx/modularization/mydsl1 |tail -n +2|head -n -2

### Grammar MyDsl1.tx
Note: we use the grammar rule "Greeting" from "mydsl". See metamodel.py how
this is resolved ("refrenced_metamodels").

::shellcmd-start:: 
echo "::antlr"
cat docs/examples/textx/modularization/mydsl1/mydsl1/MyDsl1.tx
::shellcmd-end:: 

### metamodel.py
The metamodel is created based on the grammar, the metamodel to be
referenced and some scope providers (to allow to "import" other model
files)...

::shellcmd-start:: 
echo "::python"
cat docs/examples/textx/modularization/mydsl1/mydsl1/metamodel.py
::shellcmd-end:: 

### \_\_init\_\_.py
The entry point for the DSL "compiler" (it just outputs some model data)...

::shellcmd-start:: 
echo "::python"
cat docs/examples/textx/modularization/mydsl1/mydsl1/__init__.py
::shellcmd-end:: 

### setup.py
The installer configuration (see 
[textx_project_setupx.md](textx_project_setup.md) for more details).
The language "mydsl1" depends on "mydsl".

::shellcmd-start:: 
echo "::python"
echo "..."
grep "name=" docs/examples/textx/modularization/mydsl1/setup.py
echo "..."
grep "install_requires=" docs/examples/textx/modularization/mydsl1/setup.py
echo "..."
grep "entry_points=" -A4 docs/examples/textx/modularization/mydsl1/setup.py
echo "..."
::shellcmd-end:: 

------------------------

## Usage

### Install both DSLs and compilers

The option "find-links" is used to point to the local version of 
mydsl (created above; setup.py of "mydsl1" includes this dependency):

    ::bash
    pip3 install . --find-links=file:///$(pwd)/../mydsl/dist

### Model file data.mydsl
::shellcmd-start:: 
echo "::java"
cat docs/examples/textx/modularization/model/data.mydsl
::shellcmd-end:: 

### Model file data.mydsl1
::shellcmd-start:: 
echo "::java"
cat docs/examples/textx/modularization/model/data.mydsl1
::shellcmd-end:: 

### Model file error.mydsl1
::shellcmd-start:: 
echo "::java"
cat docs/examples/textx/modularization/model/error.mydsl1
::shellcmd-end:: 

### Example using mydslc and mydsl1c
    
    ::bash
    $ mydslc model/data.mydsl
     - hello for 'Pi'
     - hello for 'Tim'
    $ mydsl1c model/data.mydsl1
     - hello for referenced 'Pi'
     - hello for referenced 'Tim'
    $ mydsl1c model/error.mydsl1
    ...
    textx.exceptions.TextXSemanticError: model/error.mydsl1:2:11: 
    error: Unknown object "NoName" of class "Greeting"
