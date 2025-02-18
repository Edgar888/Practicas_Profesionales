-- Creación de Tablas
CREATE TABLE "Clientes" (
  "IDCliente" serial PRIMARY KEY,
  "Nombre" varchar(255) NOT NULL,
  "Direccion" text NOT NULL,
  "Telefono" varchar(15) NOT NULL CHECK(length("Telefono") > 0)
);

CREATE TABLE "Autos" (
  "IDAuto" serial PRIMARY KEY,
  "Modelo" varchar(50) NOT NULL,
  "Marca" varchar(50) NOT NULL,
  "AnioFabricacion" int NOT NULL CHECK("AnioFabricacion" > 0),
  "Precio" decimal(10,2) NOT NULL CHECK("Precio" >= 0.0)
);

CREATE TABLE "Empleados" (
  "IDEmpleado" serial PRIMARY KEY,
  "Nombre" varchar(255) NOT NULL,
  "Direccion" text NOT NULL,
  "Telefono" varchar(15) NOT NULL CHECK(length("Telefono") > 0),
  "Rol" varchar(50) NOT NULL
);

CREATE TABLE "Servicios" (
  "IDServicio" serial PRIMARY KEY,
  "NombreServicio" varchar(100) NOT NULL,
  "Descripcion" text NOT NULL,
  "Precio" decimal(10,2) NOT NULL CHECK("Precio" >= 0.0)
);

CREATE TABLE "Mantenimientos" (
  "IDMantenimiento" serial PRIMARY KEY,
  "IDAuto" int NOT NULL,
  "IDCliente" int NOT NULL,
  "IDEmpleado" int NOT NULL,
  "IDServicio" int NOT NULL,
  "FechaMantenimiento" date NOT NULL,
  FOREIGN KEY ("IDAuto") REFERENCES "Autos"("IDAuto") ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY ("IDCliente") REFERENCES "Clientes"("IDCliente") ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY ("IDEmpleado") REFERENCES "Empleados"("IDEmpleado") ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY ("IDServicio") REFERENCES "Servicios"("IDServicio") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "HojalateriaPintura" (
  "IDHojalateriaPintura" serial PRIMARY KEY,
  "IDAuto" int NOT NULL,
  "IDCliente" int NOT NULL,
  "IDEmpleado" int NOT NULL,
  "IDServicio" int NOT NULL,
  "FechaHojalateriaPintura" date NOT NULL,
  FOREIGN KEY ("IDAuto") REFERENCES "Autos"("IDAuto") ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY ("IDCliente") REFERENCES "Clientes"("IDCliente") ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY ("IDEmpleado") REFERENCES "Empleados"("IDEmpleado") ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY ("IDServicio") REFERENCES "Servicios"("IDServicio") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "SegurosAuto" (
  "IDSeguro" serial PRIMARY KEY,
  "IDAuto" int NOT NULL,
  "IDCliente" int NOT NULL,
  "TipoSeguro" varchar(50) NOT NULL,
  "Cobertura" text NOT NULL,
  "Precio" decimal(10,2) NOT NULL CHECK("Precio" >= 0.0),
  FOREIGN KEY ("IDAuto") REFERENCES "Autos"("IDAuto") ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY ("IDCliente") REFERENCES "Clientes"("IDCliente") ON DELETE CASCADE ON UPDATE CASCADE
);

-- Relaciones de las tablas.
ALTER TABLE "Mantenimientos" ADD FOREIGN KEY ("IDAuto") REFERENCES "Autos" ("IDAuto");
ALTER TABLE "Mantenimientos" ADD FOREIGN KEY ("IDCliente") REFERENCES "Clientes" ("IDCliente");
ALTER TABLE "Mantenimientos" ADD FOREIGN KEY ("IDEmpleado") REFERENCES "Empleados" ("IDEmpleado");
ALTER TABLE "Mantenimientos" ADD FOREIGN KEY ("IDServicio") REFERENCES "Servicios" ("IDServicio");
ALTER TABLE "HojalateriaPintura" ADD FOREIGN KEY ("IDAuto") REFERENCES "Autos" ("IDAuto");
ALTER TABLE "HojalateriaPintura" ADD FOREIGN KEY ("IDCliente") REFERENCES "Clientes" ("IDCliente");
ALTER TABLE "HojalateriaPintura" ADD FOREIGN KEY ("IDEmpleado") REFERENCES "Empleados" ("IDEmpleado");
ALTER TABLE "HojalateriaPintura" ADD FOREIGN KEY ("IDServicio") REFERENCES "Servicios" ("IDServicio");
ALTER TABLE "SegurosAuto" ADD FOREIGN KEY ("IDAuto") REFERENCES "Autos" ("IDAuto");
ALTER TABLE "SegurosAuto" ADD FOREIGN KEY ("IDCliente") REFERENCES "Clientes" ("IDCliente");

