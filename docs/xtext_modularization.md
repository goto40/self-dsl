# Xtext: Model Modularization

In this section we present possibilities to modularize your model
data across multiple files, in order to reuse model data and to divide
model data into smaller parts.

## Modularization within the same Meta Model

This topic is covered in [xtext_scoping.md](xtext_scoping.md).

## Referencing Model Elements form other Meta Models

When you have ab existing meta model (an Xtext language, e.g., 
"org.xtext.example.mydsl"), you can create another language referencing this
existing language.

In the new language (in eclipse, created side-by-side to the existing language,
e.g., "org.xtext.example.mydsl1"):

 * Add the eclipse project of the original language to the build path 
    ("org.xtext.example.mydsl"):
       * right-click on the project and select "Configure Build Path"
       * select tab "Projects"
       * "Add..." the existing project (e.g., "org.xtext.example.mydsl")
 * Add plugin dependency in MANIFEST.MF
       * open org.xtext.example.mydsl1/META_INF/MANIFEST.MF
       * click on "Dependencies"
       * "Add..." in "required packages"
       * select the existing language (e.g. "org.xtext.example.mydsl")
       * save MANIFEST.MF (CTRL-S)
 * In the mwe2.file (side-by-side to the grammar of your new language)
       * add to section "language" (after "name"; you can check the path and the 
         file name in your existing language)
  
  
            referencedResource = "platform:/resource/org.xtext.example.mydsl/model/generated/MyDsl.genmodel"

 * In your new grammar, import the existing language (check the grammar of 
   the existing language for the URL). You can reference elements from your
   exisiting language as shown below:
 
 
        import "http://www.xtext.org/example/mydsl/MyDsl" as existingDsl
        ...
    	'Hello' '-->' ref=[existingDsl::Greeting];

