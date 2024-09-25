# Readers Digest API

## Overview

Readers Digest API is the back-end for a Django-based web application that allows users to review books. Users can create, retrieve, update, and delete reviews for various books. The application uses Django REST framework to provide a RESTful API for managing reviews.

## Primary Learning Objectives

- **ERD**: Simplified approach to creating a models based off a well-thought out Entity Relationship Diagram.
- **Many-To-Many Relationships**: Learning how to navigate Django's approach to many-to-many relationships with a "ManyToManyField" method & related fields. 
- **SQLite & DB Management**: Continued practice with seeding a SQLite3 database using fixtures & navigating Django's ORM.

## Features

<details>
    
- **User Authentication**: Secure user authentication and authorization.
- **Book Details**: Users can create, read, update and delete books they want to keep track of.
- **Book Reviews**: Users can create, read, update, and delete reviews for books.
- **CORS Support**: Configured to handle Cross-Origin Resource Sharing (CORS) for frontend integration.
</details>

## Installation
<details>
<summary>Intructions</summary>

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/readers-digest.git
    cd readers-digest
    ```

2. **Create a virtual environment**:
    ```sh
    pipenv shell
    ```

3. **Install dependencies**:
    ```sh
    pip install
    ```

4. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

6. **Run the development server**:
    ```sh
    python manage.py runserver
    ```
</details>

## API Endpoints

<details>
<summary>Details</summary>

### Authentication

- **Login**: `/digestapi/auth/login/`
- **Logout**: `/digestapi/auth/logout/`

### Reviews

- **List Reviews**: `GET /digestapi/reviews/`
- **Create Review**: `POST /digestapi/reviews/`
- **Retrieve Review**: `GET /digestapi/reviews/{id}/`
- **Update Review**: `PUT /digestapi/reviews/{id}/`
- **Delete Review**: `DELETE /digestapi/reviews/{id}/`

</details>

<details>
<summary>Example Requests</summary>

## Example POST Request for Creating a Book

```json
{
    "title": "The Neverending Story",
    "author": "Edwin R. Billows",
    "isbn_number": "8573282904",
    "cover_image": "http://www.allbooks.com/neverendingstory/images/cover.png",
    "categories": [3, 5]
}
```

## Example POST Request for Creating a Review

```json
{
    "book_id": 1,
    "user_id": 1,
    "rating": 5,
    "comment": "An absolute masterpiece! Couldn't put it down."
}
```
</details>
