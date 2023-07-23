[![Github Actions Status](https://github.com/danokp/store-warehouse/workflows/linter/badge.svg)](https://github.com/danokp/store-warehouse/actions)
# Store-Warehouse application

Store-Warehouse - a Django (Django Rest Framework) application that can work in two modes: store or warehouse.
In "Store" mode, it is able to create a new order and synchronize it with the connected warehouse.
On the other hand, in "Warehouse" mode, you can change the order status and synchronize the updated status with the connected store.
The synchronization of databases is done using REST API.


## Installation
To download and install this project use the following commands:
```bash
git clone git@github.com:danokp/store-warehouse.git
cd task-manager
```

## Usage
1. Make sure that Docker and Docker-compose are installed.
```bash
docker -v
docker compose version
```
2. `.env.store` and `.env.warehouse` files have been already created for faster demonstration.
3. Run the applications using `docker compose`:
```bash
docker compose up
```
4. Open the applications in web browser:
   - Store at [http://localhost:8001/admin](http://localhost:8001/admin);
   - Warehouse at [http://localhost:8002/admin](http://localhost:8002/admin).
5. Superuser has been automatically created. In order to start using login as an admin (`username`: _admin_, `password`: _admin_).
