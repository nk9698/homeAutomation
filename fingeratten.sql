-- phpMyAdmin SQL Dump
-- version 3.4.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 12, 2017 at 03:48 PM
-- Server version: 5.5.20
-- PHP Version: 5.3.9

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `fingeratten`
--

-- --------------------------------------------------------

--
-- Table structure for table `asheet`
--

CREATE TABLE IF NOT EXISTS `asheet` (
  `id` int(10) NOT NULL,
  `rollno` varchar(50) NOT NULL,
  `tlmaths` int(10) NOT NULL DEFAULT '0',
  `almaths` int(10) NOT NULL DEFAULT '0',
  `mathsper` int(10) NOT NULL DEFAULT '0',
  `tlsci` int(10) NOT NULL DEFAULT '0',
  `alsci` int(10) NOT NULL DEFAULT '0',
  `sciper` int(10) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `asheet`
--

INSERT INTO `asheet` (`id`, `rollno`, `tlmaths`, `almaths`, `mathsper`, `tlsci`, `alsci`, `sciper`) VALUES
(11, '15ce01', 0, 0, 0, 0, 0, 0),
(12, '15ce02', 0, 0, 0, 0, 0, 0),
(13, '15ce03', 0, 0, 0, 0, 0, 0),
(14, '15ce04', 0, 0, 0, 0, 0, 0),
(15, '15ce05', 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `facsub`
--

CREATE TABLE IF NOT EXISTS `facsub` (
  `id` int(10) NOT NULL,
  `subtl` int(10) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `facsub`
--

INSERT INTO `facsub` (`id`, `subtl`) VALUES
(1, 0),
(2, 0);

-- --------------------------------------------------------

--
-- Table structure for table `registor`
--

CREATE TABLE IF NOT EXISTS `registor` (
  `id` int(10) NOT NULL,
  `rollno` varchar(50) NOT NULL,
  `date` int(10) NOT NULL,
  `maths` int(10) NOT NULL DEFAULT '0',
  `sci` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE IF NOT EXISTS `student` (
  `id` int(10) NOT NULL,
  `rollno` varchar(50) NOT NULL,
  `almaths` int(10) NOT NULL DEFAULT '0',
  `alsci` int(10) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `rollno`, `almaths`, `alsci`) VALUES
(11, '15ce01', 0, 0),
(12, '15ce02', 0, 0),
(13, '15ce03', 0, 0),
(14, '15ce04', 0, 0),
(15, '15ce05', 0, 0);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
