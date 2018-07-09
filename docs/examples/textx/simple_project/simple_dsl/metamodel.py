from textx import metamodel_from_str
from textx.scoping.providers import RelativeName, FQN
import simple_dsl.validation as validation

def get_metamodel():
    # GRAMMAR
    # (you also use metamodel_from_file with a *.tx file)
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

    # SCOPING
    meta_model.register_scope_providers({
        '*.*': FQN(),
        'Testcase.config': RelativeName('scenario.configs')
    })

    # ADD VALIDATION
    meta_model.register_obj_processors({
            'Testcase': validation.check_testcase
    })

    return meta_model

