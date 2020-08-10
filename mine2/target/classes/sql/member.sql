
/* Drop Tables */

DROP TABLE t_comment CASCADE CONSTRAINTS;
DROP TABLE t_article CASCADE CONSTRAINTS;
DROP TABLE t_board CASCADE CONSTRAINTS;
DROP TABLE t_user CASCADE CONSTRAINTS;



/* Drop Sequences */

DROP SEQUENCE seq_article;
DROP SEQUENCE seq_board;
DROP SEQUENCE seq_comment;
DROP SEQUENCE seq_user;




/* Create Sequences */

CREATE SEQUENCE seq_article;
CREATE SEQUENCE seq_board INCREMENT BY 10 START WITH 100;
CREATE SEQUENCE seq_comment;
CREATE SEQUENCE seq_user;



/* Create Tables */

CREATE TABLE t_article
(
	art_no number NOT NULL,
	art_title varchar2(200) NOT NULL,
	art_content clob NOT NULL,
	art_like number(5) DEFAULT 0 NOT NULL,
	art_dislike number(5) DEFAULT 0 NOT NULL,
	art_regdate date DEFAULT sysdate NOT NULL,
	art_readcnt number(5) DEFAULT 0 NOT NULL,
	art_com_cnt number(4) DEFAULT 0 NOT NULL,
	art_ip varchar2(35),
	boa_no number NOT NULL,
	usr_no number NOT NULL,
	PRIMARY KEY (art_no)
);


CREATE TABLE t_board
(
	boa_no number NOT NULL,
	boa_name varchar2(20) NOT NULL,
	boa_status number(1) DEFAULT 1 NOT NULL,
	usr_no number NOT NULL,
	PRIMARY KEY (boa_no)
);


CREATE TABLE t_comment
(
	com_no number NOT NULL,
	com_content varchar2(1000) NOT NULL,
	com_regdate date DEFAULT sysdate NOT NULL,
	com_like number(5) DEFAULT 0 NOT NULL,
	com_dislike number(5) DEFAULT 0 NOT NULL,
	com_ip varchar2(35),
	art_no number NOT NULL,
	usr_no number NOT NULL,
	PRIMARY KEY (com_no)
);


CREATE TABLE t_user
(
	usr_no number NOT NULL,
	usr_id varchar2(20) NOT NULL UNIQUE,
	usr_pw varchar2(128) NOT NULL,
	usr_name varchar2(30) NOT NULL,
	usr_info varchar2(1000),
	usr_level number(1) DEFAULT 1 NOT NULL,
	usr_status number(1) DEFAULT 0 NOT NULL,
	usr_regdate date DEFAULT sysdate NOT NULL,
	usr_lastlogin date DEFAULT sysdate NOT NULL,
	usr_logcnt number(7) DEFAULT 0 NOT NULL,
	usr_ip varchar2(35),
	usr_zipcode varchar2(7),
	usr_address varchar2(100),
	usr_address_detail varchar2(60),
	PRIMARY KEY (usr_no)
);



/* Create Foreign Keys */

ALTER TABLE t_comment
	ADD FOREIGN KEY (art_no)
	REFERENCES t_article (art_no)
;


ALTER TABLE t_article
	ADD FOREIGN KEY (boa_no)
	REFERENCES t_board (boa_no)
;


ALTER TABLE t_article
	ADD FOREIGN KEY (usr_no)
	REFERENCES t_user (usr_no)
;


ALTER TABLE t_board
	ADD FOREIGN KEY (usr_no)
	REFERENCES t_user (usr_no)
;


ALTER TABLE t_comment
	ADD FOREIGN KEY (usr_no)
	REFERENCES t_user (usr_no)
;

insert into t_user(usr_no,	usr_id, usr_pw, usr_name, usr_info)
values(seq_user.nextval, 'paraiso', '1004','희','초보 개발자');

insert into t_board(boa_no, boa_name, usr_no)
values(seq_board.nextval, '자유 게시판', 1);
insert into t_board(boa_no, boa_name, usr_no)
values(seq_board.nextval, '공지 사항', 1);
insert into t_board(boa_no, boa_name, usr_no)
values(seq_board.nextval, 'Q&A 게시판', 1);

update t_user set
		usr_pw = 'cc364f14fdaddcff740ad9992b02b3f78caaf7d77cc61d83005e67f148b34cebf8b6a6c8e8f1016de571162f94220092aa6435e24dea4a0e72666d6aaa8759b0';


commit

select * from t_comment;
select * from t_article;
select * from t_board;
select * from t_user;

