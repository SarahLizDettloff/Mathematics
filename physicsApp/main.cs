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
    public partial class main : Form
    {
        public main()
        {
            InitializeComponent();
        }

        private void btnBigFour_Click(object sender, EventArgs e)
        {
            bigfour bigFour = new bigfour();
            bigFour.Show();
            this.Hide();
        }

        private void btnFibonacci_Click(object sender, EventArgs e)
        {
            fibonacci fibonacci = new fibonacci();
            fibonacci.Show();
            this.Hide();
        }

        private void btnBuoyancy_Click(object sender, EventArgs e)
        {
            buoyancy buoyancy = new buoyancy();
            buoyancy.Show();
            this.Hide();
        }

        private void btnPlanck_Click(object sender, EventArgs e)
        {
            plancksconstant planck = new plancksconstant();
            planck.Show();
            this.Hide();
        }

        private void btnFrustumVolume_Click(object sender, EventArgs e)
        {
            frustumVolume frustum = new frustumVolume();
            frustum.Show();
            this.Hide();
        }

        private void main_Load(object sender, EventArgs e)
        {

        }

        private void btnAbout_Click(object sender, EventArgs e)
        {
            about about = new about();
            about.Show();
            this.Hide();
        }
    }
}
