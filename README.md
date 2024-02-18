# maxbit_test_sol
Мое решение тестового из компании maxbit solutions

## Решение

- В книжке `research.ipynb` представлены анализ данных и формирование модели (не забудьте развернуть виртуальное окружение описанное в файле `requirements.txt` в папку `venv`);
- В файле `app.py` представлено описание сервиса на `fastapi` который имплементирует разработанную модель;
- Так же подготовлено все необходимое для развертывания сервиса в `docker`.

## Развертывание

Для того, чтобы собрать решение в docker образ используй команду:

```bash
docker build -t recommendation .
```

Для того, чтобы поднять сервис используй команду:
```bash
docker run --name recommendation --rm -p 8000:8000 recommendation
```

## Использование

Сервис ожидает в качестве параметра `user_id` id пользователя которому надо предложить какую-то игру. А на выходе будет получен список с множеством названий игр отсортированный в порядке от наиболее предпочтительного до наимнее предпочтительного.

Так, например, в linux комманда `curl http://localhost:8000/?user_id=user_5` ответит:
```
["game_26","game_15","game_14","game_28","game_30","game_35","game_16","game_17","game_4","game_8","game_47","game_41","game_27","game_1","game_31","game_44","game_39","game_32","game_34","game_22","game_50","game_19","game_20","game_36","game_46","game_38","game_3","game_7","game_45","game_33","game_48","game_24","game_12","game_13","game_42","game_37","game_21","game_43","game_9","game_23","game_5","game_10","game_6","game_11","game_49","game_40","game_18","game_29","game_25","game_2"]
```

Или то-же самое на `python`:

```python
import requests
resp = requests.get("http://localhost:8000/?user_id=user_5")
print(resp.content)
```

Будет иметь результат:
```
b'["game_26","game_15","game_14","game_28","game_30","game_35","game_16","game_17","game_4","game_8","game_47","game_41","game_27","game_1","game_31","game_44","game_39","game_32","game_34","game_22","game_50","game_19","game_20","game_36","game_46","game_38","game_3","game_7","game_45","game_33","game_48","game_24","game_12","game_13","game_42","game_37","game_21","game_43","game_9","game_23","game_5","game_10","game_6","game_11","game_49","game_40","game_18","game_29","game_25","game_2"]'
```