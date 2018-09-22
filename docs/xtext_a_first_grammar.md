# A First Grammar

Here we highlight some information when walking through
::namedref::(references.md#xtext15min).

## Goal

In this section you will learn

 * How to model hierarchical data structures (things containing things).
 * How to model references (things referencing things).
 * How to identify model elements (by name). 
 * How to model specialization.

Note: How to identify model elements in other hierarchical elements
(e.g. packages) will be handled later.

## Step 1: Create and run an Xtext project

Take your time for this tutorial now and continue reading afterwards.
You may __stop before "Second Iteration"__ where "packages"
are added to the model.

## Step 2: Questions

Check if you understood thw following points:

 * What is the role of the __start rule__ of a grammar in a meta model?
 * What is the meaning of "Type: DataType | Entity;" in terms of inheritance? 
    Explore the generated Java Interfaces for the classes Type, DataType, 
    Entity in  src-gen/org/example/domainmodel/domainmodel in your main 
    project.
 * How do you typically add keywords to your language (like "entity")?
 * What is the difference between "x=Rule1" and "x=[Rule1]"?
 * How can you model the following?
    * "a _named_ __University__ aggregates _named_ __Students__".
    * "a __House__ is composed of __Rooms__" 
        ::namedref::{xtext_Composition:Composition}.
 * Explain the role of "?" in the following examples: 
    * (x=INT)?
    * enabled?='enabled'
    
    
Note:

 * Optional attributes can be defined using "?". Note: some types, like 
   references, are null if not set. Others have default values (like an empty
   String for STRING, "0" for INT or the first enum value defined for enums).
 * Rules without attributes doe not yield an object 
   (e.g.: "Thing: INT"). You can force the object creation with the
   following syntax using curly brackets: "Thing: {Thing} INT".

## Step 3: More examples

Can you interpret the following snippet:


    ::antlr
    // ...
    Model: customers+=Customer* computers+=Computer* owns+=Owns*;
    Computer: 'computer' name=ID;
    Customer: 'customer' name=ID;
    Own: 'the' computer=[Computer] 
         'is' 'owned' 'by' customer=[Customer] 
         'since' date=STRING;

What changes, when we define the 'Model' differently:


    ::antlr
    Model: (customers+=Customer computers+=Computer owns+=Owns)*;

## Step 4: Editor

In addition to the text editor,
you can also edit the model with a __tree editor__:
open wthe file with "Open With..." - "Sample Ecore Model Editor".

When editing the model graph, the model text is changed accordingly: 
see the Xtext ["Formatter"](https://blogs.itemis.com/en/tabular-formatting-with-the-new-formatter-api) 
in the online help of Xtext (in the internet or within eclipse): 



## Step 5: Visualize the meta model

The __ecore model__  deduced from the grammar can be __visualized__:
see ::namedref::(references.md#mooji2017a),
section "Optional: Ecore diagram" („Initialize Ecore Diagram ...“).

Moreover a __syntax tree__ can be rendered from the grammar:
see ::namedref::(references.md#mooji2017a),
section "Optional: View Diagram of Xtext Grammar"
(Window/Show View/Other.../Xtext/Xtext Syntax Graph).

## Optional Step 6: Adapt you unittests

Adapt your unittests.
