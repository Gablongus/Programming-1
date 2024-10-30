﻿import System.Drawing
import math
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.Color.Black
        self._listBox1.Font = System.Drawing.Font("Segoe Fluent Icons", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.ForeColor = System.Drawing.SystemColors.Window
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 15
        self._listBox1.Location = System.Drawing.Point(295, 11)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(537, 409)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.RoyalBlue
        self._button1.Font = System.Drawing.Font("Yu Gothic", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button1.Location = System.Drawing.Point(12, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(277, 100)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.RoyalBlue
        self._button2.Font = System.Drawing.Font("Yu Gothic", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button2.Location = System.Drawing.Point(12, 134)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(277, 100)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.RoyalBlue
        self._button3.Font = System.Drawing.Font("Yu Gothic", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button3.Location = System.Drawing.Point(12, 255)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(277, 100)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Navy
        self.ClientSize = System.Drawing.Size(844, 438)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "Prog 122h"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e): # Calculate
        Num = 1
        Heading = "Number\tSquare\tSquare Root\tCube\t4th Root"
        self._listBox1.Items.Add(Heading)
        for num in range(0,20):
            Square = Num**2
            SquareRoot = round(math.sqrt(Num),4)
            Cube = Num**3
            FourthRoot = round(Num **(1./4),4)
            line = str(Num) + "\t" + str(Square) + "\t" + str(SquareRoot) + "\t\t" + str(Cube) + "\t" + str(FourthRoot)
            self._listBox1.Items.Add(line)
            Num = Num +1

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()