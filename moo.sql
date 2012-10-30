drop table games cascade ;
create table games (
       id		serial primary key ,
       goal_code	char(4) not null ,
       last_move	char(4) ,
       move_count	smallint default 0
       ) ;
       
drop table users ;
create table users (
       phone_number	text primary key ,
       current_game	smallint references games (id) ,
       validation_code	smallint
       ) ;

drop table moves ;
create table moves (
       game		integer references games (id) ,
       move_count	smallint ,       
       move		char(4) ,
       bulls		smallint ,
       cows		smallint
       ) ;
       
