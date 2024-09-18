CREATE TABLE `miempresa`.`direcciones` (`Identificador` INT NOT NULL AUTO_INCREMENT , `calle` VARCHAR(100) NOT NULL , `codigopostal` VARCHAR(50) NOT NULL , `pais` VARCHAR(50) NOT NULL , `empleados_nombre` INT NOT NULL , PRIMARY KEY (`Identificador`)) ENGINE = InnoDB;

INSERT INTO `direcciones` (`Identificador`, `calle`, `codigopostal`, `pais`, `empleados_nombre`) VALUES (NULL, 'Calle principal, 5', '46000', 'España', '1');
