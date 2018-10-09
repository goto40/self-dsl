import argparse
from mydsl.metamodel import get_metamodel

def mydslc():
    parser = argparse.ArgumentParser(description='generate code for the model.')
    parser.add_argument('model_files', metavar='model_files', type=str, nargs='+',
                        help='model filenames')

    args = parser.parse_args()
    mm = get_metamodel()

    for model_file in args.model_files:
        model = mm.model_from_file(model_file)
        for greeting in model.greetings:
            print(" - hello for '{}'".format(greeting.name)) 
