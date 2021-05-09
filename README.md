# finstc

Решение тестового задания. \
Список эндпоинтов:
- `/car/<int:car_id>`
- `/dealer/<int:dealer_id>`
- `/dealer/<int:dealer_id>/car/<int:car_id>`\

Запросы:
- GET `/car/<int:car_id>`:
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
- POST `/car/add`:
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
- DELETE `/car/<int:car_id>`:
    - Данные: -

    - Возвращаемое значение: 
    ```
  {
    "success": boolean
  }
    ```
- PATCH `/car/<int:car_id>`:
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

- GET `/dealer/<int:dealer_id>`:
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
- POST `/dealer/add`:
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
- DELETE `/dealer/<int:dealer_id>`:
    - Данные: -

    - Возвращаемое значение: 
    ```
  {
    "success": boolean
  }
    ```
- PATCH `/dealer/<int:dealer_id>`:
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

- GET `/dealer/<int:dealer_id>/car/<int:car_id>`:
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
- POST `/dealer/<int:dealer_id>/car/<int:car_id>`:
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
- DELETE `/dealer/<int:dealer_id>/car/<int:car_id>`:
    - Данные: -

    - Возвращаемое значение: 
    ```
  {
    "success": boolean
  }
    ```
- PATCH `/dealer/<int:dealer_id>/car/<int:car_id>`:
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