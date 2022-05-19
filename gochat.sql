/*
 Navicat Premium Data Transfer

 Source Server         : IngramLu
 Source Server Type    : MySQL
 Source Server Version : 80028
 Source Host           : localhost:3306
 Source Schema         : gochat

 Target Server Type    : MySQL
 Target Server Version : 80028
 File Encoding         : 65001

 Date: 19/05/2022 09:56:03
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 72 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int NULL DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 39 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for home_addfriends
-- ----------------------------
DROP TABLE IF EXISTS `home_addfriends`;
CREATE TABLE `home_addfriends`  (
  `ApplicantID` int NOT NULL AUTO_INCREMENT,
  `UserID` int NOT NULL,
  `ObjectID` int NOT NULL,
  `FriendsGroupID` int NOT NULL,
  `Remarksname` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Addway` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Remarks` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Sendtime` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Responsetime` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Rep_results` int NOT NULL COMMENT '0：申请中 1：同意 -1：拒绝 2:忽略',
  PRIMARY KEY (`ApplicantID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 61 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for home_addgroups
-- ----------------------------
DROP TABLE IF EXISTS `home_addgroups`;
CREATE TABLE `home_addgroups`  (
  `ApplicantID` int NOT NULL AUTO_INCREMENT,
  `UserID` int NOT NULL,
  `ObjectID` int NOT NULL,
  `Addway` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Remarks` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Sendtime` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Responsetime` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Rep_results` int NOT NULL,
  `ProcessorID` int NULL DEFAULT NULL,
  PRIMARY KEY (`ApplicantID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for home_friends
-- ----------------------------
DROP TABLE IF EXISTS `home_friends`;
CREATE TABLE `home_friends`  (
  `RelationID` bigint NOT NULL AUTO_INCREMENT,
  `FriendID` int NOT NULL,
  `UserID` int NOT NULL,
  `Name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `FriendTypeID` int NOT NULL,
  `FriendGroupsID` int NOT NULL,
  PRIMARY KEY (`RelationID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 58 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for home_friendsgroup
-- ----------------------------
DROP TABLE IF EXISTS `home_friendsgroup`;
CREATE TABLE `home_friendsgroup`  (
  `GroupID` int NOT NULL AUTO_INCREMENT,
  `UserID` int NOT NULL,
  `GroupName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `SerialNumber` int NOT NULL,
  `CreateTime` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`GroupID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 45 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for home_friendtype
-- ----------------------------
DROP TABLE IF EXISTS `home_friendtype`;
CREATE TABLE `home_friendtype`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `TypeName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for home_group
-- ----------------------------
DROP TABLE IF EXISTS `home_group`;
CREATE TABLE `home_group`  (
  `GroupID` int NOT NULL AUTO_INCREMENT,
  `GroupName` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `GroupleaderID` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `GroupAvatars` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT 'Groupdefault.png',
  `GroupIntro` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Groupverification` int NOT NULL COMMENT '1：任何人\r\n2：需通过验证\r\n3：不允许加入',
  `Createtime` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`GroupID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10009 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for home_groupmembers
-- ----------------------------
DROP TABLE IF EXISTS `home_groupmembers`;
CREATE TABLE `home_groupmembers`  (
  `ApplicantID` int NOT NULL AUTO_INCREMENT,
  `UserID` int NOT NULL,
  `GroupID` int NOT NULL,
  `GroupName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Role` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Jointime` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`ApplicantID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 32 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for home_messages
-- ----------------------------
DROP TABLE IF EXISTS `home_messages`;
CREATE TABLE `home_messages`  (
  `MessagesID` int NOT NULL AUTO_INCREMENT,
  `PostMessages` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `Status` int NOT NULL,
  `SendTime` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `MessagesType` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `FromUserID` int NOT NULL,
  `ToUserID` int NOT NULL,
  PRIMARY KEY (`MessagesID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 604 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for home_messageslist
-- ----------------------------
DROP TABLE IF EXISTS `home_messageslist`;
CREATE TABLE `home_messageslist`  (
  `MessageslistID` int NOT NULL AUTO_INCREMENT,
  `UserID` int NOT NULL,
  `ObjectID` int NOT NULL,
  `Time` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `MessagesType` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `CreateTime` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `UnreadNum` int NOT NULL DEFAULT 0,
  PRIMARY KEY (`MessageslistID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 106 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for home_messagestype
-- ----------------------------
DROP TABLE IF EXISTS `home_messagestype`;
CREATE TABLE `home_messagestype`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `TypeName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for home_securityquestion
-- ----------------------------
DROP TABLE IF EXISTS `home_securityquestion`;
CREATE TABLE `home_securityquestion`  (
  `QuestionID` int NOT NULL AUTO_INCREMENT,
  `Question` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`QuestionID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `LoginID` int NOT NULL AUTO_INCREMENT COMMENT '账号',
  `Password` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '密码',
  `UserName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户名',
  `Sex` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '性别',
  `Age` int NULL DEFAULT NULL COMMENT '年龄',
  `HeadPortrait` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '头像',
  `PhoneNumber` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '手机号',
  `Address` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '' COMMENT '地址',
  `BloodType` varchar(4) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '血型',
  `DateBirth` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '出生日期',
  `Constellation` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '无' COMMENT '星座',
  `ShengXiao` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '无' COMMENT '生肖',
  `Sign` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '无' COMMENT '签名',
  `Profession` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '无' COMMENT '职业',
  `Region` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '无' COMMENT '所处地区',
  `Mail` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '' COMMENT '邮箱',
  `AddtimeID` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '注册时间序列',
  `Registertime` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `LoginStatus` int NOT NULL COMMENT '登录状态',
  `HeaderColor` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '#3483D5' COMMENT '头颜色',
  `question1` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '密保问题1',
  `question2` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `answer1` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '密保问题2',
  `answer2` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`LoginID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10044 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Triggers structure for table home_friends
-- ----------------------------
DROP TRIGGER IF EXISTS `删除好友`;
delimiter ;;
CREATE TRIGGER `删除好友` AFTER DELETE ON `home_friends` FOR EACH ROW begin 
	delete from home_messageslist where home_messageslist.UserID=old.UserID and home_messageslist.ObjectID=old.FriendID and home_messageslist.MessagesType='friend';
end
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table home_group
-- ----------------------------
DROP TRIGGER IF EXISTS `插入群主关系`;
delimiter ;;
CREATE TRIGGER `插入群主关系` AFTER INSERT ON `home_group` FOR EACH ROW begin 
	INSERT into home_groupmembers (UserID,GroupID,Role,Jointime) VALUES(new.GroupleaderID,new.GroupID,'Groupleader',new.CreateTime);
end
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table home_group
-- ----------------------------
DROP TRIGGER IF EXISTS `解散群`;
delimiter ;;
CREATE TRIGGER `解散群` BEFORE DELETE ON `home_group` FOR EACH ROW begin 
	delete from home_groupmembers where home_groupmembers.GroupID=old.GroupID;
end
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table home_groupmembers
-- ----------------------------
DROP TRIGGER IF EXISTS `退群`;
delimiter ;;
CREATE TRIGGER `退群` AFTER DELETE ON `home_groupmembers` FOR EACH ROW begin 
	delete from home_messageslist where home_messageslist.UserID=old.UserID and home_messageslist.ObjectID=old.GroupID and home_messageslist.MessagesType='group';
end
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table home_messages
-- ----------------------------
DROP TRIGGER IF EXISTS `自动新增最近会话`;
delimiter ;;
CREATE TRIGGER `自动新增最近会话` BEFORE INSERT ON `home_messages` FOR EACH ROW begin 
if NOT EXISTS (SELECT * FROM home_messageslist WHERE home_messageslist.UserID=new.ToUserID AND home_messageslist.ObjectID=new.FromUserID and home_messageslist.MessagesType='friend') and new.MessagesType='friend' then
	INSERT into home_messageslist(UserID,ObjectID,Time,MessagesType,CreateTime,UnreadNum) SELECT new.ToUserID,new.FromUserID,date_format(NOW(), '%Y/%m/%d %H:%i:%s'),'friend',date_format(NOW(), '%Y/%m/%d %H:%i:%s'),1
FROM dual;
end if;

if new.MessagesType='group' and (select UserID from home_groupmembers where home_groupmembers.GroupID=new.ToUserID and home_groupmembers.UserID!=new.FromUserID and home_groupmembers.UserID not in(select UserID from home_messageslist where home_messageslist.ObjectID=new.ToUserID and home_messageslist.MessagesType='group')) is not null then
	INSERT into home_messageslist(UserID,ObjectID,Time,MessagesType,CreateTime,UnreadNum) SELECT UserID,new.ToUserID,date_format(NOW(), '%Y/%m/%d %H:%i:%s'),'group',date_format(NOW(), '%Y/%m/%d %H:%i:%s'),1 from home_groupmembers where home_groupmembers.GroupID=new.ToUserID and home_groupmembers.UserID!=new.FromUserID and home_groupmembers.UserID not in(select UserID from home_messageslist where home_messageslist.ObjectID=new.ToUserID and home_messageslist.MessagesType='group');
end if;
end
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table home_messages
-- ----------------------------
DROP TRIGGER IF EXISTS `好友信息自动增长未读数`;
delimiter ;;
CREATE TRIGGER `好友信息自动增长未读数` BEFORE INSERT ON `home_messages` FOR EACH ROW begin 
if new.MessagesType='friend' then
	update home_messageslist set UnreadNum=UnreadNum+1 where UserID=new.ToUserID and ObjectID=new.FromUserID;
	end if;
	
	if new.MessagesType='group' then
	update home_messageslist set UnreadNum=UnreadNum+1 where ObjectID=new.ToUserID and UserID in (select UserID from home_groupmembers where home_groupmembers.GroupID=new.ToUserID and home_groupmembers.UserID!=new.FromUserID);
	end if;
end
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table home_messages
-- ----------------------------
DROP TRIGGER IF EXISTS `Update_time`;
delimiter ;;
CREATE TRIGGER `Update_time` AFTER INSERT ON `home_messages` FOR EACH ROW begin 
if new.MessagesType='friend' then
	UPDATE home_messageslist SET home_messageslist.Time=date_format(NOW(), '%Y/%m/%d %H:%i:%s') WHERE (home_messageslist.UserID=new.FromUserID and home_messageslist.ObjectID=new.ToUserID) or (home_messageslist.UserID=new.ToUserID and home_messageslist.ObjectID=new.FromUserID) and home_messageslist.MessagesType='friend';
	end if;
	
	if new.MessagesType='group' then
	UPDATE home_messageslist SET home_messageslist.Time=date_format(NOW(), '%Y/%m/%d %H:%i:%s') WHERE home_messageslist.ObjectID=new.ToUserID and home_messageslist.MessagesType='group';
	end if;
end
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table user
-- ----------------------------
DROP TRIGGER IF EXISTS `Create_account`;
delimiter ;;
CREATE TRIGGER `Create_account` AFTER INSERT ON `user` FOR EACH ROW begin 
	insert into home_friendsgroup(UserID,GroupName,SerialNumber,CreateTime) values(new.LoginID,'我的好友',1,date_format(NOW(), '%Y%m%d%H%i%s'));
end
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
