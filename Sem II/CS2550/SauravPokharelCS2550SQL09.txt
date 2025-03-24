-- Saurav Pokharel
-- CS2550
-- SQL Assignment 08
-- 04/29/2020

-- 01
SELECT Distinct 
    s.FIRSTNAME,
    s.LASTNAME,
    to_char(s.admissiondate, 'MON DD YYYY HH:MI AM') AS EnrollmentDate,
    s.StreetAddress,
    s.CITY AS City,
    s.STATE AS State,
    s.ZIP AS ZipCode,
    asrc.ASSIGNMENTNUMBER,
    at.DESCRIPTION
FROM 
    students s
INNER JOIN 
    REGISTRATION r ON s.studentid = r.STUDENTID
INNER JOIN 
    ASSIGNMENTSCORE asrc ON r.STUDENTID = asrc.STUDENTID
INNER JOIN 
    ASSIGNMENTCODE at ON asrc.ASSIGNMENTTYPEID = at.ASSIGNMENTTYPEID
WHERE 
    asrc.ASSIGNMENTNUMBER = '5'
    and at.description = 'Quiz' AND s.admissiondate = 
    (SELECT MAX(admissiondate) 
    FROM students s
    inner join registration r 
    on r.studentid = s.studentid
    inner join assignmentscore ascr 
    on r.sectionid = ascr.sectionid 
    and r.studentid = ascr.studentid
    where ASSIGNMENTNUMBER = '5'
    and assignmenttypeid = 'QZ') 
    
ORDER BY 
    s.LASTNAME, s.FIRSTNAME;


--02
select c.subjectdescription, c.subjectcode, c.coursenumber, s.capacity, c.coursetitle
from courses c
inner join sections s on s.courseid = c.courseid
where s.sectionstartdate = (select min(sectionstartdate) from sections)
order by c.subjectcode, c.coursenumber;

--03
SELECT
    SUM(s.CAPACITY) AS totalcapacity,
    c.SUBJECTCODE,
    c.COURSENUMBER,
    c.COURSETITLE
FROM
    COURSES c
JOIN
    SECTIONS s ON c.COURSEID = s.COURSEID
WHERE
    c.SUBJECTCODE = 'WEB'
GROUP BY
    c.SUBJECTCODE, c.COURSENUMBER, c.COURSETITLE
HAVING
    SUM(s.CAPACITY) > (
        SELECT AVG(s1.CAPACITY)
        FROM SECTIONS s1
        JOIN COURSES c1 ON s1.COURSEID = c1.COURSEID
        WHERE c1.SUBJECTCODE = 'WEB'
    )
ORDER BY
    totalcapacity DESC, c.SUBJECTCODE DESC, c.COURSENUMBER DESC;
	
--04
SELECT s.studentID, s.firstName, s.lastName, s.city, s.state, s.zip, COUNT(*) AS NUMCOURSES
FROM students s
INNER JOIN registration r ON s.studentID = r.studentID
INNER JOIN sections sec ON r.sectionID = sec.sectionID
INNER JOIN courses c ON sec.courseID = c.courseID
WHERE c.subjectCode = 'NET'
GROUP BY s.studentID, s.firstName, s.lastName, s.city, s.state, s.zip
HAVING COUNT(DISTINCT c.courseID) = (
    SELECT MAX(course_count)
    FROM (
        SELECT COUNT(DISTINCT c2.courseID) AS course_count
        FROM students s2
        INNER JOIN registration r2 ON s2.studentID = r2.studentID
        INNER JOIN sections sec2 ON r2.sectionID = sec2.sectionID
        INNER JOIN courses c2 ON sec2.courseID = c2.courseID
        WHERE c2.subjectCode = 'NET'
        GROUP BY s2.studentID
    ))
ORDER BY s.studentID;

--05
SELECT p.CITY, p.STATE, COUNT(*) AS numprofessors
FROM PROFESSORS p
JOIN SECTIONS sec ON p.PROFESSORID = sec.PROFESSORID
JOIN COURSES c ON sec.COURSEID = c.COURSEID
WHERE c.SUBJECTCODE = 'CS'
GROUP BY p.CITY, p.STATE
HAVING COUNT(*) = (
    SELECT MAX(professor_count)
    FROM (
        SELECT COUNT(*) AS professor_count
        FROM PROFESSORS p
        JOIN SECTIONS sec ON p.PROFESSORID = sec.PROFESSORID
        JOIN COURSES c ON sec.COURSEID = c.COURSEID
        WHERE c.SUBJECTCODE = 'CS'
        GROUP BY p.CITY, p.STATE
    )
)
ORDER BY p.CITY, p.STATE;

