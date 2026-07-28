from __future__ import annotations

from abc import ABC, abstractmethod

import discord


class Scene(ABC):
    """
    Base class for every scene in Soul World.

    A Scene is responsible only for constructing the
    Discord content required for that checkpoint.

    It NEVER:
    - Updates SQL
    - Decides game logic
    - Decides player progression

    Those responsibilities belong to:
        - PlayerService
        - JourneyService
        - CheckpointManager
    """

    def __init__(
        self,
        player,
        hero=None
    ):

        self.player = player
        self.hero = hero

    @property
    @abstractmethod
    def scene_name(self) -> str:
        """
        Unique scene identifier.

        Example:
            ARRIVAL
            WELCOME
            COLLAPSE
        """
        pass

    @abstractmethod
    def build_embed(self) -> discord.Embed:
        """
        Returns the embed shown for this scene.
        """
        pass

    @abstractmethod
    def build_view(self) -> discord.ui.View | None:
        """
        Returns the Discord View attached to the scene.

        Return None if the scene has no buttons.
        """
        pass