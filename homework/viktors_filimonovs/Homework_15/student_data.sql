-- Create student
INSERT INTO students (name, second_name, group_id)
VALUES ('Valerij', 'Leontjev', NULL);

-- Create books
INSERT INTO books (title, taken_by_student_id)
VALUES 
('Docker', LAST_INSERT_ID()),
('Clean Code', LAST_INSERT_ID()),
('Python Tricks', LAST_INSERT_ID());

-- create group
INSERT INTO `groups` (title, start_date, end_date)
VALUES ('Dev Ninjas', '2025-09-01', '2026-06-30');

-- connect group to student
-- save into variable last added student
SET @student_id := (SELECT MAX(id) FROM students);
-- save into variable last added group
SET @group_id := (SELECT id FROM `groups` ORDER BY id DESC LIMIT 1);
-- update record in table students, create connection between student and group
UPDATE students SET group_id = @group_id WHERE id = @student_id;

-- create lesson
INSERT INTO subjets (title)
VALUES ('Databases'), ('Software Testing');

-- create lessons
INSERT INTO lessons (title, subject_id)
VALUES
('SQL Basics', (SELECT id FROM subjets WHERE title = 'Databases')),
('Index Optimization', (SELECT id FROM subjets WHERE title = 'Databases'));

-- create lessons
INSERT INTO lessons (title, subject_id)
VALUES
('Unit Testing', (SELECT id FROM subjets WHERE title = 'Software Testing')),
('Bug Hunting', (SELECT id FROM subjets WHERE title = 'Software Testing'));

-- marks
INSERT INTO marks (value, lesson_id, student_id)
VALUES
(4, (SELECT id FROM lessons WHERE title = 'SQL Basics'), (SELECT MAX(id) FROM students)),
(5, (SELECT id FROM lessons WHERE title = 'Index Optimization'), (SELECT MAX(id) FROM students)),
(5, (SELECT id FROM lessons WHERE title = 'Unit Testing'), (SELECT MAX(id) FROM students)),
(3, (SELECT id FROM lessons WHERE title = 'Bug Hunting'), (SELECT MAX(id) FROM students));


-- students marks
SELECT value
FROM marks
WHERE student_id = (SELECT MAX(id) FROM students);

-- books own by student
SELECT title
FROM books
WHERE taken_by_student_id = (SELECT MAX(id) FROM students);

-- all info about student
SELECT
    s.name AS student_name,
    s.second_name AS student_surname,
    g.title AS group_title,
    b.title AS book_title,
    subj.title AS subject_title,
    l.title AS lesson_title,
    m.value AS mark_value
FROM students s
JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjets subj ON l.subject_id = subj.id
WHERE s.id = (SELECT MAX(id) FROM students);
