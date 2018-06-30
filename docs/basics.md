# Basics of meta modeling for domain models

In this section we describe typical meta modeling tasks.
Meta modeling is the creation of a meta model.
This defines what can be modeled in a model for that given meta model.

## Introductory example

An Example: A meta model for a programming language defines that, e.g.,
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
and [textX](http://www.igordejanovic.net/textX/).

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

Note: Domain objects in the meta-model represent a blueprint or a class of a
concrete instances of such objects in a concrete model.

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

## Scoping

Scoping is relevant to __describe what objects are identifiable__ when __referencing
other objects__. This is especially of importance, when some default visibility
is not valid (most default scoping mechanisms allow all identifiable objects to be
referenced globally).

Assume the following meta-model snippet, where a "Scenario" is composed of
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

## Combining meta models

To foster modularization, meta models can be splitted and still allow to
reference domain objects from one meta model to the other. In our last example
we could define a meta model for "Testcases" and one meta-model for
"Scenarios". This feature is more demanding to the underlying technology but
allows a __modularization of the meta-model and, thus, the glossary__.

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

## Validation

TODO