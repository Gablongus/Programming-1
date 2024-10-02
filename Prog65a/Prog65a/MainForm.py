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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self._textBox3 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.RosyBrown
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("NSimSun", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label1.Location = System.Drawing.Point(119, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(189, 72)
        self._label1.TabIndex = 0
        self._label1.Text = "European Dating App!!"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(55, 129)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 1
        self._label2.Text = "Insert Date:"
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.White
        self._textBox1.ForeColor = System.Drawing.Color.Gainsboro
        self._textBox1.Location = System.Drawing.Point(162, 129)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(55, 20)
        self._textBox1.TabIndex = 2
        self._textBox1.Text = "Month"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Mongolian Baiti", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(216, 125)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 3
        self._label3.Text = "/"
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.White
        self._textBox2.ForeColor = System.Drawing.Color.LightGray
        self._textBox2.Location = System.Drawing.Point(236, 128)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(55, 20)
        self._textBox2.TabIndex = 4
        self._textBox2.Text = "Day"
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Mongolian Baiti", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(290, 125)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(27, 23)
        self._label4.TabIndex = 6
        self._label4.Text = "/"
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.White
        self._textBox3.ForeColor = System.Drawing.Color.Silver
        self._textBox3.Location = System.Drawing.Point(313, 128)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(55, 20)
        self._textBox3.TabIndex = 7
        self._textBox3.Text = "Year"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LightSalmon
        self.ClientSize = System.Drawing.Size(432, 435)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog65a"
        self.ResumeLayout(False)
        self.PerformLayout()

    
