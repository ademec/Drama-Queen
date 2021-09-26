
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


DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `item` (
  `itemid` varchar(100) NOT NULL,
  `date` int(11) DEFAULT NULL,
  `decade` int(11) DEFAULT NULL,
  `url` varchar(2000) DEFAULT NULL,
  `itemtype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`itemid`)
);


DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `person` (
  `personid` varchar(100) NOT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `firstname` varchar(100) DEFAULT NULL,
  `birthdate` datetime DEFAULT NULL,
  `deathdate` datetime DEFAULT NULL,
  `isTrue` tinyint(1) DEFAULT NULL,
  `fullname` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`personid`)
);
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS `person_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `person_item` (
  `personid` varchar(100) DEFAULT NULL,
  `itemid` varchar(100) DEFAULT NULL,
  `isTrue` tinyint(1) DEFAULT NULL
);
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS `person_thesis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `person_thesis` (
  `personid` varchar(100) DEFAULT NULL,
  `thesisid` varchar(100) DEFAULT NULL,
  `isTrue` tinyint(1) DEFAULT NULL
);
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS `thesis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `thesis` (
  `thesisid` varchar(100) NOT NULL,
  `title` varchar(3000) DEFAULT NULL,
  `defensedate` int(11) DEFAULT NULL,
  `decade` int(11) DEFAULT NULL,
  `isTrue` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`thesisid`)
);
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS `thesis_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `thesis_item` (
  `thesisid` varchar(100) DEFAULT NULL,
  `itemid` varchar(100) DEFAULT NULL,
  `isTrue` tinyint(1) DEFAULT NULL
);
/*!40101 SET character_set_client = @saved_cs_client */;

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

