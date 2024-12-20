﻿import System.Drawing
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
        self._listBox1.Font = System.Drawing.Font("Yu Gothic UI", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 25
        self._listBox1.Location = System.Drawing.Point(264, 17)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(412, 404)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.MediumPurple
        self._button1.Font = System.Drawing.Font("Yu Gothic UI", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button1.Location = System.Drawing.Point(12, 17)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(246, 68)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.MediumPurple
        self._button2.Font = System.Drawing.Font("Yu Gothic UI", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button2.Location = System.Drawing.Point(12, 91)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(246, 68)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.MediumPurple
        self._button3.Font = System.Drawing.Font("Yu Gothic UI", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button3.Location = System.Drawing.Point(12, 165)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(246, 68)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Indigo
        self.ClientSize = System.Drawing.Size(688, 437)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "Prog 122i"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e): # Calculate
        Num = -25
        Heading = "Number\tNumber Cube\tCube Root"
        self._listBox1.Items.Add(Heading)
        for num in range(-25, 26):
            Cube = Num**3
            if Num > -1:
                CubeRoot = Num**(1./3)
            else: CubeRoot = (Num *-1) **(1./3) *-1
            Line = str(Num) + "\t" + str(Cube) + "\t\t" + str(round(CubeRoot,5))
            self._listBox1.Items.Add(Line)
            Num = Num+1
            

    def Button2Click(self, sender, e):
        pass

    def Button3Click(self, sender, e): 
        pass