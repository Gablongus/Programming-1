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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label5 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label1.Font = System.Drawing.Font("Microsoft Yi Baiti", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(22, 18)
        self._label1.Name = "label1"
        self._label1.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label1.Size = System.Drawing.Size(211, 133)
        self._label1.TabIndex = 0
        self._label1.Text = "Quantity Sold:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label2.Font = System.Drawing.Font("Microsoft Yi Baiti", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(34, 52)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(78, 23)
        self._label2.TabIndex = 2
        self._label2.Text = "Package A:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label3.Font = System.Drawing.Font("Microsoft Yi Baiti", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(34, 84)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(78, 23)
        self._label3.TabIndex = 3
        self._label3.Text = "Package B:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label4.Font = System.Drawing.Font("Microsoft Yi Baiti", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(34, 110)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(78, 23)
        self._label4.TabIndex = 4
        self._label4.Text = "Package C:"
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(119, 52)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 20)
        self._textBox1.TabIndex = 5
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(119, 81)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 20)
        self._textBox2.TabIndex = 6
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(119, 110)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(100, 20)
        self._textBox3.TabIndex = 7
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._button1.Font = System.Drawing.Font("Microsoft Yi Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(22, 155)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(211, 48)
        self._button1.TabIndex = 8
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._button2.Font = System.Drawing.Font("Microsoft Yi Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(22, 209)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(109, 48)
        self._button2.TabIndex = 9
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._button3.Font = System.Drawing.Font("Microsoft Yi Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(137, 209)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(96, 48)
        self._button3.TabIndex = 10
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label5.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label5.Font = System.Drawing.Font("Microsoft Yi Baiti", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(240, 18)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(177, 239)
        self._label5.TabIndex = 11
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(429, 274)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg 269 Sales"
        self.ResumeLayout(False)
        self.PerformLayout()


    

    def Button1Click(self, sender, e):
        #Todo: All of this
        Aamount = int(self._textBox1.Text)
        Bamount = int(self._textBox2.Text)
        Camount = int(self._textBox3.Text)
        
        Adiscount = 0
        Bdiscount = 0
        Cdiscount = 0
        
        Aprice = 0
        Bprice = 0
        Cprice = 0
        
        if Aamount >= 10 and Aamount <= 19:
            Adiscount = 0.20
        elif Aamount >= 20 and Aamount <= 49:
            Adiscount = 0.30
        elif Aamount >= 50 and Aamount <= 99:
            Adiscount = 0.40
        elif Aamount >= 100:
            Adiscount = 0.50
            
        if Bamount >= 10 and Bamount <= 19:
            Bdiscount = 0.20
        elif Bamount >= 20 and Bamount <= 49:
            Bdiscount = 0.30
        elif Bamount >= 50 and Bamount <= 99:
            Bdiscount = 0.40
        elif Bamount >= 100:
            Bdiscount = 0.50
        
        if Camount >= 10 and Camount <= 19:
            Cdiscount = 0.20
        elif Camount >= 20 and Camount <= 49:
            Cdiscount = 0.30
        elif Camount >= 50 and Camount <= 99:
            Cdiscount = 0.40
        elif Camount >= 100:
            Cdiscount = 0.50
            
        Aprice = (Aamount * 99) - ((Aamount * 99)*Adiscount)
        Bprice = (Bamount * 199) - ((Bamount * 199)*Bdiscount)
        Cprice = (Camount * 299) - ((Camount * 299)*Cdiscount)
            
        
        
        
        self._label5.Text += ("Package A: $" + str(Aprice))
        self._label5.Text += ("\nPackage B: $" + str(Bprice))
        self._label5.Text += ("\nPackage C: $" + str(Cprice))
        self._label5.Text += ("\nGrand Total: $" + str(Aprice + Bprice + Cprice))
        
        
        
        

    def Button2Click(self, sender, e):
        self._label5.Text = ""
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()