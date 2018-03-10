import unittest

import toy_robot
from .test_helpers import InputBuffer,OutputBuffer


class ToyRobotCLITestSuite(unittest.TestCase):
    def test_main(self):
        # with patch('builtins.input', return_value='EXIT\n'), OutputBuffer() as bf:
        with InputBuffer('EXIT\n'), OutputBuffer() as bf:
            self.assertIsNone(toy_robot.main_loop())
        self.assertEqual(bf.out, '')

    def test_main_report(self):
        with InputBuffer('REPORT\nEXIT\n'), OutputBuffer() as bf:
            self.assertIsNone(toy_robot.main_loop())
        self.assertEqual(bf.out, '0, 0, NORTH\n')

    def test_main_left(self):
        with InputBuffer('LEFT\nREPORT\nEXIT\n'), OutputBuffer() as bf:
            self.assertIsNone(toy_robot.main_loop())
        self.assertEqual(bf.out, '0, 0, WEST\n')

    def test_main_right(self):
        with InputBuffer('RIGHT\nREPORT\nEXIT\n'), OutputBuffer() as bf:
            self.assertIsNone(toy_robot.main_loop())
        self.assertEqual(bf.out, '0, 0, EAST\n')

    def test_main_move(self):
        with InputBuffer('MOVE\nREPORT\nEXIT\n'), OutputBuffer() as bf:
            self.assertIsNone(toy_robot.main_loop())
        self.assertEqual(bf.out, '0, 1, NORTH\n')

    def test_main_place(self):
        with InputBuffer('PLACE 3,4,SOUTH\nREPORT\nEXIT\n'), OutputBuffer() as bf:
            self.assertIsNone(toy_robot.main_loop())
        self.assertEqual(bf.out, '3, 4, SOUTH\n')


if __name__ == '__main__':
    unittest.main()
