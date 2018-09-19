# Basics of meta modeling for domain models

In this section we describe typical meta modeling tasks.
Meta modeling is the creation of a meta model.
This defines what can be modeled in a model for that given meta model.

All aspects identified here can be found in a tutorial style
in corresponding sections for TextX and Xtext of this documentation.


## Introductory example

An example: A meta model for a programming language defines that, e.g.,
variables can be defined. The model, in turn, is a concrete programm
with many variable definitions.


A meta model may, thus, be sketched as follows:

::uml:: format="svg" classes="uml MetaModelExample" alt="Meta Model Example"
class Program {
  name
}
class VariableDefinition {
  name
  value
}
Program *- "n" VariableDefinition
Model *- Program
::end-uml::


A program (domain model) may look as follows:

::uml:: format="svg" classes="uml MetaModelExample" alt="Meta Model Example"
object example_program {
}
object i {
  value=0
}
object j {
  value=-2
}
object k {
  value=10
}
object l {
  value=8
}
example_program *-- i
example_program *-- j
example_program *-- k
example_program *-- l
::end-uml::

## Overview: aspects of meta modeling

A summary of different aspects to be specified by the meta model is given
as follows. This list is inspired by the grammar based toolset
[Xtext](https://www.eclipse.org/Xtext/)
and [TextX](http://www.igordejanovic.net/textX/).

  * Which __domain objects__ exist (__glossary__)?
  * How are objects identified (__named__)?
  * Which __attributes__ do objects have?
  * What objects are __composed__ of other objects?
  * What objects __aggregates__ other objects?
  * How do objects __reference__ each other (including context effects/__scoping__)?
  * How can I __specialize__ objects?
  * How can I __connect__ objects?
  * __Modularization__: How can an object reference another object from another model
    (form the same meta model or a different one)?
  * __Interoperability__: How can an object reference something from outside
    the toolset scope (inter-tool operability)?
  * __Validation__: How can custom rules be checked automatically?


## Domain objects: identification and attributes

Domain objects represent a central part of a __glossary__. Thus,
defining such objects is a central part of any software specification
and must be using through its design.

__Domain objects__ can represent things, like "Customers", "Computers",
"State machines". In our context they can also represent activities
and relationships,  like "owns" (a customers owns a computer) or
"runs" (a computer runs a state machine).
Domain objects may have __attributes__, some of them optional. These attributes
may have a __scalar__ value or represent a __list__ of entries. The value of the
attributes can be specified to represent some __basic type__ (like a string or a
number) or __other domain__ objects.

Importantly, some domain objects need to be identified by a name (like a
"Customer"), while other objects do not (like the "Birthday" in our
example below).

::uml:: format="svg" classes="uml MetaModelExample" alt="Meta Model Example"
class Customer {
  name:string
  birthday:Birthday
}
class Birthday {
 date
}
::end-uml::

Note: Domain objects in the meta model represent a blueprint or a class of a
concrete instances of such objects in a concrete model.

See also:

   * Xtext: [xtext_a_first_grammar.md](xtext_a_first_grammar.md)
   * TextX: ::namedref::(textx_project_setup.md#textx_meta_model)


## Composing objects

Domain objects may be composed of other domain objects. Such a relationship
can be described by an attribute with a domain object type (like in the last
section). An alternative representation is illustrated as follows, but
describes exactly the same thing:

::uml:: format="svg" classes="uml MetaModelExample" alt="Meta Model Example"
class Customer {
  name:string
}
Customer *- Birthday
class Birthday {
 date
}
::end-uml::

Note: in this example, a Customer is composed of a Birthday object.
The Birthday object cannot exist without the Customer. This relationship
is called __composition__ and has clear __ownership__ semantics.

See also:

   * Xtext: [xtext_a_first_grammar.md](xtext_a_first_grammar.md)
   * TextX: ::namedref::(textx_project_setup.md#textx_meta_model)

## References and Aggregation

Some domain objects need to reference identifiable objects without
having their ownership. This happens, e.g.,
when describing domain object relationships within the model (e.g. a
Customer owns a Computer; relationship "own"). Such relationships themselves
can own additional attributes (e.g. "owns since date").

::uml:: format="svg" classes="uml MetaModelExample" alt="Meta Model Example"
class Customer {
  name:string
}
Customer o- Computer
class Computer {
  name:ip
}
(Customer,Computer) .. Owns
class Owns {
 since:date
}
::end-uml::

Note: non-owning knowlegde of other objects is called __aggregation__. Simple
relationships can be presented by a simple link (without attributes and without
own rule/class definition).

See also:

   * Xtext: [xtext_a_first_grammar.md](xtext_a_first_grammar.md)
   * TextX: ::namedref::(textx_project_setup.md#textx_meta_model)

## Scoping

Scoping is relevant to __describe what objects are identifiable__ when __referencing
other objects__. This is especially of importance, when some default visibility
is not valid (most default scoping mechanisms allow all identifiable objects to be
referenced globally).

Assume the following meta model snippet, where a "Scenario" is composed of
"Configurations" and a "Testcase" references "Scenarios" and "Configurations":

::uml:: format="svg" classes="uml MetaModelExample" alt="Meta Model Example"
class Scenario {
  name
}
class Configuration {
  name
}
class Testcase {
 name
}
Scenario *- "n" Configuration
Testcase o-- "1" Scenario
Testcase o-- "1" Configuration
::end-uml::

In this case, we want that __only "Configurations" of the "Scenario"
referenced by a "Testcase" are visible to the "Testcase"__. This
restriction is context specific (to the context of the "Testcase" described
by the referenced "Scenario"). Scoping mechanisms allow to define this scope.

See also:

   * Xtext: TODO
   * TextX: ::namedref::(textx_project_setup.md#textx_meta_model)

## Specialization (base classes/base rules)

Sometimes it happens that some domain object is too generic and needs to
be specialized. This may happen when the language evolves.
During the initial design commonalities are identified which lead to
the same pattern (base class and specialization).

::uml:: format="svg" classes="uml MetaModelExample" alt="Meta Model Example"
class Scenario {
  name
}
class Configuration {
  name
}
class GoodConfiguration {
  success_code
}
class BadConfiguration {
  error_code
}
Scenario *- Configuration
Configuration <|-- GoodConfiguration
Configuration <|-- BadConfiguration
::end-uml::

See also:

   * Xtext: TODO
   * TextX: TODO


## Modularization

This happens when a model is splitted  in multiple submodels
(e.g., different files).

::uml:: format="svg" classes="uml MetaModelExample" alt="Meta Model Example"
package scenarios.model <<Frame>> {
    object scenario_001 {
    }
    object config_A {
    }
    object config_B {
    }
}
package tests.model <<Frame>> {
    object test_T1 {
    }
}
scenario_001 *-- config_A
scenario_001 *-- config_B
test_T1 o- scenario_001
test_T1 o- config_B
::end-uml::

See also:

   * Xtext: TODO
   * TextX: TODO


## Combining meta models

To foster modularization, meta models can be splitted and still allow to
reference domain objects of one meta model from the other meta model. In our last example
we could define a meta model for "Testcases" and one meta model for
"Scenarios". This feature is more demanding to the underlying technology but
allows a __modularization of the meta model and, thus, the glossary__.

See also:

   * Xtext: TODO
   * TextX: TODO


## Interoperability with other toolsets or software components

In larger projects external databases or models may need to be referenced.
Such external sources of information may be, e.g., am existing database of
requirements, some JSON or XML file or similar things. Interoperability with
these sources of information allow to link the model to that source.

::uml:: format="svg" classes="uml MetaModelExample" alt="Meta Model Example"
package My-Meta-Model <<Cloud>> {
    class Testcase {
        name
    }
}
package "JSON-File definition" <<Cloud>> {
    class "JSON-File" {
        name
    }
    class Attribute {
        name
        value
    }
}
"JSON-File" *-- Attribute
Testcase o- Attribute
::end-uml::

##  <a name="validation"></a> Validation

The validation of a model consists of __additional checks on top of structural
consistency__ defined by the grammar and scoping.

  * Error in the structure
    result in classical syntax errors ("__expected__ 'XY' instead of 'AB'").
  * Scoping, in turn, defines the possible references in some context and,
    thus, yields errors of the catergory "referenced element 'XY' __not found__.".
  * The __validation__ described in this section is about additional
    __logical checks__, once the model is correctly parsed and all
    references resolved. This additional checks typically have a
    __strong relation to the domain__.

__Example:__ Assume a model where "testcases" reference "configurations of
scenarios" which have certain "aspects". On the other hand a "testcase" may
need certain aspects. If any of the "Aspects" required by a "testcase" is not
availabe in the referenced "configuration", a logical error is reported
(validation error).

__Rationale__ for choosing a validation over a scoping solution in this case:
When modeling a situation where a "configuration" is chosen by a "testcase"
without providing the correct "aspects", one would not like to get a
"configuration not found", which would result if only "configurations" with matching
"aspects" are defined in the __scope__ of a "testcase". In contrast, the
__validation__ will allow all "configurations" of the selected "scenario" of
a "testcase" to be visible, but some of them will produce a
__meaningful domain error__, such as
"configuration 'config_B' does not provide the aspect 'aspect_X' required
by testcase 'test_T1'".

The structure defined in the meta model is shown as follows:

::uml:: format="svg" classes="uml MetaModelExample" alt="Meta Model Example"
class Aspect {
  name
}
class Scenario {
  name
}
class Configuration {
  name
}
class Testcase {
 name
}
Scenario *- "n" Configuration
Testcase o-- "1" Scenario
Testcase o-- "1" Configuration
Configuration o-- "n" Aspect: haves
Testcase o-- "n" Aspect: needs
::end-uml::

A model with validation error (__"configuration 'config_B' does not provide the aspect 'aspect_X' required
by testcase 'test_T1'"__) is shown as follows:

    ::java
    scenario scenario_001 {
        configuration config_A has {aspect_X}
        configuration config_B has {aspect_Y}
    }
    testcase test_T1 {
        use scenario_001 with config_B
        and needs {aspect_X}
    }

::uml:: format="svg" classes="uml MetaModelExample" alt="Meta Model Example"
object scenario_001 {
}
object config_A {
}
object config_B {
}
object test_T1 {
}
object aspect_X {
}
object aspect_Y {
}

scenario_001 *-- config_A
scenario_001 *-- config_B
test_T1 o- scenario_001: use
test_T1 o-[bold,#red]- config_B: with
test_T1 o-[bold,#red]- aspect_X: needs
config_A o- aspect_X: haves
config_B o- aspect_Y: haves
config_B o-[bold,dashed,#red]- aspect_X : not part of haves
::end-uml::

A model without validation error is shown as follows:

    ::java
    scenario scenario_001 {
        configuration config_A has {aspect_X}
        configuration config_B has {aspect_Y, aspect_X}
    }
    testcase test_T1 {
        use scenario_001 with config_B
        and needs {aspect_X}
    }

::uml:: format="svg" classes="uml MetaModelExample" alt="Meta Model Example"
object scenario_001 {
}
object config_A {
}
object config_B {
}
object test_T1 {
}
object aspect_X {
}
object aspect_Y {
}

scenario_001 *-- config_A
scenario_001 *-- config_B
test_T1 o- scenario_001: use
test_T1 o-[bold,#green]- config_B: with
test_T1 o-[bold,#green]- aspect_X: needs
config_A o- aspect_X: haves
config_B o- aspect_Y: haves
config_B o-[bold,#green]- aspect_X : haves
::end-uml::

See also:

   * Xtext: ::namedref::(xtext_model_validation.md#xtext_validation)
   * TextX: ::namedref::(textx_project_setup.md#textx_validation)
