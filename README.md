# Flask Practice - Raccoons

This application is being built by a wildlife organization to track raccoon visits to residential trashcans.

## Getting Started

Fork and clone this repo. Use `pipenv install` and `pipenv shell` to begin. Be sure to `cd server`.

There are no tests so be sure to use the `flask shell` and Postman to be certain everything's working correctly!

## Models

You have three models:

### Raccoon

- `name` (string): Cannot be null, must be unique
- `age` (integer): Cannot be null, must be a number greater than 0

### Trashcan

- `address` (string): Cannot be null

### Visit

- `date` (string): Cannot be null

## Relationships

This is a many-to-many relationship.

- An Raccoon has many Visits and a Visit belongs to an Raccoon.

- A Trashcan has many Visits and a Visit belongs to a Trashcan.

- A Trashcan has many Raccoons and a Raccoon has many Trashcans through Visits.

`Raccoon --< Visit >-- Trashcan`

The foreign keys aren't specified so you'll have to determine where they go.

## Seeding

You can either use the `seed.py` to create your seeds or you can seed manually with `flask shell`. The `seed.py` file has already been populated and should work once your models are prepared.

## Routes

Build out these routes:


### Raccoon

#### `GET /Raccoons`

Returns a list of all Raccoons formatted like so:

```json
[
    {
        "id": 1,
        "name": "Bob",
        "age": 10
    },
    {
        "id": 2,
        "name": "Jimbo",
        "age": 7
    }
    
]
```

#### `GET /raccoons/:id`

Returns an Raccoon with the matching id. If there is no Raccoon, returns a message that the Raccoon could not be found along with a 404.

Format your Raccoon object like so:

```json
    {
        "id": 1,
        "name": "Bob",
        "age": 10,
        "visits": [
            {
                "id": 1,
                "trashcan_id": 1,
                "raccoon_id": 1,
                "date": "2023 8 18"
            },
            {
                "id": 2,
                "trashcan_id": 2,
                "raccoon_id": 1,
                "date": "2022 12 5"
            }
        ]
    }
    
```

#### `DELETE /raccoons/:id`

Deletes the Raccoon and all associated Visits from the database. Returns 204 if the Raccoon was successfully deleted or 404 and an appropriate message if that Raccoon could not be found.


### Trashcan

#### `GET /trashcans`

Returns a list of all Trashcans.

```json
[
    {
        "id": 1,
        "address": "123 Woodland Dr"
    },
    {
        "id": 2,
        "address": "456 Grey Mtn Rd"
    }
]
```


#### `GET /trashcans/:id`

Returns a Trashcan with the matching id. If there is no Trashcan, returns a message that the Trashcan could not be found along with a 404.

```json
{
    "id": 2,
    "address": "456 Grey Mtn Rd"
}
```


### Visit

#### `POST /visits`

Creates a new Visit. The Visit must belong to a Raccoon and a Trashcan. Return the new Visit details like so:

```json
{
    "id": 3,
    "date": "2021 10 31",
    "raccoon": {
      "id": 2,
      "name": "Jimbo",
      "age": 7
    },
    "trashcan": {
        "id": 1,
        "address": "123 Woodland Dr"
    }
}
```

#### `DELETE /visits/:id`

Deletes the Visit from the database. Returns 204 if the Visit was successfully deleted or 404 and an appropriate message if that Visit could not be found.