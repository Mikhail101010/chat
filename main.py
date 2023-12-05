class Mood:
    mood = {}

    @classmethod
    def set(cls, mood, value):
        cls.mood[mood] = value
    
    @classmethod
    def change(cls, mood, value):
        if cls.mood[mood]:
            cls.mood[mood] += value
        else:
            cls.set(mood, value)


class Chance:
    def __init__(self, value, **mood);


class ResponseOption:
    def __init__(self, value, chance, require):


class
