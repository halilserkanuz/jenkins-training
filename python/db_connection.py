import psycopg2
import psycopg2.extras


cnx = psycopg2.connect(
            host="localhost",
            database="buytogether",
            user="postgres",
            password="37291944"
        )

with cnx.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
    
    cur.execute("SELECT * FROM _prisma_migrations")
    rows = cur.fetchall()

print(rows)