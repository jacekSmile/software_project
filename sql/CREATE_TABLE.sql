DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `uid` int(11) NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `username` varchar(50) NOT NULL COMMENT '用户账号',
  `password` varchar(255) NOT NULL COMMENT '用户密码',
  `nickname` varchar(32) NOT NULL COMMENT '用户昵称',
  `avatar` varchar(500) DEFAULT NULL COMMENT '用户头像url',
  `background` varchar(500) DEFAULT NULL COMMENT '主页背景图url',
  `gender` tinyint(4) NOT NULL DEFAULT '2' COMMENT '性别 0女 1男 2未知',
  `description` varchar(100) DEFAULT NULL COMMENT '个性签名',
  `exp` int(11) NOT NULL DEFAULT '0' COMMENT '经验值',
  `coin` double NOT NULL DEFAULT '0' COMMENT '硬币数',
  `vip` tinyint(4) NOT NULL DEFAULT '0' COMMENT '会员类型 0普通用户 1月度大会员 2季度大会员 3年度大会员',
  `state` tinyint(4) NOT NULL DEFAULT '0' COMMENT '状态 0正常 1封禁 2注销',
  `role` tinyint(4) NOT NULL DEFAULT '0' COMMENT '角色类型 0普通用户 1管理员 2超级管理员',
  `auth` tinyint(4) NOT NULL DEFAULT '0' COMMENT '官方认证 0普通用户 1个人认证 2机构认证',
  `auth_msg` varchar(30) DEFAULT NULL COMMENT '认证说明',
  `create_date` datetime NOT NULL COMMENT '创建时间',
  `delete_date` datetime DEFAULT NULL COMMENT '注销时间',
  PRIMARY KEY (`uid`),
  UNIQUE KEY `uid` (`uid`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `nickname` (`nickname`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='用户表';
