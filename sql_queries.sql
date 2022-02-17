
CREATE TABLE `users` ( 
     `ID` TINYINT(5) NOT NULL AUTO_INCREMENT ,
     `NAME` VARCHAR(16) NOT NULL , 
     `PASSWORD` VARCHAR(8) NOT NULL , 
     PRIMARY KEY (`ID`)
    ) ENGINE = InnoDB;

CREATE TABLE `shops` ( 
     `ID` INT NOT NULL AUTO_INCREMENT , 
     `Name` VARCHAR(24) NOT NULL , 
     `Rent` INT NOT NULL ,
     `Location` VARCHAR(8) NOT NULL , 
     PRIMARY KEY (`ID`)
     ) ENGINE = InnoDB;


ALTER TABLE `shops` ADD UNIQUE(`Name`);
