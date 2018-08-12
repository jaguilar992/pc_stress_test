import sys
from ui import *
import cpu
from barra_progreso_hilo import BarraProgresoHilo
procesador = cpu.Procesador()
app = QtWidgets.QApplication(sys.argv)
ventana = QtWidgets.QMainWindow()

def apagar_todo():
  procesador.apaga_todos()
  refresh_listas()
def encender_todo():
  procesador.enciende_todos()
  refresh_listas()

def apagar_nucleo():
  item = ui.listaEncendidos.currentItem()
  if item!=None:
    numero_nucleo = int(item.text()[3:])
    procesador.apaga_nucleo(numero_nucleo)
    refresh_listas()

def encender_nucleo():
  item = ui.listaApagados.currentItem()
  if item!=None:
    numero_nucleo = int(item.text()[3:])
    procesador.enciende_nucleo(numero_nucleo)
    refresh_listas()

def refresh_listas():
  encendidos = procesador.get_lista_encendidos()
  apagados = procesador.get_lista_apagados()
  ui.listaEncendidos.clear()
  ui.listaEncendidos.addItems(encendidos)
  ui.listaApagados.clear()
  ui.listaApagados.addItems(apagados)
  

ui = Ui_MainWindow() # importado desde el modulo ui
ui.setupUi(ventana)
refresh_listas()

# Manejo de eventos
ui.btnApagarTodo.clicked.connect(apagar_todo)
ui.btnReiniciar.clicked.connect(encender_todo)
ui.btnApagar.clicked.connect(apagar_nucleo)
ui.btnEncender.clicked.connect(encender_nucleo)

ui.cpu0bar.setValue(procesador.get_porcentaje_n(0))
ui.cpu1bar.setValue(procesador.get_porcentaje_n(1))
ui.cpu2bar.setValue(procesador.get_porcentaje_n(2))
ui.cpu3bar.setValue(procesador.get_porcentaje_n(3))

progreso0 = BarraProgresoHilo(ui.cpu0bar, procesador, 0)
progreso1 = BarraProgresoHilo(ui.cpu1bar, procesador, 1)
progreso2 = BarraProgresoHilo(ui.cpu2bar, procesador, 2)
progreso3 = BarraProgresoHilo(ui.cpu3bar, procesador, 3)

progreso0.start()
progreso1.start()
progreso2.start()
progreso3.start()

ventana.show()
sys.exit(app.exec_())
