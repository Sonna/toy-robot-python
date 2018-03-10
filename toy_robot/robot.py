class Robot:
    MOVE = {
        'NORTH': {'x': 0, 'y': 1},
        'SOUTH': {'x': 0, 'y': -1},
        'EAST': {'x': 1, 'y': 0},
        'WEST': {'x': -1, 'y': 0}
    }

    TURN = {
        'NORTH': {'LEFT': 'WEST', 'RIGHT': 'EAST'},
        'SOUTH': {'LEFT': 'EAST', 'RIGHT': 'WEST'},
        'EAST': {'LEFT': 'NORTH', 'RIGHT': 'SOUTH'},
        'WEST': {'LEFT': 'SOUTH', 'RIGHT': 'NORTH'}
    }

    def __init__(self, x=None, y=None, facing=None):
        if x is None:
            x = 0
        if y is None:
            y = 0
        if facing is None:
            facing = 'NORTH'

        self.x = x
        self.y = y
        self.facing = facing

    def call(self, command, args=None):
        return {
            'PLACE': self.place,
            'MOVE': self.move,
            'LEFT': self.left,
            'RIGHT': self.right,
            'REPORT': self.report
        }.get(command, lambda _: None)(args)

    def place(self, cooridinates):
        dx, dy, dfacing = cooridinates.split(',')
        self.x = int(dx)
        self.y = int(dy)
        self.facing = dfacing

    def report(self, _args=None):
        print('{}, {}, {}'.format(self.x, self.y, self.facing))

    def left(self, _args=None):
        # self.facing = self.TURN.get(self.facing).get('LEFT')
        self.facing = self.TURN[self.facing]['LEFT']

    def right(self, _args=None):
        # self.facing = self.TURN.get(self.facing).get('RIGHT')
        self.facing = self.TURN[self.facing]['RIGHT']

    def move(self, _args=None):
        self.x += self.MOVE[self.facing]['x']
        self.y += self.MOVE[self.facing]['y']

        if (self.x < 0 or self.x > 4):
            self.x -= self.MOVE[self.facing]['x']

        if (self.y < 0 or self.y > 4):
            self.y -= self.MOVE[self.facing]['y']
