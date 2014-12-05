
Create a table in your mysql database with:
==========================================
CREATE TABLE todo (
    id INT AUTO_INCREMENT,
    title TEXT,
    primary key (id)
);

Then run this app
===================
DATABASE_IP (Required)
DATABASE (Required)
USER = root
PASS = ""
PORT = 3306

docker run -it -rm -e DATABASE_IP=10.13.217.60 -e DATABASE=mysql -p 5000:8080 todolist
