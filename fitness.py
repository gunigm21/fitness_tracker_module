M_IN_KM = 1000
M_IN_H = 60


class InfoMessage:
    def __init__(self, 
                 training_type: str, 
                 duration: float, 
                 distance: float, 
                 speed: float, 
                 calories: float
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):
        output = (f'Тип тренировки: {self.training_type};'
                  f'Длительность: {self.duration} ч.;'
                  f'Дистанция: {self.distance:.3f} км;'
                  f'Ср. скорость: {self.speed:.3f} км/ч;'
                  f'Потрачено ккал: {self.calories:.3f}.'
                  )
        print (output)


class Training:
    LEN_STEP = 0.65
    def __init__(self, 
                 action: int, 
                 duration: float, 
                 weight: float
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self):
        distance = self.action * self.LEN_STEP / M_IN_KM
        return distance
    
    def get_mean_speed(self):
        speed = self.get_distance() / self.duration
        return speed 
    
    def get_spent_calories(self):
        pass

    def show_training_info(self):
        return InfoMessage(self.__class__.__name__,
                           self.duration, 
                           self.get_distance(), 
                           self.get_mean_speed(), 
                           self.get_spent_calories()
                           )
    

class Running(Training):
    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79 
    
    def __init__(self, 
                 action: int, 
                 duration: float, 
                 weight: float
                 ) -> None:
        super().__init__(action, duration, weight)

    def get_spent_calories(self):
        calories = ((self.CALORIES_MEAN_SPEED_MULTIPLIER 
                     * self.get_mean_speed() 
                     + self.CALORIES_MEAN_SPEED_SHIFT)
                    * self.weight / M_IN_KM * self.duration
                    ) 
        return calories


class SportsWalking(Training):
    CALORIES_COEF1 = 0.035
    CALORIES_COEF2 = 0.029

    def __init__(self, 
                 action: int, 
                 duration: float, 
                 weight: float,
                 height: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self):
        calories = ((self.CALORIES_COEF1 * self.weight
                     + (self.get_mean_speed()**2 / self.height)
                     * self.CALORIES_COEF2 * self.weight) 
                     * self.duration
                     ) 
        return calories


class Swimming(Training):
    LEN_STEP = 1.38
    CALORIES_COEF1 = 1.1
    CALORIES_COEF2 = 2

    def __init__(self, 
                 action: int, 
                 duration: float, 
                 weight: float,
                 length_pool,
                 count_pool
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self):
        speed = (self.length_pool * self.count_pool 
                 / M_IN_KM / self.duration)
        return speed
    
    def get_spent_calories(self):
        calories = ((self.get_mean_speed() + self.CALORIES_COEF1)
                    * self.CALORIES_COEF2 * self.weight * self.duration)
        return calories


def read_package(workout_type, data):
    '''Функция read_package() должна определить тип тренировки и создать объект соответствующего класса, 
    передав ему на вход параметры, полученные во втором аргументе. Этот объект функция должна вернуть.
Функция read_package() должна принимать на вход код тренировки и список её параметров.
В теле функции (или рядом с ней) должен быть словарь, в котором сопоставляются коды тренировок и классы, 
какие нужно вызвать для каждого типа тренировки.'''
    training_dict = {'SWM': Swimming,
                     'RUN': Running,
                     'WLK': SportsWalking
                     }
    training_type = training_dict[workout_type](*data)
    return training_type

def main(training: Training):
    info = training.show_training_info()
    print(info.get_message())

if __name__ == '__main__':
    packages = [        
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training) 
