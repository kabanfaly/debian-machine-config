# run docker-compose first
docker exec -it `docker ps | grep mongo | awk '{print $1}'` mongo
