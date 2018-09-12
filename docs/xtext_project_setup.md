# Xtext Project Setup

## Create a new Xtext Project

Follow section "Create A New Xtext Project"
in ::namedref::(references.md#xtext15min).

In addition to the information from the tutorial we
suggest the following details for the other examples
discussed on this site:
![model.dot](images/xtext_new_project2.png "xtext_new_project2.png")


The example grammar (automatically created after project
initialization) defines a "Model" consisting of 
"Greetings" is shown in the following. A "Model" contains "Greetings".
Every "Greeting" consists of the Text 'Hello' and a name followed by '!'
(details below).

    ::antlr
    grammar org.example.domainmodel.Domainmodel with
                                      org.eclipse.xtext.common.Terminals
    generate domainmodel "http://www.example.org/domainmodel/Domainmodel"

    Model:
        greetings+=Greeting*;
      
    Greeting:
        'Hello' name=ID '!';


::uml:: format="svg" classes="uml GreetingMetaModel" alt="Greeting Meta Model"
class Model {
}
class Greeting {
  name
}
Model *- "n" Greeting
::end-uml::

Notes:

 * "+=" denotes the owner relationship of one Model containing many Greetings 
    (__composition__).
 * "name=ID" defines an attribute "name" of the Rule "Greeting" (allowing to 
    define model elements of the type "Greeting"; __attributes__ of 
    __model elements__).
 * The attribute name has a special meaning by default, to denote the 
    identifier of the Rule (__identification of model elements__).
 * ID is a terminal (like INT, STRING, etc.; see grammar, and click "F3" on
      "org.eclipse.xtext.common.Terminals" to see definition).
   "name=ID" means that the attribute "name" is parsed as "ID" (which in turn
   is - more or less - an alphanumerical word staring with no number)

TODO Note: Use "Team -> Git -> Project for "Automatically ignore derived resources"
to add an appropriate .gitignore file to your project (when using git).

## ::namedref::{xtext_compile_and_run:Compile and Run the Project}

Without modifing the grammar (or anything else), follow the steps in
section "Generate Language Artifacts" in 
::namedref::(references.md#xtext15min).

After this, you can use explore the editor and enter a model according to 
the example meta model grammar provided by the Xtext project setup. 

Now you can play with your new language (type CTRL-Space to get auto
completion). Enter the following example:

    ::raw
    Hello Pierre!
    Hello Tim!
    Hello Markus!

## Build meta model using maven

When maven is selected as build tool, you can also use maven (instead of
eclipse) to build your project on the command line: Go to the "parent" 
project and run "mvn package".

Maven will download all required packages in "~/.m2" (locally) and then build 
your subprojects. The output is located in the folder "target" of each 
subproject.

See also: ::namedref::(references.md#maven).

