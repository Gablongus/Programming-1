import System.Drawing
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
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.FormattingEnabled = True
        self._listBox1.Location = System.Drawing.Point(12, 12)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(228, 420)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.MediumOrchid
        self._button1.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button1.Location = System.Drawing.Point(267, 116)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(207, 94)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.MediumOrchid
        self._button2.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button2.Location = System.Drawing.Point(267, 227)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(207, 94)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.MediumOrchid
        self._button3.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button3.Location = System.Drawing.Point(267, 338)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(207, 94)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Thistle
        self._label1.Font = System.Drawing.Font("Microsoft YaHei UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(267, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(207, 43)
        self._label1.TabIndex = 4
        self._label1.Text = "Sum of Numbers:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Font = System.Drawing.Font("Microsoft YaHei UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(267, 56)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(207, 43)
        self._label2.TabIndex = 5
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Purple
        self.ClientSize = System.Drawing.Size(500, 442)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "Prog152a"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        mnum = 1
        linenum = 3
        total = 0
        
        while (linenum)<9669:
            linenum = mnum*3
            mnum = mnum + 1
            line = str(linenum) + " +" 
            self._listBox1.Items.Add(line)
            total = total + linenum
        
        self._label2.Text = str(total)

    def Button2Click(self, sender, e):
        self._listBox1.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()