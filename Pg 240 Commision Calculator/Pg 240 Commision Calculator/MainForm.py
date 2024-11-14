import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Myanmar Text", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label1.Location = System.Drawing.Point(64, 10)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(173, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "Sales For this Month:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(243, 7)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(159, 26)
        self._textBox1.TabIndex = 1
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(243, 52)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(159, 26)
        self._textBox2.TabIndex = 2
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Myanmar Text", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label2.Location = System.Drawing.Point(48, 52)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(187, 23)
        self._label2.TabIndex = 3
        self._label2.Text = "Advance Pay Awarded:"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Myanmar Text", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label3.Location = System.Drawing.Point(90, 129)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(147, 23)
        self._label3.TabIndex = 4
        self._label3.Text = "Commision Rate:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Lavender
        self._label4.Font = System.Drawing.Font("Myanmar Text", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.ControlText
        self._label4.Location = System.Drawing.Point(243, 129)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(147, 23)
        self._label4.TabIndex = 5
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Lavender
        self._label5.Font = System.Drawing.Font("Myanmar Text", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.SystemColors.ControlText
        self._label5.Location = System.Drawing.Point(243, 169)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(147, 23)
        self._label5.TabIndex = 7
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Myanmar Text", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label6.Location = System.Drawing.Point(90, 169)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(147, 23)
        self._label6.TabIndex = 6
        self._label6.Text = "Commision:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.Lavender
        self._label7.Font = System.Drawing.Font("Myanmar Text", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.SystemColors.ControlText
        self._label7.Location = System.Drawing.Point(243, 212)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(147, 23)
        self._label7.TabIndex = 9
        # 
        # label8
        # 
        self._label8.Font = System.Drawing.Font("Myanmar Text", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label8.Location = System.Drawing.Point(90, 212)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(147, 23)
        self._label8.TabIndex = 8
        self._label8.Text = "Net Pay:"
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Nirmala UI", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 259)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(123, 51)
        self._button1.TabIndex = 10
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkBlue
        self.ClientSize = System.Drawing.Size(414, 322)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg 240 Commision Calculator"
        self.ResumeLayout(False)
        self.PerformLayout()

