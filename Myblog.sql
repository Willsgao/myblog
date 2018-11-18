/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50721
Source Host           : localhost:3306
Source Database       : blog

Target Server Type    : MYSQL
Target Server Version : 50721
File Encoding         : 65001

Date: 2018-10-09 00:03:02
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `blogtype`
-- ----------------------------
DROP TABLE IF EXISTS `blogtype`;
CREATE TABLE `blogtype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='博客类型 - 个人博客,公开博客,其他博客';

-- ----------------------------
-- Records of blogtype
-- ----------------------------
INSERT INTO `blogtype` VALUES ('1', '个人博客');
INSERT INTO `blogtype` VALUES ('2', '公开博客');
INSERT INTO `blogtype` VALUES ('3', '其他博客');

-- ----------------------------
-- Table structure for `category`
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cate_name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COMMENT='文章分类';

-- ----------------------------
-- Records of category
-- ----------------------------
INSERT INTO `category` VALUES ('1', 'Python');
INSERT INTO `category` VALUES ('2', 'Python Web');
INSERT INTO `category` VALUES ('3', '爬虫');
INSERT INTO `category` VALUES ('4', '人工智能');

-- ----------------------------
-- Table structure for `reply`
-- ----------------------------
DROP TABLE IF EXISTS `reply`;
CREATE TABLE `reply` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `topic_id` int(11) NOT NULL,
  `content` text NOT NULL,
  `reply_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_Reply_User` (`user_id`),
  KEY `FK_Reply_Topic` (`topic_id`),
  CONSTRAINT `FK_Reply_Topic` FOREIGN KEY (`topic_id`) REFERENCES `topic` (`id`),
  CONSTRAINT `FK_Reply_User` FOREIGN KEY (`user_id`) REFERENCES `user` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='博客回复';

-- ----------------------------
-- Records of reply
-- ----------------------------

-- ----------------------------
-- Table structure for `topic`
-- ----------------------------
DROP TABLE IF EXISTS `topic`;
CREATE TABLE `topic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `pub_date` datetime NOT NULL,
  `read_num` int(11) DEFAULT NULL,
  `content` text NOT NULL,
  `images` text,
  `blogtype_id` int(11) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_Topic_User` (`user_id`),
  KEY `FK_Topic_Blogtype` (`blogtype_id`),
  KEY `FK_Topic_Category` (`category_id`),
  CONSTRAINT `FK_Topic_Blogtype` FOREIGN KEY (`blogtype_id`) REFERENCES `blogtype` (`id`),
  CONSTRAINT `FK_Topic_Category` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`),
  CONSTRAINT `FK_Topic_User` FOREIGN KEY (`user_id`) REFERENCES `user` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COMMENT='博客文章';

