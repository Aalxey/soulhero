from bot.services.player_service import PlayerService


hero = PlayerService.get_player_hero(
    "762322750978916362"
)


print(hero)