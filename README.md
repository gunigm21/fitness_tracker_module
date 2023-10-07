# Модуль фитнес-трекера.

## Функционал трекера: 
Разработанный программный модуль фитнес-трекера рассчитывает и отображает результаты тренировки. Он обрабатывает данные для трёх видов тренировок: бега, спортивной ходьбы и плавания. Данный модуль принимает от блока датчиков информацию о прошедшей тренировке, определяет вид тренировки, рассчитывает результаты тренировки, выводит информационное сообщение о результатах тренировки. Информационное сообщение включает такие данные: тип тренировки (бег, ходьба или плавание); длительность тренировки; дистанция, которую преодолел пользователь, в километрах; средняя скорость на дистанции, в км/ч; расход энергии, в килокалориях.
 
## Описание модуля:
Программный модуль для фитнес-трекера написан на языке Python с использованием парадигмы ООП. 

Базовый класс Training содержит все основные свойства и методы для тренировок. Каждый класс, описывающий определённый вид спортивной активности, дополняет и расширяет базовый класс: бег → класс Running; спортивная ходьба → класс SportsWalking; плавание → класс Swimming. Конструктор каждого из классов получает информацию с датчиков: action — количество совершённых действий (число шагов при ходьбе и беге либо гребков — при плавании); duration — длительность тренировки; weight — вес спортсмена. Методы базового класса, которые отвечают за обработку данных: get_distance() возвращает дистанцию (в километрах), которую преодолел пользователь за время тренировки; get_mean_speed() возвращает значение средней скорости движения во время тренировки; get_spent_calories() возвращает расчёт количества калорий, израсходованных за тренировку; show_training_info() возвращает объект класса сообщения.

Все свойства и методы дочернего класса Running без изменений наследуются от базового класса, за исключением метода расчёта калорий, который переопределен.
Конструктор класса SportsWalking принимает дополнительный параметр height — рост спортсмена. Расчёт калорий для этого класса также переопределен с учетом особенностей данного вида активности.
Конструктор класса Swimming, кроме свойств базового класса, принимает ещё два параметра: length_pool (длина бассейна в метрах) и count_pool (сколько раз пользователь переплыл бассейн).В классе Swimming переопределен не только метод расчёта калорий, но и метод, который рассчитывает среднюю скорость. Так как расстояние, преодолеваемое за один гребок, отличается от длины шага, то в классе Swimming переопределен также атрибут LEN_STEP базового класса.

Для проверки работоспособности модуля в коде реализована имитация получения данных от блока датчиков фитнес-трекера путем передачи в программу заранее подготовленных тестовых данных.
Последовательность данных в принимаемых пакетах:
Плавание
Код тренировки: 'SWM'.
Элементы списка: количество гребков, время в часах, вес пользователя, длина бассейна, сколько раз пользователь переплыл бассейн.
Бег
Код тренировки: 'RUN'.
Элементы списка: количество шагов, время тренировки в часах, вес пользователя.
Спортивная ходьба
Код тренировки: 'WLK'.
Элементы списка: количество шагов, время тренировки в часах, вес пользователя, рост пользователя.
Программа перебирает в цикле список пакетов, распаковывает каждый кортеж и передаёт данные в функцию read_package(). 

Функция чтения принятых пакетов read_package() определяет тип тренировки и создать объект соответствующего класса, передав ему на вход параметры, полученные во втором аргументе (этот объект функция возвращает): функция read_package() принимает на вход код тренировки и список её параметров; в теле функции расположен словарь, в котором сопоставляются коды тренировок и классы, какие нужно вызвать для каждого типа тренировки. 

Функция main() принимает на вход экземпляр класса Training. При выполнении функции main() для этого экземпляра вызвается метод show_training_info(), результатом выполнения которого является объект класса InfoMessage, который сохраняется в переменную info.
Для объекта InfoMessage, сохранённого в переменной info, вызывается метод, который возвращает строку сообщения с данными о тренировке, которая передается в функцию print().

класс InfoMessage - это самостоятельный класс для создания объектов сообщений. У этого класса имеется метод для вывода сообщений на экран. Объекты этого класса создаются вызовом метода show_training_info() для классов тренировок.
Свойства класса InfoMessage: training_type — имя класса тренировки; duration — длительность тренировки в часах; distance — дистанция в километрах, которую преодолел пользователь за время тренировки; speed — средняя скорость, с которой двигался пользователь;
calories — количество килокалорий, которое израсходовал пользователь за время тренировки. Метод get_message() класса InfoMessage возвращает строку сообщения с информацией о типе тренировки, длительности, дистанции, средней скорости и потраченных калориях. 

## Установка и запуск модуля на локальном компьютере из репозитория GitHub

__Клонируем себе на компьютер репозиторий__: 
```
git clone git@github.com:OksanaAstashkina/fitness_tracker_module.git
```

__Переходим в директорию с клонированным репозиторием__:
```
cd fitness_tracker_module
```

__Разворачиваем в репозитории виртуальное окружение__:
```
python -m venv venv (python3 -m venv venv)
```

__Активируем виртуальное окружение__:
```
source venv/Scripts/activate (для Linux и MacOS: source venv/bin/activate)
```

__Установаем зависимости__:
```
pip install -r requirements.txt
```

__Запускаем модуль трекера__:
```
python fitness_tracker.py
```

***
## *Автор*
Оксана Асташкина - [GitHub](https://github.com/OksanaAstashkina)

### *Дата создания*
Январь, 2023
