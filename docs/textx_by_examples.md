# TextX by Examples

The [TextX project page](references.md#textx)
gives a nice introduction to the concepts of TextX.
Read the docs to explore different aspects, like
the grammar or scoping. The unittests are
also a great source of information, because they contain
many examples for different topics.

Note: validators are implemented as so-called object_processors.
These object_processors are meant to post process the
parsed model (possibly modifying the model). They can also
be used to raise exceptions in order to indicate a logical
domain error (as in the [initial example](textx_intro.md)).

