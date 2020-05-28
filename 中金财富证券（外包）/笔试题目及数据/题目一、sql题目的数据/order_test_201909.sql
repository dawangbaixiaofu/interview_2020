/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50720
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2020-03-03 10:08:43
*/
USE test;
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for order_test_201909
-- ----------------------------
DROP TABLE IF EXISTS `order_test_201909`;
CREATE TABLE `order_test_201909` (
  `客户编号` varchar(12) DEFAULT NULL,
  `客户姓名` varchar(128) DEFAULT NULL,
  `组合名称` varchar(255) DEFAULT NULL,
  `签约日期` date DEFAULT NULL,
  `签约方式` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_test_201909
-- ----------------------------
INSERT INTO `order_test_201909` VALUES ('50181013', '陈xx', '珠玉二期', '2019-04-19', '现金');
INSERT INTO `order_test_201909` VALUES ('40591014', '陈x', '超跌反弹一号', '2019-03-22', '现金');
INSERT INTO `order_test_201909` VALUES ('46721017', '蓝x', '步步为赢', '2019-09-12', '现金');
INSERT INTO `order_test_201909` VALUES ('14091020', '陈xx', '价值掘金1期', '2019-03-26', '现金');
INSERT INTO `order_test_201909` VALUES ('14091020', '陈xx', '超跌反弹二号', '2019-09-03', '现金');
INSERT INTO `order_test_201909` VALUES ('14091020', '陈xx', null, '2019-04-01', '现金');
INSERT INTO `order_test_201909` VALUES ('14091020', '陈xx', null, '2019-04-17', '现金');
INSERT INTO `order_test_201909` VALUES ('14091020', '陈xx', '稳健成长', '2019-09-17', '现金');
INSERT INTO `order_test_201909` VALUES ('80021020', '严xx', '超跌反弹二号', '2019-09-16', '现金');
INSERT INTO `order_test_201909` VALUES ('19891033', '陈xx', '超跌反弹二号', '2019-03-28', '现金');
INSERT INTO `order_test_201909` VALUES ('35611037', '向xx', '游骑兵2号', '2019-03-11', '现金');
INSERT INTO `order_test_201909` VALUES ('58991040', '符xx', null, '2019-09-17', '现金');
INSERT INTO `order_test_201909` VALUES ('19691042', '魏x', '超跌反弹二号', '2019-09-04', '现金');
INSERT INTO `order_test_201909` VALUES ('19691042', '魏x', '快赢5号', '2019-09-17', '现金');
INSERT INTO `order_test_201909` VALUES ('21111042', '张xx', '超跌反弹二号', '2019-09-17', '现金');
INSERT INTO `order_test_201909` VALUES ('77611218', '王x', '惟道乾龙', '2019-03-21', '现金');
INSERT INTO `order_test_201909` VALUES ('14831224', '高x', '游骑兵1号', '2019-03-27', '现金');
INSERT INTO `order_test_201909` VALUES ('10111232', '卓xx', '快赢7号', '2019-10-01', '绝对佣金率');
INSERT INTO `order_test_201909` VALUES ('41371303', '唐xx', '快赢7号', '2019-02-15', '现金');
INSERT INTO `order_test_201909` VALUES ('24171336', '王xx', '超跌反弹一号', '2018-12-04', '现金');
INSERT INTO `order_test_201909` VALUES ('92701342', '彭xx', '快赢3号', '2019-03-28', '现金');
INSERT INTO `order_test_201909` VALUES ('02531827', '冯xx', '超跌反弹一号', '2019-03-21', '现金');
INSERT INTO `order_test_201909` VALUES ('88201830', '董xx', '游骑兵5号', '2019-04-17', '绝对佣金率');
INSERT INTO `order_test_201909` VALUES ('22331844', '李xx', '快赢3号', '2018-11-28', '现金');
INSERT INTO `order_test_201909` VALUES ('65431846', '黄xx', '超跌反弹二号', '2018-11-29', '现金');
INSERT INTO `order_test_201909` VALUES ('12861857', '吴xx', '超跌反弹二号', '2019-03-28', '现金');
INSERT INTO `order_test_201909` VALUES ('04891893', '陈xx', '快赢7号', '2019-03-28', '现金');
INSERT INTO `order_test_201909` VALUES ('30041898', '黄xx', '波段狙击一号', '2018-08-17', '现金');
INSERT INTO `order_test_201909` VALUES ('71881904', '刘xx', '波段狙击三号', '2019-03-26', '现金');
INSERT INTO `order_test_201909` VALUES ('55622001', '王xx', '超跌反弹二号', '2018-09-17', '绝对佣金率');
INSERT INTO `order_test_201909` VALUES ('86572040', '向xx', '智投一号', '2019-03-26', '现金');
INSERT INTO `order_test_201909` VALUES ('24902041', '蔡xx', '超跌反弹一号', '2019-03-28', '现金');
INSERT INTO `order_test_201909` VALUES ('24212060', '张xx', '快赢7号', '2019-03-21', '现金');
INSERT INTO `order_test_201909` VALUES ('24212060', '张xx', '超跌反弹二号', '2018-11-27', '现金');
INSERT INTO `order_test_201909` VALUES ('24212060', '张xx', '游骑兵3号', '2019-07-01', '绝对佣金率');
INSERT INTO `order_test_201909` VALUES ('40782060', '王xx', '超跌反弹一号', '2019-03-21', '现金');
INSERT INTO `order_test_201909` VALUES ('52912060', '李xx', null, '2019-03-22', '现金');
INSERT INTO `order_test_201909` VALUES ('48392061', '王xx', '快赢4号', '2019-09-10', '绝对佣金率');
INSERT INTO `order_test_201909` VALUES ('91762370', '杨x', null, '2019-03-26', '现金');
INSERT INTO `order_test_201909` VALUES ('98632501', '倪xx', '惟道珠玉', '2018-12-04', '现金');
INSERT INTO `order_test_201909` VALUES ('49692641', '陈x', '珠玉四期', '2019-03-28', '现金');
INSERT INTO `order_test_201909` VALUES ('58162850', '陆x', '超跌反弹二号', '2019-03-27', '现金');
INSERT INTO `order_test_201909` VALUES ('82642850', '张xx', '价值掘金2期', '2019-03-26', '现金');
INSERT INTO `order_test_201909` VALUES ('37512860', '廖xx', '超跌反弹二号', '2019-03-01', '绝对佣金率');
INSERT INTO `order_test_201909` VALUES ('27032870', '徐xx', '长水一号', '2019-03-26', '现金');
INSERT INTO `order_test_201909` VALUES ('29102900', '许xx', '价值掘金3期', '2018-11-28', '现金');
INSERT INTO `order_test_201909` VALUES ('82962901', '孙xx', '超跌反弹二号', '2019-03-27', '现金');
INSERT INTO `order_test_201909` VALUES ('12033040', '杨xx', '珠玉三期', '2019-03-27', '现金');
INSERT INTO `order_test_201909` VALUES ('12033040', '杨xx', '珠玉一期', '2018-12-05', '现金');
INSERT INTO `order_test_201909` VALUES ('29173051', '吴xx', '快赢7号', '2019-03-28', '现金');
