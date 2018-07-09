# Quickfixes

Open the *QuickfixProvider.xtend file of your ui-project, e.g.,
"kurs.xtext.dataflow.ui.quickfix.DataFlowDslQuickfixProvider.xtend".
Here you can implement Quickfixes.
 
The example provided as commented code can be activated
for our [initial example](xtext_a_first_grammar.md) more or
less without modifications:

    ::xtend
	@Fix(DataFlowDslValidator.INVALID_NAME)
	def capitalizeName(Issue issue, IssueResolutionAcceptor acceptor) {
		acceptor.accept(issue, 'Capitalize name', 'Capitalize the name.', 'upcase.png') [
			context |
			val xtextDocument = context.xtextDocument
			val firstLetter = xtextDocument.get(issue.offset, 1)
			xtextDocument.replace(issue.offset, 1, firstLetter.toUpperCase)
		]
	}

The [ID of the validation](xtext_model_validation.md) 
(here "INVALID_NAME") allows to identify the type of the
issue to be fixed. 

In the last example, the Quickfix uses direct access
to the model text. Alternatively, the model itself can
be modified:

    ::xtend
	@Fix(DataFlowDslValidator.INVALID_NAME)
	def capitalizeName2(Issue issue, IssueResolutionAcceptor acceptor) {
		acceptor.accept(issue, 'Capitalize name 2', 'Capitalize the name.', 'upcase.png') [
			element, context |
			val c=element as KComponent
			c.name = c.name.toFirstUpper
		]
	}

The annotation "@Fix" marks a method as Quickfix-method and
controls the mapping to the validation ID.

Note: relevant details concerning Xtend are discussed in
[this section](textx_xtend.md)
(e.g., the meaning of „val“, „as“, etc.).