-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.4.11-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             9.3.0.4984
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping database structure for registerdb
CREATE DATABASE IF NOT EXISTS `registerdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `registerdb`;


-- Dumping structure for table registerdb.states
CREATE TABLE IF NOT EXISTS `states` (
  `state_id` int(11) NOT NULL AUTO_INCREMENT,
  `state_name` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`state_id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;

-- Dumping data for table registerdb.states: ~29 rows (approximately)
DELETE FROM `states`;
/*!40000 ALTER TABLE `states` DISABLE KEYS */;
INSERT INTO `states` (`state_id`, `state_name`, `created_at`, `updated_at`, `deleted_at`) VALUES
	(1, 'Andhra Pradesh', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(2, 'Arunachal Pradesh', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(3, 'Assam', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(4, 'Bihar', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(5, 'Chhattisgarh', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(6, 'Goa', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(7, 'Gujarat', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(8, 'Haryana', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(9, 'Himachal Pradesh', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(10, 'Jammu and Kashmir', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(11, 'Jharkhand', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(12, 'Karnataka', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(13, 'Kerala', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(14, 'Madhya Pradesh', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(15, 'Maharashtra', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(16, 'Manipur', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(17, 'Meghalaya', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(18, 'Mizoram', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(19, 'Nagaland', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(20, 'Odisha', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(21, 'Punjab', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(22, 'Rajasthan', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(23, 'Sikkim', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(24, 'Tamil Nadu', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(25, 'Telangana', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(26, 'Tripura', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(27, 'Uttar Pradesh', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(28, 'Uttarakhand', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00'),
	(29, 'West Bengal', '2021-01-29 23:15:00', '2021-01-29 23:15:00', '0000-00-00 00:00:00');
/*!40000 ALTER TABLE `states` ENABLE KEYS */;


-- Dumping structure for table registerdb.users
CREATE TABLE IF NOT EXISTS `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `mobile` varchar(45) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `dob` varchar(45) DEFAULT NULL,
  `state` varchar(45) DEFAULT NULL,
  `skills` varchar(250) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `password` varchar(250) DEFAULT NULL,
  `confirm_password` varchar(250) DEFAULT NULL,
  `last_login` datetime DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table registerdb.users: ~4 rows (approximately)
DELETE FROM `users`;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`user_id`, `name`, `email`, `mobile`, `gender`, `dob`, `state`, `skills`, `created_at`, `updated_at`, `deleted_at`, `password`, `confirm_password`, `last_login`) VALUES
	(1, 'Ganesn', 'ganesanja@gmail.com', '8637643225', 'Male', NULL, '24', NULL, '2021-01-30 09:36:10', '2021-01-31 22:19:35', NULL, '1234', '1234', '2021-02-01 01:06:58'),
	(3, 'Sridhar', 'sri@gmail.com', '9952514049', 'Male', NULL, '24', NULL, '2021-01-30 23:32:57', '2021-02-01 00:56:17', NULL, '1111', '1111', '2021-01-30 23:33:08'),
	(4, 'Mathivanan', 'mathi@gmail.com', '8686868686', 'Male', NULL, '1', NULL, '2021-01-31 07:08:15', '2021-02-01 00:29:16', NULL, '1234', '1234', '2021-02-01 01:10:45'),
	(6, 'Sukanya K B.Sc', 'sukanya@gmail.com', '9750896557', 'Female', NULL, '6', NULL, '2021-02-01 00:00:15', '2021-02-01 00:48:24', NULL, '123456', '123456', '2021-02-01 00:00:36');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
