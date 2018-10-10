# Xtext HOWTOs

Here, we collect short snippets to solve common problems.

## Define a named object

Use the special attribute "name" in combination with
default scope providers.

    ::antlr
    ...
    MyObj: 'myobj' name=ID

## Define an optional attribute

Use "(...)?". Note:
  * Some types, like INT or enums have default values (like 0 for INTs) and, 
    thus, an unset value cannot be distinguished from, e.g., the value 0.
  * Using helper objects (like "Other" in the example below) helps to detect
    unset optional values, since the object is "null", if not set.


    ::antlr
    ...
    MyObj: 'myobj' name=ID (option_int=INT)?  (option_obj=Other)?;
    Other: 'other' val=INT;

## Define a boolean flag based on the presence of a keyword

See Xtext documentation:

    ::antlr
    ...
    MyObj: 'myobj' name=ID (option_flag?='flag_keyword')? 
    
## Define an enum

See Xtext docu.
Note: The first enum value is the default value.

    ::antlr
    ...
    MyObj: 'myobj' name=ID '=' value=MyEnum;
    enum MyEnum: val1='VAL1'|val2='VAL2'|val3='VAL3';


## Force the creation of an object when no attributes are defined

Object without attributes are not instantiated as objects in the model
representation. This can also happen, when all attributes are optional
and not set in a concrete model (in this case you get a warning in your 
grammar). Use "{Rule-name}" to force instantiation.

    ::antlr
    MyObj: {MyObj} 'myobj' (value=MyVal)?;
    MyVal: text=STING;


## Define an attribute containing a list

    ::antlr
    ...
    Model: things+=Thing*;
    Thing: 'thing' name=ID;

## Add one element to a list

    ::antlr
    ...
    Model: things+=Thing;
    Thing: 'thing' name=ID;

## Define a comma separated list

    ::antlr
    ...
    Model: things+=Thing (',' things+=Thing)*;
    Thing: 'thing' name=ID;

## Define an element to represent either a signed int or a float

Example grammar snippet defining a 'myobj' containing a name and either a 
float or an integer value:

    ::antlr
    import "http://www.eclipse.org/emf/2002/Ecore" as ecore
    ...
    MyObj: 'myobj' name=ID '=' (value=MyVal)?;
    MyVal: MyInt|MyFloat;
    MyInt: ivalue=MYINT_T;
    MyFloat: fvalue=MYFLOAT_T;
    terminal MYINT_T returns ecore::EInt: '-'?INT;
    terminal MYFLOAT_T returns ecore::EFloat: '-'?INT'.'INT;
    

With the test illustrating the types (int/float):

    ::xtend
	@Inject extension
	ParseHelper<Model> parseHelper
	@Inject extension
	ValidationTestHelper testHelper;
    ...    
	@Test 
	def void testFloatInt() {
		val result = '''
		myobj pi=3.1415
		myobj N=4
		'''.parse
		result.assertNotNull
		result.assertNoErrors
		
		assertTrue( result.objs.head.value instanceof MyFloat )
		val f = (result.objs.head.value as MyFloat).fvalue
		assertEquals(  3.1415, f, 1e-4 )

		assertTrue( result.objs.last.value instanceof MyInt )
		val i = (result.objs.last.value as MyInt).ivalue
		assertEquals(  4, i )
	}

## Allow keywords as name of elements

**Problem**: keywords (like 'myobj' or 'ref' in the example below) are not 
classified as "ID" by the lexer. Thus, they cannot be used as ID (the default
lexer token for references).

    ::antlr
    ...
    MyObj: 'myobj' name=ID 
    Ref: 'ref' [MyObj]; // same as [MyObj|ID]

**Solution**: see https://blogs.itemis.com/en/xtext-hint-identifiers-conflicting-with-keywords
for more details. Define a VALID_ID, including the desired keywords to be 
allowed as name:

    ::antlr
    ...
    MyObj: 'myobj' name=ID 
    Ref: 'ref' [MyObj|VALID_ID];
    VALID_ID: ID|'ref'|'myobj'


## Define a list of objects with the same base type

Example:

    struct Simple {
        scalar x
        array y[10]
        scalar z
    }

With grammar:

    ::antlr
    ...
    Struct: 'struct' name=ID '{' attrs+=Attribute+ '}';
    Attribute: ScalarAttribute|ArrayAttribute;
    ScalarAttribute: 'scalar' name=ID;
    ArrayAttribute: 'array' name=ID '[' dim=INT ']';


## Allow to model a mix of objects of unrelated type

Example (same as in last example):

    struct Simple {
        scalar x
        array y[10]
        scalar z
    }

With grammar:

    ::antlr
    ...
    Struct: 'struct' name=ID '{' 
        (s+=ScalarAttribute | a+=ArrayAttribute)* 
        '}'
    ;
    ScalarAttribute: 'scalar' name=ID;
    ArrayAttribute: 'array' name=ID '[' dim=INT ']';

## Define multiline string attributes

You can use the "->" feature for terminals. You need to strip the 
leading and trailing '"""' when accessing the multiline string (e.g.,
with a xtend extension method).

Grammar snippet:

    ::antlr
    ...
    MultlineInfo: 'info' text=MLTEXT;
    terminal MLTEXT: '"""' -> '"""';

Xtend code snippet and test:

    ::xtend
	static def getMltext(MultlineInfo info) {
		info.text.replaceAll('^"""','').replaceAll('"""$','');
	}

	@Test 
	def void testMlInfo() {
		val result = '''
		info """Hello World"""
		info """Hello Multiline
		World"""
		'''.parse
		result.assertNotNull
		result.assertNoErrors
		assertEquals( '"""Hello World"""', result.infos.head.text )
		assertEquals( "Hello World", result.infos.head.mltext )
		assertEquals( "Hello Multiline\nWorld", result.infos.last.mltext )
	}
	
## Filter a list based on a type

    ::xtend 
    resource.allContents.filter(Entity)

## Filter a list based on an attribute value

    ::xtend 
    resource.allContents.filter(Entity).filter[name="Tom"]
        
## Transform a list

    ::xtend 
    resource.allContents.filter(Entity).map[e|'the name is '+e.name]

## Concatenate two lists

    ::xtend 
    // list1 and list2 are of type java.util.List<...>
    (list1+list2).toList
