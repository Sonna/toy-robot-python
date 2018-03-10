from robot import Robot


def main():
    """Entry point for the application script"""
    print('hello world')


def main_loop():
    robot = Robot()
    command = ''

    while command != 'EXIT':
        args = ''
        line = raw_input('')
        # command, args = line.split(r'[ \n]')
        # values = line.split(r'[ \n]')
        values = line.split()
        command = values[0]
        if len(values) > 1:
            args = values[1]

        robot.call(command, args)
