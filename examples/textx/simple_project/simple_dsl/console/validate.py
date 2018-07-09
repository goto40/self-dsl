import argparse
from simple_dsl import get_metamodel

def validate():
    mm = get_metamodel()
    parser = argparse.ArgumentParser(description='validate simple_dsl files.')
    parser.add_argument('model_files', metavar='model_files', type=str,
                        nargs='+',
                        help='model filenames')
    args = parser.parse_args()

    for filename in args.model_files:
        try:
            print('validating {}'.format(filename))
            _ = mm.model_from_file(filename)
        except BaseException as e:
            print('  WARNING/ERROR: {}'.format(e))


if __name__=='__main__':
    validate()