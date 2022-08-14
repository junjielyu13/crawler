import pdfplumber;
import psycopg2;


conn=psycopg2.connect(
    database="pdfcrawlerdb",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
    )
cur = conn.cursor()

with pdfplumber.open("./source/pdf/Notes-de-tall-via-PAU-CFGS.pdf") as pdf:
    cur.execute('''
        CREATE TABLE IF NOT EXISTS "majors_info"(
            "id"             SERIAL  PRIMARY KEY  NOT NULL,
            "id_major"       INTEGER NOT NULL,
            "name"           TEXT    NOT NULL,
            "poble"          TEXT    NOT NULL,
            "university"     TEXT    NOT NULL,
            "scores"         TEXT[]
        )
    ''')
    conn.commit() 

    for pageindex in range(len(pdf.pages)):

        page = pdf.pages[pageindex]
        table = page.extract_table()
        header = table[:3]
        body = table[3:]
        for rowindex in range(len(body)): 
            info = body[rowindex]

            print(info)

            name_major = info[1].replace("'","")
            pooble_name = info[2].replace("'","")

            cur.execute('''
                INSERT INTO "majors_info"(id_major, name, poble, university, scores) \
                VALUES (%d, %s, %s, %s, ARRAY[%s])
            '''
            %(int(info[0]), "'" + name_major + "'", "'"+pooble_name+"'", "'"+info[3]+"'", info[4:len(info)])
            )

            conn.commit()
    cur.close()


conn.close()