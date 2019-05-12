create table department(dno int primary key,dname TEXT);
CREATE table student( sid int PRIMARY KEY, fname TEXT, lname TEXT, bdate date, dno INT, FOREIGN KEY(dno) REFERENCES department(dno)); 
CREATE table teachers(tid int PRIMARY KEY, fname TEXT, lname TEXT);
CREATE TABLE pre(pid int PRIMARY KEY, pname TEXT);
CREATE TABLE courses (cno int PRIMARY KEY, cname text, chours int, dno int, pid int, FOREIGN KEY (dno) REFERENCES department (dno), FOREIGN KEY(pid) REFERENCES pre(pid));
CREATE TABLE section(sno int PRIMARY KEY, year int(4), cno int, tid int, FOREIGN KEY (cno) REFERENCES courses (cno), FOREIGN KEY (tid) REFERENCES teachers (tid));
CREATE TABLE teaches (sid int, tid int, FOREIGN KEY(sid) REFERENCES student(sid), FOREIGN KEY(tid) REFERENCES teachers(tid));
CREATE TABLE belongto(dno int, tid int, FOREIGN KEY (dno) REFERENCES department (dno), FOREIGN KEY (tid) REFERENCES teachers (tid));
CREATE TABLE attend( grade double, sid int, sno int, FOREIGN KEY (sid) REFERENCES student (sid), FOREIGN KEY (sno) REFERENCES section (sno), check(grade<=100 AND grade>=0), check('SELECT count(*)<=6 from attend where sid=sid'));
