# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
import design
import formulas
from math import prod, sin


class App(QtWidgets.QMainWindow, design.Ui_CCalculator_0_1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.answer_btn.clicked.connect(self.not_null_in_line)
        self.answer_btn.clicked.connect(self.calculate)
        self.method_box.currentTextChanged.connect(self.set_value)
        self.submethod_box.currentIndexChanged.connect(self.values_in_line_and_label)
        self.submethod_box.currentIndexChanged.connect(self.set_formula_lite)   
        
        
    def not_null_in_line(self):
        a_null = self.a_line.text()
        b_null = self.b_line.text()
        c_null = self.c_line.text()
        e_null = self.e_line.text()
        d_null = self.d_line.text()
        if a_null == "":
            self.a_line.setText("0")
        if b_null == "":
            self.b_line.setText("0")
        if c_null == "":
            self.c_line.setText("0")
        if d_null == "":
            self.d_line.setText("0")
        if e_null == "":
            self.e_line.setText("0") 
            
        if self.a_label.isEnabled() == False:
            self.a_line.setText("")            
        if self.b_label.isEnabled() == False:
            self.b_line.setText("")        
        if self.c_label.isEnabled() == False:
            self.c_line.setText("")            
        if self.d_label.isEnabled() == False:
            self.d_line.setText("")            
        if self.e_label.isEnabled() == False:
            self.e_line.setText("")
    def set_value(self):
        value = self.method_box.currentText()
        self.value_label_2.setText(f"{value}")
        self.set_formula()
        self.num_set()
        
    def set_formula_lite(self):
        formula = self.submethod_box.currentText()
        self.formula_label_2.setText(f"{formula}") 
        value = self.method_box.currentText()
        self.values_in_line_and_label()
        self.num_set()
        
    def set_formula(self):
        formula = self.submethod_box.currentText()
        self.formula_label_2.setText(f"{formula}") 
        value = self.method_box.currentText()
        
        if value == " ????????????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.velocity)

        if value == " ????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.path)

        if value == " ??????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.time)

        if value == " ??????????????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.density)

        if value == " ??????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.mass)

        if value == " ??????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.volume)

        if value == " ????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.force)

        if value == " ??????????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.square)           

        if value == " ??????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.lenght)           

        if value == " ????????????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.pressure)           
            
        if value == " ????????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.work)
            
        if value == " ????????????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.power)
            
        if value == " ???????????? ????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.force_moment)
            
        if value == " ??????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.efficiency)
            
        if value == " ??????????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.energy)
            
        if value == " ??????????????????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.temperature)
            
        if value == " ???????????????????? ??????????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.heat)
            
        if value == " ????????????????\n ????????????????????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.specific_heat)
        
        if value == " ???????????????? ??????????????\n ????????????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.specific_heat_of_combustion)
        
        if value == " ???????????????? ??????????????\n ??????????????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.specific_heat_of_fusion)
            
        if value == " ?????????????????? ??????????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.air_humidity)
            
        if value == " ???????????????? ??????????????\n ??????????????????????????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.specific_heat_of_vaporization)
            
        if value == " ?????????????????????????? ??????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.electric_charge)
                
        if value == " ???????? ????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.amperage)
            formula = self.submethod_box.currentText()
            self.formula_label_2.setText(f"{formula}")
            
        if value == " ????????????????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.voltage)
	
        if value == " ??????????????????????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.resistance)
            
        if value == " ????????????????\n ??????????????????????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.resistivity)
            
        if value == " ???????????????? ????. ????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.electric_current_power)
        
        if value == " ????????????????????????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.electric_capacity)
                
        if value == " ?????????????? ????. ????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.energy_electric_field)
        
        if value == " ????????????????????\n ??????????????????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.relative_refractive_index)
    
        if value == " ???????? ????????????????????\n ??????????":
            self.submethod_box.clear()
            self.submethod_box.addItems(formulas.optical_lens_power)
        
        formula = self.submethod_box.currentText()
        self.formula_label_2.setText(f"{formula}")        
	    
        self.values_in_line_and_label()
            
            
    def values_in_line_and_label(self):
        formula = self.submethod_box.currentText()
        if formula == "v = S/t":
            self.a_label.setText('???????????????? S')
            self.b_label.setText('???????????????? t')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "S = vt":
            self.a_label.setText('???????????????? v')
            self.b_label.setText('???????????????? t')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "t = S/v":
            self.a_label.setText('???????????????? S')
            self.b_label.setText('???????????????? v')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "?? = m/V":
            self.a_label.setText('???????????????? m')
            self.b_label.setText('???????????????? V')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "m = ??V":
            self.a_label.setText('???????????????? ??')
            self.b_label.setText('???????????????? V')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "V = m/??":
            self.a_label.setText('???????????????? m')
            self.b_label.setText('???????????????? ??')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "F?????? = k??l":
            self.a_label.setText('???????????????? k')
            self.b_label.setText('???????????????? ??l')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "F?????? = mg":
            self.a_label.setText('???????????????? m')
            self.b_label.setText('')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "p = F/S":
            self.a_label.setText('???????????????? F')
            self.b_label.setText('???????????????? S')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "p = g??h":
            self.a_label.setText('???????????????? ??')
            self.b_label.setText('???????????????? h')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "m = ??Sh":
            self.a_label.setText('???????????????? ??')
            self.b_label.setText('???????????????? S')
            self.c_label.setText('???????????????? h')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "p = g??Sh":
            self.a_label.setText('???????????????? ??')
            self.b_label.setText('???????????????? S')
            self.c_label.setText('???????????????? h')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "F?? = g????V??":
            self.a_label.setText('???????????????? ??')
            self.b_label.setText('???????????????? V')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "F?? = g????Sh":
            self.a_label.setText('???????????????? ??')
            self.b_label.setText('???????????????? S')
            self.c_label.setText('???????????????? h')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "A = FS":
            self.a_label.setText('???????????????? F')
            self.b_label.setText('???????????????? S')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "A = -F????S":
            self.a_label.setText('???????????????? F')
            self.b_label.setText('???????????????? S')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "N = A/t":
            self.a_label.setText('???????????????? A')
            self.b_label.setText('???????????????? t')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "A = Nt":
            self.a_label.setText('???????????????? N')
            self.b_label.setText('???????????????? t')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "M = Fl":
            self.a_label.setText('???????????????? F')
            self.b_label.setText('???????????????? l')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "?? = A??/A?? ?? 100%":
            self.a_label.setText('???????????????? A??')
            self.b_label.setText('???????????????? A??')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "M = Fl":
            self.a_label.setText('???????????????? F')
            self.b_label.setText('???????????????? l')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "?? = A??/A?? ?? 100%":
            self.a_label.setText('???????????????? A??')
            self.b_label.setText('???????????????? A??')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "E = Fh":
            self.a_label.setText('???????????????? F')
            self.b_label.setText('???????????????? h')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "E = gmh":
            self.a_label.setText('???????????????? m')
            self.b_label.setText('???????????????? h')            
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "E?? = mv?? / 2":
            self.a_label.setText('???????????????? m')
            self.b_label.setText('???????????????? v')            
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "Q = cm(t1-t2)":
            self.a_label.setText('???????????????? c')
            self.b_label.setText('???????????????? m')            
            self.c_label.setText('t1')
            self.d_label.setText('t2')
            self.e_label.setText('')
        if formula == "Q = cm??t":
            self.a_label.setText('???????????????? c')
            self.b_label.setText('???????????????? m')            
            self.c_label.setText('??t')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "Q = qm":
            self.a_label.setText('???????????????? q')
            self.b_label.setText('???????????????? m')            
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "?? = Q/(m(t2-t1)":
            self.a_label.setText('???????????????? Q')
            self.b_label.setText('???????????????? m')            
            self.c_label.setText('t1')
            self.d_label.setText('t2')
            self.e_label.setText('')
        if formula == "?? = Q/(m??t)":
            self.a_label.setText('???????????????? q')
            self.b_label.setText('???????????????? m')            
            self.c_label.setText('??t')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "Q = qV":
            self.a_label.setText('???????????????? q')
            self.b_label.setText('???????????????? V')            
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "q = Q/m":
            self.a_label.setText('???????????????? Q')
            self.b_label.setText('???????????????? m')            
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "q = Q/V":
            self.a_label.setText('???????????????? Q')
            self.b_label.setText('???????????????? V')            
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "??t = t1-t2":
            self.a_label.setText('???????????????? t1')
            self.b_label.setText('???????????????? t1')            
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "???t = Q/cm":
            self.a_label.setText('???????????????? Q')
            self.b_label.setText('???????????????? c')            
            self.c_label.setText('???????????????? m')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "???t = Q/qm":
            self.a_label.setText('???????????????? Q')
            self.b_label.setText('???????????????? q')            
            self.c_label.setText('???????????????? m')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "Q = ??m":
            self.a_label.setText('???????????????? ??')
            self.b_label.setText('???????????????? m')            
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "?? = Q/m":
            self.a_label.setText('???????????????? Q')
            self.b_label.setText('???????????????? m')            
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "m = Q/??":
            self.a_label.setText('???????????????? Q')
            self.b_label.setText('???????????????? ??')            
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "?? = p/p0 ?? 100%":
            self.a_label.setText('???????????????? p')
            self.b_label.setText('???????????????? p0')            
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "Q = Lm":
            self.a_label.setText('???????????????? L')
            self.b_label.setText('???????????????? m')            
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "L = Q/m":
            self.a_label.setText('???????????????? L')
            self.b_label.setText('???????????????? m')            
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "m = Q/L":
            self.a_label.setText('???????????????? Q')
            self.b_label.setText('???????????????? L')            
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula ==  "?? = A/Q1 ?? 100%":
            self.a_label.setText('???????????????? A')
            self.b_label.setText('???????????????? Q1')            
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula ==  "?? = Q1-Q2/Q1 ?? 100%":
            self.a_label.setText('???????????????? Q1')
            self.b_label.setText('???????????????? Q2')            
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "I = q/t":
            self.a_label.setText('???????????????? q')
            self.b_label.setText('???????????????? I')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "q = It":
            self.a_label.setText('???????????????? I')
            self.b_label.setText('???????????????? t')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "t = qI":
            self.a_label.setText('???????????????? q')
            self.b_label.setText('???????????????? I')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula ==  "U = A/q":
            self.a_label.setText('???????????????? A')
            self.b_label.setText('???????????????? q')            
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "U = IR":
            self.a_label.setText('???????????????? I')
            self.b_label.setText('???????????????? R')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "R = I/U":
            self.a_label.setText('???????????????? I')
            self.b_label.setText('???????????????? U')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "I = Aq":
            self.a_label.setText('???????????????? U')
            self.b_label.setText('???????????????? q')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "q = A/U":
            self.a_label.setText('???????????????? A')
            self.b_label.setText('???????????????? U')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "R = ??l/S":
            self.a_label.setText('???????????????? ??')
            self.b_label.setText('???????????????? l')
            self.c_label.setText('???????????????? S')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "?? = RS/l":
            self.a_label.setText('???????????????? R')
            self.b_label.setText('???????????????? S')
            self.c_label.setText('???????????????? l')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "S = ??l/R":
            self.a_label.setText('???????????????? ??')
            self.b_label.setText('???????????????? l')
            self.c_label.setText('???????????????? R')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "l = SR/??":
            self.a_label.setText('???????????????? S')
            self.b_label.setText('???????????????? R')
            self.c_label.setText('???????????????? ??')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "S = pF":
            self.a_label.setText('???????????????? m')
            self.b_label.setText('???????????????? ??')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "I = U/R":
            self.a_label.setText('???????????????? U')
            self.b_label.setText('???????????????? R')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "U = U1 + U2 + Ui":
            self.a_label.setText('???????????????? U1')
            self.b_label.setText('???????????????? U2')
            self.c_label.setText('???????????????? U3')
            self.d_label.setText('???????????????? U4')
            self.e_label.setText('???????????????? U5')
        if formula == "R = R1 + R2 + Ri":
            self.a_label.setText('???????????????? R1')
            self.b_label.setText('???????????????? R2')
            self.c_label.setText('???????????????? R3')
            self.d_label.setText('???????????????? R4')
            self.e_label.setText('???????????????? R5')
        if formula == "I = I1 + I2 + Ii":
            self.a_label.setText('???????????????? I1')
            self.b_label.setText('???????????????? I2')
            self.c_label.setText('???????????????? I3')
            self.d_label.setText('???????????????? I4')
            self.e_label.setText('???????????????? I5')
        if formula == "R = R1 ?? Ri / R1 + Ri":
            self.a_label.setText('???????????????? R1')
            self.b_label.setText('???????????????? R2')
            self.c_label.setText('???????????????? R3')
            self.d_label.setText('???????????????? R4')
            self.e_label.setText('???????????????? R5')
        if formula == "A = UIt":
            self.a_label.setText('???????????????? U')
            self.b_label.setText('???????????????? I')
            self.c_label.setText('???????????????? t')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "P = UI":
            self.a_label.setText('???????????????? U')
            self.b_label.setText('???????????????? I')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "Q = I??Rt":
            self.a_label.setText('???????????????? I')
            self.b_label.setText('???????????????? R')
            self.c_label.setText('???????????????? t')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "C = q/U":
            self.a_label.setText('???????????????? q')
            self.b_label.setText('???????????????? U')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "W = qU/2":
            self.a_label.setText('???????????????? q')
            self.b_label.setText('???????????????? U')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "W = CU??/2":
            self.a_label.setText('???????????????? C')
            self.b_label.setText('???????????????? U')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "W = q??/2C":
            self.a_label.setText('???????????????? q')
            self.b_label.setText('???????????????? C')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "n = sin(??)/sin(??)":
            self.a_label.setText('???????????????? ??')
            self.b_label.setText('???????????????? ??')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
        if formula == "D = 1/F":
            self.a_label.setText('???????????????? F')
            self.b_label.setText('')
            self.c_label.setText('')
            self.d_label.setText('')
            self.e_label.setText('')
            
    def num_set(self):
        formula = self.submethod_box.currentText()
                    
        if formula in formulas.one_number:
            self.a_line.setEnabled(True)
            self.a_label.setEnabled(True)
            self.b_line.setEnabled(False)
            self.b_label.setEnabled(False)
            self.c_line.setEnabled(False)
            self.c_label.setEnabled(False)
            self.d_line.setEnabled(False)
            self.d_label.setEnabled(False)
            self.e_line.setEnabled(False)
            self.e_label.setEnabled(False)
            
            self.a_line.setFrame(True)
            self.b_line.setFrame(False)
            self.c_line.setFrame(False)
            self.d_line.setFrame(False)
            self.e_line.setFrame(False)
        if formula in formulas.two_numbers:
            self.a_line.setEnabled(True)
            self.a_label.setEnabled(True)
            self.b_line.setEnabled(True)
            self.b_label.setEnabled(True) 
            self.c_line.setEnabled(False)
            self.c_label.setEnabled(False)
            self.d_line.setEnabled(False)
            self.d_label.setEnabled(False)
            self.e_line.setEnabled(False)
            self.e_label.setEnabled(False) 
            
            self.a_line.setFrame(True)
            self.b_line.setFrame(True)
            self.c_line.setFrame(False)
            self.d_line.setFrame(False)
            self.e_line.setFrame(False)            
        if formula in formulas.three_numbers:
            self.a_line.setEnabled(True)
            self.a_label.setEnabled(True)
            self.b_line.setEnabled(True)
            self.b_label.setEnabled(True)
            self.c_line.setEnabled(True)
            self.c_label.setEnabled(True) 
            self.d_line.setEnabled(False)
            self.d_label.setEnabled(False)
            self.e_line.setEnabled(False)
            self.e_label.setEnabled(False)
            
            self.a_line.setFrame(True)
            self.b_line.setFrame(True)
            self.c_line.setFrame(True)
            self.d_line.setFrame(False)
            self.e_line.setFrame(False)            
        if formula in formulas.four_numbers:
            self.a_line.setEnabled(True)
            self.a_label.setEnabled(True)
            self.b_line.setEnabled(True)
            self.b_label.setEnabled(True)
            self.c_line.setEnabled(True)
            self.c_label.setEnabled(True)
            self.d_line.setEnabled(True)
            self.d_label.setEnabled(True)
            self.e_line.setEnabled(False)
            self.e_label.setEnabled(False)
            
            self.a_line.setFrame(True)
            self.b_line.setFrame(True)
            self.c_line.setFrame(True)
            self.d_line.setFrame(True)
            self.e_line.setFrame(False)            
        if formula in formulas.five_numbers:
            self.a_line.setEnabled(True)
            self.a_label.setEnabled(True)
            self.b_line.setEnabled(True)
            self.b_label.setEnabled(True)
            self.c_line.setEnabled(True)
            self.c_label.setEnabled(True)
            self.d_line.setEnabled(True)
            self.d_label.setEnabled(True)
            self.e_line.setEnabled(True)
            self.e_label.setEnabled(True)
            
            self.a_line.setFrame(True)
            self.b_line.setFrame(True)
            self.c_line.setFrame(True)
            self.d_line.setFrame(True)
            self.e_line.setFrame(True)            
        
    def calculate(self):
          
        formula = self.submethod_box.currentText()
        value_a = self.a_line.text()
        value_b = self.b_line.text()
        value_c = self.c_line.text()
        value_d = self.d_line.text()
        value_e = self.e_line.text()
        if formula == "v = S/t":
            s = float(value_a)
            t = float(value_b)
            try:
                answer = s / t
                self.answer_label_2.setText(f"{answer} ??/??")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                
        if formula == "S = vt":
            v = float(value_a)
            t = float(value_b) 
            answer = v * t
            self.answer_label_2.setText(f"{answer} ??")
            
        if formula == "t = S/v":
            s = float(value_a)
            v = float(value_b)
            try:
                answer = s / v
                self.answer_label_2.setText(f"{answer} ??")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')  
                
        if formula == "?? = m/V":
            m = float(value_a)
            v = float(value_b)
            try:
                answer = m / v
                self.answer_label_2.setText(f"{answer} ????/????")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')  
                
        if formula == "m = ??V":
            v = float(value_a)
            t = float(value_b) 
            answer = v * t
            self.answer_label_2.setText(f"{answer} ????")
            
        if formula == "V = m/??":
            s = float(value_a)
            t = float(value_b)
            try:
                answer = s / t
                self.answer_label_2.setText(f"{answer} ????")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                
        if formula == "F?????? = k??l":
            k = float(value_a)
            ??l = float(value_b) 
            answer = k * ??l
            self.answer_label_2.setText(f"{answer} ??")
            
        if formula == "F?????? = mg":
            m = float(value_a)
            g = 9.8
            answer = m * g
            self.answer_label_2.setText(f"{answer} ??")
            
        if formula == "p = F/S":
            f = float(value_a)
            s = float(value_b)
            try:
                answer = f / s
                self.answer_label_2.setText(f"{answer} ????")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                
        if formula == "p = g??h":
            ?? = float(value_a)
            h = float(value_b)
            g = 9.8
            answer = g * ?? * h
            self.answer_label_2.setText(f"{answer} ????")
            
        if formula == "m = ??Sh":
            ?? = float(value_a)
            s = float(value_b)
            h = float(value_c)
            answer = ?? * s * h
            self.answer_label_2.setText(f"{answer} ????")
            
        if formula == "p = g??Sh":
            ?? = float(value_a)
            s = float(value_b)
            h = float(value_c)
            g = 9.8
            answer = g * ?? * s * h
            self.answer_label_2.setText(f"{answer} ????")
            
        if formula == "F?? = g????V??":
            ?? = float(value_a)
            v = float(value_b)
            g = 9.8
            answer = g * ?? * v
            self.answer_label_2.setText(f"{answer} ??")
            
        if formula == "F?? = g????Sh":
            ?? = float(value_a)
            s = float(value_b)
            h = float(value_c)
            g = 9.8
            answer = g * ?? * s * h
            self.answer_label_2.setText(f"{answer} ??")
            
        if formula == "A = FS":
            f = float(value_a)
            s = float(value_b)
            answer = f * s
            self.answer_label_2.setText(f"{answer} ????")
            
        if formula == "A = -F????S":
            f = float(value_a)
            s = float(value_b)
            answer = -1 * f * s
            self.answer_label_2.setText(f"{answer} ????")
            
        if formula == "N = A/t":
            a = float(value_a)
            t = float(value_b)
            try:
                answer = a / t
                self.answer_label_2.setText(f"{answer} ????")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                
        if formula == "A = Nt":
            n = float(value_a)
            t = float(value_b)
            answer = n * t
            self.answer_label_2.setText(f"{answer} ????")
                
        if formula == "M = Fl":
            f = float(value_a)
            l = float(value_b)
            answer = f * l
            self.answer_label_2.setText(f"{answer}")
                
        if formula == "?? = A??/A?? ?? 100%":
            a_u = float(value_a)
            a_c = float(value_b)
            try:
                answer = a_u / a_c * 100
                self.answer_label_2.setText(f"{answer}%")
                if answer > 100:
                    self.answer_label_2.setText(f"?????? ??? 100% > ")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                    
        if formula == "E = Fh":
            f = float(value_a)
            h = float(value_b)
            answer = f * h
            self.answer_label_2.setText(f"{answer} ????")
                            
        if formula == "E = gmh":
            m = float(value_a)
            h = float(value_b)
            g = 9.8
            answer = g * m * h
            self.answer_label_2.setText(f"{answer} ????")
        
        if formula == "E?? = mv?? / 2":
            m = float(value_a)
            v = float(value_b)
            try:
                answer = m * v ** 2 / 2
                self.answer_label_2.setText(f"{answer} ????")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                
        if formula == "Q = cm(t1-t2)":
            c = float(value_a)
            m = float(value_b)
            t1 = float(value_c)
            t2 = float(value_d)
            ??t = t1 - t2
            if ??t < 0:
                ??t = ??t * -1
            answer = c * m * ??t
            self.answer_label_2.setText(f"{answer} ????")
                
        if formula == "Q = cm??t":
            c = float(value_a)
            m = float(value_b)
            ??t = float(value_c)
            answer = c * m * ??t
            self.answer_label_2.setText(f"{answer} ????")
                    
        if formula == "Q = qm":
            q = float(value_a)
            m = float(value_b)
            q = q * 10 ** 7
            answer = q * m
            self.answer_label_2.setText(f"{answer} ????")
                
        if formula == "?? = Q/(m(t2-t1)":
            q = float(value_a)
            m = float(value_b)
            t1 = float(value_c)
            t2 = float(value_d)
            ??t = t1 - t2
            if ??t < 0:
                ??t = ??t * -1
            answer = m * ??t
            try:
                answer = q / answer
                self.answer_label_2.setText(f"{answer} ????/????/??c")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
       
        if formula == "?? = Q/(m??t)":
            q = float(value_a)
            m = float(value_b)
            ??t = float(value_c)
            if ??t < 0:
                ??t = ??t * -1
            answer = m * ??t
            try:
                answer = q / answer
                self.answer_label_2.setText(f"{answer} ????/????/??c")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                
        if formula == "Q = qV":
            q = float(value_a)
            v = float(value_b)
            q = q * 10 ** 7
            answer = q * v
            self.answer_label_2.setText(f"{answer} ????")
            
        if formula == "U = IR":
            i = float(value_a)
            r = float(value_b)
            answer = i * r
            self.answer_label_2.setText(f"{answer} ??")
            
        if formula == "q = Q/m":
            q = float(value_a)
            m = float(value_b) 
            try:
                answer = q / m
                self.answer_label_2.setText(f"{answer} ????/????")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
            
        if formula == "q = A/q":
            a = float(value_a)
            q = float(value_b) 
            try:
                answer = a / q
                self.answer_label_2.setText(f"{answer} ????")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
            
        if formula == "q = Q/V":
            q = float(value_a)
            v = float(value_b) 
            try:
                answer = q / v
                self.answer_label_2.setText(f"{answer} ????/????")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
        
        if formula == "??t = t1 - t2":
            t1 = float(value_a)
            t2 = float(value_b)
            ??t = t1 - t2
            if ??t < 0:
                ??t = ??t * -1
            answer = ??t
            self.answer_label_2.setText(f"{answer} ??c")
            
        if formula == "???t = Q/cm":
            q = float(value_a)
            m = float(value_b)
            c = float(value_c)
            try:
                answer = q / c * m
                self.answer_label_2.setText(f"{answer}??c")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                
        if formula == "???t = Q/qm":
            q1 = float(value_a)
            q2 = float(value_b)
            m = float(value_c)
            try:
                answer = q1 / q2 * m
                self.answer_label_2.setText(f"{answer}??c")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                
        if formula == "Q = ??m":
            ?? = float(value_a)
            m = float(value_b)
            answer = ?? * 10 ** 5 * m
            self.answer_label_2.setText(f"{answer} ????")
                    
        if formula == "?? = Q/m":
            q = float(value_a)
            m = float(value_b)
            try:
                answer = q / m
                self.answer_label_2.setText(f"{answer} ????/????")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                    
        if formula == "m = Q/??":
            q = float(value_a)
            ?? = float(value_b)
            try:
                answer = q / ??
                self.answer_label_2.setText(f"{answer} ????")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                
        if formula == "?? = p/p0 ?? 100%":
            p = float(value_a)
            p0 = float(value_b)
            try:
                answer = p / p0 * 100
                self.answer_label_2.setText(f"{answer}%")
                if answer > 100:
                    self.answer_label_2.setText(f"?? ??? 100% > ")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                
        if formula == "Q = Lm":
            l = float(value_a)
            m = float(value_b)
            answer = l * 10 ** 6 * m
            self.answer_label_2.setText(f"{answer} ????")
                            
        if formula == "L = Q/m":
            q = float(value_a)
            m = float(value_b)
            try:
                answer = q / m
                self.answer_label_2.setText(f"{answer} ????/????")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                            
        if formula == "m = Q/L":
            q = float(value_a)
            l = float(value_b)
            try:
                answer = q / l
                self.answer_label_2.setText(f"{answer} ????")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
        
        if formula == "?? = A/Q1 ?? 100%":
            a = float(value_a)
            q1 = float(value_b)
            try:
                answer = a / q1 * 100
                self.answer_label_2.setText(f"{answer}%")
                if answer > 100:
                    self.answer_label_2.setText(f"?????? ??? 100% > ")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                
        if formula == "?? = Q1-Q2/Q1 ?? 100%":
            q1 = float(value_a)
            q2 = float(value_b)
            try:
                q3 = q1 - q2
                answer = q3 / q2 * 100
                self.answer_label_2.setText(f"{answer}%")
                if answer > 100:
                    self.answer_label_2.setText(f"?????? ??? 100% > ")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
            
        if formula == "I = q/t":
            q = float(value_a)
            t = float(value_b)
            try:
                answer = q / t
                self.answer_label_2.setText(f"{answer} A")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                        
        if formula == "t = qI":
            q = float(value_a)
            i = float(value_b) 
            answer = q * i
            self.answer_label_2.setText(f"{answer} ??")
                    
        if formula == "q = It":
            i = float(value_a)
            t = float(value_b) 
            answer = i * t
            self.answer_label_2.setText(f"{answer} ????")
            
        if formula == "U = A/q":
            a = float(value_a)
            q = float(value_b)
            try:
                answer = a / q
                self.answer_label_2.setText(f"{answer} ??")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                
        if formula == "R = I/U":
            i = float(value_a)
            u = float(value_b)
            try:
                answer = i / u
                self.answer_label_2.setText(f"{answer} ????")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                
        if formula == "I = Aq":
            u = float(value_a)
            q = float(value_b) 
            answer = u * q
            self.answer_label_2.setText(f"{answer} ??")
            
        if formula == "q = A/U":
            a = float(value_a)
            u = float(value_b)
            try:
                answer = a / u
                self.answer_label_2.setText(f"{answer} ????")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
        
        if formula == "R = ??l/S":
            ?? = float(value_a)
            l = float(value_b)
            s = float(value_c)
            try:
                answer = ?? * l / s
                self.answer_label_2.setText(f"{answer} ????")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                
        if formula == "?? = RS/l":
            r = float(value_a)
            s = float(value_b)
            l = float(value_c)
            try:
                answer = r * s / l
                self.answer_label_2.setText(f"{answer} ???? ?? ??????/ ????")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                
        if formula == "S = ??l/R":
            ?? = float(value_a)
            l = float(value_b)
            r = float(value_c)
            try:
                answer = ?? * l / r
                self.answer_label_2.setText(f"{answer} ????")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                
        if formula == "l = SR/??":
            s = float(value_a)
            r = float(value_b)
            ?? = float(value_c)
            try:
                answer = s * r / ??
                self.answer_label_2.setText(f"{answer} ??")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
        
        if formula == "I = U/R":
            u = float(value_a)
            r = float(value_b)
            try:
                answer = u / r
                self.answer_label_2.setText(f"{answer} ??")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                
        if formula == "S = pF":
            p = float(value_a)
            f = float(value_b) 
            answer = p * f
            self.answer_label_2.setText(f"{answer} ????")
            
        if formula == "U = U1 + U2 + Ui":
            u1 = float(value_a)
            u2 = float(value_b)
            u3 = float(value_c)
            u4 = float(value_d)
            u5 = float(value_e)
            answer = u1 + u2 + u3 + u4 + u5
            self.answer_label_2.setText(f"{answer} ??")
        
        if formula == "R = R1 + R2 + Ri":
            r1 = float(value_a)
            r2 = float(value_b)
            r3 = float(value_c)
            r4 = float(value_d)
            r5 = float(value_e)
            answer = r1 + r2 + r3 + r4 + r5
            self.answer_label_2.setText(f"{answer} ????")
            
        if formula == "I = I1 + I2 + Ii":
            i1 = float(value_a)
            i2 = float(value_b)
            i3 = float(value_c)
            i4 = float(value_d)
            i5 = float(value_e)
            answer = i1 + i2 + i3 + i4 + i5
            self.answer_label_2.setText(f"{answer} ??")
            
        if formula == "R = R1 ?? Ri / R1 + Ri":
            r1 = float(value_a)
            r2 = float(value_b)
            r3 = float(value_c)
            r4 = float(value_d)
            r5 = float(value_e)
            elements = [r1, r2 ,r3 ,r4 ,r5]
            values = []
            for element in elements:
                if element != 0:
                    values.append(element)      
                    a = sum(values)
                    b = prod(values)
            try:
                answer = b / a
                self.answer_label_2.setText(f"{answer} ????")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                
        if formula == "A = UIt":
            u = float(value_a)
            i = float(value_b)
            t = float(value_c)
            answer = u * i * t
            self.answer_label_2.setText(f"{answer} ????")
                
        if formula == "P = UI":
            u = float(value_a)
            i = float(value_b) 
            answer = u * i
            self.answer_label_2.setText(f"{answer} ????")
                
        if formula == "Q = I??Rt":
            i = float(value_a)
            r = float(value_b)
            t = float(value_c)
            answer = i ** 2 * r * t
            self.answer_label_2.setText(f"{answer} ????")
        
        if formula == "C = q/U":
            q = float(value_a)
            u = float(value_b)
            try:
                answer = q / u
                self.answer_label_2.setText(f"{answer} ??")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                
        if formula == "W = qU/2":
            q = float(value_a)
            u = float(value_b)
            try:
                answer = q * u / 2
                self.answer_label_2.setText(f"{answer} ??/??")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                
        if formula == "W = CU??/2":
            c = float(value_a)
            u = float(value_b)
            u = u ** 2
            try:
                answer = c * u / 2
                self.answer_label_2.setText(f"{answer} ??/??")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                
        if formula == "W = q??/2C":
            q = float(value_a)
            c = float(value_b)
            q = q ** 2
            c = c * 2
            try:
                answer = q / c
                self.answer_label_2.setText(f"{answer} ??/??")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
            
        if formula == "n = sin(??)/sin(??)":
            ?? = float(value_a)
            ?? = float(value_b)
            ?? = sin(??)
            ?? = sin(??)
            try:
                answer =  ?? / ??
                self.answer_label_2.setText(f"{answer}")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
                
        if formula == "D = 1/F":
            d = float(value_a)
            try:
                answer = 1 / d
                self.answer_label_2.setText(f"{answer} ????????")
            except ZeroDivisionError:
                self.answer_label_2.setText('?????????????? ???? ????????')
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()
    
if __name__ == '__main__':
    main()