-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 29-06-2026 a las 02:50:15
-- Versión del servidor: 8.4.7
-- Versión de PHP: 8.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_peliculas`
--
CREATE DATABASE IF NOT EXISTS `bd_peliculas` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `bd_peliculas`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pelicula`
--

DROP TABLE IF EXISTS `pelicula`;
CREATE TABLE IF NOT EXISTS `pelicula` (
  `id_pelicula` int NOT NULL AUTO_INCREMENT,
  `titulo_pelicula` varchar(45) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `duracion` int NOT NULL,
  `fecha_de_estreno` date NOT NULL,
  `genero` int NOT NULL,
  `idioma` int NOT NULL,
  `director` varchar(45) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  PRIMARY KEY (`id_pelicula`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `pelicula`
--

INSERT INTO `pelicula` (`id_pelicula`, `titulo_pelicula`, `duracion`, `fecha_de_estreno`, `genero`, `idioma`, `director`) VALUES
(2, 'Avatar 2', 192, '2022-12-16', 2, 2, 'James Cameron'),
(3, 'scary movie 6', 126, '2026-06-16', 3, 1, 'john sinna');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
