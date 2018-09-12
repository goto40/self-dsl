# Xtext: deploy a command line version of the code generator

## Generate a command line version of the code generator

Add the following entries to your mwe2 file (located side-by-side to your 
grammar; see e.g. ::namedref::(references.md#bettini2016)):
    
    ...
    language = StandardLanguage {
        ...
        generator = {
            generateJavaMain = true
        }
        ...
    }
    ...
    

When running the mwe2 script (compiling your grammar; 
see ::namedref::(xtext_project_setup.md#xtext_compile_and_run)), a Main.java
file is created in the generator namespace side-by-side to your grammar.

## Modify Main.java

The Main-class expects a model file to be processed: parsed, validated and
generated code from the model.

 * You can manually set the destination path (__change "src-gen"__ to something 
    else).
 * There is no workspace for the model files; you must modify the Main.java 
    file in order to manually __add other model files__ (e.g. from some sub folder or 
    specified via the command line). 
    E.g.:


        ::java
        protected void runGenerator(String main_model_filename, String[] all_other_filenames) {
            // Load the resource
            ResourceSet set = resourceSetProvider.get();
            Resource resource = set.getResource(URI.createFileURI(main_model_filename), true);
            List<Resource> all_resources = new ArrayList<Resource>();
            all_resources.add(resource);
        
            // Load all other requried resources
            for(String m:all_other_filenames) {
                if (!m.equals(main_model_filename)) {
                    Resource other = set.getResource(URI.createFileURI(m), true);
                    all_resources.add(other);
                }
            }
    
            // Validate all resources
            for (Resource r: all_resources) {
                List<Issue> list = validator.validate(r, CheckMode.ALL, CancelIndicator.NullImpl);
                if (!list.isEmpty()) {
                    for (Issue issue : list) {
                        System.err.println(issue);
                    }
                    return;
                }
            }
    
            // Configure and start the generator
            fileAccess.setOutputPath("src-gen/");
            GeneratorContext context = new GeneratorContext();
            context.setCancelIndicator(CancelIndicator.NullImpl);
            generator.generate(resource, fileAccess, context);
    
            System.out.println("Code generation finished.");
        }
         

## Manually create a runnable JAR file with the command line compiler

In eclipse you can "__Export__" your generator as "__Runnable JAR__":

 * Create a Run Configuration by right-clicking on your Main.java and select 
    "Run as" / "Java Application".
 * Then right-click on the project containing the Main.java file and select 
    "Export", "Runnable JAR file".
 * Select "Main" in the "Launch configurazion".
 * Select "Package requried libraries into generated JAR file".
 * Specify your destination JAR file name and click "Finish".

## Create the command line compiler with maven

 * Close eclipse 
 * Clone [https://github.com/basilfx/xtext-standalone-maven-build](https://github.com/basilfx/xtext-standalone-maven-build)
   (There is a good description there what to do)
 * Copy the ...standalone-folder into your ...parent folder (side-by-side 
    to your other projects)
 * Rename the folder to match your project name (e.g. 
    "org.xtext.example.mydsl.standalone" to 
    "org.example.domainmodel.standalone")
 * Rename (find/replace) the project name (replace "org.xtext.example.mydsl"
    with "org.example.domainmodel") in all files in the copied folder.
 * Add the new folder/module to the modules list in your master pom.xml file
    (section "modules").
 * try "mvn package" in your master directory and check if the target in
    the new standalone module is created. The generated JAR file can then be 
    tested as follows (assuming some model files are available):
    
        ::shell
        java -jar org.example.domainmodel.standalone/target/org.example.domainmodel.standalone-1.0.0-SNAPSHOT.jar *.dmodel

Note: 
 * no need to add (import) the standalone project into the ecplise 
    workspace.
 * You can use the standalone code generator as "compiler" in a Makefile
    (like gcc). It will perform a model sytanx check, a model validation and a 
    code generation.