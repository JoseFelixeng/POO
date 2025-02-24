'''
The wide-mouth frog is particularly interested in the eating habits of other creatures.

He just can't stop asking the creatures he encounters what they like to eat. But, then he meets the alligator who just LOVES to eat wide-mouthed frogs!

When he meets the alligator, it then makes a tiny mouth.

Your goal in this kata is to create complete the mouth_size method this method takes one argument animal which corresponds to the animal encountered by the frog. If this one is an alligator (case-insensitive) return small otherwise return wide.

'''

def mouth_size(animal): 
    if animal.lower() != 'alligator':
        return 'wide'
    else: 
        return 'small'


## Teste

import codewars_test as test
from solution import mouth_size

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(mouth_size("toucan"),"wide")
        test.assert_equals(mouth_size("ant bear"),"wide")
        test.assert_equals(mouth_size("alligator"),"small")