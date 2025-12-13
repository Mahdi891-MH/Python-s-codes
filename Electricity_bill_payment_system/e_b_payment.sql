-- MySQL dump 10.13  Distrib 5.7.16, for Win64 (x86_64)
--
-- Host: localhost    Database: e_b_payment
-- ------------------------------------------------------
-- Server version	5.7.16-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bill` (
  `bill_ID` int(11) NOT NULL AUTO_INCREMENT,
  `cust_ID` int(11) NOT NULL,
  `usage_ID` int(11) NOT NULL,
  `bill_date` date NOT NULL,
  PRIMARY KEY (`bill_ID`),
  UNIQUE KEY `usage_ID` (`usage_ID`),
  KEY `cust_ID` (`cust_ID`),
  CONSTRAINT `bill_ibfk_1` FOREIGN KEY (`cust_ID`) REFERENCES `customer` (`cust_ID`) ON UPDATE CASCADE,
  CONSTRAINT `bill_ibfk_2` FOREIGN KEY (`usage_ID`) REFERENCES `meter_usage` (`usage_ID`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1052 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
INSERT INTO `bill` VALUES (1001,100,126,'2024-02-03'),(1002,106,121,'2024-01-29'),(1003,103,122,'2024-02-10'),(1004,104,123,'2024-02-12'),(1005,105,124,'2024-02-15'),(1007,113,125,'2024-09-28'),(1008,115,127,'2023-10-17'),(1034,101,129,'2020-11-23'),(1035,106,130,'2023-10-28'),(1036,107,131,'2020-01-13'),(1037,109,132,'2020-01-20'),(1038,108,133,'2021-10-28'),(1039,110,134,'2022-11-14'),(1045,116,136,'2020-09-02'),(1048,114,138,'2020-12-20'),(1049,111,139,'2025-01-27'),(1050,117,140,'2025-10-01'),(1051,118,141,'2025-09-25');
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `cust_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Full_name` varchar(32) NOT NULL,
  `phone` char(10) NOT NULL,
  `address` varchar(128) NOT NULL,
  `connect_date` date NOT NULL,
  PRIMARY KEY (`cust_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=128 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (100,'Hassan Yasa','0774545345','Kabul, Pol-e-Sokhta','2015-02-14'),(101,'Bashir Mohammadi','0708965781','Kabul, Dasht-e-Barchi','2020-10-16'),(102,'Farhad Nasiri','0785647965','Kabul, Shahr Naw','2025-01-12'),(103,'Emran Jamal','0776545326','Kabul, Karte Char','2020-02-15'),(104,'Hassan Muradi','0794545364','Kabul, Darlaman','2015-02-16'),(105,'Ahmad Danish','0784785334','Kabul, Karte Se','2025-02-10'),(106,'Omid Mohammadi','0745783450','Kabul','2017-08-10'),(107,'Jawad Falah','0799786512','Kabul, Kart-e-Sakhi','2019-12-01'),(108,'Nematullah Haidari','0764576361','Kabul, Dasht-e-Barchi','2012-09-12'),(109,'Hashmat Rahmani','0734576902','Kabul, Karte-e-Char','2014-08-12'),(110,'Farhad Hamidi','0796745788','Kabul','2023-09-10'),(111,'Tahir Hamta','0789867590','Herat','2020-12-11'),(112,'Edris Rahimi','0726754567','Kabul, Kote Sangi','2015-12-15'),(113,'Amin Rahimi','0776789546','Kabul','2002-02-19'),(114,'Karim Jafari','0776787890','Herat','2018-10-19'),(115,'Emran Ibrahimi','0799054609','Kabul','2010-06-17'),(116,'Bahadur Qarizada','0765678904','Herat','2009-12-19'),(117,'Rahmat Nazari','0776768564','Dasht-e-Barchi','2022-08-12'),(118,'Qasim Omid','0766754342','Kabul, Kart-e-Char','2020-12-12'),(119,'Ehsanulllah Muradi','0776545353','Kabul','2018-11-19'),(120,'Jawad Falah','0799786512','Kabul, Kart-e-Sakhi','2019-12-01'),(121,'Bashir Mohammadi','0708965781','Kabul, Dasht-e-Barchi','2020-10-16'),(122,'Ali Ahmadi','0774545345','Kabul, Pol-e-Sokhta','2015-02-14'),(123,'Karim Jafari','0776787890','Herat','2018-10-19'),(124,'Farhad Jafari','0767657542','Kabul','2020-03-17'),(125,'Nematullah Haidari','0764576361','Kabul, Dasht-e-Barchi','2012-09-12'),(126,'Rahmat Nazari','0776768564','Dasht-e-Barchi','2022-08-12'),(127,'Mohammad Qasimi','0786576453','Kabul','2020-09-08');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meter`
--

DROP TABLE IF EXISTS `meter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `meter` (
  `meter_ID` int(11) NOT NULL AUTO_INCREMENT,
  `cust_ID` int(11) NOT NULL,
  `meter_type` enum('Digital','Analog') NOT NULL DEFAULT 'Digital',
  `install_date` date NOT NULL DEFAULT '0000-00-00',
  `status` enum('Active','Unactive') NOT NULL DEFAULT 'Active',
  PRIMARY KEY (`meter_ID`),
  KEY `cust_ID` (`cust_ID`),
  CONSTRAINT `meter_ibfk_1` FOREIGN KEY (`cust_ID`) REFERENCES `customer` (`cust_ID`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=136 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meter`
--

LOCK TABLES `meter` WRITE;
/*!40000 ALTER TABLE `meter` DISABLE KEYS */;
INSERT INTO `meter` VALUES (111,100,'Digital','2022-09-23','Active'),(112,106,'Digital','2017-08-23','Active'),(113,103,'Analog','2020-02-20','Active'),(114,104,'Digital','2025-02-20','Active'),(115,105,'Analog','2025-02-25','Active'),(116,116,'Digital','2020-11-19','Active'),(117,110,'Digital','2023-09-02','Active'),(118,111,'Digital','2024-11-19','Active'),(119,101,'Analog','2019-11-23','Active'),(120,102,'Analog','2013-10-27','Unactive'),(121,107,'Digital','2016-01-13','Active'),(122,108,'Digital','2019-11-23','Active'),(123,109,'Digital','2023-06-24','Active'),(124,112,'Analog','2010-11-29','Unactive'),(125,113,'Digital','2014-01-13','Active'),(126,114,'Analog','2015-11-12','Active'),(127,115,'Analog','2009-11-16','Active'),(128,116,'Digital','2024-08-26','Active'),(129,117,'Digital','2010-11-29','Active'),(130,118,'Digital','2020-12-18','Active'),(131,119,'Digital','2018-11-25','Active'),(132,120,'Digital','2018-11-25','Active'),(133,121,'Digital','2014-01-13','Active'),(134,122,'Analog','2015-11-12','Active'),(135,123,'Digital','2010-11-20','Active');
/*!40000 ALTER TABLE `meter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meter_usage`
--

DROP TABLE IF EXISTS `meter_usage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `meter_usage` (
  `usage_ID` int(11) NOT NULL AUTO_INCREMENT,
  `meter_ID` int(11) NOT NULL,
  `reading_date` date NOT NULL,
  `unit_consumed` decimal(10,2) NOT NULL,
  PRIMARY KEY (`usage_ID`),
  KEY `meter_ID` (`meter_ID`),
  CONSTRAINT `meter_usage_ibfk_1` FOREIGN KEY (`meter_ID`) REFERENCES `meter` (`meter_ID`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=145 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meter_usage`
--

LOCK TABLES `meter_usage` WRITE;
/*!40000 ALTER TABLE `meter_usage` DISABLE KEYS */;
INSERT INTO `meter_usage` VALUES (121,112,'2024-01-25',233.60),(122,113,'2024-02-01',260.00),(123,114,'2024-02-05',344.50),(124,115,'2024-02-06',180.32),(125,117,'2023-07-13',145.00),(126,111,'2024-01-20',19.99),(127,116,'2022-08-15',233.50),(129,118,'2019-11-23',334.12),(130,119,'2019-10-27',240.00),(131,120,'2016-01-13',120.50),(132,121,'2019-11-20',338.12),(133,122,'2018-11-12',124.10),(134,123,'2018-11-23',454.34),(136,125,'2019-11-20',167.19),(137,126,'2017-10-29',242.00),(138,127,'2019-11-28',335.80),(139,128,'2024-10-25',334.00),(140,129,'2025-10-15',120.45),(141,134,'2025-10-07',200.00),(142,131,'2025-10-06',145.56),(143,132,'2025-10-06',147.90),(144,133,'2018-11-23',454.34);
/*!40000 ALTER TABLE `meter_usage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payment` (
  `payment_ID` int(11) NOT NULL AUTO_INCREMENT,
  `bill_ID` int(11) NOT NULL,
  `payment_date` date NOT NULL,
  `amount_paid` int(11) NOT NULL,
  `payment_method` varchar(16) DEFAULT 'cash',
  PRIMARY KEY (`payment_ID`),
  KEY `bill_ID` (`bill_ID`),
  CONSTRAINT `payment_ibfk_1` FOREIGN KEY (`bill_ID`) REFERENCES `bill` (`bill_ID`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=120 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
INSERT INTO `payment` VALUES (101,1001,'2024-09-11',50,'cash'),(102,1007,'2024-09-11',363,'cash'),(103,1002,'2025-03-18',300,'cash'),(104,1002,'2025-03-28',284,'cash'),(105,1003,'2025-03-18',200,'cash'),(106,1008,'2025-07-10',584,'cash'),(107,1005,'2025-04-11',451,'cash'),(108,1004,'2025-07-12',400,'cash'),(109,1004,'2025-07-13',461,'cash'),(111,1034,'2025-07-13',835,'cash'),(112,1039,'2025-07-13',500,'cash'),(114,1035,'2025-07-13',600,'cash'),(115,1045,'2025-09-10',418,'cash'),(116,1003,'2025-09-10',450,'cash'),(117,1036,'2025-09-10',301,'cash'),(118,1037,'2025-09-10',845,'cash'),(119,1038,'2025-09-10',310,'cash');
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `user_ID` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `password` varchar(64) NOT NULL,
  `role` varchar(64) NOT NULL,
  PRIMARY KEY (`user_ID`),
  UNIQUE KEY `user_name` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin','123','Admin'),(2,'operator','123','Operator'),(3,'auditor','*23AE809DDACAF96AF0FD78ED04B6A265E05AA257','Auditor');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-13 16:40:13
