CREATE TABLE `programacion`.`clientes` (`Identificador` INT NOT NULL AUTO_INCREMENT , `nombre` VARCHAR(255) NOT NULL , `apellidos` VARCHAR(255) NOT NULL , `email` VARCHAR(255) NOT NULL , PRIMARY KEY (`Identificador`)) ENGINE = InnoDB;

CREATE TABLE `programacion`.`productos` (`Identificador` INT NOT NULL AUTO_INCREMENT , `nombre` VARCHAR(255) NOT NULL , `descripcion` VARCHAR(255) NOT NULL , `precio` DECIMAL(20,2) NOT NULL , PRIMARY KEY (`Identificador`)) ENGINE = InnoDB;

CREATE TABLE `programacion`.`categorias` (`Identificador` INT NOT NULL AUTO_INCREMENT , `nombre` VARCHAR(255) NOT NULL , PRIMARY KEY (`Identificador`)) ENGINE = InnoDB;

