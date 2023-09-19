# Flask Practice - Car Dealership

This application is being built to track cars sold by car dealerships.

## Getting Started

Fork and clone this repo. Use `pipenv install` and `pipenv shell` to begin. Be sure to `cd server`.

There are no tests so be sure to use the `flask shell` and Postman to be certain everything's working correctly!

## Models

You have three models:

### Owner

- `first_name` (string): Cannot be null
- `last_name` (string): Cannot be null

### Dealership

- `name` (string): Cannot be null
- `address` (string): Cannot be null

### Car

- `make` (string): Cannot be null
- `model` (string): Cannot be null
- `date_sold` (datetime): Cannot be null

## Relationships

This is a many-to-many relationship.

- An owner has many cars and a car belongs to an owner.

- A dealership has many cars and a car belongs to a dealership.

- A dealership has many owners and an owner has many dealerships through cars.

`Owner --< Car >-- Dealership`

The foreign keys aren't specified so you'll have to determine where they go.

## Seeding

You can either use the `seed.py` to create your seeds or you can seed manually with `flask shell`.

## Routes

Build out these routes:


### Owner

#### `GET /owners`

Returns a list of all owners formatted like so:

```json
[
    {
        "id": 1,
        "first_name": "Mohammad",
        "last_name": "Hossain"
    },
    {
        "id": 2,
        "first_name": "Alina",
        "last_name": "Pisarenko"
    }
]
```

#### `GET /owners/:id`

Returns an owner with the matching id. If there is no owner, returns a message that the owner could not be found along with a 404.

Format your owner object like so:

```json
    {
        "id": 1,
        "first_name": "Mohammad",
        "last_name": "Hossain",
        "cars": [
            {
                "id": 1,
                "make": "Ford",
                "model": "Taurus",
                "date_sold": "2002-08-18 00:00:00"
            },
            {
                "id": 2,
                "make": "Chevrolet",
                "model": "Corvette",
                "date_sold": "2001-12-31 00:00:00"
            }
        ]
    }
```

#### `DELETE /owners/:id`

Deletes the owner and all associated cars from the database. Returns 204 if the owner was successfully deleted or 404 and an appropriate message if that owner could not be found.


### Dealership

#### `GET /dealerships`

Returns a list of all dealerships.

```json
[
    {
        "id": 1,
        "name": "Crazy Bob's Car Rodeo",
        "address": "123 Woodland Dr"
    },
    {
        "id": 2,
        "name": "King Auto's Castle",
        "address": "456 Roundtable Ln"
    }
]
```


#### `GET /dealerships/:id`

Returns a dealership with the matching id. If there is no dealership, returns a message that the dealership could not be found along with a 404.

```json
{
    "id": 2,
    "name": "King Auto's Castle",
    "address": "456 Roundtable Ln"
}
```


### Car

#### `POST /cars`

Creates a new car. The car must belong to a owner and a dealership. Return the new car details like so:

```json
{
    "id": 3,
    "make": "Ford",
    "model": "Pinto",
    "owner": {
      "id": 2,
      "first_name": "Alina",
      "last_name": "Pisarenko"
    },
    "dealership": {
        "id": 1,
        "name": "Crazy Bob's Car Rodeo",
        "address": "123 Woodland Dr"
    }
}
```

#### `DELETE /cars/:id`

Deletes the car from the database. Returns 204 if the car was successfully deleted or 404 and an appropriate message if that car could not be found.

*Please note the json that gets serialized may be a different order for any given response, don't focus on the order so much as making sure everything gets returned correctly...*
