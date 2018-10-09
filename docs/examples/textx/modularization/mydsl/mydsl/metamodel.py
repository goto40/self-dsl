from textx import metamodel_from_file
from os.path import dirname, abspath, join

def get_metamodel():
    this_folder = dirname(abspath(__file__))
    meta_model = metamodel_from_file(join(this_folder,"MyDsl.tx"))
    return meta_model

