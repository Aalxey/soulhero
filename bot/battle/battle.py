import uuid


class Battle:

    def __init__(

        self,

        player1,

        player2

    ):

        self.id = str(uuid.uuid4())

        self.player1 = player1
        self.player2 = player2

        self.turn = player1.discord_id

        self.finished = False