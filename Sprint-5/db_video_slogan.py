import sqlite3
con = sqlite3.connect('db_video_type_slogan.sqlite')
cur = con.cursor()
results = cur.execute('''
    SELECT video_products.title,
       slogans.slogan_text,
       product_types.title
    FROM video_products
    JOIN slogans ON video_products.slogan_id = slogans.id
    JOIN product_types ON video_products.type_id = product_types.id; 
''')
for result in results:
    print(result)

con.close() 