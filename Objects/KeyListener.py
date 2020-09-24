from GameFrame import RoomObject
import pygame


class KeyListener(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.set_image(self.load_image('listener.png'), 1, 1)
        self.can_key = True
        self.handle_key_events = True

    def key_pressed(self, key):
        if self.can_key:
            if key[pygame.K_LEFT]:
                self.can_key = False
                self.set_timer(10, self.reset_key)
                self.room.left_key()
            elif key[pygame.K_RIGHT]:
                self.can_key = False
                self.set_timer(10, self.reset_key)
                self.room.right_key()

    def reset_key(self):
        self.can_key = True
