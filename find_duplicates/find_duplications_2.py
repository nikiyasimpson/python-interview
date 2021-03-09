import unittest


def find_duplicate(int_list):

    # Find a number that appears more than once ... in O(n) time
    n = len(int_list) - 1
    
    # Start at position n +1 and find another position in the cycle
    position_in_cycle = n + 1
    
    
    for _ in range(n):
        position_in_cycle = int_list[position_in_cycle - 1]
        # we subtract 1 from the currect position to step ahead
        # the 2nd "position" in the list is "index" 1
        
    
    # Find the length of the cycle by remembering the position in the cycle
    # and counting the steps it takes to get back to that position
    
    remembered_position_in_cycle = position_in_cycle
    
    current_position_in_cycle = int_list[position_in_cycle -1]
    cycle_step_count = 1
    
    
    while current_position_in_cycle != remembered_position_in_cycle:
        current_position_in_cycle = int_list[current_position_in_cycle -1]
        cycle_step_count += 1
        
    # Step 3: Find the first node of the cycle
    # Start two pointers (1) at position n+ 1, (2) ahead of position n+1 as many steps as the cycle's length
    
    pointer_start = n + 1
    pointer_ahead = n + 1
    
    for _ in range(cycle_step_count):
        pointer_ahead = int_list[pointer_ahead - 1]
    
    
    # Advance until the pointers are in the same position, which is the first node in the cycle
    
    while pointer_start != pointer_ahead:
        pointer_start = int_list[pointer_start - 1]
        pointer_ahead = int_list[pointer_ahead - 1]
    
    
    #Since there are multiple vlaues pointing to the first node
    # in the cycle, its position is the duplicate in our list
    
    return pointer_start



# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_duplicate([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_duplicate([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_duplicate([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_duplicate([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)