from functools import partial
from typing import cast

import pygame as pg

from src import config
from src.bases import GUIBase
from src.interfaces.elements import Button, GUIColors, Menu
from src.misc.states import Mode
from src.misc.type_aliases import Resolution, ResultToDrawing


class GUI(GUIBase):
    """A user interface class that renders all interactive parts of the game.

    Attributes:
        screen: The main surface on which the user interface is rendered.
        resolution: The resolution of window game.
        buttons: Dictionary of all game buttons
                    - Moore
                    - Neumann
                    - open menu
                    - hide menu

        hide_menu: The flag that determines whether the menu or the Internet is closed.

        __menu: Side-Menu object which include another buttons.
        __drawing_cells: Result to drawing cells on playing area.

    """

    __menu: Menu
    __drawing_cells: ResultToDrawing

    def __init__(self, screen: pg.SurfaceType, resolution: Resolution) -> None:
        self.screen = screen
        self.resolution = resolution

        self.hide_menu = False
        self.__menu = Menu(
            parent_resolution=self.resolution,
            height=int(self.resolution.height * 0.16 * 2),
            width=int(self.resolution.width * 0.08),
        )

        self.buttons = {}
        self._init_buttons()

        self._draw_bg_rect_on_display = partial(pg.draw.rect, surface=self.screen, color=GUIColors.INTERFACE.rgb())
        self._draw_frame_rect_on_display = partial(pg.draw.rect, surface=self.screen, color=GUIColors.BLACK.rgb())

        self.__drawing_cells = []

    @property
    def drawing_cells(self) -> ResultToDrawing:
        """Property for `drawing_cells` attribute."""
        return self.__drawing_cells

    @drawing_cells.setter
    def drawing_cells(self, value: ResultToDrawing) -> None:
        self.__drawing_cells = value

    def _init_buttons(self) -> None:
        """Initializes buttons."""
        self.buttons["hide_menu"] = Button(
            left=self.__menu.x + self.__menu.width - self.__menu.radius,
            top=self.__menu.y + self.__menu.height - self.__menu.height * 0.01,
            width=self.__menu.radius * 2,
            height=self.__menu.radius * 2,
            draw=True,
        )
        self.buttons["open_menu"] = Button(
            left=-self.resolution.width * 0.02,
            top=self.resolution.height / 2 - self.resolution.height * 0.2 / 2,
            width=self.resolution.width * 0.04,
            height=self.resolution.height * 0.2,
            draw=False,
        )
        self.buttons["Moore"] = Button(
            left=self.__menu.x * 2,
            top=self.__menu.y + self.__menu.x,
            width=self.__menu.width - self.__menu.x * 2,
            height=self.__menu.width - self.__menu.x * 2,
            draw=True,
        )
        self.buttons["Neumann"] = Button(
            left=self.__menu.x * 2,
            top=self.__menu.y + self.__menu.width + self.__menu.x,
            width=self.__menu.width - self.__menu.x * 2,
            height=self.__menu.width - self.__menu.x * 2,
            draw=True,
        )

        self.buttons["Moore"].drawing_name("M")
        self.buttons["Neumann"].drawing_name("N")

    def draw_cells(self) -> None:
        """Draws the cells in self.area on the monitor."""
        for x, y in self.drawing_cells:
            pg.draw.rect(
                surface=self.screen,
                color=config.GameSettings.GUIColors.cell.get_rgb(),
                rect=(
                    x * config.GameSettings.Sizes.cell,
                    y * config.GameSettings.Sizes.cell,
                    config.GameSettings.Sizes.cell - 1,
                    config.GameSettings.Sizes.cell - 1,
                ),
            )

    def draw_menu(self, mode: Mode) -> None:
        """Draws a menu containing buttons on the left.

        The menu can be hidden by clicking on the arrow in the lower right
        corner of the menu. You can also open by clicking on the button at
        the left border of the screen if self.hide_menu is True.

        The menu is drawn relative to the size of the window. It all depends
        on the length and width of the window.

        Returns:
            None

        """
        if not self.hide_menu:
            params = {"rect": self.__menu.rect, "border_radius": self.__menu.radius}
            self._draw_bg_rect_on_display(**params)
            self._draw_frame_rect_on_display(**params, width=2)

            font = pg.font.SysFont("arial", int(self.buttons["open_menu"].width / 2.8))
            img = font.render(f"Mode: {mode.name[0]}", True, GUIColors.WHITE.rgb())  # noqa: FBT003
            self.screen.blit(
                img,
                (
                    self.__menu.rect.left + self.__menu.rect.width / 2 - img.get_width() / 2,
                    self.__menu.rect.top + self.__menu.rect.height - img.get_height() - self.__menu.rect.left,
                ),
            )

            params = {
                "surface": self.screen,
                "center": (
                    self.__menu.x + self.__menu.width,  # x
                    self.__menu.y + (self.__menu.parent_resolution.height / 2) * 2 + self.resolution.width * 0.01,  # y
                ),
                "radius": self.__menu.radius,
            }

            pg.draw.circle(**params, color=GUIColors.WHITE.rgb())  # type: ignore
            pg.draw.circle(**params, color=GUIColors.BLACK.rgb(), width=2)  # type: ignore
        else:
            width_open_menu = self.resolution.width * 0.04
            params = {
                "rect": (
                    -width_open_menu / 2,  # x
                    self.resolution.height / 2 - self.resolution.height * 0.2 / 2,  # y
                    width_open_menu,  # width
                    self.resolution.height * 0.2,  # height
                ),
                "border_radius": self.__menu.radius,
            }
            self._draw_bg_rect_on_display(**params)
            self._draw_frame_rect_on_display(**params, width=2)

    def draw_buttons(self) -> None:
        """Renders all buttons located in `self.buttons` dictionary if `self.hide_menu` is False."""
        if not self.hide_menu:
            for button in [btn for btn in self.buttons.values() if btn.draw is not False]:
                params = {"rect": button.coord, "border_radius": self.__menu.radius}

                self._draw_bg_rect_on_display(**params)
                self._draw_frame_rect_on_display(**params, width=2)

            font = pg.font.SysFont("arial", int(self.buttons["open_menu"].width))

            # drawing text on buttons
            for button in [btn for btn in self.buttons.values() if btn.name is not None]:
                button.name = cast(str, button.name)
                img = font.render(button.name, True, GUIColors.WHITE.rgb())  # noqa: FBT003
                self.screen.blit(
                    img,
                    (  # render text in center of button
                        button.width / 2 - (font.size(button.name)[0] / 2) + button.left,  # x for text
                        button.height / 2 - (font.size(button.name)[1] / 2) + button.top,  # y for text
                    ),
                )

    def draw_fps(self, frame_per_second: int) -> None:
        """Draws FPS on the screen in the upper right corner of the game.

        Args:
            frame_per_second: Just a number that will be displayed as fps
                on the screen.

        Returns:
            None

        """
        radius = int(self.resolution.width * 0.04)
        height = int(self.resolution.height * 0.08)

        width_point = int(self.resolution.width * 0.94)
        height_point = -int(height / 2)

        params = {"rect": (width_point, height_point, 1000, height), "border_radius": radius}
        self._draw_bg_rect_on_display(**params)
        self._draw_frame_rect_on_display(**params, width=2)

        font = pg.font.SysFont("arial", int(height / 3))

        # Draw red fps if it's too low
        color = GUIColors.RED.rgb() if frame_per_second <= config.GameSettings.low_fps else GUIColors.GREEN.rgb()

        img = font.render(f"fps {frame_per_second}", True, color)  # noqa: FBT003
        self.screen.blit(img, (self.resolution.width * 0.952, self.resolution.height * 0.004))

    def fill_bg(self) -> None:
        """Fill screen background color."""
        self.screen.fill(GUIColors.BG.rgb())

    def update_display(self) -> None:
        """Update screen."""
        pg.display.update()
