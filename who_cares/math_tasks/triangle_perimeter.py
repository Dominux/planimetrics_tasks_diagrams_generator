from base import MathTask


class TrianglePerimeterTask(MathTask):
    prompt_template = """
        Сторона {side_1} треугольника {triangle} равна {side_1_size} {units_1}, 
        сторона {side_2} вдвое больше стороны {side_1}, 
        а сторона {side_3} на {side_3_side_2_diff} {units_2} меньше сторона {side_2}.
        Найдите периметр треугольника {triangle}.
    """
