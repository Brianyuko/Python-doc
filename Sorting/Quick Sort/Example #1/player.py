class Player:

    daftar_pemain = []

    def __init__(self,
        name,
        number,
        height,
        weight,
        position,
        shot_power,
        curve,
        penalties,
        gk_reflexes,
    ):
        self.__name = name
        self.__number = number
        self.__height = height
        self.__weight = weight
        self.__position = position
        self.__shot_power = shot_power
        self.__curve = curve
        self.__penalties = penalties
        self.__gk_reflexes = gk_reflexes
        self.__class__.daftar_pemain.append(self)

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    def get_height(self):
        return self.__height

    def get_weight(self):
        return self.__weight

    def get_position(self):
        return self.__position

    def get_shot_power(self):
        return self.__shot_power

    def get_curve(self):
        return self.__curve

    def get_penalties(self):
        return self.__penalties

    def gk_reflexes(self):
        return self.__gk_reflexes
    
    def __str__(self):
        text = "\033[1mName:\033[0m " + self.__name + "\n"
        text += "\033[1mKit Number:\033[0m " + str(self.__number) + "\n"
        text += "\033[1mHeight:\033[0m " + str(self.__height) + "\n"
        text += "\033[1mWeight:\033[0m " + str(self.__weight) + "\n"
        text += "\033[1mPosition:\033[0m " + str(self.__position) + "\n"
        text += "\033[1mShot Power:\033[0m " + str(self.__shot_power) + "\n"
        text += "\033[1mCurve:\033[0m " + str(self.__curve) + "\n"
        text += "\033[1mPenalties:\033[0m " + str(self.__penalties) + "\n"
        text += "\033[1mGK Reflexes:\033[0m " + str(self.__gk_reflexes) + "\n"
        return text
