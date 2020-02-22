# method-optimization-resit

Запуск производится из pycharm. 
Для запуска нужно переопределить environment/working directory на корень репозитория.

## Генерации данных:

src/generated_dataset/generated_dataset.py

Есть обязательный параметр function_name

подробнее про аргументы запуска в src/generate_dataset/args.py

Для удобства на каждую функцию сделан отдельный файл 
(src/generated_dataset/args_settings/*),
в котором можно указать и сохранить отдельные конкретные настройки 
для данного метода. По умолчанию эта функцию отключена. 
Чтобы ее включить, добавьтe --use_save_args_settings

Здесь также можно посмотреть на формат принимаемых данных

## Запуск метода оптимизации:

src/main/main.py


Есть два обязательный аргумента: optim_method, function_name 

подробнее про аргументы запуска в src/main/args.py

Для удобства на каждую пару (optim_method, function_name) сделан отдельный файл 
(src/main/args_settings/*),
в котором можно указать и сохранить отдельные конкретные настройки 
для данного метода. По умолчанию эта функцию отключена. 
Чтобы ее включить, добавьтe --use_save_args_settings

## Постановка задачи
./task.pdf

## Простой способ проверить, что что-то работает

PYTHONPATH="." python src/generate_dataset/generate_dataset.py --function_name poisson_regression --use_save_args_settings

PYTHONPATH="." python src/main/main.py --function_name poisson_regression --optim_method adam --use_save_args_settings



# Примечания
Так как мы рассматриваем пуассоновскую регрессию, 
ответ найденый алгоритмом, может быть лучше сгенерированного изначально

Все алгоритмы запускались и тестировались только с одним типом stop_condition,
остановкой по количеству итераций. Так как не было поставленно задачи 
по поддержанию различных условий остановки. На данном этапе не рекомендуется 
использовать другой критерии остановки.
