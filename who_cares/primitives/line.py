from numbers import Number

import drawSvg as draw


class Line(draw.Line):
    def __init__(
        self,
        x1: Number,
        y1: Number,
        x2: Number,
        y2: Number,
        stroke_width: Number,
        stroke: str,
    ) -> None:
        super().__init__(
            sx=x1, sy=y1, ex=x2, ey=y2, stroke_width=stroke_width, stroke=stroke
        )
