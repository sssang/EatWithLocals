CREATE TABLE Rest
(
        restid INTEGER unsigned AUTO_INCREMENT NOT NULL,
        restname VARCHAR(50) DEFAULT NULL,
        picurl VARCHAR(255) NOT NULL,
        resttag VARCHAR(225) NOT NULL,
        rating double DEFAULT NULL,
        address varchar(225) not null,
        place varchar(225) not null,
        created TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
        lastupdated TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        PRIMARY KEY(restid)
);

CREATE TABLE Photo
(
        picid VARCHAR(40) NOT NULL,
        url VARCHAR(225) NOT NULL,
        format CHARACTER(3) NOT NULL,
        created TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY(picid)

);

create table Review
(
        revid integer unsigned auto_increment not null,
        rating double not null,
        content varchar(225) not null,
        created timestamp null default current_timestamp,
        lastupdated timestamp null default current_timestamp on update current_timestamp,
        primary key(revid)
);

CREATE TABLE PhotoContain
(
        restid INTEGER unsigned NOT NULL,
        picid VARCHAR(40) NOT NULL,
        caption VARCHAR(225) DEFAULT NULL,
        sequencenum INTEGER unsigned NOT NULL,
        CONSTRAINT pc_restid_frk FOREIGN KEY (restid) REFERENCES Rest(restid) ON DELETE CASCADE ON UPDATE CASCADE,
        CONSTRAINT pc_picid_frk FOREIGN KEY (picid) REFERENCES Photo(picid) ON DELETE CASCADE ON UPDATE CASCADE
);

create table ReviewContain
(
        restid integer unsigned not null,
        revid integer unsigned not null,
        sequencenum integer unsigned not null,
        constraint rc_restid_frk foreign key (restid) references Rest(restid) on delete cascade on update cascade,
        constraint rc_revid_frk foreign key (revid) references Review(revid) on delete cascade on update cascade
);