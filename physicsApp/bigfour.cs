using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Mathematics
{
    public partial class bigfour : Form
    {

        public bigfour()
        {
            InitializeComponent();
            if (Control.ModifierKeys == Keys.Escape)
            {
               ActiveForm.Close();
                this.Close();
            }
        }

        private void radioButton4_CheckedChanged(object sender, EventArgs e)
        {

            if (sender is RadioButton)
            {
                RadioButton radioButton = (RadioButton)sender;
                if (radioButton.Checked)
                {
                    lb1.Text = "Enter the inital velocity of the object in m/s:";
                    lb2.Text = "Enter the time in seconds:";
                    lbl3.Text = "Enter the acceleration in m/s^2:";
                }
                showVariables();
            }
        }

        private void bigfour_Load(object sender, EventArgs e)
        {

            rbDisplacementwithAcc.TabStop = false;
            rbDisplacementwithout.TabStop = false;
            rbFinalVelocity.TabStop = false;
            rbFinalVelocitySquared.TabStop = false;

            lb1.Hide();
            txtVariable1.Hide();

            lb2.Hide();
            txtVariable2.Hide();

            lbl3.Hide();
            txtVariables3.Hide();
        }

        private void btnBack_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        public void showVariables()
        {
            lb1.Show();
            lb2.Show();
            lbl3.Show();
            txtVariable1.Show();
            txtVariable2.Show();
            txtVariables3.Show();
        }

        public void rbDisplacementwithAcc_CheckedChanged(object sender, EventArgs e)
        {
            if (sender is RadioButton)
            {
                RadioButton radioButton = (RadioButton)sender;
                if (radioButton.Checked)
                {
                    lb1.Text = "Enter the inital velocity of the object in m/s:";
                    lb2.Text = "Enter the time in seconds:";
                    lbl3.Text = "Enter the acceleration in m/s^2:";
                }
                showVariables();
            }
        }

        public void rbDisplacementwithout_CheckedChanged(object sender, EventArgs e)
        {
            if (sender is RadioButton)
            {
                RadioButton radioButton = (RadioButton)sender;
                if (radioButton.Checked)
                {
                    lb1.Text = "Enter the inital velocity of the object in m/s:";
                    lb2.Text = "Enter the time in seconds:";
                    lbl3.Text = "Enter the final velocity of the object in m/s:";
                }
                showVariables();
            }
        }

        public void rbFinalVelocitySquared_CheckedChanged(object sender, EventArgs e)
        {
            if (sender is RadioButton)
            {
                RadioButton radioButton = (RadioButton)sender;
                if (radioButton.Checked)
                {
                    lb1.Text = "Enter the acceleration in m/s^2:";
                    lb2.Text = "Enter the inital velocity of the object in m/s:";
                    lbl3.Text = "Enter the displacement in m:";
                }
                showVariables();
            }
        }

        private void btnClear_Click(object sender, EventArgs e)
        {
            lb1.Hide();
            lb2.Hide();
            lbl3.Hide();
            txtVariable1.Clear();
            txtVariable2.Clear();
            txtVariables3.Clear();
            txtVariable1.Hide();
            txtVariable2.Hide();
            txtVariables3.Hide();
            lblResult.Text = "";
            rbDisplacementwithAcc.TabStop = false;
            rbDisplacementwithout.TabStop = false;
            rbFinalVelocity.TabStop = false;
            rbFinalVelocitySquared.TabStop = false;

        }

        private void btnEnter_Click(object sender, EventArgs e)
        {
            double result = 0;
            double initialVelocity = 0;
            double time = 0;
            double acceleration = 0;
            double finalVelocity = 0;
            double displacement = 0;

            if (rbDisplacementwithAcc.Checked)
            {
                try
                {
                    initialVelocity = double.Parse(txtVariable1.Text);
                    time = double.Parse(txtVariable2.Text);
                    acceleration = double.Parse(txtVariables3.Text);
                }
                catch
                {
                    MessageBox.Show("You did not enter all of the values. The empty variable will be assumed as null.");
                }
                finally
                {
                    result = (initialVelocity * time + 0.5 * acceleration * time);
                    lblResult.Text = result.ToString();
                }

            }
            else if (rbDisplacementwithout.Checked)
            {
                try
                {
                    initialVelocity = double.Parse(txtVariable1.Text);
                    time = double.Parse(txtVariable2.Text);
                    finalVelocity = double.Parse(txtVariables3.Text);
                }
                finally
                {
                    result = (initialVelocity * (finalVelocity / 2)) * time;
                    lblResult.Text = result.ToString();
                }

            }
            else if (rbFinalVelocity.Checked)
            {
                try
                {
                    initialVelocity = double.Parse(txtVariable1.Text);
                    time = double.Parse(txtVariable2.Text);
                    acceleration = double.Parse(txtVariables3.Text);
                }
                finally
                {
                    result = initialVelocity + time * acceleration;
                    lblResult.Text = result.ToString();
                }
            }
            else if (rbFinalVelocitySquared.Checked)
            {
                try
                {
                    acceleration = double.Parse(txtVariable1.Text);
                    initialVelocity = double.Parse(txtVariable2.Text);
                    displacement = double.Parse(txtVariables3.Text);
                }
                finally
                {
                    result = initialVelocity + (2 * acceleration * displacement);
                    lblResult.Text = result.ToString();
                }
            }
            else
            {
                MessageBox.Show("Click on a radio button to execute the equation of your choice.", "The Big Four - Kinematic Equations");
            }
        }
    }
}
