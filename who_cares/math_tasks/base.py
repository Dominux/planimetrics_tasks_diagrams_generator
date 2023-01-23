import abc


class MathTask(abc.ABC):
    """
    Base class for math tasks
    """

    prompt_template: str = ""
