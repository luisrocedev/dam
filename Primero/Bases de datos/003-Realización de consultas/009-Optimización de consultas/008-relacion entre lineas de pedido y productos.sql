ALTER TABLE `lineaspedido` ADD CONSTRAINT `lineasaproductos` FOREIGN KEY (`productos_nombre`) REFERENCES `productos`(`Identificador`) ON DELETE RESTRICT ON UPDATE RESTRICT;

