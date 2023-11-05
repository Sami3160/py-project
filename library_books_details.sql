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
-- Table structure for table `books_details`
--

DROP TABLE IF EXISTS `books_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books_details` (
  `book_name` varchar(40) DEFAULT NULL,
  `book_code` decimal(4,0) NOT NULL,
  `author_name` varchar(15) DEFAULT NULL,
  `book_type` varchar(40) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `price` int NOT NULL,
  PRIMARY KEY (`book_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_details`
--

LOCK TABLES `books_details` WRITE;
/*!40000 ALTER TABLE `books_details` DISABLE KEYS */;
INSERT INTO `books_details` VALUES ('Football strategy',1134,'Penaldo','Sports',1,35),('World war hulk comic',1200,'Stan lee','Entertainment',1,550),('Marvel zombies',1234,'Stan lee','Entertainment',0,300),('Data Communication (basic)',1616,'J. S. Katre','Study-network',1,250),('Data Communication (advanced)',2626,'J. S. Katre','Study-network',1,230),('Demon Slayer manga',2643,'Nejuko','Entertainment',1,799),('Tijutsu',2646,'Might Guy','Sports',1,1799),('GUI developement using vb.net',2993,'V. B. Sable','Study-coding',1,390),('Learning JAVA;',3165,'M. patil','Study-coding-java',1,249),('One Punch-Man manga s2',3452,'Murata','Entertainment',1,250),('Python applicaction developement',3636,'S. Kavle','Study-coding-python',1,199),('Python UI designing',4646,'Harry','Study-coding-python',1,200),('Python basics',5656,'Harry','Study-coding-python',0,349),('Football strategy',8787,'Messi','Sports',1,1099),('One Punch-Man manga s1',9087,'Murata','Entertainment',1,250);
/*!40000 ALTER TABLE `books_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-28 21:05:44
