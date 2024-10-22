ALTER TABLE `equipos` ADD CONSTRAINT `divisionesaequipos` FOREIGN KEY (`divisiones_nombre`) REFERENCES `divisiones`(`Identificador`) ON DELETE RESTRICT ON UPDATE RESTRICT;
