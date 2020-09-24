from GameFrame import RoomObject, Globals


class Eel(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.set_image(self.load_image('block.png'), Globals.block_size, Globals.block_size)

        self.register_collision_object('Eel')
        self.register_collision_object('Obstacle')

    def handle_collision(self, other, other_type):
        if other_type == 'Eel':
            self.room.end_game()
        elif other_type == 'Obstacle':
            self.delete_object(other)
            Globals.SCORE += 1
