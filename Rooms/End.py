from GameFrame import Level, TextObject, Globals


class End(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        score = TextObject(
            self,
            Globals.SCREEN_WIDTH / 2,
            Globals.SCREEN_HEIGHT / 2,
            f"SCORE : {Globals.SCORE}",
            colour=(255, 255, 255)
        )
        score.x -= score.width / 2
        score.y -= score.height / 2

        self.add_room_object(score)

        self.set_timer(90, self.restart_game)

    def restart_game(self):
        self.running = False
