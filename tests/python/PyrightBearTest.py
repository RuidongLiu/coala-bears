from bears.python.PyrightBear import PyrightBear
from coalib.testing.LocalBearTestHelper import verify_local_bear


good_file = '''
i: int = 42
i = 56

'''


bad_file = '''
i: int = 42
i = "F"

'''

PyrightBearTest = verify_local_bear(
    PyrightBear,
    valid_files=(good_file,),
    invalid_files=(bad_file,))
