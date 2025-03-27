/* select distinct s.studentid, s.city, NVL(t1.NumStudentspercity,0) as NumStudentspercity
from students s
left outer join
    (select city, COUNT(*) as NumStudentspercity
    from
        (select distinct r.studentid, city
        from registration r 
        inner join students s on s.studentid = r.studentid)
        group by city) t1 
    on t1.city =  s.city
    where state = 'ID'; 
    
    select firstname, lastname, 'students' as TableName
    from students 
    where state = 'ID'
    union 
    select firstname, lastname, 'Professors'
    from professors
    where state = 'ID'
    order by lastname, firstname; 

    -- 01
SELECT 
    b.BUILDING,    
    b.BUILDINGNAME, 
    r.ROOM, 
    COUNT(*) AS NUM_SECTIONS
FROM SECTIONS sec
INNER JOIN LOCATIONS r ON sec.LOCATIONID = r.LOCATIONID
INNER JOIN BUILDINGS b ON r.BUILDING = b.BUILDING
INNER JOIN COURSES c ON sec.COURSEID = c.COURSEID
WHERE c.SUBJECTCODE = 'WEB' 
    AND b.BUILDINGNAME != 'Online Class'
GROUP BY b.BUILDING, b.BUILDINGNAME, r.ROOM
HAVING COUNT(*) = (SELECT MAX(COUNT(*)) 
                                     FROM SECTIONS sec
                                     INNER JOIN LOCATIONS r ON sec.LOCATIONID = r.LOCATIONID
                                     INNER JOIN BUILDINGS b ON r.BUILDING = b.BUILDING
                                     INNER JOIN COURSES c ON sec.COURSEID = c.COURSEID
                                     WHERE c.SUBJECTCODE = 'WEB' 
                                         AND b.BUILDINGNAME != 'Online Class'
                                     GROUP BY b.BUILDING, b.BUILDINGNAME, r.ROOM)
ORDER BY b.BUILDINGNAME, b.BUILDING, r.ROOM;

SELECT distinct p.professorID, 
       p.firstName, 
       p.lastName
FROM professors p
INNER JOIN sections s ON p.professorID = s.professorID
INNER JOIN courses c ON s.courseID = c.courseID
WHERE c.subjectCode = 'CS'
AND s.locationID NOT IN (SELECT  building FROM locations WHERE Building = 'OL')
ORDER BY p.lastName, p.firstName;