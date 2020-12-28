# run docker-compose first
sudo docker exec -it `docker ps | grep mongo | awk '{print $1}'` mongo
