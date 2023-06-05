import sqlite3

conn=sqlite3.connect('base_datos.db')
c=conn.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS Base_Expedientes(Num_Expediente TEXT,Titulo TEXT,Nombre_1 TEXT,Nombre_2 TEXT,Apellido_1 TEXT,Apellido_2 TEXT,Domicilio TEXT,Ciudad TEXT,Estado TEXT,Cod_Postal TEXT,Medico TEXT,Sexo TEXT,Fech_Nac TEXT,Lug_Nac TEXT,Correo TEXT,Num_Seguro TEXT,Edad TEXT,Telf_Dom TEXT,Telf_Oficina TEXT,Observaciones TEXT)")
	#conn.commit()
	
	#c.close()
	#conn.close()
	
def data_entry():
	c.execute("INSERT INTO Base_Expedientes VALUES('EXP-3487','','Marco','Jhoel','Churata','Torres','Jr.Sucre 1450','Juliaca','Peru','20103','Alex Miguel','Masculion','12/12/22','Juliaca','marco@gmai.com','456657','22','926536242','329973','Programando_ando')")
	conn.commit()
	
	c.close()
	conn.close()

	
create_table()
data_entry()