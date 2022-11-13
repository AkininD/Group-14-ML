ML14# Group-14-ML

# Обнаружение объектов с помощью DETR (Detection Transformer)
--
учебный проект группы 14 Программная инженерия

#### Оглавление
- Как запустить проект (ссылка)
- итд

### Описание проекта

![DETR](.github/DETR.png)


### Подготовка тестовых данных

Тестовые данные для первичного запуска проекта расположены в директории проекта `originals`.

Тестовые изображения получены из ресурса [cocodataset.org](https://cocodataset.org/), а так же из интернета.

Демонстрационная модель поддерживает только изображения до 1600 пикселей на каждой стороне.


### Требование к окружению:

- Интерпретатор Python не ниже 3.8
- программа для просмотра изображений (jpg)
- подключение к интернету
- OS Ubuntu 20+ (прим: на Mac OS и Windows не тестировалось)

### Как запустить и работать с проектом:

Перед запуском кода необходимо установить зависимости:

```bash
pip install torch
pip inctall matplotlib
pip install timm
```

Помещаем тестовые изображения формата jpg, png в директорий originals
и запускаем проект командой

```bash
python3 main.py
```

### Пример как работает программа

Пример 1.

Оригинальное изображение:

<img src=".github/before1.jpg" alt="cats" width="400"/>

Обработанное изображение:

<img src=".github/after1.jpg" alt="cats" width="400"/>

----

Пример 2.

Оригинальное изображение:
<img src=".github/before2.jpg" alt="cats" width="400"/>

Обработанное изображение:
<img src=".github/after2.jpg" alt="cats" width="400"/>

### Issues

Мы используем GitHub issues для отслеживания ошибок. Пожалуйста, убедитесь, что ваше описание понятно и содержит достаточные инструкции для воспроизведения проблемы.

### Глоссарий

- COCO (Common Objects in Context) - это большой набор данных для решения задач распознавания объектов, сегментации и субтитров. [cocodataset.org](https://cocodataset.org/)
- PyTorch - фреймворк машинного обучения для языка Python с открытым исходным кодом, созданный на базе [Torch](https://ru.wikipedia.org/wiki/Torch).


### Источники:
https://github.com/facebookresearch/detr
https://colab.research.google.com/github/facebookresearch/detr/blob/colab/notebooks/detr_demo.ipynb#scrollTo=Jf59UNQ37QhJ
https://habr.com/ru/company/recognitor/blog/553478/
https://en.wikipedia.org/wiki/Transformer_(machine_learning_model), ([на русском](https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D1%84%D0%BE%D1%80%D0%BC%D0%B5%D1%80_(%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C_%D0%BC%D0%B0%D1%88%D0%B8%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%8F)))
https://github.com/NielsRogge/Transformers-Tutorials/tree/master/DETR
https://huggingface.co/docs/transformers/model_doc/detr


### Авторы:
Искужин И., Акинин Дмитрий, Ахметов Вадим
студенты 1 курса магистратуры "Инженерия машинного обучения" УрФУ.

ноябрь, 2022 год.


TODO: добавить какие данные можно передавать
- перекрестные сслыки на этой странице (на заголовок и содержание)
- добавить лицензию
- добавить датасет пробный
- выводы, что есть модели получше
