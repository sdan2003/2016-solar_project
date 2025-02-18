# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename, encoding='utf8') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":  ### FIXME: do the same for planet
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == 'planet':
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    list_of_data = line.split()
    star.R = float(list_of_data[1])
    star.color = list_of_data[2]
    star.m = 1000000*float(list_of_data[3])
    star.x = float(list_of_data[4])
    star.y = float(list_of_data[5])
    star.Vx = 1000*float(list_of_data[6])
    star.Vy = 1000*float(list_of_data[7])
    return star
    ### FIXME: not done yet

def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    list_of_data = line.split()
    planet.R = float(list_of_data[1])
    planet.color = list_of_data[2]
    planet.m = 1000000*float(list_of_data[3])
    planet.x = float(list_of_data[4])
    planet.y = float(list_of_data[5])
    planet.Vx = 1000*float(list_of_data[6])
    planet.Vy = 1000*float(list_of_data[7])
    return planet
    ### FIXME: not done yet...


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            if obj.type == 'Star':
                print(out_file, 'Star ' + obj.R + ' ' + obj.color + ' ' + obj.m +
                    ' ' + obj.x + ' ' + obj.y + ' ' + obj.Vx + ' ' + obj.Vy)
            elif obj.type == 'Planet':
                print(out_file, 'Planet ' + str(obj.R) + ' ' + str(obj.color) + ' ' + str(obj.m) +
                    ' ' + str(obj.x) + ' ' + str(obj.y) + ' ' + str(obj.Vx) + ' ' + str(obj.Vy))
            ### FIXME: should store real values
            # Надо посмотреть переход на следующую строку

# FIXME: хорошо бы ещё сделать функцию, сохраняющую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")
