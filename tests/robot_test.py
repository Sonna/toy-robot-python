import unittest

from .test_helpers import OutputBuffer
from toy_robot.robot import Robot


class RobotTestSuite(unittest.TestCase):
    def test_robot_constructor(self):
        subject = Robot(1, 2, 'SOUTH')
        self.assertEqual(subject.x, 1)
        self.assertEqual(subject.y, 2)
        self.assertEqual(subject.facing, 'SOUTH')

    def test_robot_default_constructor(self):
        subject = Robot()
        self.assertEqual(subject.x, 0)
        self.assertEqual(subject.y, 0)
        self.assertEqual(subject.facing, 'NORTH')

    def test_robot_report(self):
        subject = Robot()
        with OutputBuffer() as bf:
            self.assertIsNone(subject.report())
        self.assertEqual(bf.out, '0, 0, NORTH\n')

    def test_robot_place(self):
        subject = Robot()
        subject.place('4,2,EAST')

        self.assertEqual(subject.x, 4)
        self.assertEqual(subject.y, 2)
        self.assertEqual(subject.facing, 'EAST')

    def test_robot_left(self):
        subject = Robot()
        subject.left()

        self.assertEqual(subject.x, 0)
        self.assertEqual(subject.y, 0)
        self.assertEqual(subject.facing, 'WEST')

    def test_robot_right(self):
        subject = Robot()
        subject.right()

        self.assertEqual(subject.x, 0)
        self.assertEqual(subject.y, 0)
        self.assertEqual(subject.facing, 'EAST')

    def test_robot_move(self):
        subject = Robot()
        subject.move()

        self.assertEqual(subject.x, 0)
        self.assertEqual(subject.y, 1)
        self.assertEqual(subject.facing, 'NORTH')

    def test_robot_move_east_from_origin(self):
        subject = Robot()
        subject.right()
        subject.move()

        self.assertEqual(subject.x, 1)
        self.assertEqual(subject.y, 0)
        self.assertEqual(subject.facing, 'EAST')

    def test_robot_move_west_from_origin(self):
        subject = Robot()
        subject.left()
        subject.move()

        self.assertEqual(subject.x, 0)
        self.assertEqual(subject.y, 0)
        self.assertEqual(subject.facing, 'WEST')

    def test_robot_move_south_from_origin(self):
        subject = Robot()
        subject.left()
        subject.left()
        subject.move()

        self.assertEqual(subject.x, 0)
        self.assertEqual(subject.y, 0)
        self.assertEqual(subject.facing, 'SOUTH')

    def test_robot_move_south_from_place_2_2_south(self):
        subject = Robot()
        subject.place('2,2,SOUTH')
        subject.move()

        self.assertEqual(subject.x, 2)
        self.assertEqual(subject.y, 1)
        self.assertEqual(subject.facing, 'SOUTH')

    def test_robot_move_east_from_place_2_2_east(self):
        subject = Robot()
        subject.place('2,2,EAST')
        subject.move()

        self.assertEqual(subject.x, 3)
        self.assertEqual(subject.y, 2)
        self.assertEqual(subject.facing, 'EAST')

    def test_robot_move_west_from_place_2_2_west(self):
        subject = Robot()
        subject.place('2,2,WEST')
        subject.move()

        self.assertEqual(subject.x, 1)
        self.assertEqual(subject.y, 2)
        self.assertEqual(subject.facing, 'WEST')

    def test_robot_move_north_from_place_2_2_north(self):
        subject = Robot()
        subject.place('2,2,NORTH')
        subject.move()

        self.assertEqual(subject.x, 2)
        self.assertEqual(subject.y, 3)
        self.assertEqual(subject.facing, 'NORTH')

    def test_robot_call_report(self):
        subject = Robot()
        with OutputBuffer() as bf:
            self.assertIsNone(subject.call('REPORT'))
        self.assertEqual(bf.out, '0, 0, NORTH\n')

    def test_robot_call_place(self):
        subject = Robot()
        subject.call('PLACE', '4,2,EAST')

        self.assertEqual(subject.x, 4)
        self.assertEqual(subject.y, 2)
        self.assertEqual(subject.facing, 'EAST')

    def test_robot_call_left(self):
        subject = Robot()
        subject.call('LEFT')

        self.assertEqual(subject.x, 0)
        self.assertEqual(subject.y, 0)
        self.assertEqual(subject.facing, 'WEST')

    def test_robot_call_right(self):
        subject = Robot()
        subject.call('RIGHT')

        self.assertEqual(subject.x, 0)
        self.assertEqual(subject.y, 0)
        self.assertEqual(subject.facing, 'EAST')

    def test_robot_call_move(self):
        subject = Robot()
        subject.call('MOVE')

        self.assertEqual(subject.x, 0)
        self.assertEqual(subject.y, 1)
        self.assertEqual(subject.facing, 'NORTH')

    def test_robot_call_unknown(self):
        subject = Robot()
        subject.call('UNKNOWN')

        self.assertEqual(subject.x, 0)
        self.assertEqual(subject.y, 0)
        self.assertEqual(subject.facing, 'NORTH')


if __name__ == '__main__':
    unittest.main()
