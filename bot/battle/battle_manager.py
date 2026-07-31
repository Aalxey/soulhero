class BattleManager:

    _battles = {}

    @classmethod
    def create(cls, battle):

        cls._battles[battle.id] = battle

        return battle

    @classmethod
    def get(cls, battle_id):

        return cls._battles.get(battle_id)

    @classmethod
    def remove(cls, battle_id):

        cls._battles.pop(battle_id, None)