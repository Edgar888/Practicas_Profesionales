-- Consulta 1: Obtener la información de los clientes que han realizado mantenimientos
-- en sus autos junto con los detalles de los mantenimientos.
SELECT
  c."IDCliente",
  c."Nombre" AS "NombreCliente",
  c."Direccion" AS "DireccionCliente",
  c."Telefono" AS "TelefonoCliente",
  m."IDMantenimiento",
  m."IDAuto",
  a."Marca",
  a."Modelo",
  m."FechaMantenimiento",
  s."NombreServicio",
  s."Descripcion",
  s."Precio" AS "PrecioServicio"
FROM
  "Clientes" c
JOIN
  "Mantenimientos" m ON c."IDCliente" = m."IDCliente"
JOIN
  "Autos" a ON m."IDAuto" = a."IDAuto"
JOIN
  "Servicios" s ON m."IDServicio" = s."IDServicio";

-- Consulta 2: Obtener la cantidad total de autos que han sido sometidos a hojalatería 
-- y pintura, agrupados por marca.
SELECT
  a."Marca",
  COUNT(hp."IDHojalateriaPintura") AS "CantidadAutosHojalateriaPintura"
FROM
  "Autos" a
LEFT JOIN
  "HojalateriaPintura" hp ON a."IDAuto" = hp."IDAuto"
GROUP BY
  a."Marca";

-- Consulta 3: Obtener la lista de empleados y la cantidad de mantenimientos que han
-- realizado cada uno, ordenados de mayor a menor cantidad.
SELECT
  e."IDEmpleado",
  e."Nombre" AS "NombreEmpleado",
  COUNT(m."IDMantenimiento") AS "CantidadMantenimientos"
FROM
  "Empleados" e
LEFT JOIN
  "Mantenimientos" m ON e."IDEmpleado" = m."IDEmpleado"
GROUP BY
  e."IDEmpleado", e."Nombre"
ORDER BY
  "CantidadMantenimientos" DESC;

-- Vista 1: Información Detallada de Mantenimientos con Detalles de Clientes y Autos.
CREATE VIEW VistaMantenimientosDetallados AS
SELECT
  m."IDMantenimiento",
  c."IDCliente",
  c."Nombre" AS "NombreCliente",
  c."Direccion" AS "DireccionCliente",
  c."Telefono" AS "TelefonoCliente",
  a."IDAuto",
  a."Marca",
  a."Modelo",
  m."FechaMantenimiento"
FROM
  "Mantenimientos" m
JOIN
  "Clientes" c ON m."IDCliente" = c."IDCliente"
JOIN
  "Autos" a ON m."IDAuto" = a."IDAuto";

-- Vista 2: Total de Mantenimientos Realizados por Cada Empleado.
CREATE VIEW VistaTotalMantenimientosPorEmpleado AS
SELECT
  e."IDEmpleado",
  e."Nombre" AS "NombreEmpleado",
  COUNT(m."IDMantenimiento") AS "TotalMantenimientos"
FROM
  "Empleados" e
LEFT JOIN
  "Mantenimientos" m ON e."IDEmpleado" = m."IDEmpleado"
GROUP BY
  e."IDEmpleado", e."Nombre";

-- Vista 3: Resumen de Precios de Servicios Agrupados por Tipo de Servicio.
CREATE VIEW VistaResumenPreciosServicios AS
SELECT
  "NombreServicio",
  AVG("Precio") AS "PrecioPromedio",
  MAX("Precio") AS "PrecioMaximo",
  MIN("Precio") AS "PrecioMinimo"
FROM
  "Servicios"
GROUP BY
  "NombreServicio";
