from textx.exceptions import TextXError
from textx.scoping.tools import get_location

def check_testcase(testcase):
    """
    checks that the config used by the testcase fulfills its needs
    """
    for need in testcase.needs:
        if need not in testcase.config.haves:
            raise (TextXError("{}: {} not found in {}.{}".format(
                    testcase.name,
                    need.name, 
                    testcase.scenario.name,
                    testcase.config.name
                    ),
                **get_location(testcase) # unpack location info
            ))

