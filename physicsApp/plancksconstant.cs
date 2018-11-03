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
    public partial class plancksconstant : Form
    {
        public plancksconstant()
        {
            InitializeComponent();
            if (Control.ModifierKeys == Keys.Escape)
            {
                ActiveForm.Close();
                this.Close();
            }
        }

        public void showVariables()
        {
            lb1.Show();
            lb2.Show();
            txtVariable1.Show();
            txtVariable2.Show();
        }

        private void plancksconstant_Load(object sender, EventArgs e)
        {
            rbFrequency.TabStop = false;
            rbWavelength.TabStop = false;
            rbknownFrequency.TabStop = false;
            rbPhoton.TabStop = false;

            lb1.Hide();
            txtVariable1.Hide();

            lb2.Hide();
            txtVariable2.Hide();

            lbl3.Hide();
            txtVariables3.Hide();
        }

        private void btnEnter_Click(object sender, EventArgs e)
        {
            double result = 0;
            double wavelength = 0;
            double energy = 0;
            double speedLight = 0;
            double planksConstantperSec = 0;
            double frequencyLight = 0;

            if (rbPhoton.Checked)
            {
                try
                {
                    planksConstantperSec = double.Parse(txtVariable1.Text);
                    frequencyLight = double.Parse(txtVariable2.Text);
                }
                catch
                {
                    MessageBox.Show("You did not enter all of the values. The empty variable will be assumed as null.");
                }
                finally
                {
                    result = planksConstantperSec * frequencyLight;
                    lblResult.Text = result.ToString();
                }

            }
            else if (rbknownFrequency.Checked)
            {
                try
                {
                    energy = double.Parse(txtVariable1.Text);
                    frequencyLight = double.Parse(txtVariable2.Text);
                }
                catch
                {
                    MessageBox.Show("You did not enter all of the values. The empty variable will be assumed as null.");
                }
                finally
                {
                    result = energy * frequencyLight;
                    lblResult.Text = result.ToString();
                }

            }
            else if (rbFrequency.Checked)
            {
                try
                {
                    speedLight = double.Parse(txtVariable1.Text);
                    wavelength = double.Parse(txtVariable2.Text);
                }
                catch
                {
                    MessageBox.Show("You did not enter all of the values. The empty variable will be assumed as null.");
                }
                finally
                {
                    result = speedLight * wavelength;
                    lblResult.Text = result.ToString();
                }
            }
            else if (rbWavelength.Checked)
            {
                try
                {
                    energy = double.Parse(txtVariable1.Text);
                    wavelength = double.Parse(txtVariable2.Text);
                    speedLight = double.Parse(txtVariables3.Text);
                }
                catch
                {
                    MessageBox.Show("You did not enter all of the values. The empty variable will be assumed as null.");
                }
                finally
                {
                    result = (energy * (wavelength / speedLight));
                    lblResult.Text = result.ToString();
                }
            }
            else
            {
                MessageBox.Show("Click on a radio button to execute the equation of your choice.", "Planck's Constant");
            }
        }

        private void rbPhoton_CheckedChanged(object sender, EventArgs e)
        {
            if (sender is RadioButton)
            {
                RadioButton radioButton = (RadioButton)sender;
                if (radioButton.Checked)
                {
                    lb1.Text = "Planck's constant per second:";
                    lb2.Text = "frequency of light in hertz:";
                    txtVariables3.Hide();
                }
                showVariables();
            }
        }

        private void rbFrequency_CheckedChanged(object sender, EventArgs e)
        {
            if (sender is RadioButton)
            {
                RadioButton radioButton = (RadioButton)sender;
                if (radioButton.Checked)
                {
                    lb1.Text = "Speed of light:";
                    lb2.Text = "Wavelength in meters:";
                    txtVariables3.Hide();
                }
                showVariables();
            }
        }

        private void rbWavelength_CheckedChanged(object sender, EventArgs e)
        {
            if (sender is RadioButton)
            {
                RadioButton radioButton = (RadioButton)sender;
                if (radioButton.Checked)
                {
                    lb1.Text = "Energy of the light photon:";
                    lb2.Text = "Wavelength of light in meters:";
                    lbl3.Text = "Speed of light:";
                    txtVariables3.Show();
                    lbl3.Show();
                }
                showVariables();
            }
        }

        private void rbknownFrequency_CheckedChanged(object sender, EventArgs e)
        {
            if (sender is RadioButton)
            {
                RadioButton radioButton = (RadioButton)sender;
                if (radioButton.Checked)
                {
                    lb1.Text = "Energy of light photon:";
                    lb2.Text = "Frequency of light in hertz:";
                }
                showVariables();
            }
        }

        private void btnBack_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void btnClear_Click(object sender, EventArgs e)
        {
            txtVariable1.Clear();
            txtVariable2.Clear();
            txtVariables3.Clear();

            lblResult.Text = "";

            rbFrequency.TabStop = false;
            rbWavelength.TabStop = false;
            rbknownFrequency.TabStop = false;
            rbPhoton.TabStop = false;

            lb1.Hide();
            txtVariable1.Hide();

            lb2.Hide();
            txtVariable2.Hide();

            lbl3.Hide();
            txtVariables3.Hide();
        }
    }
}
