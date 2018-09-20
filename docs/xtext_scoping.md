# Xtext Scoping

## Goal

In this seciton you will learn thw following:
 * What scoping means and where you need it.
 * How to customize scoping for special lookups of local elements.
 * How to select scope providers to handle multifile lookups.
 
## Scoping: What is it and where do I need it?

Scoping is always relevant, when a reference 
(e.g., "Thing: ref=[OtherThing]") is resolved after 
parsing the model text. 

These references can be resolved in order to idnetify an object 
globally (e.g., by name) or with respect to other model data: e.g.:
"Call: object=[Object] '.' method=[Method];"

## Scoping: Global identification of elements

When you identify an element by name (in order to reference it) you use
the default scope provider of Xtext. It resembles the Java scope (based on
packages separated by dots).

### Problem
In order to make use of the full qualified name of an elements the default
format of references is not enough to formulate the name (because dots are not
part of this default format):

    ::antlr
    Model: packages+=P*;
    P: 'package' name=ID '{' (a+=A | b+=B)* '}';
    A: 'a' name=ID;
    B: 'b' ref=[A] // same as "ref=[A|ID]";

With this grammar the default format "ID" is used to reference A objects
in B objects.

The following will work because all elements are in the same hierachical
element (Package):

    package p1 {
        a a1
        a a2
        b a1
        b a2
    }

The following will not work

    package p1 {
        a a1
    }
    package p2 {
        a a2
        b a1 // will not work (a1 is located in p1) 
        b a2
    }

### Solution

    ::antlr
    Model: packages+=P*;
    P: 'package' name=ID '{' (a+=A | b+=B)* '}';
    A: 'a' name=ID;
    B: 'b' ref=[A|FQN];
    FQN hidden(): ID('.' ID)*;

Here we allow the format of the reference to be a dot-separated name.
*The optional "hidden()" controls which tokens are ignored (hidden). Hidden
tokens are, e.g., whitespaces and comments by default. 
With "hidden()" no such tokens are ignored, thus, not allowing, e.g.,
whitespaces between the dot separated parts of a name.*
With this the default scope provide works as follows:

The following will not work

    package p1 {
        a a1
    }
    package p2 {
        a a2
        b p1.a1  
        b a2
    }

## Customize lookup of local elements

## Select scope providers