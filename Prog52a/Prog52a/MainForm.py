﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Teal
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.Control
        self._label1.Location = System.Drawing.Point(110, 41)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(208, 67)
        self._label1.TabIndex = 0
        self._label1.Text = "Length:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Teal
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.Control
        self._label2.Location = System.Drawing.Point(122, 90)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(208, 67)
        self._label2.TabIndex = 1
        self._label2.Text = "Width:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Teal
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.Control
        self._label3.Location = System.Drawing.Point(122, 191)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(208, 67)
        self._label3.TabIndex = 2
        self._label3.Text = "Area:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Teal
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.Control
        self._label4.Location = System.Drawing.Point(57, 258)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(208, 67)
        self._label4.TabIndex = 3
        self._label4.Text = "Perimeter:"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
        self._label5.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(290, 175)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(368, 44)
        self._label5.TabIndex = 4
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
        self._label6.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(290, 247)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(368, 46)
        self._label6.TabIndex = 5
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.PaleTurquoise
        self._button1.Location = System.Drawing.Point(57, 362)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(173, 75)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.PaleTurquoise
        self._button2.Location = System.Drawing.Point(290, 362)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(173, 75)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.PaleTurquoise
        self._button3.Location = System.Drawing.Point(521, 362)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(173, 75)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(290, 41)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(368, 31)
        self._textBox1.TabIndex = 9
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(290, 94)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(368, 31)
        self._textBox2.TabIndex = 10
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Teal
        self.ClientSize = System.Drawing.Size(748, 462)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "Prog52a"
        self.ResumeLayout(False)
        self.PerformLayout()

    
    
    def Button1Click(self, sender, e):
        length = int(self._textBox1.Text)
        width  = int(self._textBox2.Text)
        area   = length * width
        perim  = 2 * length + 2 * width
        self._label5.Text = str(area)
        self._label6.Text = str(perim)
        # + - * / %     ** pow     // divide & round down
        # int (Integer): a whole number, pos/neg
        # float (Floating-Point Number): any number w/ a decimal
        # str (String): a string of text

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label5.Text = ""
        self._label6.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()