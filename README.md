# ANPR Project
A Django fullstack app that handles vehilce plate management for a gated community.


## Installation
Create a virtual environment to install dependencies, eg:
```console
python3 -m venv venv
```

Activate the virtual environment (Windows)
```console
.\venv\Scripts\activate
```

```console
source venv/bin/activate
```

Pip install this repo. (Tested on python3.9 and above)
```console
pip install -r requirements.txt
```

## Run
```console
python manage.py runserver
```

## Complete request file with all available fields
```console
openapi: 3.0.3
info:
  title: ''
  version: 0.0.0
paths:
  /drf/bulk-register/:
    post:
      operationId: drf_bulk_register_create
      tags:
      - drf
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Vehicle'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Vehicle'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Vehicle'
        required: true
      security:
      - cookieAuth: []
      - basicAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Vehicle'
          description: ''
  /drf/resident-delete/{id}/:
    delete:
      operationId: drf_resident_delete_destroy
      parameters:
      - in: path
        name: id
        schema:
          type: string
        required: true
      tags:
      - drf
      security:
      - cookieAuth: []
      - basicAuth: []
      - {}
      responses:
        '204':
          description: No response body
  /drf/residents-list/:
    get:
      operationId: drf_residents_list_retrieve
      tags:
      - drf
      security:
      - cookieAuth: []
      - basicAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Tenant'
          description: ''
  /drf/tenant-create/:
    post:
      operationId: drf_tenant_create_create
      tags:
      - drf
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Tenant'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Tenant'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Tenant'
        required: true
      security:
      - cookieAuth: []
      - basicAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Tenant'
          description: ''
  /drf/vehicle-create/:
    post:
      operationId: drf_vehicle_create_create
      tags:
      - drf
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Vehicle'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Vehicle'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Vehicle'
        required: true
      security:
      - cookieAuth: []
      - basicAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Vehicle'
          description: ''
  /drf/vehicle-delete/{id}/:
    delete:
      operationId: drf_vehicle_delete_destroy
      parameters:
      - in: path
        name: id
        schema:
          type: string
        required: true
      tags:
      - drf
      security:
      - cookieAuth: []
      - basicAuth: []
      - {}
      responses:
        '204':
          description: No response body
  /drf/vehicle-update/:
    put:
      operationId: drf_vehicle_update_update
      tags:
      - drf
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Vehicle'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Vehicle'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Vehicle'
        required: true
      security:
      - cookieAuth: []
      - basicAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Vehicle'
          description: ''
  /drf/vehicle/{plate_number}/:
    get:
      operationId: drf_vehicle_retrieve
      parameters:
      - in: path
        name: plate_number
        schema:
          type: string
        required: true
      tags:
      - drf
      security:
      - cookieAuth: []
      - basicAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Vehicle'
          description: ''
  /drf/vehicles-list/:
    get:
      operationId: drf_vehicles_list_retrieve
      tags:
      - drf
      security:
      - cookieAuth: []
      - basicAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Vehicle'
          description: ''
components:
  schemas:
    Tenant:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        name:
          type: string
          maxLength: 100
        phone_number:
          type: string
          maxLength: 15
        created_at:
          type: string
          format: date-time
          readOnly: true
        updated_at:
          type: string
          format: date-time
          readOnly: true
      required:
      - created_at
      - id
      - name
      - phone_number
      - updated_at
    Vehicle:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        plate_number:
          type: string
          maxLength: 20
        vehicle_name:
          type: string
          maxLength: 100
        vehicle_color:
          type: string
          maxLength: 100
        created_at:
          type: string
          format: date-time
          readOnly: true
        updated_at:
          type: string
          format: date-time
          readOnly: true
        tenant:
          type: integer
          nullable: true
      required:
      - created_at
      - id
      - plate_number
      - updated_at
      - vehicle_color
      - vehicle_name
  securitySchemes:
    basicAuth:
      type: http
      scheme: basic
    cookieAuth:
      type: apiKey
      in: cookie
      name: sessionid
```
# Resources
https://www.youtube.com/watch?v=xlcYLlndqz4&ab_channel=CryceTruly