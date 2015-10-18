import sqlite3

def makePost(title, body, ID, points, date, uname):
    conn = sqlite3.connect("backend")
    c = conn.cursor()
    T = title
    B = body
    I = ID
    P = points
    D = date
    U = uname
    params = (T, B, I, P, D, U)
    c.execute("INSERT INTO users VALUES(?,?,?,?,?,?)", params)
    conn.commit()

def retrievePost():
    conn = sqlite3.connect("backend")
    c = conn.cursor()
    c.execute('SELECT * FROM posts')
    posts = c.fetchall()
    return posts
