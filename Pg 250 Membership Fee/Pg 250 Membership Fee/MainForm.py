import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
        self.decDiscount4to6 = 0.05
        self.decDiscount7to9 = 0.08
        self.decDiscount10orMore = 0.1
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._radioButton4 = System.Windows.Forms.RadioButton()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._checkBox3 = System.Windows.Forms.CheckBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Thistle
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.Font = System.Drawing.Font("MS Reference Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label1.Location = System.Drawing.Point(13, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(231, 153)
        self._label1.TabIndex = 0
        self._label1.Text = """Type of membership:
"""
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Thistle
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label2.Font = System.Drawing.Font("MS Reference Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label2.Location = System.Drawing.Point(259, 13)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(231, 153)
        self._label2.TabIndex = 1
        self._label2.Text = "Options:"
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.Color.Thistle
        self._radioButton1.Font = System.Drawing.Font("MS Reference Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(29, 37)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(196, 24)
        self._radioButton1.TabIndex = 2
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Standard Adult"
        self._radioButton1.UseVisualStyleBackColor = False
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.Color.Thistle
        self._radioButton2.Font = System.Drawing.Font("MS Reference Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(29, 67)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(204, 24)
        self._radioButton2.TabIndex = 3
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Child (12 and under)"
        self._radioButton2.UseVisualStyleBackColor = False
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.Color.Thistle
        self._radioButton3.Font = System.Drawing.Font("MS Reference Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(29, 97)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(204, 24)
        self._radioButton3.TabIndex = 4
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Student"
        self._radioButton3.UseVisualStyleBackColor = False
        # 
        # radioButton4
        # 
        self._radioButton4.BackColor = System.Drawing.Color.Thistle
        self._radioButton4.Font = System.Drawing.Font("MS Reference Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton4.Location = System.Drawing.Point(29, 127)
        self._radioButton4.Name = "radioButton4"
        self._radioButton4.Size = System.Drawing.Size(204, 24)
        self._radioButton4.TabIndex = 5
        self._radioButton4.TabStop = True
        self._radioButton4.Text = "Senior Citizen "
        self._radioButton4.UseVisualStyleBackColor = False
        # 
        # checkBox1
        # 
        self._checkBox1.BackColor = System.Drawing.Color.Thistle
        self._checkBox1.Font = System.Drawing.Font("MS Reference Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox1.Location = System.Drawing.Point(276, 37)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(202, 24)
        self._checkBox1.TabIndex = 6
        self._checkBox1.Text = "Yoga"
        self._checkBox1.UseVisualStyleBackColor = False
        # 
        # checkBox2
        # 
        self._checkBox2.BackColor = System.Drawing.Color.Thistle
        self._checkBox2.Font = System.Drawing.Font("MS Reference Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox2.Location = System.Drawing.Point(276, 68)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(202, 24)
        self._checkBox2.TabIndex = 7
        self._checkBox2.Text = "Karate"
        self._checkBox2.UseVisualStyleBackColor = False
        # 
        # checkBox3
        # 
        self._checkBox3.BackColor = System.Drawing.Color.Thistle
        self._checkBox3.Font = System.Drawing.Font("MS Reference Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox3.Location = System.Drawing.Point(276, 97)
        self._checkBox3.Name = "checkBox3"
        self._checkBox3.Size = System.Drawing.Size(202, 24)
        self._checkBox3.TabIndex = 8
        self._checkBox3.Text = "Personal Trainer"
        self._checkBox3.UseVisualStyleBackColor = False
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Thistle
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label3.Font = System.Drawing.Font("MS Reference Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label3.Location = System.Drawing.Point(13, 185)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(231, 121)
        self._label3.TabIndex = 9
        self._label3.Text = "Membership length:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Thistle
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label4.Font = System.Drawing.Font("MS Reference Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label4.Location = System.Drawing.Point(259, 185)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(231, 121)
        self._label4.TabIndex = 10
        self._label4.Text = "Membership fees:"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Thistle
        self._label5.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(54, 207)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(120, 39)
        self._label5.TabIndex = 11
        self._label5.Text = "Enter number of months:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("MS Reference Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(54, 258)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(145, 26)
        self._textBox1.TabIndex = 12
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.Thistle
        self._label6.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(276, 220)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(95, 26)
        self._label6.TabIndex = 13
        self._label6.Text = "Monthly Fee:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.Thistle
        self._label7.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(276, 259)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(95, 26)
        self._label7.TabIndex = 14
        self._label7.Text = "Total:"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label8.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(383, 220)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(95, 26)
        self._label8.TabIndex = 15
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label9.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(383, 258)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(95, 26)
        self._label9.TabIndex = 16
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Plum
        self._button1.Font = System.Drawing.Font("Nirmala UI", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(29, 335)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(109, 59)
        self._button1.TabIndex = 17
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Plum
        self._button2.Font = System.Drawing.Font("Nirmala UI", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(199, 335)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(109, 59)
        self._button2.TabIndex = 18
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Plum
        self._button3.Font = System.Drawing.Font("Nirmala UI", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(369, 335)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(109, 59)
        self._button3.TabIndex = 19
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkMagenta
        self.ClientSize = System.Drawing.Size(504, 422)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._checkBox3)
        self.Controls.Add(self._checkBox2)
        self.Controls.Add(self._checkBox1)
        self.Controls.Add(self._radioButton4)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg 250 Membership Fee"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        decBaseFee = 0.0
        decDiscount = 0.0
        decTotalFee= 0.0
        intMonths = 0.0
        
        try:
            intMonths = int(self._textBox1.Text)
        except:
            MessageBox.Show("Months must be a valid integer", "Input Error")
            return
        
        if intMonths < 1 or intMonths > 24:
            MessageBox.Show("Months must be a valid integer", "Input Error")
            return
        
        if self._radioButton1.Checked == True:
            decBaseFee = 40
        elif self._radioButton2.Checked == True:
            decBaseFee = 20
        elif self._radioButton3.Checked == True:
            decBaseFee = 25
        elif self._radioButton4.Checked == True:
            decBaseFee = 30

        if self._checkBox1.Checked == True:
            decBaseFee += 10
        if self._checkBox1.Checked == True:
            decBaseFee += 30
        if self._checkBox1.Checked == True:
            decBaseFee += 50
            
        if intMonths <= 3:
            decDiscount = 0.0
        elif intMonths >= 4 and intMonths <= 6:
            decDiscount = decBaseFee * self.decDiscount4to6
        elif intMonths >= 7 and intMonths <= 9:
            decDiscount = decBaseFee * self.decDiscount7to9
        elif intMonths >10:
            decDiscount = decBaseFee * self.decDiscount10orMore
            
        decBaseFee -= decDiscount
        decTotalFee = decBaseFee * intMonths
        
        self._label8.Text = str(round(decBaseFee, 2))
        self._label9.Text = str(round(decTotalFee, 2))