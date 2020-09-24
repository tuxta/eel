from GameFrame import Level, TextObject, Globals


class Start(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        start_text = TextObject(
            self,
            Globals.SCREEN_WIDTH / 2,
            Globals.SCREEN_HEIGHT / 2,
        )
        start_text.colour = (255, 0, 0)
        start_text.text = "The EEL game!"
        start_text.update_text()

        self.add_room_object(start_text)
        start_text.x -= start_text.width / 2
        start_text.y -= start_text.height / 2

        self.set_timer(90, self.start_game)

    def start_game(self):
        Globals.SCORE = 0
        self.running = False
