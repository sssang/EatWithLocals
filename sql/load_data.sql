insert into Rest (restname, picurl, resttag,description, rating, address, city,state,country)
values ("Angelo's", "static/pictures/angelos.jpg", "Breakfast & Brunch","Family-run eatery serves diner-style breakfasts & light lunch, plus bread baked daily in-house.", "5", "1100 Catherine St, Ann Arbor, Mi 48104", "ann arbor","michigan","united stats");

insert into Rest (restname, picurl, resttag,description, rating, address,  city,state,country)
values ("Zingerman's", "static/pictures/zingerman.jpg", "Delis, Breakfast & Brunch","Zingerman's, or Zingerman's Community of Businesses, is a gourmet food business group headquartered in Ann Arbor, Michigan, USA. The original business and current flagship operation is Zingerman's Delicatessen. ", "4.5", "422 Detroit St, Ann Arbor, MI 48104", "ann arbor","michigan","united stats");

insert into Photo(picid,url)
values ("1","http://www.zingermansdeli.com/wp-content/uploads/2015/12/NoahsArchetypalReuben-e1449265674501.jpg");

insert into PhotoContain(restid,picid,caption,sequencenum)
values ("2","1","Reuben","1");

insert into Photo(picid,url)
values ("2","http://www.zingermansdeli.com/wp-content/uploads/2015/11/BLCplatter-e1449265717770.jpg");

insert into PhotoContain(restid,picid,caption,sequencenum)
values ("2","2","BLC","2");

insert into Photo(picid,url)
values ("3","http://www.zingermansdeli.com/wp-content/uploads/2010/05/zingermans-cornedbeef-sandwiches.jpg");

insert into PhotoContain(restid,picid,caption,sequencenum)
values ("2","3","corn-beef","3");


insert into Photo(picid,url)
values ("4","http://www.angelosa2.com/themes/angelos/img/photos/interior_05.jpg");

insert into PhotoContain(restid,picid,caption,sequencenum)
values ("1","4","burger","1");

insert into Photo(picid,url)
values ("5","http://www.angelosa2.com/themes/angelos/img/photos/food_05.jpg");

insert into PhotoContain(restid,picid,caption,sequencenum)
values ("1","5","sandwich","2");

insert into Photo(picid,url)
values ("6","http://www.angelosa2.com/themes/angelos/img/photos/food_14.jpg");

insert into PhotoContain(restid,picid,caption,sequencenum)
values ("1","6","breakfast","3");





insert into Review(rating, content,city,state,country)
values ("4","This restaurant is pretty good","ann arbor","michigan","united state");

insert into ReviewContain(restid,revid,sequencenum)
values ("2","1","1");

insert into Review(rating, content,city,state,country)
values ("1","This restaurant is too expensive","ann arbor","michigan","united state");

insert into ReviewContain(restid,revid,sequencenum)
values ("2","2","2");

insert into Review(rating, content,city,state,country)
values ("3","This restaurant is so so","ann arbor","michigan","united state");

insert into ReviewContain(restid,revid,sequencenum)
values ("2","3","3");



insert into Review(rating, content,city,state,country)
values ("5","There brunch is pretty good","ann arbor","michigan","united state");

insert into ReviewContain(restid,revid,sequencenum)
values ("1","4","1");

insert into Review(rating, content,city,state,country)
values ("1","This restaurant is too small","ann arbor","michigan","united state");

insert into ReviewContain(restid,revid,sequencenum)
values ("1","5","2");

insert into Review(rating, content,city,state,country)
values ("3","The service is horrible","ann arbor","michigan","united state");

insert into ReviewContain(restid,revid,sequencenum)
values ("1","6","3");