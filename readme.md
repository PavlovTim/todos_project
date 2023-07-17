# Todos

### Models
- ~~Todo (fk на родительский todo, может быть null)~~
- ~~Priority (one-to-many)~~
- ~~Label (many-to-many)~~

### Templates (можно использовать bootstrap и тд для стилизации)

- ~~Отображение списка дел с иерархией для конкретного пользователя~~
- ~~Возможность удалять задачи (можно при помощи ajax)~~
- ~~Страница с добавлением задачи + возможность выбирать родительскую задачу~~
- ~~Возможность обновлять задачу~~
- ~~Complete задачи~~
- *Пагинация - подгрузка по 10 задач при помощи ajax
- Добавить фильтрацию по label и priority
- Реализовать поиск по title
- Реализовать навигацию (navbar)
- Работа с пользователем:
  - форма для входа
  - форма для регистрации
  - кнопка log-out

### REST

- получение задач с подзадачами
  - *реализовать пагинацию
  - реализовать поиск по фильтрам
- ~~добавление задачи~~
- ~~обновление задачи~~
- ~~удаление задачи~~
  - *soft delete
- ~~получение данных о конкретной задаче~~
  - добавить флаг, чтобы можно было получить все связанные задачи

### DRF

- получение задач с подзадачами
  - реализовать пагинацию
  - реализовать поиск по фильтрам
- добавление задачи
- обновление задачи
- удаление задачи
- получение данных о конкретной задаче
- реализовать эндпоинты для работы с priority
- реализовать эндпоинты для работы с label
- работа с пользователем:
  - работа с jwt
  - регистрация пользователя


