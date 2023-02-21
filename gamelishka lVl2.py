from play import*
#0 это границы 1 пустатаааа 2 розовая квака 3 финиш +_+
level='''
111111111111
100100000021
101000000001
100000000001
100001000001
101000000001
100000100001
100010000001
100000010011
110000000001
100031000001
111111111111
'''
class Lalka():
    def __init__(self,color,x,y,width,height,border_color,border_width,transperency,rank):
        self.color=color
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.border_color=border_color
        self.border_width=border_width
        self.transperency=transperency
        self.rank=rank
        self.box=new_box(self.color,self.x,self.y,self.width,self.height,self.border_color,self.border_width,0,self.transperency)
    def update(self):
        self.box.x=self.x
        self.box.y=self.y
    def muvright(self,empty):
        if self.x+int(1000/12)==empty.x and self.y==empty.y:  
            self.x+=int(1000/12)
            empty.x-=int(1000/12)
    def muvleft(self,empty):
        if self.x-int(1000/12)==empty.x and self.y==empty.y:  
            self.x-=int(1000/12)
            empty.x+=int(1000/12)
    def muvdown(self,empty):
        if self.y-int(1000/12)==empty.y and self.x==empty.x and empty.rank=='pustataa':  
            self.y-=int(1000/12)
            empty.y+=int(1000/12)
    def muvup(self,empty):
        if self.y+int(1000/12)==empty.y and self.x==empty.x:  
            self.y+=int(1000/12)
            empty.y-=int(1000/12)
set_backdrop((168,83,157))
xx=-500
yy=535
granizz=list()
pustataa=list()
wh=int(1000/12)
for i in level:
    if i == '0':
        b1=Lalka((210,179,206),xx,yy,wh,wh,(168,83,157),0,100,'pustataa')
        pustataa.append(b1)
    elif i=='1':
        b1=Lalka((249,249,249),xx,yy,wh,wh,(210,179,206),3,100,'granizz')
        granizz.append(b1)
    elif i=='2':
        plueer=Lalka((168,83,157),xx,yy,wh,wh,(222,28,170),6,100,'plueer')
    elif i=='3':
        b1=Lalka((210,179,206),xx,yy,wh,wh,(168,83,157),0,100,'pustataa')
        pustataa.append(b1)
        vanish=Lalka((125,125,125),xx,yy,wh,wh,'black',0,35,'vanish')
    elif i =='\n':
        yy-=wh
        xx=-500
    xx+=wh
@repeat_forever
def game():
    if vanish.x==plueer.x and vanish.y==plueer.y:
        new_text('люлюлюлюлюлюлюлю,ты...... прошел уроввень')
    if key_is_pressed('s'):
        for luli in range(12):  
            for i in pustataa:
                plueer.muvdown(i)
                i.update()
                plueer.update()
    if key_is_pressed('a'):
        for luli in range(12):
            for i in pustataa:
                plueer.muvleft(i)
                i.update()
                plueer.update()
    if key_is_pressed('w'):
        for luli in range(12):
            for i in pustataa:
                plueer.muvup(i)
                i.update()
                plueer.update()
    if key_is_pressed('d'):
        for luli in range(12):
            for i in pustataa:
                plueer.muvright(i)
                i.update()
                plueer.update()         
start_program()
#238,187,224
