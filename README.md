# finstc

Решение тестового задания. \
Запуск сервера - `python src/api.py`.\
В файле `test.py` лежат примеры запросов.

Список эндпоинтов:
- `/car/<int:car_id>`
- `/dealer/<int:dealer_id>`
- `/dealer/<int:dealer_id>/car/<int:car_id>`

Запросы:
- GET `/car/<int:car_id>` - получить предложения всех диллеров по данному автомобилю:
    - Данные: -
    - Возвращаемое значение: 
    ```
  {
    "car_id": int, 
    "dealers": [{
        "dealer_name": string,
        "price": int,
        "quantity": int
        }]
  }
    ```
- POST `/car/add` - создать новый автомобиль:
    - Данные: 
    ```
  {
  "name": string
  }
  ```
    - Возвращаемое значение: 
    ```
  {
    "id": int,
    "name": string
  }
    ```
- DELETE `/car/<int:car_id>` - удалить автомобиль (вместе со всеми предложениями по данному автомобилю):
    - Данные: -

    - Возвращаемое значение: 
    ```
  {
    "success": boolean
  }
    ```
- PATCH `/car/<int:car_id>` - изменить название автомобиля:
    - Данные: 
    ```
  {
  "name": string
  }
  ```
    - Возвращаемое значение: 
    ```
  {
    "success": boolean
  }
    ```

- GET `/dealer/<int:dealer_id>` - получить все предложения диллера:
    - Данные: -
    - Возвращаемое значение: 
    ```
  {
    "dealer_id": int, 
    "cars": [{
        "car_name": string,
        "price": int,
        "quantity": int
        }]
  }
    ```
- POST `/dealer/add` - создать нового диллера:
    - Данные: 
    ```
  {
  "name": string
  }
  ```
    - Возвращаемое значение: 
    ```
  {
    "id": int,
    "name": string
  }
    ```
- DELETE `/dealer/<int:dealer_id>` - удалить диллера (вместе со всеми его предложениями):
    - Данные: -

    - Возвращаемое значение: 
    ```
  {
    "success": boolean
  }
    ```
- PATCH `/dealer/<int:dealer_id>` - изменить название диллера:
    - Данные: 
    ```
  {
  "name": string
  }
  ```
    - Возвращаемое значение: 
    ```
  {
    "success": boolean
  }
    ```

- GET `/dealer/<int:dealer_id>/car/<int:car_id>` - получить предложения диллера по конкретному автомобилю:
    - Данные: -
    - Возвращаемое значение: 
    ```
  {
    "dealer_id": int, 
    "car": {
        "car_name": string,
        "price": int,
        "quantity": int
        }
  }
    ```
- POST `/dealer/<int:dealer_id>/car/<int:car_id>` - создать предложение диллера по автомобилю:
    - Данные: 
    ```
  {
  "quantity": int,
  "price": int
  }
  ```
    - Возвращаемое значение: 
    ```
  {
    "success": boolean
  }
    ```
- DELETE `/dealer/<int:dealer_id>/car/<int:car_id>` - удалить предложение диллера по автомобилю:
    - Данные: -

    - Возвращаемое значение: 
    ```
  {
    "success": boolean
  }
    ```
- PATCH `/dealer/<int:dealer_id>/car/<int:car_id>` - изменить количество доступных единиц и/или стоимость автомобиля у диллера:
    - Данные: 
    ```
  {
  "quantity": int,
  "price": int
  }
  ```
    - Возвращаемое значение: 
    ```
  {
    "success": boolean
  }
    ```