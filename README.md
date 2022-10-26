# spatial_data_API
An example of a spatial database (PostGIS) API that is used in GIS. This is just part of my corporate project. This project uses a test database and a user.
<img src="http://cp82453.tmweb.ru/public_images/spapi.jpg">
## How to run
- clone this repo
- create .env file and come up a key `SECRET=< your symbols >`
- docker-compose up --build -d 
- open [127.0.0.1:8000](127.0.0.1:8000) in your browser
- there will be a test user admin admin
## Peculiarities
This api was created for an already existing database that has been used and managed by our company from QGIS for a long time. Here, a model was created based on an existing table containing construction objects. This API allows you to view, move (change geometry), change attributes, add new and delete objects. GEOS was used to work with geometry. ListView serializes data to Geojson, which allows you to add it to any GIS.