--06
SELECT DISTINCT s.firstname, s.lastname, s.city, s.state, s.zip, zs.NumStudents
FROM students s
INNER JOIN registration r ON s.studentid = r.studentid
INNER JOIN
    (SELECT zip, COUNT(*) AS NumStudents
     FROM
         (SELECT DISTINCT s.zip, r.studentid
          FROM registration r
          INNER JOIN students s ON r.studentid = s.studentid) StudentZip
     GROUP BY zip
     HAVING COUNT(*) =
         (SELECT MAX(NumStudents)
          FROM
              (SELECT zip, COUNT(*) AS NumStudents
               FROM
                   (SELECT DISTINCT s.zip, r.studentid
                    FROM registration r
                    INNER JOIN students s ON r.studentid = s.studentid) StudentZip
               GROUP BY zip) ZipCounts)) zs
ON s.zip = zs.zip
ORDER BY s.firstname, s.lastname;

--07
SELECT DISTINCT s.STUDENTID, s.FIRSTNAME, s.LASTNAME, s.STREETADDRESS, s.CITY, s.STATE, s.ZIP
FROM STUDENTS s
INNER JOIN REGISTRATION r 
ON s.STUDENTID = r.STUDENTID
INNER JOIN SECTIONS sec 
ON r.SECTIONID = sec.SECTIONID
INNER JOIN COURSES c 
ON sec.COURSEID = c.COURSEID
WHERE c.SUBJECTCODE = 'WEB'
AND s.STUDENTID NOT IN (
    SELECT DISTINCT r.STUDENTID
    FROM REGISTRATION r
    INNER JOIN SECTIONS sec ON r.SECTIONID = sec.SECTIONID
    INNER JOIN COURSES c ON sec.COURSEID = c.COURSEID
    WHERE c.SUBJECTCODE IN ('CS', 'NET')
)
ORDER BY s.LASTNAME, s.FIRSTNAME;

--08
SELECT s.FIRSTNAME, s.LASTNAME, COUNT(*) AS NUM_ASSIGNMENTS, 
       c.SUBJECTCODE, c.COURSENUMBER, c.COURSETITLE
FROM STUDENTS s
INNER JOIN ASSIGNMENTSCORE a ON s.STUDENTID = a.STUDENTID
INNER JOIN SECTIONS sec ON a.SECTIONID = sec.SECTIONID
INNER JOIN COURSES c ON sec.COURSEID = c.COURSEID
WHERE a.SCORE >= 90
GROUP BY s.STUDENTID, s.FIRSTNAME, s.LASTNAME, c.SUBJECTCODE, c.COURSENUMBER, c.COURSETITLE
HAVING COUNT(*) = (
    SELECT MAX(assign_count)
    FROM (
        SELECT COUNT(*) AS assign_count
        FROM ASSIGNMENTSCORE a2
        WHERE a2.SCORE >= 90
        GROUP BY a2.STUDENTID, a2.SECTIONID
    ) max_assignments_table
)
ORDER BY c.SUBJECTCODE, c.COURSENUMBER, s.LASTNAME, s.FIRSTNAME;

--09
SELECT sec.SECTIONID, sec.capacity, COUNT(*) AS ENROLLED, c.SUBJECTCODE, c.COURSENUMBER, c.COURSETITLE
FROM SECTIONS sec
INNER JOIN COURSES c ON sec.COURSEID = c.COURSEID
LEFT JOIN REGISTRATION r ON sec.SECTIONID = r.SECTIONID
GROUP BY sec.SECTIONID, c.SUBJECTCODE, c.COURSENUMBER, c.COURSETITLE, sec.CAPACITY
HAVING COUNT(r.STUDENTID) >= sec.CAPACITY
ORDER BY sec.CAPACITY DESC, c.SUBJECTCODE, c.COURSENUMBER;

--10
SELECT DISTINCT s.FIRSTNAME, s.LASTNAME, 
s.CITY, s.STATE, s.ZIP, s.PHONE
FROM STUDENTS s
INNER JOIN REGISTRATION r ON s.STUDENTID = r.STUDENTID
INNER JOIN SECTIONS sec ON r.SECTIONID = sec.SECTIONID
INNER JOIN COURSES c ON sec.COURSEID = c.COURSEID
WHERE c.SUBJECTCODE = 'CS'
AND s.STUDENTID IN (
    SELECT r.STUDENTID
    FROM REGISTRATION r
    INNER JOIN SECTIONS sec ON r.SECTIONID = sec.SECTIONID
    INNER JOIN COURSES c ON sec.COURSEID = c.COURSEID
    WHERE c.SUBJECTCODE IN ('CHNS', 'FRCH', 'GRMN', 'ITLN', 'JPNS', 'PTGS', 'SPAN')
)
ORDER BY s.STATE, s.CITY, s.LASTNAME, s.FIRSTNAME;
