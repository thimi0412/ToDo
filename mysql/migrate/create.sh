#!/bin/bash
mysql -u root -ppassw0rd <<EOF
CREATE TABLE test.todo (
  id INT NOT NULL AUTO_INCREMENT,
  user_name VARCHAR(45) NOT NULL,
  task_title VARCHAR(45) NOT NULL,
  task_details VARCHAR(255) NULL,
  task_limit DATETIME NOT NULL,
  insert_date DATETIME NOT NULL,
  update_date DATETIME NOT NULL,
  is_complete VARCHAR(1) NOT NULL,
  del_flg VARCHAR(1) NOT NULL,
  PRIMARY KEY (id));
EOF