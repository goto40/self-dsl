# Xtext Project Setup

## Create a new Xtext Project

Follow section "Create A New Xtext Project"
in ::namedref::(references.md#xtext15min).

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

 * "+=" denotes the owner relationship of one Model containing many Greetings.
 * "name=ID" defines an attribute "name" of the Rule "Greeting".
 * The attribute name has a special meaning by default, to denote the 
    identifier of the Rule.
 * ID defines an indentifier (a string; see org.eclipse.xtext.common.Terminals)

Note: Use "Team -> Git -> Project for "Automatically ignore derived resources"
to add an appropriate .gitignore file to your project (when using git).

## Compile and Run the Project

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

