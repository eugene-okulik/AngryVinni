import mysql.connector

try:
    conn = mysql.connector.connect(
        user='st-onl',
        password='AVNS_tegPDkI5BlB2lW5eASC',
        host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
        port=25060,
        database='st-onl'
    )
    cursor = conn.cursor()

    if conn.is_connected():
        print("Connection to DB is established")
    else:
        raise Exception("Failed to connect to DB")

    # Insert group
    cursor.execute("""
        INSERT INTO `groups` (title, start_date, end_date)
        VALUES (%s, %s, %s)
    """, ('Traktorists', '2025-09-01', '2026-06-30'))
    group_id = cursor.lastrowid

    # Insert student
    cursor.execute("""
        INSERT INTO students (name, second_name, group_id)
        VALUES (%s, %s, %s)
    """, ('Ernest', 'Subhatilov', group_id))
    student_id = cursor.lastrowid

    # Insert books
    book_titles = ['Algorithms', 'Database Systems', 'Operating Systems']
    book_data = [(title, student_id) for title in book_titles]
    cursor.executemany("""
        INSERT INTO books (title, taken_by_student_id)
        VALUES (%s, %s)
    """, book_data)

    # Insert subjets
    subjet_titles = ['Mathematics', 'Computer Science']
    subjet_ids = []
    for title in subjet_titles:
        cursor.execute("INSERT INTO subjets (title) VALUES (%s)", (title,))
        subjet_ids.append(cursor.lastrowid)

    # Insert lessons
    lesson_titles = {
        subjet_ids[0]: ['Linear Algebra', 'Calculus'],
        subjet_ids[1]: ['Programming', 'Networking']
    }
    lesson_ids = []
    for subj_id, lessons in lesson_titles.items():
        for title in lessons:
            cursor.execute("""
                INSERT INTO lessons (title, subject_id)
                VALUES (%s, %s)
            """, (title, subj_id))
            lesson_ids.append(cursor.lastrowid)

    # Insert marks
    mark_values = [5, 4, 5, 3]
    marks_data = [(value, lesson_id, student_id)
                  for lesson_id, value in zip(lesson_ids, mark_values)]
    cursor.executemany("""
        INSERT INTO marks (value, lesson_id, student_id)
        VALUES (%s, %s, %s)
    """, marks_data)

    conn.commit()

    # Get data
    print("\nStudent's marks:")
    cursor.execute(
        "SELECT value FROM marks WHERE student_id = %s",
        (student_id,)
    )
    for row in cursor.fetchall():
        print(row)

    print("\nBooks taken by the student:")
    cursor.execute("SELECT title FROM books WHERE taken_by_student_id = %s",
                   (student_id,))
    for row in cursor.fetchall():
        print(row)

    print("\nFull student info:")
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
        LEFT JOIN subjets subj ON l.subject_id = subj.id
        WHERE s.id = %s
    """, (student_id,))
    for row in cursor.fetchall():
        print(row)

finally:
    # Safe cleanup
    try:
        cursor.close()
        print("\nCursor closed.")
    except Exception as e:
        print("Cursor close failed:", e)

    try:
        conn.close()
        print("Connection closed.")
    except Exception as e:
        print("Connection close failed:", e)
