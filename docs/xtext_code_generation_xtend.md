# Code Generation (with Xtend)

Xtend is highly optimized to be used
for code generation. It has a optimized template engine (e.g., with
automatic indentation support) and
is fully integrated in the Eclipse IDE (auto completion
for model data).

Here we highlight some information when walking through
::namedref::(references.md#xtext15minext), 
section "Writing a Code Generator With Xtend".

## Goal of this section

 * You learn how to generate artifacts in form of text files (e.g. source code).
 * You learn how to format the output and how to access model data.
 * After some basic steps you may have a look at 
    [xtext_xtend.md](xtext_xtend.md) to learn more about the language xtend 
    employed for the artifact generator.
 * Finally, you see how you can generate a C++-file based on the model. You
   will see how you can start from an example code and iteratively replace
   concrete code with model data.

## Step 1: Walk through

When reading ::namedref::(references.md#xtext15minext), start with the
first section "Writing a Code Generator With Xtend" (until 
"Unit Testing the Language"): 

  * Locate the file where the **artifact generator** is implemented 
    (DomainmodelGenerator.xtend).
  * "**doGenerate**" is the method called when generating artifacts from a model.
  * Ignore the "IQualifiedNameProvider": You can just use "obj.name" in your 
    example (instead of obj.fullyQualifiedName) for the moment.
  * Xtend allows to use templates (indicated by multiline strings with
    three single quotes): 
    * Inside this templates you can place **text which 
      is directly inserted** in the output. 
    * **Special commands** like "IF" or "FOR" can be used if placed between 
      "«" and "»" 
      ("«" and "»" can be entered using CTRL-< and CTRL-> within eclipse).
    * It is also possible to **insert local variable constants** (typically model 
      data, e.g. '''the name of the entity is «entity_var.name»''').
    * Tabs are inserted in an intelligent way, such that **indentation** associated
      with generator logic (e.g., after an "«IF»") are not inserted into the
      output (such indentation is visually highlighted in the editor).
  * **Optional model elements** which are represented as a class are null, when
    not used. Caution: Other elements, such as enums, INT, and STRING have
    default values.
  * The example also shows that a **modularization** is possible (see how 
    code for "Features" is inserted).
  * Many aspects may look scary at first sight, but are extremely valuable 
    for the given task of textual artifact generation: 
    See [xtext_xtend.md](xtext_xtend.md).

Note:

  * This following example als illustrates how to get the
    root of the model (val model=...). This object can be passed to
    a function generating some text from it.
    
        ::xtend
        val model = resource.contents.get(0) as Domainmodel
    
  * It also shows how to cast an object: „obj as Type“.

## Step 2: Question

What is the following code doing? See [xtext_xtend.md](xtext_xtend.md).

    ::xtend
	override void doGenerate(Resource resource, IFileSystemAccess2 fsa, IGeneratorContext context) {
		fsa.generateFile('greetings.txt', 'People to greet: ' + 
			resource.allContents
				.filter(Entity)
				.map[name]
				.join(', '))
	}

## Step 3: Next step: Extended example

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
    
Then start replacing your example code with model information:  


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

## Optional Step 4: Create a command line version of your "compiler"

See [xtext_deploy_command_line.md](xtext_deploy_command_line.md).
