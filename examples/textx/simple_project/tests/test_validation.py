from pytest import raises
from simple_dsl import get_metamodel
from os.path import dirname, join
from textx import get_children_of_type

def test_validation_ok():
    mm = get_metamodel()
    m = mm.model_from_file(join(dirname(__file__),
                            'models',
                            'model_ok.dsl'))
    assert 2==len(get_children_of_type('Aspect',m))

def test_validation_not_ok():
    mm = get_metamodel()
    with raises(Exception,
                match=r'NetworkTraffic.*not found.*S001.*NoNetworkTraffic'):
        _ = mm.model_from_file(join(dirname(__file__),
                                'models',
                                'model_not_ok.dsl'))
