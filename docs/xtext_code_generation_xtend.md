# Code Generation (with Xtend)

Xtend is highly optimized to be used
for code generation. It has a optimzed template engine (e.g., with
automatic indentation support) and
is fully integrated in the Eclipse IDE (auto completition
for model data).

Here we highlight some information when walking through
::namedref::(references.md#xtext15minext), 
section "Writing a Code Generator With Xtend".

  * "doGenerate" is the method called when generating artefact from a model.
  * xxx TODO @Inject
  * Xtend allows to use templates (indicated by multiline strings with
    three single quotes): Inside this templates special commands like "IF"
    or "FOR" can be used. Is is also possible to to directly insert local
    variable contensts (typically model data).

Note:

  * This following example als illustrates how to get the
    root of the model (val model=...).
    
        ::xtend
        val model = resource.contents.get(0) as Domainmodel
    
  * It also shows how to cast an object: „obj as Type“.

## Question

What is the following code doing? See [xtext_xtend.md](xtext_xtend.md).

    ::xtend
	override void doGenerate(Resource resource, IFileSystemAccess2 fsa, IGeneratorContext context) {
		fsa.generateFile('greetings.txt', 'People to greet: ' + 
			resource.allContents
				.filter(Entity)
				.map[name]
				.join(', '))
	}

## Extended example

Try to generate a C-code snippet:

    ::cpp
    #ifndef __MYSTRUCT_H_
    #define __MYSTRUCT_H_
    #include <cstdint>

    struct MyStruct {
        float attribute1;
        int32_t attribute2;
    };
    
    #endif

When starting a new generator snippet, it can help to copy-paste
the code to be generate as an example into your code:

    ::xtend
    def generateCppCode(Entity e) {
        '''
        #ifndef __MYSTRUCT_H_
        #define __MYSTRUCT_H_
        #include <cstdint>
    
        struct MyStruct {
            float attribute1;
            int32_t attribute2;
        };
        
        #endif
        '''
    }  
    
Then start replacing your example code with model information 
("«" and "»" can be 
entered using CTRL-< and CTRL-> within eclipse):  


    ::xtend
    def generateCppCode(Entity e) {
        '''
        #ifndef __MYSTRUCT_H_ // TODO
        #define __MYSTRUCT_H_ // TODO
        #include <cstdint>
    
        struct «e.name» {
		«FOR f : e.features»
			TODO «f.name»;
		«ENDFOR»
        };
        
        #endif
        '''
    }  
    

... and integrate
your new functionality in your "doGenerate" method:

    ::xtend
    // integrate the new generator
    for (e : resource.allContents.filter(Entity).toIterable) {
        fsa.generateFile(e.name+'.h', generateCppCode(e))
    }
