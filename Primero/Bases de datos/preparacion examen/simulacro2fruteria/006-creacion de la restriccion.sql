ALTER TABLE `Producto` ADD CONSTRAINT `productoaproveedor` FOREIGN KEY (`ID_Proveedor`) REFERENCES `Proveedor`(`ID_Proveedor`) ON DELETE RESTRICT ON UPDATE RESTRICT;
