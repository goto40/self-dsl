# Xtext: Model Modularization

In this section we present possibilities to modularize your model
data across multiple files, in order to reuse model data and to divide
model data into smaller parts.

## Modularization within the same Meta Model

This topic is covered in [xtext_scoping.md](xtext_scoping.md).

## Referencing Model Elements form other Meta Models

When you have an existing metamodel (an Xtext language, e.g., 
"org.xtext.example.mydsl"), you can create another language referencing this
existing language.

In the new language (in eclipse a new project, created side-by-side to the 
existing language, e.g., "org.xtext.example.mydsl1.MyDsl1"; details see
::namedref::(references.md#mooji2017b)):

 * Add plugin dependency in MANIFEST.MF in your new language project 
   (e.g., "org.xtext.example.mydsl1")
       * open org.xtext.example.mydsl1/META_INF/MANIFEST.MF
       * click on "Dependencies" 
       * "Add..." in "Required Plug-Ins"
       * select the existing language and the ui package
         (e.g. "org.xtext.example.mydsl" and "org.xtext.example.mydsl.ui")
       * save MANIFEST.MF (CTRL-S)
 * Add plugin dependency in MANIFEST.MF of your new "ui" project (e.g.,
  "org.xtext.example.mydsl1.ui").
       * same as for the language project.
 * In the mwe2.file (side-by-side to the grammar of your new language)
       * add to section "language" (after "name"; you can check the path and the 
         file name in your existing language)
  
  
            referencedResource = "platform:/resource/org.xtext.example.mydsl/model/generated/MyDsl.genmodel"

 * In your new grammar, import the existing language (check the grammar of 
   the existing language for the URL). You can reference elements from your
   existing language as shown below:
 
 
        import "http://www.xtext.org/example/mydsl/MyDsl" as existingDsl
        ...
    	Greeting: 'Hello' '-->' ref=[existingDsl::Greeting];

 * For the standalone setup in Main.java (command line version), you need to run the following code before ```Injector injector = new MyDslStandaloneSetup().createInjectorAndDoEMFRegistration();
```:

        org.xtext.example.mydsl.MyDslStandaloneSetup stse_ref = new org.xtext.example.mydsl.MyDslStandaloneSetup();
        Injector i_ref = stse_ref.createInjector();
        stse_ref.register(i_ref);

Note: Do not forget to have the "Build Automatically" enabled in the eclipse 
menu "Project".