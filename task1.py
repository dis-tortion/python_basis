'''
1. Создать класс TrafficLight (светофор) и определить у него один атрибут
    color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
    В рамках метода реализовать переключение светофора в режимы:
    красный, желтый, зеленый. Продолжительность первого состояния (красный)
    составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
    на ваше усмотрение. Переключение между режимами должно осуществляться
    только в указанном порядке (красный, желтый, зеленый).
    Проверить работу примера, создав экземпляр и вызвав описанный метод.
    Задачу можно усложнить, реализовав проверку порядка режимов, и при его
    нарушении выводить соответствующее сообщение и завершать скрипт.
'''
import sys
import time
import itertools


class TrafficLight:
    __color = 'RED'
    _lights_duaration_info = [('RED', 1), ('YELLOW', 1), ('GREEN', 1)]

    def __init__(self):
        self.full_cycle_duaration = sum(
            [d for c, d in self._lights_duaration_info]
        )
        self.is_running = False

    def running(self):
        self.time_start = time.time()
        self.is_running = True

    def get_color(self):
        if self.is_running:
            delta_time = time.time() - self.time_start
            light_epoch = delta_time % self.full_cycle_duaration
            tmp_duaration_sum = 0
            for light, duaration in self._lights_duaration_info:
                tmp_duaration_sum += duaration
                if light_epoch <= tmp_duaration_sum:
                    break
            self.__color = light

        return self.__color


if __name__ == '__main__':
    N_ITERATIONS = 5

    print('Тест светофора')
    tl = TrafficLight()
    time_check_list_iter = itertools.cycle(
        [d for c, d in tl._lights_duaration_info])
    light_status_iter = itertools.cycle(
        [c for c, d in tl._lights_duaration_info])

    tl.running()

    print(f'Запускаем {N_ITERATIONS} тестовых итераций')
    prev_duaration = 0
    for _ in range(N_ITERATIONS):
        light_duaration = next(time_check_list_iter)
        sleep_time = (prev_duaration + light_duaration) / 2
        time.sleep(sleep_time)
        next_color = next(light_status_iter)
        curr_color = tl.get_color()
        if curr_color != next_color:
            print(
                f'Светофор сломался! '
                f'Должен быть {next_color}, а загорелся {curr_color}')
            sys.exit(-1)
        print(
            f'Текущий цвет светофора - {tl.get_color()}')
        prev_duaration = light_duaration
