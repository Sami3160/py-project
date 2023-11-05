-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer_details`
--

DROP TABLE IF EXISTS `customer_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_details` (
  `first_name` varchar(10) NOT NULL,
  `mid_name` varchar(10) NOT NULL,
  `last_name` varchar(10) NOT NULL,
  `ph_no` decimal(10,0) DEFAULT NULL,
  `address` varchar(30) DEFAULT NULL,
  `cus_id` decimal(4,0) NOT NULL,
  `pass` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`cus_id`),
  UNIQUE KEY `ph_no` (`ph_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_details`
--

LOCK TABLES `customer_details` WRITE;
/*!40000 ALTER TABLE `customer_details` DISABLE KEYS */;
INSERT INTO `customer_details` VALUES ('Naruto','Minato','Uzumaki',9123456789,'Hidden leaf village,konoha',1000,'leaf'),('stu3','mid3','last3',9201835647,'Haidar nagar, ajra',2352,'3000'),('Nilesh','Mahesh','Sable',3459345988,'Maharashtra, India',5078,'2323'),('Ramesh','Sunil','Desai',2354679898,'Maharashtra, India',5096,'8989'),('stu1','mid1','last1',9226431818,'Shivaji nagar,Ajra',7444,'1000'),('stu4','mid4','last4',9191277289,'Ambedkar colney, gadhinglaj',8763,'40000'),('Rakesh','Rohit','last2',4215368791,'Toraskr chuk, kolhapur',9831,'2000');
/*!40000 ALTER TABLE `customer_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-28 21:05:45
