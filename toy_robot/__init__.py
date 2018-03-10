from robot import Robot


def main(argv=None):
    robot = Robot()
    args = ''

    if argv != None and len(argv) > 1:
        filename = argv[1] # get second argv, since 0 is 'toy_robot'

        with open(filename, 'r') as file:
            for line in file:
                input_args = line.split()
                command = input_args[0]

                if len(input_args) > 1:
                    args = input_args[1]

                robot.call(command, args)
    else:
        command = ''

        while command != 'EXIT':
            line = raw_input('')

            input_args = line.split()
            command = input_args[0]
            if len(input_args) > 1:
                args = input_args[1]

            robot.call(command, args)