-- ----------------------------
-- Records of topic
-- ----------------------------
INSERT INTO `topic` VALUES ('1', '简单而直接的Python Web框架', '2018-08-08 20:37:20', '123', 'From：https://www.oschina.net/question/5189_4306\r\n\r\nFrom：https://www.oschina.net/question/5189_4306\r\n\r\n\r\n\r\nWeb.py Cookbook 简体中文版：http://webpy.org/cookbook/index.zh-cn\r\n\r\nweb.py 0.3 新手指南：http://webpy.org/docs/0.3/tutorial.zh-cn\r\n\r\n\r\n\r\nwebpy 官网文档：http://webpy.org/ web.py 十分钟创建简易博客：http://blog.csdn.net/freeking101/article/details/53020728\r\n\r\nweb.py 是一个Python 的web 框架，它简单而且功能强大。web.py 是公开的，无论用于什么用途都是没有限制的。而且相当的小巧，应当归属于轻量级的web 框架。但这并不影响web.py 的强大，而且使用起来很简单、很直接。在实际应用上，web.py 更多的是学术上的价值，因为你可以看到更多web 应用的底层，这在当今“抽象得很好”的web 框架上是学不到的 ：） 如果想了解更多web.py，可以访问web.py 的官方文档。 先感受一下web.py 的简单而强大：\r\n\r\n上面就是一个基于web.py 的完整的Web 应用。将上面的代码保存为文件code.py，在命令行下执行python code.py。然后打开你的浏览器，打开地址：http://localhost:8080 或者 http://localhost:8080/test 没有意外的话(当然要先安装web.py，下面会有介绍)，浏览器会显示“Hello, world”或者 “Hello, test”。 \r\n\r\n\r\n\r\n1. 安装 下载 web.py 的安装文件，将下载得到的文件 web.py 解压，进入解压后的文件夹，在命令行下执行：python setup.py install，在Linux 等系统下，需要root 的权限，可以执行：sudo python setup.py install。 2. URL 处理 对于一个站点来说，URL 的组织是最重要的一个部分，因为这是用户看得到的部分，而且直接影响到站点是如何工作的，例如：www.baidu.com ，其URLs 甚至是网页界面的一部分。而web.py 以简单的方式就能够构造出一个强大的URLs。 在每个web.py 应用，必须先import web 模块：', 'images/banner01.jpg', '1', '2', '1');
INSERT INTO `topic` VALUES ('2', 'Python-win10下使用定时任务执行程序', '2017-10-01 00:00:00', '4567', 'webpy 官网文档：http://webpy.org/ web.py 十分钟创建简易博客：http://blog.csdn.net/freeking101/article/details/53020728\r\n\r\nweb.py 是一个Python 的web 框架，它简单而且功能强大。web.py 是公开的，无论用于什么用途都是没有限制的。而且相当的小巧，应当归属于轻量级的web 框架。但这并不影响web.py 的强大，而且使用起来很简单、很直接。在实际应用上，web.py 更多的是学术上的价值，因为你可以看到更多web 应用的底层，这在当今“抽象得很好”的web 框架上是学不到的 ：） 如果想了解更多web.py，可以访问web.py 的官方文档。 先感受一下web.py 的简单而强大：\r\n\r\n上面就是一个基于web.py 的完整的Web 应用。将上面的代码保存为文件code.py，在命令行下执行python code.py。然后打开你的浏览器，打开地址：http://localhost:8080 或者 http://localhost:8080/test 没有意外的话(当然要先安装web.py，下面会有介绍)，浏览器会显示“Hello, world”或者 “Hello, test”。 \r\n\r\n\r\n\r\n1. 安装 下载 web.py 的安装文件，将下载得到的文件 web.py 解压，进入解压后的文件夹，在命令行下执行：python setup.py install，在Linux 等系统下，需要root 的权限，可以执行：sudo python setup.py install。 2. URL 处理 对于一个站点来说，URL 的组织是最重要的一个部分，因为这是用户看得到的部分，而且直接影响到站点是如何工作的，例如：www.baidu.com ，其URLs 甚至是网页界面的一部分。而web.py 以简单的方式就能够构造出一个强大的URLs。 在每个web.py 应用，必须先import web 模块：\r\nwebpy 官网文档：http://webpy.org/ web.py 十分钟创建简易博客：http://blog.csdn.net/freeking101/article/details/53020728\r\n\r\nweb.py 是一个Python 的web 框架，它简单而且功能强大。web.py 是公开的，无论用于什么用途都是没有限制的。而且相当的小巧，应当归属于轻量级的web 框架。但这并不影响web.py 的强大，而且使用起来很简单、很直接。在实际应用上，web.py 更多的是学术上的价值，因为你可以看到更多web 应用的底层，这在当今“抽象得很好”的web 框架上是学不到的 ：） 如果想了解更多web.py，可以访问web.py 的官方文档。 先感受一下web.py 的简单而强大：\r\n\r\n上面就是一个基于web.py 的完整的Web 应用。将上面的代码保存为文件code.py，在命令行下执行python code.py。然后打开你的浏览器，打开地址：http://localhost:8080 或者 http://localhost:8080/test 没有意外的话(当然要先安装web.py，下面会有介绍)，浏览器会显示“Hello, world”或者 “Hello, test”。 \r\n\r\n\r\n\r\n1. 安装 下载 web.py 的安装文件，将下载得到的文件 web.py 解压，进入解压后的文件夹，在命令行下执行：python setup.py install，在Linux 等系统下，需要root 的权限，可以执行：sudo python setup.py install。 2. URL 处理 对于一个站点来说，URL 的组织是最重要的一个部分，因为这是用户看得到的部分，而且直接影响到站点是如何工作的，例如：www.baidu.com ，其URLs 甚至是网页界面的一部分。而web.py 以简单的方式就能够构造出一个强大的URLs。 在每个web.py 应用，必须先import web 模块：\r\nwebpy 官网文档：http://webpy.org/ web.py 十分钟创建简易博客：http://blog.csdn.net/freeking101/article/details/53020728\r\n\r\nweb.py 是一个Python 的web 框架，它简单而且功能强大。web.py 是公开的，无论用于什么用途都是没有限制的。而且相当的小巧，应当归属于轻量级的web 框架。但这并不影响web.py 的强大，而且使用起来很简单、很直接。在实际应用上，web.py 更多的是学术上的价值，因为你可以看到更多web 应用的底层，这在当今“抽象得很好”的web 框架上是学不到的 ：） 如果想了解更多web.py，可以访问web.py 的官方文档。 先感受一下web.py 的简单而强大：\r\n\r\n上面就是一个基于web.py 的完整的Web 应用。将上面的代码保存为文件code.py，在命令行下执行python code.py。然后打开你的浏览器，打开地址：http://localhost:8080 或者 http://localhost:8080/test 没有意外的话(当然要先安装web.py，下面会有介绍)，浏览器会显示“Hello, world”或者 “Hello, test”。 \r\n\r\n\r\n\r\n1. 安装 下载 web.py 的安装文件，将下载得到的文件 web.py 解压，进入解压后的文件夹，在命令行下执行：python setup.py install，在Linux 等系统下，需要root 的权限，可以执行：sudo python setup.py install。 2. URL 处理 对于一个站点来说，URL 的组织是最重要的一个部分，因为这是用户看得到的部分，而且直接影响到站点是如何工作的，例如：www.baidu.com ，其URLs 甚至是网页界面的一部分。而web.py 以简单的方式就能够构造出一个强大的URLs。 在每个web.py 应用，必须先import web 模块：\r\nFrom：https://www.oschina.net/question/5189_4306\r\n\r\nFrom：https://www.oschina.net/question/5189_4306\r\n\r\n\r\n\r\nWeb.py Cookbook 简体中文版：http://webpy.org/cookbook/index.zh-cn\r\n\r\nweb.py 0.3 新手指南：http://webpy.org/docs/0.3/tutorial.zh-cn\r\n\r\n\r\n\r\nwebpy 官网文档：http://webpy.org/ web.py 十分钟创建简易博客：http://blog.csdn.net/freeking101/article/details/53020728\r\n\r\nweb.py 是一个Python 的web 框架，它简单而且功能强大。web.py 是公开的，无论用于什么用途都是没有限制的。而且相当的小巧，应当归属于轻量级的web 框架。但这并不影响web.py 的强大，而且使用起来很简单、很直接。在实际应用上，web.py 更多的是学术上的价值，因为你可以看到更多web 应用的底层，这在当今“抽象得很好”的web 框架上是学不到的 ：） 如果想了解更多web.py，可以访问web.py 的官方文档。 先感受一下web.py 的简单而强大：\r\n\r\n上面就是一个基于web.py 的完整的Web 应用。将上面的代码保存为文件code.py，在命令行下执行python code.py。然后打开你的浏览器，打开地址：http://localhost:8080 或者 http://localhost:8080/test 没有意外的话(当然要先安装web.py，下面会有介绍)，浏览器会显示“Hello, world”或者 “Hello, test”。 \r\n\r\n\r\n\r\n1. 安装 下载 web.py 的安装文件，将下载得到的文件 web.py 解压，进入解压后的文件夹，在命令行下执行：python setup.py install，在Linux 等系统下，需要root 的权限，可以执行：sudo python setup.py install。 2. URL 处理 对于一个站点来说，URL 的组织是最重要的一个部分，因为这是用户看得到的部分，而且直接影响到站点是如何工作的，例如：www.baidu.com ，其URLs 甚至是网页界面的一部分。而web.py 以简单的方式就能够构造出一个强大的URLs。 在每个web.py 应用，必须先import web 模块：', 'images/banner02.jpg', '1', '2', '1');
INSERT INTO `topic` VALUES ('3', '爬虫微课5小时 python学习路线', '2015-10-01 00:00:00', '0', 'Python 安装配置及基本语法篇 Python 语言速成 Python 基本知识 Python 常用表达式 Python 基础语法 Python 语法篇：菜鸟的Python笔记 Python精要参考：快速入门 《Python标... ', 'images/banner03.jpg', '1', '2', '1');
INSERT INTO `topic` VALUES ('4', 'linux升级Pip3,安装pip svn', '2016-09-21 00:00:00', '234', 'python中打开TXT文件报错2017年03月09日 14:30:57 阅读数:676 在IDLE命令行引用一文件夹下的函数,来了条错误提示:FileNotFoundError: [Errno 2] No such ...', 'images/toppic01.jpg', '1', '2', '1');
INSERT INTO `topic` VALUES ('5', '精通python变成', '2017-12-04 00:00:00', '999', '随便写点内容吧', 'images/zd01.jpg', '1', '2', '1');

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `loginname` varchar(50) NOT NULL,
  `uname` varchar(30) NOT NULL,
  `email` varchar(200) NOT NULL,
  `url` varchar(200) DEFAULT NULL,
  `upwd` varchar(30) NOT NULL,
  `is_author` tinyint(4) DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='用户信息表';

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'piye', '皮爷', 'piye@163.com', null, '123456', '1');
INSERT INTO `user` VALUES ('2', 'weiye', '魏爷', 'weimz@163.com', null, '123456', '0');
INSERT INTO `user` VALUES ('3', 'lvye', '吕爷', 'lvye@163.com', null, '123456', '0');

-- ----------------------------
-- Table structure for `voke`
-- ----------------------------
DROP TABLE IF EXISTS `voke`;
CREATE TABLE `voke` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `topic_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_Voke_User` (`user_id`),
  KEY `FK_Voke_Topic` (`topic_id`),
  CONSTRAINT `FK_Voke_Topic` FOREIGN KEY (`topic_id`) REFERENCES `topic` (`id`),
  CONSTRAINT `FK_Voke_User` FOREIGN KEY (`user_id`) REFERENCES `user` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='点赞';

-- ----------------------------
-- Records of voke
-- ----------------------------
