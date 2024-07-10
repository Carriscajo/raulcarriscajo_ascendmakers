# API de Gestión de Entregas

Esta es una API para gestionar productos, almacenes y entregas para una empresa de reparto. La API está construida con **FastAPI**.

## Requisitos

- Python 3.7+
- pip
- virtualenv

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. Ejecuta el script de instalación:

    ```bash
    chmod +x install.sh
    ./install.sh
    ```

## Uso

1. Activa el entorno virtual:

    ```bash
    source venv/bin/activate
    ```

2. Inicia el servidor:

    ```bash
    uvicorn app.main:app --reload
    ```

3. La API estará disponible en `http://127.0.0.1:8000`.

## Endpoints

### Productos

- **Crear Producto**

    `POST /productos/`

    ```json
    {
        "name": "Nombre del producto"
    }
    ```

- **Obtener Productos**

    `GET /productos/`

### Almacenes

- **Crear Almacén**

    `POST /almacenes/`

    ```json
    {
        "name": "Nombre del almacén",
        "latitud": 40.416775,
        "longitud": -3.703790
    }
    ```

- **Obtener Almacenes**

    `GET /almacenes/`

### Entregas

- **Crear Entrega**

    `POST /entregas/`

    ```json
    {
        "latitud": 40.416775,
        "longitud": -3.703790
    }
    ```

- **Obtener Entregas**

    `GET /entregas/`

### Rutas

- **Obtener Ruta Óptima**

    `GET /rutas/`

    ```json
    {
        "entregas": [1, 2, 3],
        "almacen_id": 1
    }
    ```

## Estructura del Proyecto

├── app
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
│ ├── crud.py
│ ├── database.py
│ └── routes
│ ├──├── products.py
│ ├──├── warehouses.py
│ ├──├── deliveries.py
│ └── routes.py
├── tests (NO INCUIDO EN ESTA VERSION)
│ ├── test_products.py
│ ├── test_warehouses.py
│ ├── test_deliveries.py
│ └── test_routes.py
├── install.sh
└── README.md

## NOTAS
- Asegurate de tener los permisos necesarios `chmod +xinstall.sh`
- Esto intalara las dependencias y creara la SQLite necesaria

## Aproximación para la obtencion de las rutas
Para el calculo de la ruta optima, usaremos algoritmos que nos ayuden a encontrar de forma eficiente visitar todos los puntos y luego regresar al almacen. 
Se trazar un mapa de la ruta y marcar los puntos que debes visitar. Luego, podrías trazar diferentes rutas posibles y compararlas para ver cuál es la más corta.
1. Para ello tendremos en cuenta:
    - Las coordenadas de cada entrega
    - Las coordenadas del almacen de incio
2. Calcular las distancias entre todas las entregas usando Haversine
3. Implemnetar la logica anteriormente comentada de las rutas
4. Optimizacion inical, inicalmente nos basaremos en que exieten todos los productos en el almacen, para luego incluir diferentes paradas para recoger productos en diferentes puntos
