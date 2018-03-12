import unittest

import toy_robot
from .test_helpers import InputBuffer, OutputBuffer


class ToyRobotCLITestSuite(unittest.TestCase):
    def test_main(self):
        with InputBuffer('EXIT\n'), OutputBuffer() as bf:
            self.assertIsNone(toy_robot.main())
        self.assertEqual(bf.out, '')

    def test_main_report(self):
        with InputBuffer('REPORT\nEXIT\n'), OutputBuffer() as bf:
            self.assertIsNone(toy_robot.main())
        self.assertEqual(bf.out, '0, 0, NORTH\n')

    def test_main_left(self):
        with InputBuffer('LEFT\nREPORT\nEXIT\n'), OutputBuffer() as bf:
            self.assertIsNone(toy_robot.main())
        self.assertEqual(bf.out, '0, 0, WEST\n')

    def test_main_right(self):
        with InputBuffer('RIGHT\nREPORT\nEXIT\n'), OutputBuffer() as bf:
            self.assertIsNone(toy_robot.main())
        self.assertEqual(bf.out, '0, 0, EAST\n')

    def test_main_move(self):
        with InputBuffer('MOVE\nREPORT\nEXIT\n'), OutputBuffer() as bf:
            self.assertIsNone(toy_robot.main())
        self.assertEqual(bf.out, '0, 1, NORTH\n')

    def test_main_place(self):
        input_text = 'PLACE 3,4,SOUTH\nREPORT\nEXIT\n'
        with InputBuffer(input_text), OutputBuffer() as bf:
            self.assertIsNone(toy_robot.main())
        self.assertEqual(bf.out, '3, 4, SOUTH\n')

    def test_example_a(self):
        argvs = ['toy_robot', 'tests/data/example_a.txt']
        with OutputBuffer() as bf:
            self.assertIsNone(toy_robot.main(argvs))
        self.assertEqual(bf.out, '0, 0, NORTH\n')

    def test_example_b(self):
        argvs = ['toy_robot', 'tests/data/example_b.txt']
        with OutputBuffer() as bf:
            self.assertIsNone(toy_robot.main(argvs))
        self.assertEqual(bf.out, '0, 1, NORTH\n2, 1, EAST\n')


if __name__ == '__main__':
    unittest.main()
