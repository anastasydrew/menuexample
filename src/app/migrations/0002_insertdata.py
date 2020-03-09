from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO app_treemenucategory (id, name, verbose_name) 
                VALUES (1, 'main_menu', 'Main menu');
            
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (1, 'Home', 'home', 1, null);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (2, 'Company', 'company', 1, null);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (3, 'Development', 'development', 1, null);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (4, 'Development C++', 'development_cpp', 1, 3);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (5, 'Development C++/Qt', 'development_cpp_qt', 1, 4);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (6, 'Development Python', 'development_python', 1, 3);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (7, 'Development Python/Django', 'development_python_django', 1, 6);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (8, 'Development Python/Tornado', 'development_python_tornado', 1, 6);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (9, 'Prices', 'prices', 1, null);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (10, 'GitHub', 'https://github.com/Gothness/', 1, 3);
        """)
    ]
