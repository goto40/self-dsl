from textx import metamodel_from_file
import textx.scoping as scoping
import textx.scoping.providers as scoping_providers
from os.path import dirname, abspath, join
import mydsl

def get_metamodel():
    this_folder = dirname(abspath(__file__))
    other_meta_model = mydsl.get_metamodel()
    meta_model = metamodel_from_file(join(this_folder,"MyDsl1.tx"), 
        referenced_metamodels=[other_meta_model])
    meta_model.register_scope_providers({"*.*": scoping_providers.PlainNameImportURI()})

    # register file endings
    scoping.MetaModelProvider.add_metamodel("*.mydsl", other_meta_model)
    scoping.MetaModelProvider.add_metamodel("*.mydsl1", meta_model)

    return meta_model

