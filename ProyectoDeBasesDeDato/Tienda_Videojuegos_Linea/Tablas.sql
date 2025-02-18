CREATE TABLE Cliente
(
  Id_cliente INT NOT NULL,
  NombreC VARCHAR(30) NOT NULL,
  Direccion VARCHAR(30),
  EmailC VARCHAR(255) NOT NULL,
  Num_celularC VARCHAR(15) NOT NULL,
  Saldo DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (Id_cliente)
);

CREATE TABLE Empleado
(
  Id_empleado INT NOT NULL,
  NombreE VARCHAR(30) NOT NULL,
  Cargo VARCHAR(30) NOT NULL,
  EmailE VARCHAR(255) NOT NULL,
  Num_celularE VARCHAR(15) NOT NULL,
  Horas_trabajadas INT NOT NULL,
  Supervisa_Id_empleado INT,
  PRIMARY KEY (Id_empleado)
);

ALTER TABLE Empleado
ADD CONSTRAINT fk_supervisa_empleado
FOREIGN KEY (Supervisa_Id_empleado) REFERENCES Empleado(Id_empleado);


CREATE TABLE Juego
(
  Id_juego INT NOT NULL,
  Titulo VARCHAR(100) NOT NULL,
  Genero VARCHAR(50) NOT NULL,
  Plataforma VARCHAR(50) NOT NULL,
  Precio DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (Id_juego)
);

CREATE TABLE Inventario
(
  Id_inventario INT NOT NULL,
  Stock INT NOT NULL,
  PRIMARY KEY (Id_inventario)
);

CREATE TABLE Pedido
(
  Id_pedido INT NOT NULL,
  Fecha_pedido DATE NOT NULL,
  PRIMARY KEY (Id_pedido)
);

CREATE TABLE Ventas
(
  Id_venta INT NOT NULL,
  Fecha_venta DATE NOT NULL,
  Precio_total DECIMAL(10, 2) NOT NULL,
  Id_pedido INT NOT NULL,
  PRIMARY KEY (Id_venta),
  FOREIGN KEY (Id_pedido) REFERENCES Pedido(Id_pedido) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE VentaJuegoCliente
(
  Id_venta_cliente INT NOT NULL,
  Precio_venta DECIMAL(10, 2) NOT NULL,
  Fecha_venta DATE NOT NULL,
  PRIMARY KEY (Id_venta_cliente)
);


CREATE TABLE HistorialCompras
(
  Compras_realizadas INT NOT NULL,
  Id_historial INT NOT NULL,
  Id_cliente INT NOT NULL,
  Id_pedido INT NOT NULL,
  PRIMARY KEY (Id_historial, Id_cliente, Id_pedido),
  FOREIGN KEY (Id_cliente) REFERENCES Cliente(Id_cliente) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (Id_pedido) REFERENCES Pedido(Id_pedido) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Realiza_pedido
(
  Id_cliente INT NOT NULL,
  Id_pedido INT NOT NULL,
  PRIMARY KEY (Id_cliente, Id_pedido),
  FOREIGN KEY (Id_cliente) REFERENCES Cliente(Id_cliente) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (Id_pedido) REFERENCES Pedido(Id_pedido) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Pedido_Contiene
(
  Id_pedido INT NOT NULL,
  Id_juego INT NOT NULL,
  PRIMARY KEY (Id_pedido, Id_juego),
  FOREIGN KEY (Id_pedido) REFERENCES Pedido(Id_pedido) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (Id_juego) REFERENCES Juego(Id_juego) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Hay_stock
(
  Id_inventario INT NOT NULL,
  Id_juego INT NOT NULL,
  PRIMARY KEY (Id_inventario, Id_juego),
  FOREIGN KEY (Id_inventario) REFERENCES Inventario(Id_inventario) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (Id_juego) REFERENCES Juego(Id_juego) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Cliente_Vende_juego
(
  Cantidad_Juegos_vendidos INT NOT NULL,
  Id_cliente INT NOT NULL,
  Id_venta_cliente INT NOT NULL,
  PRIMARY KEY (Id_cliente, Id_venta_cliente),
  FOREIGN KEY (Id_cliente) REFERENCES Cliente(Id_cliente) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (Id_venta_cliente) REFERENCES VentaJuegoCliente(Id_venta_cliente) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE VentaContiene_juego
(
  Id_venta_cliente INT NOT NULL,
  Id_juego INT NOT NULL,
  PRIMARY KEY (Id_venta_cliente, Id_juego),
  FOREIGN KEY (Id_venta_cliente) REFERENCES VentaJuegoCliente(Id_venta_cliente) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (Id_juego) REFERENCES Juego(Id_juego) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Detalles_Pedido
(
  Id_detalles INT NOT NULL,
  Cantidad INT NOT NULL,
  Precio_unitario DECIMAL(10, 2) NOT NULL,
  Id_pedido INT NOT NULL,
  Id_juego INT NOT NULL,
  PRIMARY KEY (Id_detalles, Id_pedido, Id_juego),
  FOREIGN KEY (Id_pedido) REFERENCES Pedido(Id_pedido) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (Id_juego) REFERENCES Juego(Id_juego) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Compra_Juegos
(
  Id_cliente INT NOT NULL,
  Id_venta INT NOT NULL,
  PRIMARY KEY (Id_cliente, Id_venta),
  FOREIGN KEY (Id_cliente) REFERENCES Cliente(Id_cliente) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (Id_venta) REFERENCES Ventas(Id_venta) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Realiza_venta
(
  Id_empleado INT NOT NULL,
  Id_venta INT NOT NULL,
  PRIMARY KEY (Id_empleado, Id_venta),
  FOREIGN KEY (Id_empleado) REFERENCES Empleado(Id_empleado) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (Id_venta) REFERENCES Ventas(Id_venta) ON DELETE CASCADE ON UPDATE CASCADE
);

