Application to service requets for sprocket factory data and sprockets. 

# Installation Instructions
1. Install mysql, python3, docker ect. 
2. In the main directory, run `docker-compose up`. This should start the webserver and the database.
3. I was unable to get DB restores working on my machine out of the box via docker, something with M1 Mac chipset. That will need to be done via a database tool like TablePlus or equivilant. The database restore file is called `db.dump`. <br> Something like `cat db.dump | docker exec -i CONTAINER /usr/bin/mysql -u user --password=password db` may also work, but I'm unsure of that

The following commands are available 
`/all_sprocket` An endpoint that returns all sprocket factory data
`/given_factory_id`	An endpoint that returns factory data for a given factory id
`/given_sprocket_id`	An endpoint that returns sprockets for a given id
`/create_new_sprocket` An endpoint that will create new sprocket
`/update_sprocket`	An endpoint that will update sprocket for a given id
