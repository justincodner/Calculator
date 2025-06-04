import tkinter as tk

def graph(f,xmin,xmax,ymin,ymax):
    window = tk.Tk()
    
    window.geometry('400x400')
    window.title('Graph')
    canvas = tk.Canvas(window,width = 400, height =400, bg = 'white')
    canvas.pack()
    
    xScale = 400/(xmax-xmin)
    yScale = 400/(ymax-ymin)
    
    def scaleX(x):
        return (x-xmin)*xScale
    
    def scaleY(y):
        return 400-(y-ymin) * yScale
    
    if xmin <= 0 and xmax >=0:
        canvas.create_line(scaleX(0),0,scaleX(0),400, fill = 'black')    
    if ymin <=0 and ymax >=0:
        canvas.create_line(0, scaleY(0), 400, scaleY(0), fill = 'black')
    
    step = (xmax - xmin) /800
    for i in range(800):
        x1 = xmin + i*step
        x2 = x1 + step
        try:
            y1 = f(x1)
            y2 = f(x2)
            canvas.create_line(scaleX(x1), scaleY(y1), scaleX(x2), scaleY(y2), fill = 'blue')
        except:
            pass #have to check div by 0 errors or other errors
    window.mainloop()
def graphMulti(fList, xmin, xmax, ymin, ymax):
    window = tk.Tk()
    
    window.geometry('400x400')
    window.title('Graph')
    canvas = tk.Canvas(window,width = 400, height =400, bg = 'white')
    canvas.pack()
    
    xScale = 400/(xmax-xmin)
    yScale = 400/(ymax-ymin)
    
    def scaleX(x):
        return (x-xmin)*xScale
    
    def scaleY(y):
        return 400-(y-ymin) * yScale
    
    if xmin <= 0 and xmax >=0:
        canvas.create_line(scaleX(0),0,scaleX(0),400, fill = 'black')    
    if ymin <=0 and ymax >=0:
        canvas.create_line(0, scaleY(0), 400, scaleY(0), fill = 'black')
    
    step = (xmax - xmin) /800
    for i in range(800):
        x1 = xmin + i*step
        x2 = x1 + step
        for f in fList:
            try:
                y1 = f(x1)
                y2 = f(x2)
                canvas.create_line(scaleX(x1), scaleY(y1), scaleX(x2), scaleY(y2), fill = 'blue')
            except:
                pass #have to check div by 0 errors or other errors
    window.mainloop() 
