from Pro_Med_Graficos import *
import sqlite3

conn=sqlite3.connect('base_datos.db')
c=conn.cursor()


ciudades=["Puno","Juli","Azángaro","Lampa","Ayaviry","Juliaca","Macusani","Huancané","Yunguyo","Moho","Ilave","Sandia"]
estados=["Perú","Bolivia","Chile"]
medicos=["Marco Jhoel Ch Torres","Jose Jose"]
sexo=["Masculino","Femenino"]


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
	def __init__(self,*args,**kwargs):
		QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
		_translate=QtCore.QCoreApplication.translate
		self.setupUi(self)
		
		self.ini_consulta.pressed.connect(self.inic_consulta)
		self.Guardar.pressed.connect(self.guardar)
		self.boton_nuevo.pressed.connect(self.nuevo_expediente)
		self.eliminar.pressed.connect(self.eliminar_datos)
	
	
	def base_datos_recv():
		dato=c.execute("select Num_Expediente from Base_Expedientes")
		print(dato)
		
	
		
	def nuevo_expediente(self):
		self.num_expediente_1.setText("")
		self.titulo_1.setText("")
		self.nombres_1.setText("")
		self.nombres_2.setText("")
		self.apellidos_1.setText("")
		self.apellidos_2.setText("")
		self.domicilio_1.setText("")
		self.ciudad_1_box.clear()
		self.ciudad_1_box.addItem("")
		for valor in ciudades:
			print(valor)
			self.ciudad_1_box.addItem(valor)
		self.estado_1_box.clear()
		self.estado_1_box.addItem("")
		for valor in estados:
			self.estado_1_box.addItem(valor)
		self.cod_postal_1.setText("")
		self.medico_1_box.clear()
		self.medico_1_box.addItem("")
		for valor in medicos:
			self.medico_1_box.addItem(valor)
		self.sexo_1_box.clear()
		self.sexo_1_box.addItem("")
		for valor in sexo:
			self.sexo_1_box.addItem(valor)
		self.fech_nac_1.setText("")
		self.lug_nac_1.setText("")
		self.correo_1.setText("")
		self.num_seguro_1.setText("")
		self.edad_1.setText("")
		self.telf_dom_1.setText("")
		self.telf_ofi_1.setText("")
		self.observaciones_1.setText("")
		
	def eliminar_datos(self):
		num_expediente=self.num_expediente_1.text()
		c.execute("DELETE FROM Base_Expedientes WHERE Num_Expediente='{}'".format(num_expediente))
		conn.commit()
		print("Eliminado")
		self.num_expediente_1.setText("")
		self.titulo_1.setText("")
		self.nombres_1.setText("")
		self.nombres_2.setText("")
		self.apellidos_1.setText("")
		self.apellidos_2.setText("")
		self.domicilio_1.setText("")
		self.ciudad_1_box.clear()
		self.ciudad_1_box.addItem("")
		for valor in ciudades:
			print(valor)
			self.ciudad_1_box.addItem(valor)
		self.estado_1_box.clear()
		self.estado_1_box.addItem("")
		for valor in estados:
			self.estado_1_box.addItem(valor)
		self.cod_postal_1.setText("")
		self.medico_1_box.clear()
		self.medico_1_box.addItem("")
		for valor in medicos:
			self.medico_1_box.addItem(valor)
		self.sexo_1_box.clear()
		self.sexo_1_box.addItem("")
		for valor in sexo:
			self.sexo_1_box.addItem(valor)
		self.fech_nac_1.setText("")
		self.lug_nac_1.setText("")
		self.correo_1.setText("")
		self.num_seguro_1.setText("")
		self.edad_1.setText("")
		self.telf_dom_1.setText("")
		self.telf_ofi_1.setText("")
		self.observaciones_1.setText("")
		
	def actualizar(self):
		num_expediente=self.num_expediente_1.text()
		titulo=self.titulo_1.text()
		nombre1=self.nombres_1.text()
		nombre2=self.nombres_2.text()
		apellido1=self.apellidos_1.text()
		apellido2=self.apellidos_2.text()
		domicilio=self.domicilio_1.text()
		ciudad=self.ciudad_1_box.currentText()
		estado=self.estado_1_box.currentText()
		cod_postal=self.cod_postal_1.text()
		medico=self.medico_1_box.currentText()
		sexo=self.sexo_1_box.currentText()
		f_nacimiento=self.fech_nac_1.text()
		l_nacimiento=self.lug_nac_1.text()
		correo=self.correo_1.text()
		num_seguro=self.num_seguro_1.text()
		edad=self.edad_1.text()
		telf_dom=self.telf_dom_1.text()
		telf_ofi=self.telf_ofi_1.text()
		observaciones=self.observaciones_1.text()
	
		c.execute("UPDATE Base_Expedientes SET Num_Expediente='{}',Titulo='{}',Nombre_1='{}',Nombre_2='{}',Apellido_1='{}',Apellido_2='{}',Domicilio='{}',Ciudad='{}',Estado='{}',Cod_Postal='{}',Medico='{}',Sexo='{}',Fech_Nac='{}',Lug_Nac='{}',Correo='{}',Num_Seguro='{}',Edad='{}',Telf_Dom='{}',Telf_Oficina='{}',Observaciones='{}' WHERE Num_Expediente='{}'".format(num_expediente,titulo,nombre1,nombre2,apellido1,apellido2,domicilio,ciudad,estado,cod_postal,medico,sexo,f_nacimiento,l_nacimiento,correo,num_seguro,edad,telf_dom,telf_ofi,observaciones,num_expediente))
		conn.commit()
	
	def guardar(self):
		num_expediente=self.num_expediente_1.text()
		titulo=self.titulo_1.text()
		nombre1=self.nombres_1.text()
		nombre2=self.nombres_2.text()
		apellido1=self.apellidos_1.text()
		apellido2=self.apellidos_2.text()
		domicilio=self.domicilio_1.text()
		ciudad=self.ciudad_1_box.currentText()
		estado=self.estado_1_box.currentText()
		cod_postal=self.cod_postal_1.text()
		medico=self.medico_1_box.currentText()
		sexo=self.sexo_1_box.currentText()
		f_nacimiento=self.fech_nac_1.text()
		l_nacimiento=self.lug_nac_1.text()
		correo=self.correo_1.text()
		num_seguro=self.num_seguro_1.text()
		edad=self.edad_1.text()
		telf_dom=self.telf_dom_1.text()
		telf_ofi=self.telf_ofi_1.text()
		observaciones=self.observaciones_1.text()
		
		#c.execute("DELETE FROM Base_Expedientes Where Num_Expediente=?",(num_expediente))
		
		#c.execute("INSERT INTO Base_Expedientes VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(num_expediente,titulo,nombre1,nombre2,apellido1,apellido2,domicilio,ciudad,estado,cod_postal,medico,sexo,f_nacimiento,l_nacimiento,correo,num_seguro,edad,telf_dom,telf_ofi,observaciones))
		#conn.commit()
			
		#c.execute("UPDATE Base_Expedientes SET Num_Expediente='{}',Titulo='{}',Nombre_1='{}',Nombre_2='{}',Apellido_1='{}',Apellido_2='{}',Domicilio='{}',Ciudad='{}',Estado='{}',Cod_Postal='{}',Medico='{}',Sexo='{}',Fech_Nac='{}',Lug_Nac='{}',Correo='{}',Num_Seguro='{}',Edad='{}',Telf_Dom='{}',Telf_Oficina='{}',Observaciones='{}' WHERE Num_Expediente='{}'".format(num_expediente,titulo,nombre1,nombre2,apellido1,apellido2,domicilio,ciudad,estado,cod_postal,medico,sexo,f_nacimiento,l_nacimiento,correo,num_seguro,edad,telf_dom,telf_ofi,observaciones,num_expediente))
		#conn.commit()
		c.execute("INSERT INTO Base_Expedientes VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(num_expediente,titulo,nombre1,nombre2,apellido1,apellido2,domicilio,ciudad,estado,cod_postal,medico,sexo,f_nacimiento,l_nacimiento,correo,num_seguro,edad,telf_dom,telf_ofi,observaciones))
		conn.commit()
		#c.close()
		#conn.close()
		

		
		
	def inic_consulta(self):
		expediente=self.num_expediente_1.text()
		ciudad=self.ciudad_1_box.currentText()
		print(ciudad)
		codigo="EXP-3487"
		dato_2=c.execute("select Num_Expediente,Titulo,Nombre_1,Nombre_2,Apellido_1,Apellido_2,Domicilio,Ciudad,Estado,Cod_Postal,Medico,Sexo,Fech_Nac,Lug_Nac,Correo,Num_Seguro,Edad,Telf_Dom,Telf_Oficina,Observaciones from Base_Expedientes where Num_Expediente=?",(expediente, ))
		fila=c.fetchone()
		if fila!=None:
			print(fila)
			self.num_expediente_1.setText(fila[0])
			self.titulo_1.setText(fila[1])
			self.nombres_1.setText(fila[2])
			self.nombres_2.setText(fila[3])
			self.apellidos_1.setText(fila[4])
			self.apellidos_2.setText(fila[5])
			self.domicilio_1.setText(fila[6])
			self.ciudad_1_box.clear()
			self.ciudad_1_box.addItem(fila[7])
			for valor in ciudades:
				print(valor)
				self.ciudad_1_box.addItem(valor)
			self.estado_1_box.clear()
			self.estado_1_box.addItem(fila[8])
			for valor in estados:
				self.estado_1_box.addItem(valor)
			self.cod_postal_1.setText(fila[9])
			self.medico_1_box.clear()
			self.medico_1_box.addItem(fila[10])
			for valor in medicos:
				self.medico_1_box.addItem(valor)
			self.sexo_1_box.clear()
			self.sexo_1_box.addItem(fila[11])
			for valor in sexo:
				self.sexo_1_box.addItem(valor)
			self.fech_nac_1.setText(fila[12])
			self.lug_nac_1.setText(fila[13])
			self.correo_1.setText(fila[14])
			self.num_seguro_1.setText(fila[15])
			self.edad_1.setText(fila[16])
			self.telf_dom_1.setText(fila[17])
			self.telf_ofi_1.setText(fila[18])
			self.observaciones_1.setText(fila[19])
		else:
			print("No existe")

	
	
	def eliminar(self):
		print("asd")
	
	def historia_clinica_pdf(self):
		print("asfdsad")
	
	
	
		
		
		
if __name__=="__main__":
	#crear_tabla
	app=QtWidgets.QApplication([])
	window=MainWindow()
	window.show()
	app.exec_()