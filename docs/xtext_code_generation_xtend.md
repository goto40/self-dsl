# Code Generation (with Xtend)

Xtend is highly optimized to be used
for code generation. It has a optimzed template engine (e.g., with
automatic indentation support) and
is fully integrated in the Eclipse IDE (auto completition
for model data).

## Example

Opne the *Generator.xtend file in your project, e.g.,
kurs.xtext.dataflow.generator.DataFlowDslGenerator.xtend. 
Here, you can implement your first code generator:
You have model access (parameter "resource") and file system access
(parameter "fsa").

    :::xtend
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

TODO
xxx