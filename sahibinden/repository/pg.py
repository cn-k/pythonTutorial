import psycopg2

def car_insert(car):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="password",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")

        cursor = connection.cursor()
        # Executing a SQL query to insert data into  table
        for c in car:
            print(c.id, "|", c.brand, "|", c.model, "|", c.package, "|", c.year, "|", c.km, "|", c.color, "|", c.price,
                  "|", c.href, "|", c.img)
            insert_query = f""" INSERT INTO sahibinden.cars (id, brand, model, package, year, km, color, price, href, img) VALUES ({c.id}, '{c.brand}', '{c.model}', '{c.package}', {c.year}, '{c.km}', '{c.color}', '{c.price}', '{c.href}', '{c.img}')"""
            cursor.execute(insert_query)
            connection.commit()
            print("1 Record inserted successfully")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")