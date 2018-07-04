# Xtend: Selected Aspects

In addition to the features sketched in the
["code generation with Xtend" section](xtext_code_generation_xtend.md)
this section provides some selected aspects we found useful for our work.


## Extension mechanism

Xtend has its name from the the fact that it allows to extend classes of
the language without using inheritance. There are different possibilities
to achieve this task. One simple example of such an extended class 
is java.lang.String, which was extended by Xtend to provide 
a method "toFirstUpper".

A simple possibility to achieve such an extension is to define a locally
visible method "__f(__TypeX x, __...)__" (see [Xtend documentation](references.md)).
With this, TypeX is extened by a method __f(...)__.

    :::xtend
	def printNTimes(String s, int n) {
		for(var i=0;i<n;i++) println(s)
	}

	...		
		"Hello".printNTimes(3)
	...

Other possibilities (see [Xtend documentation](references.md)) 
allow to use static methods in a similar way ("extension imports") which can
be imported by other modules: 
"import static extension package.Type.printNTimes".


## Dispatch methods

A method (used as extension of not) can be marked with the keyword 
"__dispatch__". If such a method is defined multiple times with different 
specialized types as argument, the correct version of the method if called
depending what object is passed (runtime polymorphy). The code behaves if
an "if obj instanceof TYPE" is called to determine which version has to be called.


## Misc
  * „==“ vs. „===“ (analog „!=“ vs. „!==“):
    * „==“ uses the method "equals" to determine the result.
    * „===“ checks if the identical object is referenced (like a pointer comparison).
  * It is posisble to check if an optional modell element is present or not
    by comparing it to null.
  * It is possible to check if a model element is not yet loaded
    (eIsProxy==true).


## EMF Parent Relationship (model mavigation)

Sometimes (while generating code or validating the model)
it is useful to navigate to the parent of a model object.
This can be done with the attribute "eContainer" of every model
element. It may be necessary to cast this parent to an appropriate type
(this can also happen via a dispatch method).
