# ToDo
## 環境
* Python : 3.6.5
* MySQL : 5.7.22

pip
```
pip3 install flask mysql-connector-python-rf
```
or
pipenv
```
pipenv install flask mysql-connector-python-rf
```

```
CREATE DATABASE todo
```

```
CREATE TABLE `todo`.`task` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) NOT NULL,
  `task_title` VARCHAR(45) NOT NULL,
  `task_details` VARCHAR(255) NULL,
  `task_limit` DATETIME NOT NULL,
  `insert_date` DATETIME NOT NULL,
  `update_date` DATETIME,
  PRIMARY KEY (`id`));
```

