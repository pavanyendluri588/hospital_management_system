select student.student_id,
student.stu_fname,
student.stu_lname,
technologies.tech_id,
technologies.inst_name,
technologies.technology

from student
cross join technologies
on student.student_id=technologies.tech_id;