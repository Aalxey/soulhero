class CooldownService:
    """
    Handles all cooldown operations.

    Responsible for:

    - Checking cooldown
    - Applying cooldown
    - Reducing cooldowns
    - Resetting cooldowns

    Does NOT:

    - Deal damage
    - Modify HP
    - Handle Discord
    """


    @staticmethod
    def is_ready(
        state,
        skill_slot: str
    ):

        cooldown = state.cooldown(

            skill_slot

        )


        return cooldown <= 0



    # ---------------------------------


    @staticmethod
    def apply(
        state,
        skill_slot: str,
        turns: int
    ):


        state.set_cooldown(

            skill_slot,

            turns

        )



    # ---------------------------------


    @staticmethod
    def reduce(
        state
    ):


        state.reduce_cooldowns()



    # ---------------------------------


    @staticmethod
    def remaining(
        state,
        skill_slot: str
    ):


        return state.cooldown(

            skill_slot

        )