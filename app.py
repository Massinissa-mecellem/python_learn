import psycopg2


def Create_table():

    conn = psycopg2.connect(
        host="localhost",
        dbname= "students",
        user= "postgres",
        password = "azerty",
        port = 5432
            )
    print(conn)
    print('connextion réussie!')
    cur= conn.cursor()
    cur.execute("CREATE TABLE students(student_id SERIAL PRIMARY KEY, name TEXT, adress TEXT, age INT, number TEXT);")

    print('students table created')
    conn.commit()
    conn.close()

def insert_data():
    name = input('enter name: ')
    address = input('enter address: ')
    age = input('enter age: ')
    number = input('enter number: ')
    conn = psycopg2.connect(
            host="localhost",
            dbname= "students",
            user= "postgres",
            password = "*********",
            port = 5432
                )
    print(conn)
    print('connextion réussie!')
    cur= conn.cursor()
    cur.execute("INSERT INTO students(name, adress, age, number) VALUES(%s, %s, %s, %s)",(name, address, age, number))
    print('INSERT 01')
    conn.commit()
    conn.close()



def update_data():
    
    conn = psycopg2.connect(
        host="localhost",
        dbname= "students",
        user= "postgres",
        password = "azerty",
        port = 5432
    )
    print(conn)
    print('connextion réussie!')
    cur= conn.cursor()

    student_id = input('enter user to be update: ')
    fields = {
        "1":("name", "Enter your name: "),
        "2":("adress", "Enter your addres: "),
        "3":("age", "Enter your age: "),
        "4":("number", "Enter your number: ")
    }
    print('Which field you like to be update ?')
    for key in fields:
        print(f"{key}:{fields[key][0]}")

    choise_user = input("enter your choise: ")
    if choise_user in fields:
        field_name, prompt = fields[choise_user]
        new_variable = input(prompt)
        sql = f"UPDATE students SET {field_name}=%s WHERE student_id= %s"
        cur.execute(sql, (new_variable, student_id))
        print('UPDATE 01')
    else:
        print('This is invalid choise')

    conn.commit()
    conn.close()

update_data()







