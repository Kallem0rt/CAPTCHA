import random
import string
from typing import Tuple
from PIL import Image, ImageDraw, ImageFont


class Captcha:
    def __init__(self, text=None, size=(256, 48), background=(256, 256, 256, 256), text_size=32):
        self.draw = None
        self.size = size
        self.background = background
        self.image = Image.new('RGBA', self.size, self.background)
        self.draw = ImageDraw.Draw(self.image)
        self.text = text if text else self.text()
        self.text_size = text_size

    @staticmethod
    def text(size=6, chars=string.ascii_uppercase + string.digits) -> str:
        return ''.join(random.choice(chars) for _ in range(size))

    def draw_text(self) -> None:
        font = ImageFont.truetype("font.otf", size=self.text_size)
        px, py = 0, 0
        for i in self.text:
            image2 = Image.new('RGBA', (self.text_size, self.text_size), (0, 0, 0, 0))
            draw2 = ImageDraw.Draw(image2)
            draw2.text((0, 0), text=i, font=font, fill=self.color())
            image2 = image2.rotate(random.randint(0, 30), expand=1)
            px += self.text_size
            sx, sy = image2.size
            self.image.paste(image2, (px, py, px + sx, py + sy), image2)
        self.image.show()

    def draw_lines(self) -> None:
        for i in range(random.randint(3, 10)):
            start = random.randint(0, self.size[0]), random.randint(0, self.size[1])
            end = random.randint(0, self.size[0]), random.randint(0, self.size[1])
            self.draw.line([start, end], fill=self.color(), width=3)

    def draw_points(self, size) -> None:
        for x in range(size[0]):
            for y in range(size[1]):
                if x + y >= random.randint(0, size[0] + size[1]):
                    self.draw.point([x, y], fill=self.color())

    @staticmethod
    def color() -> Tuple[int, int, int]:
        return tuple((random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)))


capt = Captcha()

capt.draw_lines()

capt.draw_text()
