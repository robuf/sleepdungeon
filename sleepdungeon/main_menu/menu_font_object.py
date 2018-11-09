from ..base.sprite import Sprite
from ..base.context import Context
from ..base.game_constants import SpriteType
from ..render_context import RenderContext
from ..res import FONT_DIR
from typing import Dict, List

from enum import Enum
import pygame

CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

class MenuFontState(Enum):
    INVISIBLE = 1
    BLEND_IN = 2
    VISIBLE = 3
    BLEND_OUT = 4

class MenuFontObject(Sprite):
    __GLYPHS: Dict[str, pygame.Surface] = {}
    __FONT: pygame.font.Font = None
    _WIDTH = 0
    _ANIMATION_LENGTH = 500
    _HEIGHT = 0
    def __init__(self, text: str, pos: List[int], visible = False):
        super().__init__()
        self.z_index = 10
        self.text = text
        self.new_text = None
        self.pos = pos
        self.state = MenuFontState.VISIBLE if visible else MenuFontState.INVISIBLE
        self.animation_t = 0
        self.glyph_delay = self._ANIMATION_LENGTH / len(text) * .7
        self.glyph_period = self._ANIMATION_LENGTH / len(text) * (1/.7)

    def blend_in(self):
        self.animation_t = 0
        self.state = MenuFontState.BLEND_IN

    def blend_out(self):
        self.animation_t = 0
        self.state = MenuFontState.BLEND_OUT

    def renew_text(self, text):
        if self.state == MenuFontState.VISIBLE:
            self.animation_t = 0
            self.state = MenuFontState.BLEND_OUT
            self.new_text = text
        else:
            self.text = text

    def update(self, context: Context):
        if self.state == MenuFontState.BLEND_IN:
            self.animation_t += context.delta_t
            if self.animation_t > self._ANIMATION_LENGTH:
                self.animation_t = 0
                self.state = MenuFontState.VISIBLE
        if self.state == MenuFontState.BLEND_OUT:
            self.animation_t += context.delta_t
            if self.animation_t > self._ANIMATION_LENGTH:
                self.animation_t = 0
                if self.new_text is not None:
                    self.state = MenuFontState.BLEND_IN
                    self.text = self.new_text
                    self.new_text = None
                else:
                    self.state = MenuFontState.INVISIBLE

    @classmethod
    def update_render_context(cls, render_context: RenderContext):
        cls.__FONT = pygame.font.Font(
            FONT_DIR + "Game_font.ttf",
            int(cls.tile_size * 1)
        )

        cls._WIDTH = render_context.resolution[0]
        cls._HEIGHT = cls.__FONT.size(CHARSET)[1]

        for c in CHARSET:
            cls.__GLYPHS[c] = cls.__FONT.render(c, True, (20,20,20))

    @property
    def image(self) -> pygame.Surface:
        if self.state == MenuFontState.INVISIBLE:
            return None
        img = pygame.Surface(self.rect.size).convert_alpha()
        img.fill((0,0,0,0))
        text_pos = self.pos[0] * self.scaling

        for c, i in zip(self.text, range(len(self.text))):
            glyph_pos = text_pos + self.__FONT.size(self.text[:i])[0]
            glyph_anim_start = (len(self.text) - i - 1) * self.glyph_delay
            glyph_anim_end = glyph_anim_start + self.glyph_period
            if self.animation_t < glyph_anim_start:
                pre_anim_visible_states = (
                    MenuFontState.VISIBLE,
                    MenuFontState.BLEND_OUT
                )
                if self.state not in pre_anim_visible_states:
                    continue
            elif glyph_anim_start <= self.animation_t < glyph_anim_end:
                anim = (self.animation_t - glyph_anim_start) / self.glyph_period

                if self.state == MenuFontState.BLEND_IN:
                    glyph_pos = int(glyph_pos * ((anim) ** 2))
                elif self.state == MenuFontState.BLEND_OUT:
                    glyph_pos = glyph_pos + int(
                        (self._WIDTH - glyph_pos) * ((anim) ** 2)
                    )
            else:
                if self.state == MenuFontState.BLEND_OUT:
                    continue
            img.blit(
                self.__GLYPHS[c],
                pygame.Rect(
                    (glyph_pos, 0),
                    self.__GLYPHS[c].get_size()
                )
            )
        return img

    @property
    def rect(self) -> pygame.Rect:
        return pygame.Rect(
            0,
            int(self.pos[1] * self.scaling),
            self._WIDTH,
            self._HEIGHT
        )

    @property
    def sprite_type(self):
        return SpriteType.GHOST
