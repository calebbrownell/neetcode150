import unittest
from arrays_and_hashing_1_9 import problem1
from arrays_and_hashing_1_9 import problem2
from arrays_and_hashing_1_9 import problem3
from arrays_and_hashing_1_9 import problem4


def main():
    print("Entering main")
    suite = unittest.TestLoader().loadTestsFromModule(problem1)
    unittest.TextTestRunner().run(suite)

    suite = unittest.TestLoader().loadTestsFromModule(problem2)
    unittest.TextTestRunner().run(suite)

    suite = unittest.TestLoader().loadTestsFromModule(problem3)
    unittest.TextTestRunner().run(suite)

    suite = unittest.TestLoader().loadTestsFromModule(problem4)
    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    main()
