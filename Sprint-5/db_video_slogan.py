import sqlite3
con = sqlite3.connect('db_video_type_slogan.sqlite')
cur = con.cursor()
results = cur.execute('''
    SELECT video_products.title,
       slogans.slogan_text
    FROM video_products
    LEFT JOIN slogans ON video_products.slogan_id = slogans.id
    UNION
    SELECT video_products.title,
        slogans.slogan_text
    FROM slogans
    LEFT JOIN video_products ON video_products.slogan_id = slogans.id; 
''')
for result in results:
    print(result)

print('==='*10)

results = cur.execute('''
    SELECT video_products.title,
       slogans.slogan_text
    FROM video_products
    CROSS JOIN slogans; 
''')
for result in results:
    print(result)
con.close() 