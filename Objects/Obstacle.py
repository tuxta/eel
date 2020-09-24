from GameFrame import RoomObject, Globals


class Obstacle(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.set_image(self.load_image('obstacle.png'), Globals.block_size, Globals.block_size)

        self.set_timer(360, self.end_it)

    def end_it(self):
        self.delete_object(self)
