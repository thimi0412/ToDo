# ToDo
## 環境
* Python : 3.6.5
* MySQL : 5.7.22

```
pip3 install flask mysql-connector-python-rf
```

```
CREATE DATABASE test
```

```
CREATE TABLE `test`.`todo` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) NOT NULL,
  `task_title` VARCHAR(45) NOT NULL,
  `task_details` VARCHAR(255) NULL,
  `task_limit` DATETIME NOT NULL,
  `insert_date` DATETIME NOT NULL,
  `update_date` DATETIME,
  `is_complete` VARCHAR(1) NOT NULL,
  `del_flg` VARCHAR(1) NOT NULL,
  PRIMARY KEY (`id`));
```

