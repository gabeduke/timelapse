*Obsolete python script for RAW Deflickering*

    from __future__ import division
    import os
    import glob
    import sys, re, time, datetime, subprocess, shlex, getopt, fnmatch
    from math import *
    from pylab import *
    import Tkinter
    import ttk
    import tkMessageBox
    from PIL import Image, ImageTk
    
    # RAW deflickering script
    # Copyright (2012) a1ex. License: GPL.
    def progress(x, interval=1):
        global _progress_first_time, _progress_last_time, _progress_message, _progress_interval
    
        try:
            p = float(x)
            init = False
        except:
            init = True
    
        if init:
            _progress_message = x
            _progress_last_time = time.time()
            _progress_first_time = time.time()
            _progress_interval = interval
        elif x:
            if time.time() - _progress_last_time > _progress_interval:
                print >> sys.stderr, "%s [%d%% done, ETA %s]..." % (_progress_message, int(100*p), datetime.timedelta(seconds = round((1-p)/p*(time.time()-_progress_first_time))))
                _progress_last_time = time.time()
    
    def change_ext(file, newext):
        if newext and (not newext.startswith(".")):
            newext = "." + newext
        return os.path.splitext(file)[0] + newext
    
    def get_median(file):
        cmd1 = "dcraw -c -D -4 -o 0 '%s'" % file
        cmd2 = "convert - -type Grayscale -scale 500x500 -format %c histogram:info:-"
        print cmd1, "|", cmd2
        p1 = subprocess.Popen(shlex.split(cmd1), stdout=subprocess.PIPE)
        p2 = subprocess.Popen(shlex.split(cmd2), stdin=p1.stdout, stdout=subprocess.PIPE)
        lines = p2.communicate()[0].split("\n")
        X = []
        for l in lines[1:]:
            p1 = l.find("(")
            if p1 > 0:
                p2 = l.find(",", p1)
                level = int(l[p1+1:p2])
                count = int(l[:p1-2])
                X += [level]*count
        m = median(X)
        return m
    
    def deflickerRAW(inputfolder, outputfolder):
        ion()
    
        progress("Analyzing RAW exposures...");
        files = sorted(os.listdir(inputfolder))
        i = 0;
        M = [];
        for k,f in enumerate(files):
            m = get_median(os.path.join(inputfolder, f))
            M.append(m);
    
            E = [-log2(m/M[0]) for m in M]
            E = detrend(array(E))
            cla(); stem(range(1,len(E)+1), E);
            xlabel('Image number')
            ylabel('Exposure correction (EV)')
            title(f)
            draw();
            progress(k / len(files))
    
        if not os.path.exists(outputfolder):
            os.makedirs(outputfolder)
    
        progress("Developing JPG images...");
        i = 0;
        for k,f in enumerate(files):
            ec = 2 + E[k];
            cmd = "ufraw-batch --out-type=jpg --overwrite --clip=film --saturation=2 --exposure=%s '%s' --output='%s/%s'" % (ec, os.path.join(inputfolder, f),outputfolder, change_ext(f, ".jpg"))
            os.system(cmd)
            progress(k / len(files))
    
    #declare variables############
    moving=False
    resize=False
    aspectx=16
    aspecty=9
    rectcenterx=0
    rectcentery=0
    rectsizex=0
    rectsizey=0
    imagesizexpre=0
    imagesizeypre=0
    imagesizex=0
    imagesizey=0
    
    #Events#########################
    #triggers on left click in canvas
    def xy(event):
        global rectcenterx, rectcentery, rectsizex, rectsizey, moving, resize
    
        #if moving or resize:
        moving=False
        resize=False
        #detect rectangle center grab for move
        if event.x>(rectcenterx-int(rectsizex/2)) and event.x<(rectcenterx+int(rectsizex/2)) and event.y<(int(rectcentery+rectsizey/2)) and event.y>(int(rectcentery-rectsizey/2)):
            moving=True
        #detect lower right rectangle corner grabs for resize
        if event.x>(rectcenterx+rectsizex-rectsizex/4) and event.x<(rectcenterx+rectsizex+rectsizex/4) and event.y<(rectcentery+rectsizey+rectsizey/4) and event.y>(rectcentery+rectsizey-rectsizey/4):
            resize=True
    
    #triggers on motion in canvas
    def canvasmotion(event, canvas, rectangle):
        global rectcenterx,rectcentery,rectsizex,rectsizey,moving,imagesizex,imagesizey,resize,aspectx,aspecty,checkboxstate
        if checkboxstate.get():
            if moving:
                if ((event.x+rectsizex<imagesizex) and (event.x-rectsizex>0)):
                    rectcenterx=event.x
                if ((event.y+rectsizey<imagesizey) and (event.y-rectsizey>0)):
                    rectcentery=event.y
            if resize:
                if (event.x<=imagesizex) and (event.x-(2*(event.x-rectcenterx))>=0) and (rectcentery-((event.x-rectcenterx)*aspecty/aspectx))>0 and int((event.x-rectcenterx)*2*imagesizexpre/imagesizex)>=1920:
                    rectsizex=event.x-rectcenterx
                    rectsizey=(rectsizex*aspecty)/aspectx
            drawRect(canvas,rectangle)
    
    def drawRect(canvas, rectangle):
        global rectcenterx,rectcentery,rectsizex,rectsizey,moving,imagesizex,imagesizey,resize,aspectx,aspecty,keyframes,currentframe
        canvas.tag_raise(rectangle)
        canvas.coords(rectangle, rectcenterx-rectsizex, rectcentery-rectsizey, rectcenterx+rectsizex, rectcentery+rectsizey)
        keyframes[currentframe]=[rectsizex,rectsizey,rectcenterx,rectcentery]
    
    def changeFrame(FrameNumSpin, outputfolder, canvas, canvasimage, rectangle,c1):
        global rectcenterx,rectcentery,rectsizex,rectsizey,photo,currentframe,checkboxstate
        currentframe = int(FrameNumSpin.get())
        files = sorted(glob.glob(outputfolder + "/IMG_*.jpg"))
        image = Image.open(files[currentframe-1])
        image.thumbnail((350, 350), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        canvas.delete(canvasimage)
        canvasimage = canvas.create_image(0,0, image=photo, anchor=Tkinter.NW)
        c1.deselect()
        for keyframe in keyframes:
            if keyframe==currentframe:
                c1.select()
                rectsizex=keyframes[currentframe][0]
                rectsizey=keyframes[currentframe][1]
                rectcenterx=keyframes[currentframe][2]
                rectcentery=keyframes[currentframe][3]
                drawRect(canvas, rectangle)
                break
    
    def checkboxClicked(canvas,rectangle,c1):
        global rectcenterx,rectcentery,rectsizex,rectsizey,moving,imagesizex,imagesizey,resize,aspectx,aspecty,imagesizex,imagesizey,imagesizexpre,imagesizeypre, photo, keyframes,currentframe,checkboxstate
        if currentframe == 1:
            c1.select()
        else:
            if checkboxstate.get():
                rectsizex=imagesizex/2
                rectsizey=(rectsizex*9)/16
                rectcenterx=imagesizex/2
                rectcentery=imagesizey/2
                #keyframes[currentframe]=[rectsizex,rectsizey,rectcenterx,rectcentery]
                drawRect(canvas,rectangle)
            else:
                del keyframes[currentframe]
                print "deleted keyframe"
                canvas.tag_lower(rectangle)
    '''
    #graceful exit
    def ask_quit(root):
        if tkMessageBox.askokcancel("Quit", "Do you want to quit now?"):
            root.destroy()
    '''
    
    def initGUI(inputfolder, outputfolder):
        #
        global rectcenterx,rectcentery,rectsizex,rectsizey,moving,imagesizex,imagesizey,resize,aspectx,aspecty,imagesizex,imagesizey,imagesizexpre,imagesizeypre, photo, keyframes,currentframe,checkboxstate
        #Create User Interface
        #
        root = Tkinter.Tk()
        #root.columnconfigure(0, weight=1)
        #root.rowconfigure(0, weight=1)
    
        canvas = Tkinter.Canvas(root)
        files = sorted(glob.glob(outputfolder + "/IMG_*.jpg"))
        #add image to canvas
        image = Image.open(files[0])
        imagesizexpre = image.size[0]
        imagesizeypre = image.size[1]
        image.thumbnail((350, 350), Image.ANTIALIAS)
        imagesizex = image.size[0]
        imagesizey = image.size[1]
    
        #set initial rect size
        rectsizex=imagesizex/2
        rectsizey=(rectsizex*9)/16
        rectcenterx=imagesizex/2
        rectcentery=imagesizey/2
        currentframe=1
        keyframes={1:[rectsizex,rectsizey,rectcenterx,rectcentery]}
    
        photo = ImageTk.PhotoImage(image)
        canvasimage = canvas.create_image(0,0, image=photo, anchor=Tkinter.NW)
        rectangle=canvas.create_rectangle(rectcenterx-rectsizex, rectcentery-rectsizey, rectcenterx+rectsizex, rectcentery+rectsizey, outline="#fb0")
        #generate header button row
        HeaderRow = Tkinter.Frame(root)
        b1 = Tkinter.Button(HeaderRow, text="One")
        b2 = Tkinter.Button(HeaderRow, text="Two")
        checkboxstate=Tkinter.IntVar()
        c1 = Tkinter.Checkbutton(HeaderRow, text="Keyframe", variable=checkboxstate, command=lambda: checkboxClicked(canvas,rectangle,c1))
        headerLabel1 = Tkinter.Label(HeaderRow, text="frame #")
        headerLabel2 = Tkinter.Label(HeaderRow, text="of %d" % len(files))
        FrameNumSpin = Tkinter.Spinbox(HeaderRow, from_=1, to_=len(files), command=lambda: changeFrame(FrameNumSpin, outputfolder,canvas,canvasimage,rectangle,c1))
        b1.pack(side = Tkinter.LEFT)
        b2.pack(side = Tkinter.LEFT)
        c1.pack(side = Tkinter.LEFT)
        headerLabel1.pack(side = Tkinter.LEFT)
        FrameNumSpin.pack(side = Tkinter.LEFT)
        headerLabel2.pack(side = Tkinter.LEFT)
        HeaderRow.grid(column=0, row=0)
        c1.select()
        #create canvas
        canvas.grid(column=0, row=1, sticky=(Tkinter.N, Tkinter.W, Tkinter.E, Tkinter.S))
        canvas.bind("", xy)
        canvas.bind("", lambda event: canvasmotion(event, canvas, rectangle))
        #generate foot button row
        FooterRow = Tkinter.Frame(root)
        footerLabel = Tkinter.Label(FooterRow, text="Useful help tips")
        b3 = Tkinter.Button(FooterRow, text="Three")
        b4 = Tkinter.Button(FooterRow,text="Process!", command=lambda: processTimelapse(imagesizex,imagesizey,imagesizexpre,imagesizeypre,inputfolder,outputfolder))
        footerLabel.pack(side = Tkinter.LEFT)
        b3.pack(side = Tkinter.LEFT)
        b4.pack(side = Tkinter.LEFT)
        FooterRow.grid(column=0, row=3)
    
        #root.protocol("WM_DELETE_WINDOW", ask_quit())
        root.title ("Timelapse")
        #w,h = root.winfo_screenwidth(), root.winfo_screenheight()
        #root.geometry("%dx%d+0+0" % (w,h))
        root.mainloop()
    
    def processTimelapse(imagesizex,imagesizey,imagesizexpre,imagesizeypre,inputfolder,outputfolder):
        global rectcenterx,rectcentery,rectsizex,rectsizey,aspectx,aspecty,keyframes
        #renumberjpeg(inputfolder,outputfolder)
        i=0
        files = sorted(glob.glob(outputfolder + "/IMG_*.jpg"))
        if not os.path.exists(outputfolder+"/resized"):
            os.makedirs(outputfolder+"/resized")
        for onefile in files:
            if fnmatch.fnmatch(onefile, '*.jpg'):
                print "cropping %s" % onefile
                filename=onefile
                image = Image.open(filename)
                for keyframe in sorted(keyframes):
                    if keyframe==i+1:
                        print "equals"
                        rectsizex=keyframes[i+1][0]
                        rectsizey=keyframes[i+1][1]
                        rectcenterx=keyframes[i+1][2]
                        rectcentery=keyframes[i+1][3]
                        interpolatelatch=0
                        rectsizexslice=0
                        rectsizeyslice=0
                        rectcenterxslice=0
                        rectcenteryslice=0
                break
                elif keyframe>(i+1):
                print "greaterthan"
                if interpolatelatch==0:
                    rectsizexslice=(keyframes[keyframe][0]-rectsizex)/(keyframe-(i))
                    rectsizeyslice=(keyframes[keyframe][1]-rectsizey)/(keyframe-(i))
                    rectcenterxslice=(keyframes[keyframe][2]-rectcenterx)/(keyframe-(i))
                    rectcenteryslice=(keyframes[keyframe][3]-rectcentery)/(keyframe-(i))
                    interpolatelatch=1
            rectsizex=rectsizex+rectsizexslice
            rectsizey=rectsizey+rectsizeyslice
            rectcenterx=rectcenterx+rectcenterxslice
            rectcentery=rectcentery+rectcenteryslice
            break
        box = (int((rectcenterx-rectsizex)*imagesizexpre/imagesizex), int((rectcentery-rectsizey)*imagesizeypre/imagesizey), int((rectcenterx+rectsizex)*imagesizexpre/imagesizex), int((rectcentery+rectsizey)*imagesizeypre/imagesizey))
        print box
    area = image.crop(box)
    area = area.resize((1920, 1080), Image.ANTIALIAS)
    area.save(outputfolder+"/resized/%03d.jpg" % i, 'jpeg')
    i=i+1
    cmd = "avconv -i %s/resized/" % outputfolder
    cmd= cmd + "%" + "03d.jpg -r 24 -s hd1080 -vcodec libx264 -crf 16 %s/timelapse.mp4" % outputfolder
    os.system(cmd)
    
    def main(argv):
        # print command line arguments
        inputfolder = ''
        outputfolder = ''
        process = 0
        try:
            opts, args = getopt.getopt(argv,"hi:o:r",["ifolder=","ofolder="])
        except getopt.GetoptError:
            print 'timelapse.py -i  -o  -r '
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print 'timelapse.py -i  -o  -r '
                sys.exit()
            elif opt in ("-i", "--ifolder"):
                inputfolder = arg
            elif opt in ("-o", "--ofolder"):
                outputfolder = arg
            elif opt == "-r":
                process = 1
    
        print 'Input folder is "', inputfolder
        print 'Output folder is "', outputfolder
        if process==1:
            deflickerRAW(inputfolder, outputfolder)
        initGUI(inputfolder, outputfolder)
    
    if __name__ == "__main__":
        main(sys.argv[1:])