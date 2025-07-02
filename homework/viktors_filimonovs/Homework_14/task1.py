import mysql.connector

# Connect to the DB
conn = mysql.connector.connect(
    user='st-onl',
    password='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)
cursor = conn.cursor()


# Print connection status
if conn.is_connected():
    print("Connection to DB is estabilished!")
else:
    print("Not connected to DB")


# Print all tables
cursor.execute("SHOW TABLES")
for table in cursor.fetchall():
    print(table)


# Function check for occupied ID
def get_next_id(table):
    cursor.execute(f"SELECT MAX(id) FROM `{table}`")
    max_id = cursor.fetchone()[0]
    return (max_id or 0) + 1


# Group creation
group_id = get_next_id("groups")
cursor.execute("""
    INSERT INTO `groups` (id, title, start_date, end_date)
    VALUES (%s, %s, %s, %s)
""", (group_id, 'Traktorists', '2025-09-01', '2026-06-30'))

# Create student
student_id = get_next_id("students")
cursor.execute("""
    INSERT INTO students (id, name, second_name, group_id)
    VALUES (%s, %s, %s, %s)
""", (student_id, 'Ernest', 'Subhatilov', group_id))

# create book
book_titles = ['Algorithms', 'Database Systems', 'Operating Systems']
for title in book_titles:
    book_id = get_next_id("books")
    cursor.execute("""
        INSERT INTO books (id, title, taken_by_student_id)
        VALUES (%s, %s, %s)
    """, (book_id, title, student_id))

# create subject
subject_titles = ['Mathematics', 'Computer Science']
subject_ids = []
for title in subject_titles:
    subject_id = get_next_id("subjects")
    subject_ids.append(subject_id)
    cursor.execute("""
        INSERT INTO subjects (id, title)
        VALUES (%s, %s)
    """, (subject_id, title))

# Create lesson
lesson_titles = {
    subject_ids[0]: ['Linear Algebra', 'Calculus'],
    subject_ids[1]: ['Programming', 'Networking']
}
lesson_ids = []
for subj_id, titles in lesson_titles.items():
    for lesson_title in titles:
        lesson_id = get_next_id("lessons")
        lesson_ids.append(lesson_id)
        cursor.execute("""
            INSERT INTO lessons (id, title, subject_id)
            VALUES (%s, %s, %s)
        """, (lesson_id, lesson_title, subj_id))

# Create marks
mark_values = [5, 4, 5, 3]
for lesson_id, mark in zip(lesson_ids, mark_values):
    mark_id = get_next_id("marks")
    cursor.execute("""
        INSERT INTO marks (id, value, lesson_id, student_id)
        VALUES (%s, %s, %s, %s)
    """, (mark_id, mark, lesson_id, student_id))

conn.commit()


# Get data
print("\nStudent's marks:")
cursor.execute("SELECT value FROM marks WHERE student_id = %s", (student_id,))
for row in cursor.fetchall():
    print(row)

print("\nBooks taken by the student: ")
cursor.execute(
    "SELECT title FROM books WHERE taken_by_student_id = %s",
    (student_id,)
)
for row in cursor.fetchall():
    print(row)

print("\nFull student info: ")
cursor.execute("""
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
    LEFT JOIN subjects subj ON l.subject_id = subj.id
    WHERE s.id = %s
""", (student_id,))
for row in cursor.fetchall():
    print(row)

# Disconnect
cursor.close()
