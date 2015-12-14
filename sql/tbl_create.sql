CREATE TABLE Rest
(
        restid INTEGER unsigned AUTO_INCREMENT NOT NULL,
        price INTEGER unsigned NOT NULL,
        restname VARCHAR(50) DEFAULT NULL,
        picurl VARCHAR(255) NOT NULL,
        resttag VARCHAR(225) NOT NULL,
        description VARCHAR(225) DEFAULT NULL,
        rating double DEFAULT 0,
        address varchar(225) not null,
        city varchar(225) not null,
        state varchar(255) not null,
        country varchar(255) not null,
        url VARCHAR(225) NOT NULL,
        created TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
        lastupdated TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        PRIMARY KEY(restid)
);

CREATE TABLE Photo
(
        picid integer unsigned AUTO_INCREMENT NOT NULL,
        url VARCHAR(225) NOT NULL,
        created TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY(picid)

);

create table Review
(
        revid integer unsigned auto_increment not null,
        rating double not null,
        content varchar(225) not null,
        city varchar(255) null,
        state varchar(255) null,
        country varchar(255) null,
        created timestamp null default current_timestamp,
        lastupdated timestamp null default current_timestamp on update current_timestamp,
        primary key(revid)
);

create table Menu
(
        menuid integer unsigned auto_increment not null,
        restid integer unsigned not null,
        revid integer unsigned  not null,
        constraint m_restid_frk foreign key (restid) references Rest (restid) on delete cascade on update cascade,
        constraint m_revid_frk foreign key (revid) references Review (revid) on delete cascade on update cascade,
        primary key (menuid)
);

create table Course
(
        courseid integer unsigned auto_increment not null,
        menuid integer unsigned not null,
        course_name varchar(255) not null,
        course_content varchar(255) not null,
        primary key(courseid),
        constraint c_menuid_frk foreign key (menuid) references Menu (menuid) on delete cascade on update cascade
);

CREATE TABLE PhotoContain
(
        restid INTEGER unsigned NOT NULL,
        picid integer unsigned NOT NULL,
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

create table CountryRating
(
        restid integer unsigned not null,
        rating double DEFAULT 0,
        country varchar(255) not null,
        constraint cr_restid_frk foreign key (restid) references Rest(restid)
);

create table RestGeo
(
        restid integer unsigned not null,
        latitude double not null,
        longitude double not null,
        constraint rg_restid_frk foreign key (restid) references Rest(restid)
);

