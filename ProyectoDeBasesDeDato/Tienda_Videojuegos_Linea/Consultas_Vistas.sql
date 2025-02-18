--Ejercicios 10 y 11: Consultas y Vistas

--Consulta 1
SELECT NombreC, Saldo
FROM Cliente
WHERE Id_cliente IN (
SELECT DISTINCT Id_cliente
FROM Compra_Juegos) AND Saldo > 100;

--Consulta 2
SELECT J.Titulo, I.Stock
FROM Juego J
INNER JOIN Hay_stock H ON J.Id_juego = H.Id_juego
INNER JOIN Inventario I ON H.Id_inventario = I.Id_inventario
WHERE J.Plataforma = 'Xbox';

--Consulta 3
SELECT NombreE
FROM Empleado
WHERE Cargo = 'Supervisor de Ventas' AND Horas_trabajadas > 40;

--Vista 1
CREATE VIEW Resumen_Stock_Juego AS
SELECT J.Id_juego, J.Titulo, J.Genero, I.Stock
FROM Juego J
JOIN Hay_stock HS ON J.Id_juego = HS.Id_juego
JOIN Inventario I ON HS.Id_inventario = I.Id_inventario;

--Ejemplo de Vista 1
SELECT * FROM Resumen_Stock_Juego;

--Vista 2
CREATE VIEW Pedidos_por_Juego AS
SELECT PC.Id_juego, J.Titulo, DP.Id_pedido, DP.Cantidad
FROM Juego J
JOIN Pedido_Contiene PC ON J.Id_juego = PC.Id_juego
JOIN Detalles_Pedido DP ON PC.Id_pedido = DP.Id_pedido AND PC.Id_juego = DP.Id_juego;

--Ejemplo de Vista 2
SELECT * FROM Pedidos_por_Juego;

--Vista 3
CREATE VIEW Total_Ventas_Empleado AS
SELECT R.Id_empleado, COUNT(R.Id_venta) AS Total_ventas
FROM Realiza_venta R
GROUP BY R.Id_empleado;

--Ejemplo de VISTA 3 
SELECT * FROM Total_Ventas_Empleado;