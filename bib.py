import sqlite3
conn = sqlite3.connect('surfaces.db')
c = conn.cursor()
c.execute('''CREATE TABLE bibliography (
kdim INT DEFAULT NULL,
pg   INT DEFAULT NULL, 
q    INT DEFAULT NULL,
K2   INT DEFAULT NULL,
chi  INT DEFAULT NULL,
e    INT DEFAULT NULL,
h11  INT DEFAULT NULL,
sp   INT,
ref  TEXT
);
''')


rationalsurfaces = [
(-1, 0, 0, None, 1, None, None, 4, "Rational surfaces"),
(-1, 0, 0, 9, 1, 3, 1, 7, '''The projective plane, birational to the Hirzebruch surface $\\Sigma_{0} = \\mathbb{P}^{1} \\times \mathbb{P}^{1}$.''')]
for n in range(2,60):
	h11 = n+1
	e = n+3
	chi = 1
	K2 = 12*chi - e
	rationalsurfaces.append((-1, 0, 0, K2, chi, e, h11, 7, "The Hirzebruch surface $\\Sigma_{" + str(n) + "}$."))

c.executemany("INSERT INTO bibliography VALUES (?,?,?,?,?,?,?,?,?)", rationalsurfaces)

c.close()
conn.commit()
