import drawSvg as draw

from who_cares.primitives import Point, Line


d = draw.Drawing(10, 10, origin="center")

p1 = Point(0, 0, 0.025, "red")
p2 = Point(0, 1, 0.025, "red")
p3 = Point(1, 1, 0.025, "red")

line1 = Line(0, 0, 0, 1, 0.025, "red")
line2 = Line(0, 1, 1, 1, 0.025, "red")
line3 = Line(1, 1, 0, 0, 0.025, "red")

for el in (p1, p2, p3, line1, line2, line3):
    d.append(el)

d.saveSvg("lmao.svg")
