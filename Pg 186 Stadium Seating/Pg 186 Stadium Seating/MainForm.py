import System.Drawing
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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.GreenYellow
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.Font = System.Drawing.Font("MS Reference Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ControlText
        self._label1.Location = System.Drawing.Point(26, 23)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(266, 347)
        self._label1.TabIndex = 0
        self._label1.Text = "Tickets Sold"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.GreenYellow
        self._label2.Font = System.Drawing.Font("MS Reference Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(26, 49)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(206, 185)
        self._label2.TabIndex = 1
        self._label2.Text = "Enter the number of tickets sold for each class of seats."
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.GreenYellow
        self._label3.Font = System.Drawing.Font("MS Reference Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(41, 152)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(106, 29)
        self._label3.TabIndex = 2
        self._label3.Text = "Class A:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.GreenYellow
        self._label4.Font = System.Drawing.Font("MS Reference Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(41, 234)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(106, 29)
        self._label4.TabIndex = 3
        self._label4.Text = "Class B:"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.GreenYellow
        self._label5.Font = System.Drawing.Font("MS Reference Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(41, 314)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(106, 29)
        self._label5.TabIndex = 4
        self._label5.Text = "Class C:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(153, 156)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 22)
        self._textBox1.TabIndex = 5
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(153, 234)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 22)
        self._textBox2.TabIndex = 6
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(153, 314)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(100, 22)
        self._textBox3.TabIndex = 7
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.YellowGreen
        self._label6.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label6.Font = System.Drawing.Font("MS Reference Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.SystemColors.ControlText
        self._label6.Location = System.Drawing.Point(328, 23)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(266, 347)
        self._label6.TabIndex = 8
        self._label6.Text = "Revenue Generated"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.YellowGreen
        self._label7.Font = System.Drawing.Font("MS Reference Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(343, 81)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(106, 29)
        self._label7.TabIndex = 9
        self._label7.Text = "Class A:"
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.YellowGreen
        self._label8.Font = System.Drawing.Font("MS Reference Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(343, 136)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(106, 29)
        self._label8.TabIndex = 10
        self._label8.Text = "Class B:"
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.YellowGreen
        self._label9.Font = System.Drawing.Font("MS Reference Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(343, 193)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(106, 29)
        self._label9.TabIndex = 11
        self._label9.Text = "Class C:"
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.YellowGreen
        self._label10.Font = System.Drawing.Font("MS Reference Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(343, 259)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(170, 29)
        self._label10.TabIndex = 12
        self._label10.Text = "Total Revenue:"
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.GreenYellow
        self._label11.Font = System.Drawing.Font("MS Reference Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(445, 81)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(127, 29)
        self._label11.TabIndex = 13
        self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.GreenYellow
        self._label12.Font = System.Drawing.Font("MS Reference Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(445, 136)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(127, 29)
        self._label12.TabIndex = 14
        self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.Color.GreenYellow
        self._label13.Font = System.Drawing.Font("MS Reference Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(445, 193)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(127, 29)
        self._label13.TabIndex = 15
        self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label14
        # 
        self._label14.BackColor = System.Drawing.Color.GreenYellow
        self._label14.Font = System.Drawing.Font("MS Reference Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label14.Location = System.Drawing.Point(343, 307)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(238, 29)
        self._label14.TabIndex = 16
        self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Green
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button1.Location = System.Drawing.Point(26, 392)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(186, 68)
        self._button1.TabIndex = 17
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Green
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button2.Location = System.Drawing.Point(218, 392)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(186, 68)
        self._button2.TabIndex = 18
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Green
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button3.Location = System.Drawing.Point(408, 392)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(186, 68)
        self._button3.TabIndex = 19
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkOliveGreen
        self.ClientSize = System.Drawing.Size(622, 470)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg 186 Stadium Seating"
        self.ResumeLayout(False)
        self.PerformLayout()


  

    def Button1Click(self, sender, e):
        ClassAtotal = int(self._textBox1.Text) * 15
        ClassBtotal = int(self._textBox2.Text) * 12
        ClassCtotal = int(self._textBox3.Text) * 9
        
        self._label11.Text = str(ClassAtotal)
        self._label12.Text = str(ClassBtotal)
        self._label13.Text = str(ClassCtotal)
        self._label14.Text = str(ClassAtotal + ClassBtotal + ClassCtotal)

    def Button2Click(self, sender, e):
        self._
        self._label11.Text = ""
        self._label12.Text = ""
        self._label13.Text = ""
        self._label14.Text = ""