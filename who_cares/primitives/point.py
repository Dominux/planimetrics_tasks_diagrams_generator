from numbers import Number

import drawSvg as draw


class Point(draw.Circle):
    def __init__(
        self,
        x: Number,
        y: Number,
        size: Number,
        fill: str,
    ) -> None:
        super().__init__(cx=x, cy=y, r=size, fill=fill)
