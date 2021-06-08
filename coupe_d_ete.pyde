from export import mousePressed

# Sketch settings saved in the .txt file
# The next commented line should not be removed 
# parameters

# Canvas size and background color
w = 800
h = 1000
bg = "#FFFFFF"
# Total number of hair on canvas
density = (w+h)*25
# Breakpoints for different zones
zones = [4, 2.3, 1.66, 1.25, 0.9]
# Hair length for each zone
lens = [28, 14, 8, 4, 1, 0.2]
# picture framing
framing = True
frame_size = 80

## End of saved parameters, this line should not be removed



class Hair(object):
    
    def __init__(self,x,y):
        self.pos = PVector(x,y)
        self.l = PVector(self.pos.x-2, self.pos.y+60)
        
        # This variable defines the shape of the different zones
        func = sin((x+width/0.9)*PI*1/height)/3+HALF_PI/1.6
        
        if self.pos.y < height/zones[0]*func:
            stroke(int(random(30)))
            self.l.setMag(lens[0])
        elif self.pos.y < height/zones[1]*func:
            stroke(int(random(60)))
            self.l.setMag(lens[1])
        elif self.pos.y < height/zones[2]*func:
            stroke(int(random(100)))
            self.l.setMag(lens[2])
        elif self.pos.y < height/zones[3]*func:
            stroke(int(random(50,150)))
            self.l.setMag(lens[3])
        elif self.pos.y < height/zones[4]*func:
            stroke(int(random(80,255)))
            self.l.setMag(lens[4])
        else:
            stroke(random(180,255))
            self.l.setMag(lens[5])
    
    def show(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        rotate(noise(self.pos.x)*self.l.heading()/2)
        line(0, 0, 0, self.l.mag())
        popMatrix()


def setup():
    size(w,h)
    background(bg)
    noLoop()
    noFill()
    

def draw():
    for i in range(density):
        x = random(80,width-80)
        y = random(80,height-80)
        h = Hair(x,y)
        h.show()
        
    # outer frame
    if framing:    
        fill(bg)
        noStroke()
        rect(0,0,width,frame_size)
        rect(0,height-frame_size,width,frame_size)
        rect(0,0,frame_size,height)
        rect(width-frame_size,0,frame_size,height)
