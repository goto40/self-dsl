# Code Generation (with Xtend)

Xtend is highly optimized to be used
for code generation. It has a optimzed template engine (e.g., with
automatic indentation support) and
is fully integrated in the Eclipse IDE (auto completition
for model data).

## Simple Example

Open the *Generator.xtend file in your project, e.g.,
kurs.xtext.dataflow.generator.DataFlowDslGenerator.xtend. 
Here, you can implement your first code generator:
You have model access (parameter "resource") and file system access
(parameter "fsa").

    ::xtend
	override void doGenerate(Resource resource, IFileSystemAccess2 fsa, 
			IGeneratorContext context) {
		// -------------------------------------------
		// Option 1:
		var txt = ""
		for (obj: resource.allContents.toIterable) {
			if (obj instanceof KComponent) { // inside this "if" obj is a KComponent
				if (txt.length>0) txt = txt + ", "
				txt = txt + obj.name;
			}
		}
		fsa.generateFile('Components1.txt', 'Component declarations: ' + txt);
		
		// -------------------------------------------
		// Option 2:
		fsa.generateFile('Components2.txt', 'Component declarations: ' + 
			resource.allContents
				.filter[ obj | obj instanceof KComponent]
				.map[ obj | return (obj as KComponent).name ]
				.join(', '))
				
		// -------------------------------------------
		// Option 3:
		fsa.generateFile('Components3.txt', 'Component declarations: ' + 
			resource.allContents.filter(KComponent).map[name].join(', '))
	}

In the last example we generate a text describing a list of components on 
three different manners.

  1. A traditional for-each loop
    * Note: "auto-casting" happens; this mean if a type of an inctance is 
      checked (if „instanceof“), 
      the object is automatically casted to that type within the 
      body of the if.
    * Semicolons are optional.
    * "var" und "val" are used to declare variable (val: final variables).
  2. A filter/map/join combination with explicit lambda („[ param | code ]“)
    * The lambda function is directly defined with square brackets '['...']'.
    * The brackets '('...')' of the function call are omitted.
    * The parameter of the lambda function are stated before the "|"
      within the '['..']'.
  3. A filter/map/join combination with compact lambdas and class filters: 
    * filter(Class) filters according to the passed class "Class".
    * map: here, the parameter is implizit defined (and can be addressed 
      with the name "it": e.g., it.name). 
      Moreover, the implicit name of the parameter can be omitted,
      thus, "name" corresponds to "it.name" here: 
      "[a | a.name]" → "[name]" oder "[it.name]"
    * "return" can be omitted: The last expression is the return value.
    
The generated files contain the text:

    ::raw
    Component declarations: PC, DF

## Xtend template engine

Xtext and Xtend provide a powerful template engine. With this engine
output text and code can be easily mixed. Moreover, indentations
in this mixed code are separated between output indentation and logical
template code indentation (see example: the indentation from the nested
FOR statement are ignored in the output).

        ::xtend
		// -------------------------------------------
		// Option 4:
		val model = resource.contents.get(0) as Model
		fsa.generateFile('Components4.txt', '''
		The Components of the model are:
		«FOR p: model.packages»
			Package «p.name»
			«FOR c: p.components»
				KComponent «c.name»
				«FOR port: c.ports SEPARATOR ", "» 
				- with port «port.name»
				«ENDFOR»
			«ENDFOR»
		«ENDFOR»
		''');

Such templates are defined with a multi line string bounded by
three single qutation marks.
Within the template special commands (like FOR-loops) can be 
expressed with text bounded by french quotes.
The editor supports many features, such as automatic completition of model
data and displaying the actual indentation. 

Note:
  * This example als illustrates how to get the
    root of the model (val model=...).
  * It also shows how to cast an object: „obj as Type“.

Output (generated artefact; note the indentation in the template is omitted):

    ::raw
    The Components of the model are:
    Package test1
    KComponent PC
    - with port in, 
    - with port out
    KComponent DF
    - with port in, 
    - with port out, 
    - with port debug
