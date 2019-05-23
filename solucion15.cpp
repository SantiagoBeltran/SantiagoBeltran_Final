#include <iostream>
#include <fstream>
using namespace std;

const float m=7294.29;
const float q=2;

void leapfrog(float t_o, float t_f, float delta_t, string filename);
float* Electric(float t);
float* dzdt(float t);

int main(){
  leapfrog(0.0, 10.0,0.1 , "datos.dat");
  return 0;
}

float* Electric(float t){
    float *E;
    E= new float[2];
    if (t<3){E[0]=0.0;E[1]=0.0;}
    else if (t>=3 && t<=7){E[0]=0.0;E[1]=3.0;}
    else if (t>7){E[0]=0.0;E[1]=0.0;}
    return E;
}

float* dzdt(float t){
 
    float *pendiente;
    pendiente =new float[2];
    pendiente[0]=q*Electric(t)[0]/m;
    pendiente[1]=q*Electric(t)[1]/m;
    return pendiente;
}

void leapfrog(float t_o, float t_f, float delta_t, string filename){
  float t=t_o;
  float *pos;
  float *vel;
  pos = new float[2];
  vel = new float[2];    
  pos[0]=1.0;
  pos[1]=0.0;
  vel[0]=0.0;
  vel[1]=1.0;  
  ofstream outfile;
  outfile.open(filename);
  while(t<t_f){    
    outfile << t << " " << pos[0] << " " << pos[1] << endl;
    pos[0] = pos[0] + 0.5 * delta_t * vel[0];
    pos[1] = pos[1] + 0.5 * delta_t * vel[1];
    vel[0] = vel[0] + delta_t* dzdt(t)[0];
    vel[1] = vel[1] + delta_t* dzdt(t)[1];
    pos[0] = pos[0] + 0.5 * delta_t * vel[0];
    pos[1] = pos[1] + 0.5 * delta_t * vel[1];
    t =t +delta_t;
  }
  outfile.close();
}
