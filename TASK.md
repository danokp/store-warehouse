# Test Task

It would be great if you can create a Django project and provide us with a link to a git repository.
Please, be aware that it's a test task, so we are not expecting a robust solution, and it's up to you how stable you want to make it.
This is a technical requirement for this project:
* Create two applications. (Store and Warehouse)
* (Store) One application should provide Orders (should be able to create order from admin page)
* (Warehouse) Another application should be able to receive these orders via the API and push back the information to the (Store).
* So when you create and order in Store, this should be synced to the Warehouse. If in warehouse you change some information this will update the information in Store (i.e. status)
* Make sure these applications can only communicate via Rest API and don't share a same database (two separate databases).

Декомпозиция задачи:
1) Реализация двойного назначения разрабатываемого приложения:
   1) Реализовать родительское приложенеи orders, в котром будет описана общая логика для обоих приложений
   2) На основе родительского orders реализовать store_orders и warehouse_orders
   3) Настроить переключение режима (MODE) в settings.py. Предполается в зависимости от значения MODE (store / warehouse) изменять файл urls.py.
2) Реализация синхронизации БД по средством API.
   1) В orders добавить возможность принимать API и обновлять БД:
   2) В store_orders добавить возможность отправлять API при добавлении новой записи
   3) Видимо, в store_orders models.py нужно добавить поле linked_warehouse, а в warehouse_orders -- linked_stores


Как ограничить создание заказов на warehouse_orders?

__!!! При настройке docker-compose file выполнить миграции только для нужного приложения !!!__

