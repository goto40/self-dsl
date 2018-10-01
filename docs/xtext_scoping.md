# Xtext Scoping

In this seciton you will learn thw following:

 * What scoping means and where you need it.
 * How to customize scoping for special lookups of local elements.
 * How to select scope providers to handle multifile lookups.
 
## Scoping: What is it and where do I need it?

Scoping is always relevant, when a reference 
(e.g., "Thing: ref=[OtherThing]") is resolved after 
parsing the model text. Details see [basics.md](basics.md).


## Scoping: Global identification of elements

When you identify an element by name (in order to reference it) you use
the default scope provider of Xtext. It resembles the Java scope (based on
packages separated by dots).

### Problem

In order to make use of the full qualified name of an elements the default
format of references is not enough to formulate the name (because dots are not
part of this default format):

    ::antlr
    Model: packages+=Pack*;
    Pack: 'package' name=ID '{' (defs+=Def | calls+=Call)* '}';
    Def: 'def' name=ID;
    Call: 'call' ref=[Def]; // same as "ref=[Def|ID]"

With this grammar the default format "ID" is used to reference A objects
in B objects.

The following will work because all elements are in the same hierachical
element (Package):

    package p1 {
        def a1
        def a2
        call a1
        call a2
    }

The following will not work

    package p1 {
        def a1
    }
    package p2 {
        def a2
        call a1 // will not work (a1 is located in p1) 
        call a2
    }

### Solution

    ::antlr
    Model: packages+=Pack*;
    Pack: 'package' name=ID '{' (defs+=Def | calls+=Call)* '}';
    Def: 'def' name=ID;
    Call: 'call' ref=[Def|FQN];
    FQN hidden(): ID('.' ID)*;

Here we allow the format of the reference to be a dot-separated name.

**Note**: The optional "hidden()" controls which tokens are ignored (hidden). 
Hidden tokens are, e.g., whitespaces and comments by default. 
With "hidden()" no such tokens are ignored, thus, not allowing, e.g.,
whitespaces between the dot separated parts of a name.*

With this, the default scope provider allows models as in the following example:

    package p1 {
        def a1
    }
    package p2 {
        def a2
        call p1.a1  
        call a2
    }

## Models distributed across multiple files

When distributing the model across different file, you can control
how model elements are allowed to reference other model elements in 
different model files.

### DefaultGlobalScopeProvider "make everything visible"

The default scope provider allows referencing any model element in the 
available resources. In case of an eclipse project with model files,
those resources consist all model files in the current project. Thus,
you can reference any model element without any import or include statement.

For example, elements from p1.mydsl:

    package p1 {
        def a1
    }

may be referenced by elements in p2.mydsl:

    package p2 {
        call p1.a1  
    }

**Note:** When creating a standalone compiler for your DSL, you do not
have such thing as a workspace. In this case, you can manually provide
this information, as illustrated in 
[xtext_deploy_command_line.md](xtext_deploy_command_line.md).

### ImportUriGlobalScopeProvider "#include &lt;other&gt;"

You can easily change the visiblity to provide a language with explicit import
statements; see e.g. ::namedref::(references.md#mooji2017b).

These steps sum up as follows for a simple default project:

  * Add the "ImportUriValidator" in your mwe2-file (side-by-side to your grammar).

        ...
        validator = {
            // composedCheck = "org.eclipse.xtext.validation.NamesAreUniqueValidator"
            composedCheck = "org.eclipse.xtext.validation.ImportUriValidator"
        }
        ...

  * Modify your grammar to include an import statement with a special 
    "importURI"-field.

        ::antlr
        Model: imports+=Import* packages+=Pack*;
        Import: "import" importURI=STRING
        ...

  * add the following to your *RuntimeModule (located side-by-side to your
      grammar)
    
        ::xtend
        override bindIGlobalScopeProvider() {
            ImportUriGlobalScopeProvider
        }
        
With this addition, the example above needs to be changed in file p2.mydsl:

    import "p1.mydsl"
    
    package p2 {
        call p1.a1
    }

## Customize lookup of local elements

The following example illustrates a 
simple object oriented language, where you can define classes, 
create instances, and call methods of classes associated to that instances.

    package p1 {
        class C1 {
            def a1
            def b1
        }
        instance i1: C1
        call i1->a1
        call i1->b1
    }

When model references point to relative model element locations, you need a 
custom scope provider for that reference. The reference to "a1" in "i1->a1"
cannot be resolved by the default scope provider, because the semantics of
the call are not defined by the grammar.

In the example shown, "i1->a1"
points to "a1", which can be resolved by following the reference to the
definition of "i1", and then following there the reference to "C1", which
contains the desired definition of "a1".

    ::antlr
    Model: imports+=Import* packages+=Pack*;
    Pack: 'package' name=ID '{' 
        (class+=Class | instances+=Instance | calls+=Call)* 
        '}';
    Class: 'class' name=ID "{" defs+=Def* "}";
    Def: 'def' name=ID;
    Instance: 'instance' name=ID ':' type=[Class|FQN];
    Call: 'call' instance=[Instance|FQN] '->' ref=[Def];
    FQN hidden(): ID('.' ID)*;
    Import: "import" importURI=STRING; 

![example image](images/model_class_instance_and_calls.png)

To resolve the reference of the "call", you need to specify a custom scope
provider in "scoping/MyDslScopeProvider.xtend", side-by-side to your grammar:

 * You get the "object" (in our case the "call"-object) and a "reference"
   identifying the part of grammar representing the reference to be resolved 
   (in our case the attribute "ref" of the "Call").
 * Using "object" and "reference" you can decide where to handle scoping
   here, or delegating scoping to the default implementation 
   "return super.getScope(...)".
 * Based on the object you can implement your scoping logic defining
    what objects are visible (e.g. all "Def"-objects in 
    "call.instance.type.defs"). Use Scopes.scopeFor(...) to return your
    selection.
 * When you decide that no elements are visible, return "IScope.NULLSCOPE".


        ::xtend
        class MyDslScopeProvider extends AbstractMyDslScopeProvider {
            override getScope(EObject object, EReference ref) {
                if (ref == MyDslPackage.Literals.CALL__REF) {
                    val call = object as Call
                    return Scopes.scopeFor(call.instance.type.defs) 
                }
                return super.getScope(object, ref)
            }	
        }
