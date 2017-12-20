# Flask Boilerplate

_Note: this code is adopted from the [docker compose tutorial](https://docs.docker.com/compose/gettingstarted/)_

launches a simple CORS-enabled flask web server on http://localhost:5000 and provides a redis datastore.

## Quickstart
- Install docker compose https://docs.docker.com/compose/install/#install-compose
- run `docker-compose up` to build containers and launch 
- run `. test.sh` to verify that your setup is working. output should be `Success!`

## Notes

- run `docker-compose build web` to rebuild the web container if you add additional python dependencies
