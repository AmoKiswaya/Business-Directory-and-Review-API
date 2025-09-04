# Business Directory + Review API

### Accounts App Endpoints
1. *Register User*
        *POST* /api/accounts/register/
        *Request Body:*
        json
        {
            "username": "AmosDoe",
            "email": "amosdoe@example.com",
            "password": "amosdoePassword123!"
        }

        *Response:*
        json
        {
            "id":3,
            "username":"AmosDoe",
            "email":"amosdoe@example.com",
            "bio":"",
            "phone_number":null,
            "is_owner":false
        }

2. *Login User*
        *POST* /api/token/
        *Request Body:*
        json
        {
            "username": "AmosDoe",
            "email": "amosdoe@example.com",
            "password": "amosdoePassword123!"
        } 

3. *Create business*
        *POST* /api/businesses/
        *Request Body:*
        json
        {
            "name": "Fifty chips",
            "description": "A fast food restaurant that sells chips",
            "location": "Nairobi Kasarani",
            "address": "Blessed Street Building 1",
            "category": 1
        }

        *Response:*
        json
        [
            "count":2,"next":null,"previous":null,"results":[{"id":1,"name":"Fifty chips","description":"A fast food restaurant that sells chips","location":"Nairobi Kasarani","address":"Blessed Street Building 1","website":"","created_at":"2025-09-04T08:54:40.366664Z","owner":3,"category":1},{"id":2,"name":"Fifty chips","description":"A fast food restaurant that sells chips","location":"Nairobi Kasarani","address":"Blessed Street Building 1","website":"","created_at":"2025-09-04T08:54:49.139360Z","owner":3,"category":1}]
        ] 