import System.Drawing
import math
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self._label15 = System.Windows.Forms.Label()
        self._label16 = System.Windows.Forms.Label()
        self._label17 = System.Windows.Forms.Label()
        self._label18 = System.Windows.Forms.Label()
        self._label19 = System.Windows.Forms.Label()
        self._label20 = System.Windows.Forms.Label()
        self._label21 = System.Windows.Forms.Label()
        self._label22 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.DarkSlateGray
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("MS Reference Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.SeaShell
        self._label1.Location = System.Drawing.Point(12, 19)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(276, 52)
        self._label1.TabIndex = 0
        self._label1.Text = "Purchase Price:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(171, 114)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 20)
        self._textBox2.TabIndex = 3
        self._textBox2.TextChanged += self.TextBox2TextChanged
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.DarkSlateGray
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("MS Reference Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.SeaShell
        self._label2.Location = System.Drawing.Point(12, 96)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(276, 52)
        self._label2.TabIndex = 2
        self._label2.Text = "Amount Given:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightSeaGreen
        self._button1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.White
        self._button1.Location = System.Drawing.Point(71, 169)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(151, 58)
        self._button1.TabIndex = 4
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightSeaGreen
        self._button2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.White
        self._button2.Location = System.Drawing.Point(71, 246)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(151, 58)
        self._button2.TabIndex = 5
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Teal
        self._button3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.White
        self._button3.Location = System.Drawing.Point(71, 323)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(151, 58)
        self._button3.TabIndex = 6
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.LightCyan
        self._label3.Font = System.Drawing.Font("MS Reference Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(360, 19)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(240, 362)
        self._label3.TabIndex = 7
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.LightCyan
        self._label4.Font = System.Drawing.Font("Segoe UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(374, 33)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(197, 24)
        self._label4.TabIndex = 8
        self._label4.Text = "Purchase Price: "
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.LightCyan
        self._label5.Font = System.Drawing.Font("Segoe UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(374, 59)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(197, 24)
        self._label5.TabIndex = 9
        self._label5.Text = "Amount Given:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.LightCyan
        self._label6.Font = System.Drawing.Font("Segoe UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(502, 32)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(82, 24)
        self._label6.TabIndex = 10
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.LightCyan
        self._label7.Font = System.Drawing.Font("Segoe UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(502, 57)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(82, 24)
        self._label7.TabIndex = 11
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.LightCyan
        self._label8.Font = System.Drawing.Font("Segoe UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(371, 81)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(213, 24)
        self._label8.TabIndex = 12
        self._label8.Text = "________________________"
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.LightCyan
        self._label9.Font = System.Drawing.Font("Segoe UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(374, 110)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(197, 24)
        self._label9.TabIndex = 13
        self._label9.Text = "Change:"
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.LightCyan
        self._label10.Font = System.Drawing.Font("Segoe UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(457, 114)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(82, 24)
        self._label10.TabIndex = 14
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.LightCyan
        self._label11.Font = System.Drawing.Font("Segoe UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(371, 134)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(213, 24)
        self._label11.TabIndex = 15
        self._label11.Text = "________________________"
        self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.LightCyan
        self._label12.Font = System.Drawing.Font("Segoe UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(374, 169)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(197, 24)
        self._label12.TabIndex = 16
        self._label12.Text = "Dollars:"
        self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.Color.LightCyan
        self._label13.Font = System.Drawing.Font("Segoe UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(457, 169)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(82, 24)
        self._label13.TabIndex = 17
        self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label14
        # 
        self._label14.BackColor = System.Drawing.Color.LightCyan
        self._label14.Font = System.Drawing.Font("Segoe UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label14.Location = System.Drawing.Point(374, 203)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(87, 24)
        self._label14.TabIndex = 18
        self._label14.Text = "Quarters:"
        self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label15
        # 
        self._label15.BackColor = System.Drawing.Color.LightCyan
        self._label15.Font = System.Drawing.Font("Segoe UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label15.Location = System.Drawing.Point(467, 203)
        self._label15.Name = "label15"
        self._label15.Size = System.Drawing.Size(82, 24)
        self._label15.TabIndex = 19
        self._label15.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label16
        # 
        self._label16.BackColor = System.Drawing.Color.LightCyan
        self._label16.Font = System.Drawing.Font("Segoe UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label16.Location = System.Drawing.Point(374, 236)
        self._label16.Name = "label16"
        self._label16.Size = System.Drawing.Size(197, 24)
        self._label16.TabIndex = 20
        self._label16.Text = "Dimes:"
        self._label16.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label17
        # 
        self._label17.BackColor = System.Drawing.Color.LightCyan
        self._label17.Font = System.Drawing.Font("Segoe UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label17.Location = System.Drawing.Point(446, 236)
        self._label17.Name = "label17"
        self._label17.Size = System.Drawing.Size(82, 24)
        self._label17.TabIndex = 21
        self._label17.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label18
        # 
        self._label18.BackColor = System.Drawing.Color.LightCyan
        self._label18.Font = System.Drawing.Font("Segoe UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label18.Location = System.Drawing.Point(374, 269)
        self._label18.Name = "label18"
        self._label18.Size = System.Drawing.Size(197, 24)
        self._label18.TabIndex = 22
        self._label18.Text = "Nickels:"
        self._label18.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label19
        # 
        self._label19.BackColor = System.Drawing.Color.LightCyan
        self._label19.Font = System.Drawing.Font("Segoe UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label19.Location = System.Drawing.Point(457, 269)
        self._label19.Name = "label19"
        self._label19.Size = System.Drawing.Size(82, 24)
        self._label19.TabIndex = 23
        self._label19.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label20
        # 
        self._label20.BackColor = System.Drawing.Color.LightCyan
        self._label20.Font = System.Drawing.Font("Segoe UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label20.Location = System.Drawing.Point(374, 304)
        self._label20.Name = "label20"
        self._label20.Size = System.Drawing.Size(197, 24)
        self._label20.TabIndex = 24
        self._label20.Text = "Pennies:"
        self._label20.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label21
        # 
        self._label21.BackColor = System.Drawing.Color.LightCyan
        self._label21.Font = System.Drawing.Font("Segoe UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label21.Location = System.Drawing.Point(457, 304)
        self._label21.Name = "label21"
        self._label21.Size = System.Drawing.Size(82, 24)
        self._label21.TabIndex = 25
        self._label21.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label22
        # 
        self._label22.BackColor = System.Drawing.Color.LightCyan
        self._label22.Font = System.Drawing.Font("Segoe UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label22.Location = System.Drawing.Point(374, 334)
        self._label22.Name = "label22"
        self._label22.Size = System.Drawing.Size(213, 24)
        self._label22.TabIndex = 26
        self._label22.Text = "________________________"
        self._label22.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(171, 33)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 20)
        self._textBox1.TabIndex = 27
        self._textBox1.TextChanged += self.TextBox1TextChanged
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.CadetBlue
        self.ClientSize = System.Drawing.Size(634, 406)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label22)
        self.Controls.Add(self._label21)
        self.Controls.Add(self._label20)
        self.Controls.Add(self._label19)
        self.Controls.Add(self._label18)
        self.Controls.Add(self._label17)
        self.Controls.Add(self._label16)
        self.Controls.Add(self._label15)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog58t Real"
        self.ResumeLayout(False)
        self.PerformLayout()


    
    def Button1Click(self, sender, e):
        Price = float(self._textBox1.Text)
        AmountGiven = float(self._textBox2.Text)
        TotalChange = AmountGiven - Price
        Dollars = int(TotalChange//1)
        Quarters = int(((TotalChange-Dollars)/25*100)//1)
        Dimes = int((TotalChange-Dollars-Quarters*0.25)*10//1)
        Nickels = int(((TotalChange-Dollars-Quarters*0.25-Dimes*0.10)/5*100)//1)
        Pennies = int((TotalChange-Dollars-Quarters*0.25-Dimes*0.10-Nickels*0.05)*100)
        self._label10.Text = str(TotalChange)
        self._label13.Text = str(Dollars)
        self._label15.Text = str(Quarters)
        self._label17.Text = str(Dimes)
        self._label19.Text = str(Nickels)
        self._label21.Text = str(Pennies)
    def TextBox1TextChanged(self, sender, e):
        self._label6.Text = "$" + str(self._textBox1.Text)

    def TextBox2TextChanged(self, sender, e):
        self._label7.Text = "$" + str(self._textBox2.Text)

    def Button2Click(self, sender, e):
        self._label10.Text = ""
        self._label13.Text = ""
        self._label15.Text = ""
        self._label17.Text = ""
        self._label19.Text = ""
        self._label21.Text = ""
        self._textBox1.Text = ""
        self._textBox2.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit