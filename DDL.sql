CREATE TABLE students(
    student_id          serial,
    first_name          text    not null,
    last_name           text    not null,
    email               text    not null    unique,
    enrollment_date     date,
    primary key(student_id)
);
