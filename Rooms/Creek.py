from GameFrame import Level, Globals
from Objects import Eel, KeyListener, Obstacle
from random import randint


class Creek(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.grow_count = 0
        self.facing = Globals.down
        
        self.speed = 8
        self.speed_count = 20
        self.speed_counter = 1

        self.key_listener = KeyListener(self, 1, 1)
        self.add_room_object(self.key_listener)
        self.eel = []
        head_eel = Eel(self, 384, 288)
        self.eel.append(head_eel)
        self.add_room_object(head_eel)

        for i in range(4):
            tail_eel = self.eel[-1]
            new_eel = Eel(self, tail_eel.x, tail_eel.y - Globals.block_size)
            self.eel.append(new_eel)
            self.add_room_object(new_eel)

        self.set_timer(10, self.move_snake)
        self.set_timer(120, self.add_obstacle)

    def move_snake(self):
        self.grow_count += 1
        self.grow_count %= self.speed
        if self.grow_count:
            tail_block = self.eel.pop()
            tail_block.x = self.eel[0].x
            tail_block.y = self.eel[0].y
        else:
            tail_block = Eel(self, self.eel[0].x, self.eel[0].y)
            self.add_room_object(tail_block)
        if self.facing == Globals.up:
            tail_block.y = self.eel[0].y - Globals.block_size
        elif self.facing == Globals.down:
            tail_block.y = self.eel[0].y + Globals.block_size
        elif self.facing == Globals.right:
            tail_block.x = self.eel[0].x + Globals.block_size
        else:
            tail_block.x = self.eel[0].x - Globals.block_size

        if tail_block.y < 0 \
                or tail_block.y > Globals.SCREEN_HEIGHT - Globals.block_size \
                or tail_block.x < 0 \
                or tail_block.x > Globals.SCREEN_WIDTH - Globals.block_size:
            self.end_game()

        self.eel.insert(0, tail_block)
        self.set_timer(self.speed, self.move_snake)
        if self.speed > 2:
            self.speed_counter += 1
            self.speed_counter %= self.speed_count
            if not self.speed_counter:
                self.speed -= 1
                self.speed_count += self.speed_count

    def right_key(self):
        self.facing += 1
        self.facing %= 4

    def left_key(self):
        self.facing -= 1
        if self.facing < 0:
            self.facing = 3

    def add_obstacle(self):
        new_obstacle = Obstacle(self, -20, -20)
        self.add_room_object(new_obstacle)
        x = randint(1, int(Globals.SCREEN_WIDTH / Globals.block_size)) * Globals.block_size - Globals.block_size
        y = randint(1, int(Globals.SCREEN_HEIGHT / Globals.block_size)) * Globals.block_size - Globals.block_size
        while new_obstacle.collides_at(new_obstacle, x, y, 'Eel'):
            x = randint(1, int(Globals.SCREEN_WIDTH / Globals.block_size)) * Globals.block_size
            y = randint(1, int(Globals.SCREEN_HEIGHT / Globals.block_size)) * Globals.block_size

        new_obstacle.x = x
        new_obstacle.y = y

        self.set_timer(60, self.add_obstacle)

    def end_game(self):
        self.running = False
