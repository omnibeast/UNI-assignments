select firstname, lastname, sectionID, subjectcode, coursenumber
From professor p
inner join section s
on p.professorID = s.professorID
inner join courses c
on c.courseID = s.courseID
where state = 'NV'
and subjectcode = 'WEB'
order by subjectcode, coursenumber, sectionid;