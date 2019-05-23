#include<iostream>
#include<fstream>
using namespace std;

double m= 7294.29;
double q=2.0;
double g=9.8;
double velocidad(double t, double x, double y);
double aceleracion(double t, double x, double y);
double runge_kuta(double *t,double *x,  double *y);

double velocidad(double t, double x, double y)
{
    return x;
}
double aceleracion(double t, double x, double y)
{
    return -g;
}

double runge_kutta(double *t,double *x,  double *y)
{
    
    double t_in, x_in, y_in;
    double h=0.01;
    double k1x,k2x,k3x,k4x, k1y,k2y,k3y,k4y ;
    t_in=*t;
    x_in=*x;
    y_in=*y;
        
    k1x = velocidad(t_in,x_in, y_in);
    k1y = aceleracion(t_in, x_in, y_in);
    k2x =  velocidad(t_in + h/2, x_in + k1x* h/2, y_in + k1y* h/2);
    k2y = aceleracion(t_in+ h/2, x_in + k1x* h/2, y_in + k2y* h/2);
    k3x = velocidad(t_in + h/2, x_in + k2x * h/2, y_in + k2y * h/2);
    k3y= aceleracion(t_in + h/2, x_in + k2x * h/2, y_in + k2y * h/2);
    k4x= velocidad(t_in + h, x_in + k3x * h, y_in + k3y * h);
    k4y= aceleracion (t_in+h/2, x_in + k3x*h/2, y_in + k3y*h/2);
    
    
    
     t_in = t_in + h;
     x_in = x_in + h * (k1x + 2*k2x + 2*k3x + k4x)/6.0;
     y_in = y_in + h * (k1y + 2*k2y + 2*k3y + k4y)/6.0;
    
    *t=t_in;
    *x=x_in;
    *y=y_in;
    
}


int main()
{
   double t=0.0;
   double x=1.0;
   double y=0.0;
   double vx = 1.0;
   double vy = 0.0;
   double delta_t;
    ofstream myfile;
    myfile.open("punto15.dat");
    while(t<7)
    {
        myfile<<t<<" " <<x << " " << y<<endl;
        runge_kutta(&t, &x, &y);
    }
    myfile.close();
    return 0;
    
}