from uuid import uuid4

from bot.battle.battle_state import BattleState


class Battle:
    """
    Represents one active battle.

    Battle stores:

    - Battle ID
    - Two combatants
    - Turn order
    - Discord message/channel
    - Winner

    Every player's temporary battle data
    lives inside BattleState.
    """

    def __init__(
        self,
        player_one,
        player_two
    ):

        self.id = str(uuid4())

        # -------------------------
        # Database Players
        # -------------------------

        self.player_one = player_one

        self.player_two = player_two

        # -------------------------
        # Temporary Battle States
        # -------------------------

        self.player_one_state = BattleState(
            player_one
        )

        self.player_two_state = BattleState(
            player_two
        )

        # -------------------------
        # Decide first turn
        # -------------------------

        if (
            self.player_one_state.speed
            >=
            self.player_two_state.speed
        ):

            self.turn = player_one.discord_id

        else:

            self.turn = player_two.discord_id

        # -------------------------
        # Discord
        # -------------------------

        self.channel_id = None

        self.message_id = None

        # -------------------------
        # Battle Result
        # -------------------------

        self.finished = False

        self.winner = None

    # -------------------------------------------------

    @property
    def players(self):

        return (

            self.player_one.discord_id,

            self.player_two.discord_id

        )

    # -------------------------------------------------

    def contains(
        self,
        discord_id: str
    ):

        return str(discord_id) in self.players

    # -------------------------------------------------

    def current_player(self):

        if self.turn == self.player_one.discord_id:

            return self.player_one

        return self.player_two

    # -------------------------------------------------

    def current_state(self):

        if self.turn == self.player_one.discord_id:

            return self.player_one_state

        return self.player_two_state

    # -------------------------------------------------

    def waiting_player(self):

        if self.turn == self.player_one.discord_id:

            return self.player_two

        return self.player_one

    # -------------------------------------------------

    def waiting_state(self):

        if self.turn == self.player_one.discord_id:

            return self.player_two_state

        return self.player_one_state

    # -------------------------------------------------

    def state_of(
        self,
        discord_id: str
    ):

        if str(discord_id) == self.player_one.discord_id:

            return self.player_one_state

        return self.player_two_state

    # -------------------------------------------------

    def opponent(
        self,
        discord_id: str
    ):

        if str(discord_id) == self.player_one.discord_id:

            return self.player_two

        return self.player_one

    # -------------------------------------------------

    def opponent_state(
        self,
        discord_id: str
    ):

        if str(discord_id) == self.player_one.discord_id:

            return self.player_two_state

        return self.player_one_state

    # -------------------------------------------------

    def next_turn(self):

        self.current_state().remove_guard()

        self.current_state().reduce_cooldowns()

        if self.turn == self.player_one.discord_id:

            self.turn = self.player_two.discord_id

        else:

            self.turn = self.player_one.discord_id

    # -------------------------------------------------

    def finish(
        self,
        winner
    ):

        self.finished = True

        self.winner = winner

    # -------------------------------------------------

    def is_finished(self):

        return (

            self.player_one_state.defeated

            or

            self.player_two_state.defeated

        )