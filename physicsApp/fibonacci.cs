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
    public partial class fibonacci : Form
    {
        public fibonacci()
        {
            InitializeComponent();
        }

        private void btnEnter_Click(object sender, EventArgs e)
        {
            double result = 0;
            double n = double.Parse(txtFib.Text);
            double phiPositive = 1.6180339 * n;
            double phiNegative = 1.6180339 * -n;
            result = (phiPositive - phiNegative) / 2.2360679775;
            lblResult.Text = result.ToString();
        }

        private void btnBack_Click(object sender, EventArgs e)
        {
            main goBack = new main();
            goBack.Show();
            this.Close();
        }

        private void btnClear_Click(object sender, EventArgs e)
        {
            lblResult.Text = "";
            txtFib.Clear();
        }

        private void fibonacci_Load(object sender, EventArgs e)
        {

        }
    }
}
