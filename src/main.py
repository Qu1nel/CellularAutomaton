import pygame as pg
from loguru import logger
from pydantic import PositiveInt
from pygame.event import EventType

from src import config
from src.bases import AppBase
from src.engines import GameEngine
from src.interfaces import GUI
from src.misc.handlers import handle_event_for_key_event, handle_event_for_mouse_event
from src.misc.states import ARGV
from src.misc.type_aliases import Resolution
from src.misc.utils import exit_from_app_with_code


class App(AppBase):
    """The main class of the game.

    Attributes:
        show_fps: A flag that determines whether to show fps or not.
        resolution: Resolution of window game.
        pause: The flag that determines the pause in the game

        screen: A screen api for drawing surface.
        clock: The clock for count fps in game.

        engine: The game engine.
        gui: The GUI of all game.

    """

    show_fps: PositiveInt

    def __init__(self, resolution: Resolution) -> None:
        super().__init__(res=resolution, pause=False)

        self.gui = GUI(self.screen, self.resolution)
        self.engine = GameEngine(app=self)

    def init(self, argv: ARGV) -> None:
        """Post initialization of class attributes from command line values."""
        self.show_fps = argv.show_fps
        self.engine.mode = argv.mode

    def _match_type(self, event: EventType) -> None:
        """Compares events and, depending on its type, determines further actions.

        Args:
            event: The event can be from the keyboard or mouse.

        Returns:
            None
        """
        match event.type:
            case pg.QUIT:
                logger.info("The user clicked on the cross")
                exit_from_app_with_code(0)
            case pg.KEYDOWN:
                logger.info("The user clicked on the key")
                handle_event_for_key_event(event, self)
            case pg.MOUSEBUTTONDOWN:
                logger.info("The user interacts with the mouse")
                handle_event_for_mouse_event(event, self)

    def _handle_events(self) -> None:
        """Processes events entered by the user.

        Calls the auxiliary function _math_type() to determine the type of event.

        Returns:
            None
        """
        for event in pg.event.get():
            self._match_type(event)

    def _draw(self) -> None:
        """Draws a picture on the display."""
        self.gui.fill_bg()
        self.gui.draw_cells()
        self.gui.draw_menu(mode=self.engine.mode)
        self.gui.draw_buttons()

        if self.show_fps:
            current_fps = int(self.clock.get_fps())
            self.gui.draw_fps(frame_per_second=current_fps)

        self.gui.update_display()
        self.clock.tick(config.GameSettings.fps if not self.pause else config.GameSettings.chill_fps)

    def _process(self) -> None:
        """Calculates necessary before trapping events."""
        if not self.pause:
            self.gui.drawing_cells = self.engine.process()

    def _loop(self) -> None:
        """Endless* game loop.

        Catches events from the user.
        Calculates the required steps for the game.
        Draws an image on the screen.
        Updates the frame rate.

        Returns:
            None
        """
        while True:
            self._handle_events()
            self._process()
            self._draw()

    def _run(self) -> None:
        """Gameplay handler and exception maintenance."""
        try:
            self._loop()
        except KeyboardInterrupt:
            logger.debug("A KeyboardInterrupt exception was caught")
            exit_from_app_with_code(0)

    def start(self) -> None:
        """Alias `run` for start a game."""
        self._run()


@logger.catch()
def _init(argv: ARGV) -> App:
    """The main init function of GameOfLive."""
    game = App(resolution=config.WindowConfig.resolution)
    game.init(argv)
    return game
