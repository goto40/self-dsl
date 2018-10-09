from textx import metamodel_from_file

def get_metamodel():
    meta_model = metamodel_from_file("MyDsl.tx")
    return meta_model

