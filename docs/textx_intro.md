# TextX Intro

TextX is a Python library to allow an easy creation of
DSL validators and artifact generators:

  * Reading model files (**grammar based parsing**, reference resolution and post processing).
  * **Validating the model**.
  * **Generating output artifacts** (e.g., code).
  
A fundamental difference to Xtext is that the
meta model classes (describing the model elements)
are dynamically generated instead of generating code
from them. Thus, a grammar in TextX in interpreted dynamically 
and not compiled.

TextX has only few dependencies and very compact 
projects can be created. Details see
::namedref::(references.md#dejanovic2017)
and the "TextX project page", see ::namedref::(references.md#textx).
TextX itself is permanently tested with different python versions.

Normally, a similar modularization as for Xtext projects 
is employed to separate different responsibilities across
software modules (e.g. modules for the 
**grammar**, **validation**, and **code generation**). 
However, it is possible to put an entire project
including grammar and the validation into one file:
the following code illustrates a meta model with an example model
which is validated (similar to the example in the 
[introductory example of validation](basics.md#validation)).

::uml:: format="svg" classes="uml MetaModelExample" alt="Meta Model Example"
class Aspect {
  name
}
class Scenario {
  name
}
class Config {
  name
}
class Testcase {
 name
}
Scenario *- "n" Config
Testcase o-- "1" Scenario
Testcase o-- "1" Config
Config o-- "n" Aspect: haves
Testcase o-- "n" Aspect: needs
::end-uml::

::shellcmd-start:: 
echo "::python"
cat docs/examples/textx/simple/simple.py
::shellcmd-end:: 

![model.dot](images/textx_simple_model_dot.svg "model.dot")

