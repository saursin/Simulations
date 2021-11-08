/*  
   Calculating MandelBrot Set
*/
int maxitr = 500;
int inf = 10;

// Coordinates of centre of canvas
float cx, cy;

float range = 2.0;

void setup()
{
  // Setup simulation window
  size(600, 600);
  cx = width/2;
  cy = height/2;
  
  background(255);    
  stroke(0);
  strokeWeight(2);
  
  float x, y;
  for(x=0; x<width; x++)
  {
    for(y=0; y<height; y++)
    {
      float Z_re = map(x, 0, width, -range, range);
      float Z_im = map(y, 0, height, -range, range);
      
      float ca = Z_re;
      float cb = Z_im;
      
      int i = 0;
      while(i<maxitr)
      {
        float Z1_re = Z_re * Z_re - Z_im * Z_im;
        float Z1_im = 2 * Z_re * Z_im;
        
        Z_re = Z1_re + ca;
        Z_im = Z1_im + cb;
        
        if(abs(Z_re + Z_im) > inf)
        {
          break;
        }
        
        i++;
      }
      
      stroke(map(i, 0, maxitr, 255, 0));
      strokeWeight(1);
      point(x, y);     
    }
  }
}

void draw(){}
