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
        self._label4 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._textBox5 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Mongolian Baiti", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(70, 9)
        self._label1.Name = "label1"
        self._label1.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label1.Size = System.Drawing.Size(279, 46)
        self._label1.TabIndex = 0
        self._label1.Text = "Glorgus Hotel"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label2.Font = System.Drawing.Font("Microsoft YaHei Light", 9, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(28, 95)
        self._label2.Name = "label2"
        self._label2.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label2.Size = System.Drawing.Size(164, 104)
        self._label2.TabIndex = 1
        self._label2.Text = "Room Information"
        # 
        # label3
        # 
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label3.Font = System.Drawing.Font("Microsoft YaHei Light", 9, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(231, 95)
        self._label3.Name = "label3"
        self._label3.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label3.Size = System.Drawing.Size(168, 104)
        self._label3.TabIndex = 2
        self._label3.Text = "Additional Charges"
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Mongolian Baiti", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(31, 149)
        self._label5.Name = "label5"
        self._label5.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label5.Size = System.Drawing.Size(97, 16)
        self._label5.TabIndex = 4
        self._label5.Text = "Nightly Charge:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Mongolian Baiti", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(248, 122)
        self._label6.Name = "label6"
        self._label6.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label6.Size = System.Drawing.Size(89, 16)
        self._label6.TabIndex = 5
        self._label6.Text = "Room Service:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("Mongolian Baiti", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(261, 149)
        self._label7.Name = "label7"
        self._label7.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label7.Size = System.Drawing.Size(76, 16)
        self._label7.TabIndex = 6
        self._label7.Text = "Telephone:"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label8
        # 
        self._label8.Font = System.Drawing.Font("Mongolian Baiti", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(279, 174)
        self._label8.Name = "label8"
        self._label8.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label8.Size = System.Drawing.Size(58, 16)
        self._label8.TabIndex = 7
        self._label8.Text = "Misc:"
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label9
        # 
        self._label9.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label9.Font = System.Drawing.Font("Microsoft YaHei UI", 9.75, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(28, 215)
        self._label9.Name = "label9"
        self._label9.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label9.Size = System.Drawing.Size(371, 193)
        self._label9.TabIndex = 8
        self._label9.Text = "Total Charges"
        # 
        # label10
        # 
        self._label10.Font = System.Drawing.Font("Mongolian Baiti", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(107, 241)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(135, 23)
        self._label10.TabIndex = 9
        self._label10.Text = "Room Charges:"
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label11
        # 
        self._label11.Font = System.Drawing.Font("Mongolian Baiti", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(107, 273)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(135, 23)
        self._label11.TabIndex = 10
        self._label11.Text = "Additional Charges:"
        self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label12
        # 
        self._label12.Font = System.Drawing.Font("Mongolian Baiti", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(108, 305)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(135, 23)
        self._label12.TabIndex = 11
        self._label12.Text = "Subtotal:"
        self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label13
        # 
        self._label13.Font = System.Drawing.Font("Mongolian Baiti", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(107, 338)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(135, 23)
        self._label13.TabIndex = 12
        self._label13.Text = "Tax:"
        self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label14
        # 
        self._label14.Font = System.Drawing.Font("Mongolian Baiti", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label14.Location = System.Drawing.Point(107, 371)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(135, 23)
        self._label14.TabIndex = 13
        self._label14.Text = "Total Charges:"
        self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label15
        # 
        self._label15.BackColor = System.Drawing.Color.White
        self._label15.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label15.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label15.Location = System.Drawing.Point(248, 241)
        self._label15.Name = "label15"
        self._label15.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label15.Size = System.Drawing.Size(100, 23)
        self._label15.TabIndex = 14
        self._label15.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label16
        # 
        self._label16.BackColor = System.Drawing.Color.White
        self._label16.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label16.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label16.Location = System.Drawing.Point(248, 273)
        self._label16.Name = "label16"
        self._label16.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label16.Size = System.Drawing.Size(100, 23)
        self._label16.TabIndex = 15
        self._label16.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label17
        # 
        self._label17.BackColor = System.Drawing.Color.White
        self._label17.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label17.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label17.Location = System.Drawing.Point(249, 305)
        self._label17.Name = "label17"
        self._label17.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label17.Size = System.Drawing.Size(100, 23)
        self._label17.TabIndex = 16
        self._label17.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label18
        # 
        self._label18.BackColor = System.Drawing.Color.White
        self._label18.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label18.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label18.Location = System.Drawing.Point(248, 338)
        self._label18.Name = "label18"
        self._label18.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label18.Size = System.Drawing.Size(100, 23)
        self._label18.TabIndex = 17
        self._label18.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label19
        # 
        self._label19.BackColor = System.Drawing.Color.White
        self._label19.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label19.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label19.Location = System.Drawing.Point(248, 371)
        self._label19.Name = "label19"
        self._label19.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label19.Size = System.Drawing.Size(100, 23)
        self._label19.TabIndex = 18
        self._label19.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Mongolian Baiti", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(39, 122)
        self._label4.Name = "label4"
        self._label4.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label4.Size = System.Drawing.Size(58, 16)
        self._label4.TabIndex = 19
        self._label4.Text = "Nights:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Azure
        self._button1.Font = System.Drawing.Font("Baskerville Old Face", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(28, 422)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(112, 39)
        self._button1.TabIndex = 20
        self._button1.Text = "Calculate Charges"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(103, 120)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(78, 22)
        self._textBox1.TabIndex = 23
        self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Azure
        self._button2.Font = System.Drawing.Font("Baskerville Old Face", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(157, 422)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(112, 39)
        self._button2.TabIndex = 24
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Azure
        self._button3.Font = System.Drawing.Font("Baskerville Old Face", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(287, 422)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(112, 39)
        self._button3.TabIndex = 25
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(134, 149)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(47, 22)
        self._textBox2.TabIndex = 26
        self._textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft YaHei", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(339, 119)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(51, 22)
        self._textBox3.TabIndex = 27
        self._textBox3.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # textBox4
        # 
        self._textBox4.Font = System.Drawing.Font("Microsoft YaHei", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.Location = System.Drawing.Point(339, 146)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(51, 22)
        self._textBox4.TabIndex = 28
        self._textBox4.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # textBox5
        # 
        self._textBox5.Font = System.Drawing.Font("Microsoft YaHei", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox5.Location = System.Drawing.Point(339, 172)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(51, 22)
        self._textBox5.TabIndex = 29
        self._textBox5.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LightCyan
        self.ClientSize = System.Drawing.Size(427, 469)
        self.Controls.Add(self._textBox5)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
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
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.RightToLeft = System.Windows.Forms.RightToLeft.No
        self.Text = "Pg 162 Room Charge"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    def MainFormLoad(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        decRoomCharges = 0.0
        decAddCharges = 0.0
        decSubTotal = 0.0
        decTax = 0.0
        decTotal = 0.0
        decTAX_RATE = 0.08
        
        try:
            decAddCharges = float(self._textBox3.Text) + \
                float(self._textBox4.Text) + \
                float(self._textBox5.Text0
            self._lblAddCharges.Text = str(round(decAddCharges, 2))
        except:
            MessageBox.Show("Room service, Telephone, and Misc. must be numbers", "Error")

    def Button2Click(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        pass