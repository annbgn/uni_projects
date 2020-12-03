1. датасет видов стекла
1. целевой столбец - последний
1. метки классов: 
      - 1 building_windows_float_processed
      - 2 building_windows_non_float_processed
      - 3 vehicle_windows_float_processed
      - 4 vehicle_windows_non_float_processed (none in this database)
      - 5 containers
      - 6 tableware
      - 7 headlamps
1. переставить местами строки (с помощью скрипта Python и функций библиотеки pandas)
так, чтобы данные одного класса были расположены подряд, [код](https://github.com/annbgn/uni_projects/blob/master/perceptron/script.py#L38)
1. произвести дискретизацию числовых столбцов (один числовой столбец превращается при
этом в несколько – обычно три – категориальных) (функция cut), [код](https://github.com/annbgn/uni_projects/blob/master/perceptron/script.py#L41)
1. произвести бинаризацию категориальных столбцов (функция get_dummies), [код](https://github.com/annbgn/uni_projects/blob/master/perceptron/script.py#L55)
1. для однослойного персептрона перевести данные из 0, 1 в -1, 1, [код](https://github.com/annbgn/uni_projects/blob/master/perceptron/script.py#L58)
1. выделить данные для обучения (80%) и для тестирования (20%), [код](https://github.com/annbgn/uni_projects/blob/master/perceptron/script.py#L66)
1. выделить входные и желаемые выходные данные (желаемые выходные данные
получаются из столбцов, в которые превратился целевой столбец – этих столбцов будет
столько, сколько меток классов было в целевом столбце), это выделение происходит как в
данных для обучения, так и в данных для тестирования, [код](https://github.com/annbgn/uni_projects/blob/master/perceptron/script.py#L70) 
1. применить однослойный персептрон, [код](https://github.com/annbgn/uni_projects/blob/master/perceptron/script.py#L81-L144)
1. применить многослойный персептрон, [код](https://github.com/annbgn/uni_projects/blob/master/perceptron/script.py#L147-L210)
1.  записать результаты тестирования, [код](https://github.com/annbgn/uni_projects/blob/master/perceptron/script.py#L142-L144) [код](https://github.com/annbgn/uni_projects/blob/master/perceptron/script.py#L208-L210)
1. подготовить краткий отчет: какой дейтасет использовался, сколько столбцов и сколько
строк в дейтасете, имена столбцов, какой по порядку целевой столбец, каковы результаты
тестирования для однослойного персептрона, каковы результаты тестирования для
многослойно сети (многослойного персептрона) – (каково количество и процент ошибок
при тестировании). [отчет](https://github.com/annbgn/uni_projects/blob/master/perceptron/%D0%BE%D1%82%D1%87%D0%B5%D1%82.md)
