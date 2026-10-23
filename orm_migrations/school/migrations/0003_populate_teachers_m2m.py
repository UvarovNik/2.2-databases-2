from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_remove_student_teacher_student_teachers_and_more'),
    ]

    operations = [
        migrations.RunSQL(
            sql=[
                "INSERT INTO school_student_teachers (student_id, teacher_id) VALUES (1, 1)",
                "INSERT INTO school_student_teachers (student_id, teacher_id) VALUES (2, 3)",
                "INSERT INTO school_student_teachers (student_id, teacher_id) VALUES (3, 3)",
            ],
            reverse_sql=[
                "DELETE FROM school_student_teachers",
            ],
        ),
    ]
