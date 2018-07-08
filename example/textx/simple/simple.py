from textx import metamodel_from_str
from textx.scoping.providers import RelativeName, FQN
from textx.export import model_export
# ------------------------------------
# GRAMMAR
#
meta_model = metamodel_from_str('''
    Model: aspects+=Aspect scenarios+=Scenario testcases+=Testcase;
    Scenario: 'SCENARIO' name=ID 'BEGIN' 
        configs+=Config
    'END';
    Config: 'CONFIG' name=ID 'HAS' '(' haves*=[Aspect] ')';
    Aspect: 'ASPECT' name=ID;
    Testcase: 'TESTCASE' name=ID 'BEGIN'
        'USES' scenario=[Scenario] 'WITH' config=[Config]
        'NEEDS' '(' needs*=[Aspect] ')'
    'END';
    Comment: /\/\/.*/;
''')

# ------------------------------------
# SCOPING
#
meta_model.register_scope_providers({
    '*.*': FQN(),
    'Testcase.config': RelativeName('scenario.configs')
})

# ------------------------------------
# VALIDATION
#
def check_testcase(testcase):
    """
    checks that the config used by the testcase fulfills its needs
    """
    for need in testcase.needs:
        if need not in testcase.config.haves:
            raise Exception("{}: {} not found in {}.{}".format(
                    testcase.name,
                    need.name, 
                    testcase.scenario.name,
                    testcase.config.name
                    ))

meta_model.register_obj_processors({
        'Testcase': check_testcase
})

# ------------------------------------
# EXAMPLE
#
model = meta_model.model_from_str('''
    ASPECT NetworkTraffic
    ASPECT FileAccess
    SCENARIO S001 BEGIN
        CONFIG HeavyNetworkTraffic HAS (NetworkTraffic)
        CONFIG NoNetworkTraffic HAS ()
    END
    SCENARIO S002 BEGIN
        CONFIG WithFileAccess HAS (NetworkTraffic FileAccess)
        CONFIG NoFileAccess HAS (NetworkTraffic)
    END
    TESTCASE T001 BEGIN
        USES S001 WITH HeavyNetworkTraffic
        NEEDS (NetworkTraffic)
    END
    TESTCASE T002 BEGIN
        //USES S001 WITH NoNetworkTraffic // Error
        USES S002 WITH NoFileAccess
        NEEDS (NetworkTraffic)
    END
''')

model_export(model, 'model.dot')
