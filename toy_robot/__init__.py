from robot import Robot


def main(argv=None):
    robot = Robot()
    command = ''

    while command != 'EXIT':
        args = ''
        line = raw_input('')

        input_args = line.split()
        command = input_args[0]
        if len(input_args) > 1:
            args = input_args[1]

        robot.call(command, args)
