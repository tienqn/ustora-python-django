-- MySQL dump 10.13  Distrib 8.1.0, for Linux (x86_64)
--
-- Host: localhost    Database: ustora
-- ------------------------------------------------------
-- Server version	8.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add slider',7,'add_slider'),(26,'Can change slider',7,'change_slider'),(27,'Can delete slider',7,'delete_slider'),(28,'Can view slider',7,'view_slider'),(29,'Can add product',8,'add_product'),(30,'Can change product',8,'change_product'),(31,'Can delete product',8,'delete_product'),(32,'Can view product',8,'view_product'),(33,'Can add viewed product',9,'add_viewedproduct'),(34,'Can change viewed product',9,'change_viewedproduct'),(35,'Can delete viewed product',9,'delete_viewedproduct'),(36,'Can view viewed product',9,'view_viewedproduct');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$260000$ZpAaOCPhYHEAep9Xvk8UWJ$WUPASBZ2BYI6xdAIwslevR/mW8c7s4r+X+cXo72CW5w=','2023-10-15 12:59:04.259996',1,'root','','','root@ustora.com',1,1,'2023-10-14 12:58:47.133164');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-10-14 12:59:54.198700','1','slide 1',1,'[{\"added\": {}}]',7,1),(2,'2023-10-14 13:02:05.961740','1','slide 1',3,'',7,1),(3,'2023-10-14 13:02:24.023865','2','gia nhi',1,'[{\"added\": {}}]',7,1),(4,'2023-10-14 13:02:40.241013','3','momy',1,'[{\"added\": {}}]',7,1),(5,'2023-10-14 13:04:20.688278','4','gia kiet',1,'[{\"added\": {}}]',7,1),(6,'2023-10-14 13:05:21.822466','4','gia kiet',3,'',7,1),(7,'2023-10-14 13:05:21.855425','3','momy',3,'',7,1),(8,'2023-10-14 13:05:21.891194','2','gia nhi',3,'',7,1),(9,'2023-10-14 13:15:05.105459','1','iphone15',1,'[{\"added\": {}}]',8,1),(10,'2023-10-14 13:15:54.565707','2','iphone6',1,'[{\"added\": {}}]',8,1),(11,'2023-10-14 13:20:07.689833','5','slide 1',1,'[{\"added\": {}}]',7,1),(12,'2023-10-14 13:20:22.133539','6','slide 2',1,'[{\"added\": {}}]',7,1),(13,'2023-10-15 13:03:14.847306','1','ViewedProduct object (1)',1,'[{\"added\": {}}]',9,1),(14,'2023-10-15 13:56:03.176840','7','slide 3',1,'[{\"added\": {}}]',7,1),(15,'2023-10-15 13:56:17.356848','8','slide 4',1,'[{\"added\": {}}]',7,1),(16,'2023-10-15 13:56:48.766748','9','slide 5',1,'[{\"added\": {}}]',7,1),(17,'2023-10-15 13:57:39.637235','3','samsum s8',1,'[{\"added\": {}}]',8,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(8,'product','product'),(9,'product','viewedproduct'),(6,'sessions','session'),(7,'slider','slider');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-10-14 12:49:37.241663'),(2,'auth','0001_initial','2023-10-14 12:49:46.084517'),(3,'admin','0001_initial','2023-10-14 12:49:48.614130'),(4,'admin','0002_logentry_remove_auto_add','2023-10-14 12:49:48.684031'),(5,'admin','0003_logentry_add_action_flag_choices','2023-10-14 12:49:48.786985'),(6,'contenttypes','0002_remove_content_type_name','2023-10-14 12:49:49.911844'),(7,'auth','0002_alter_permission_name_max_length','2023-10-14 12:49:50.446504'),(8,'auth','0003_alter_user_email_max_length','2023-10-14 12:49:50.665167'),(9,'auth','0004_alter_user_username_opts','2023-10-14 12:49:50.819277'),(10,'auth','0005_alter_user_last_login_null','2023-10-14 12:49:51.747218'),(11,'auth','0006_require_contenttypes_0002','2023-10-14 12:49:51.781473'),(12,'auth','0007_alter_validators_add_error_messages','2023-10-14 12:49:51.861962'),(13,'auth','0008_alter_user_username_max_length','2023-10-14 12:49:53.014094'),(14,'auth','0009_alter_user_last_name_max_length','2023-10-14 12:49:53.816667'),(15,'auth','0010_alter_group_name_max_length','2023-10-14 12:49:53.990733'),(16,'auth','0011_update_proxy_permissions','2023-10-14 12:49:54.136569'),(17,'auth','0012_alter_user_first_name_max_length','2023-10-14 12:49:54.757815'),(18,'product','0001_initial','2023-10-14 12:49:55.401916'),(19,'product','0002_product_sold_count','2023-10-14 12:49:55.901877'),(20,'product','0003_viewedproduct','2023-10-14 12:49:57.772071'),(21,'product','0004_alter_viewedproduct_view_time','2023-10-14 12:49:57.820747'),(22,'product','0005_auto_20231013_0406','2023-10-14 12:49:59.808003'),(23,'product','0006_alter_product_img','2023-10-14 12:49:59.920415'),(24,'product','0007_alter_product_img','2023-10-14 12:49:59.997726'),(25,'sessions','0001_initial','2023-10-14 12:50:00.549439'),(26,'slider','0001_initial','2023-10-14 12:50:01.095926'),(27,'slider','0002_alter_slider_url','2023-10-14 12:50:02.051289'),(28,'slider','0003_alter_slider_title','2023-10-14 12:50:02.296502'),(29,'slider','0004_slider_sub_title','2023-10-14 12:50:02.917316'),(30,'slider','0005_alter_slider_sub_title','2023-10-14 12:50:03.034136'),(31,'slider','0006_alter_slider_sub_title','2023-10-14 12:50:03.105181'),(32,'slider','0007_alter_slider_url','2023-10-14 12:50:03.157469'),(33,'product','0008_alter_product_img','2023-10-14 13:01:50.914076'),(34,'slider','0008_alter_slider_url','2023-10-14 13:01:50.951162');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('g6f8g44t8jhle9ivftil7ua9fkxf1nsz','.eJxVjEEOwiAQRe_C2hCgwIBL956BwMxUqoYmpV0Z765NutDtf-_9l0h5W2vaOi9pInEWWpx-t5LxwW0HdM_tNkuc27pMRe6KPGiX15n4eTncv4Oae_3W2Wgk9HGEwTnFOQYwKpYYRgrWOgTv0TDbAaL3zgFAKJYVk9LFECnx_gDTNzdf:1qs0i0:iHEkEddE3B6hK-X_EAn4k0Uh-dyRtjqXLaaGoPfJ8-c','2023-10-29 12:59:04.298405');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_product`
--

DROP TABLE IF EXISTS `product_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` longtext NOT NULL,
  `img` varchar(100) NOT NULL,
  `origil_price` decimal(10,2) NOT NULL,
  `sell_price` decimal(10,2) NOT NULL,
  `sold_count` int NOT NULL,
  `added_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_product`
--

LOCK TABLES `product_product` WRITE;
/*!40000 ALTER TABLE `product_product` DISABLE KEYS */;
INSERT INTO `product_product` VALUES (1,'iphone15','asset/images/products/product-1.jpg',1500.00,1000.00,10,'2023-10-14 13:15:05.099090'),(2,'iphone6','asset/images/products/product-2.jpg',800.00,800.00,2,'2023-10-14 13:15:54.562754'),(3,'samsum s8','asset/images/products/product-4.jpg',2000.00,1800.00,45,'2023-10-15 13:57:39.634942');
/*!40000 ALTER TABLE `product_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_viewedproduct`
--

DROP TABLE IF EXISTS `product_viewedproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_viewedproduct` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `view_time` datetime(6) NOT NULL,
  `product_id_id` bigint NOT NULL,
  `user_id_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_viewedproduc_product_id_id_0eeaa462_fk_product_p` (`product_id_id`),
  KEY `product_viewedproduct_user_id_id_aa746584_fk_auth_user_id` (`user_id_id`),
  CONSTRAINT `product_viewedproduc_product_id_id_0eeaa462_fk_product_p` FOREIGN KEY (`product_id_id`) REFERENCES `product_product` (`id`),
  CONSTRAINT `product_viewedproduct_user_id_id_aa746584_fk_auth_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_viewedproduct`
--

LOCK TABLES `product_viewedproduct` WRITE;
/*!40000 ALTER TABLE `product_viewedproduct` DISABLE KEYS */;
INSERT INTO `product_viewedproduct` VALUES (1,'2023-10-15 13:03:13.000000',1,1);
/*!40000 ALTER TABLE `product_viewedproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `slider_slider`
--

DROP TABLE IF EXISTS `slider_slider`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `slider_slider` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `url` varchar(100) NOT NULL,
  `sub_title` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `slider_slider`
--

LOCK TABLES `slider_slider` WRITE;
/*!40000 ALTER TABLE `slider_slider` DISABLE KEYS */;
INSERT INTO `slider_slider` VALUES (5,'slide 1','asset/images/sliders/h4-slide.png','sub title 1'),(6,'slide 2','asset/images/sliders/h4-slide2.png','sub title 2'),(7,'slide 3','asset/images/sliders/h4-slide3.png','sub title 3'),(8,'slide 4','asset/images/sliders/h4-slide4.png','sub title 4'),(9,'slide 5','asset/images/sliders/h4-slide7.png','sub title 5');
/*!40000 ALTER TABLE `slider_slider` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-15 14:24:09
