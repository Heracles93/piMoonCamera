__author__ = "Heracles93"
"""
source:
https://projects.raspberrypi.org/en/projects/getting-started-with-picamera
"""
from picamera import PiCamera, Color
from time import sleep

class piMoonCamera:
    
    def __init__(self, doTest : bool = False):
        """
        Init the camera and test it.
        
        Params:
            doTest : (bool) : test the camera if True (False by default)
        """
        print("Starting ...")
        self.camera = PiCamera()       
        if doTest:
            self.preview()
            print("Preview test ok")
            sleep(2)
            self.autoContrast()
            print("Contrast test ok")
            sleep(2)
            self.autoBrightness()
            print("Brightness test ok")
            sleep(2)
            self.getImage("testImage.jpg")
            print("Image captured test ok")
            sleep(2)
            self.getVideo(duration=5, name="testVideo.h264")
            print("Video captured test ok")
        print("Camera initiated ! Done")
    
    def preview(self, duration: int = 5, alpha: int = None, brightness: int = None, imageEffect : str = "none", exposure : str = "auto", whiteBalance : (str) = "auto"):
        """Show the camera for <duration> secs.

        Params:
            duration : (int) : duration in seconds.
            alpha : (int) : set the alpha level between 0 and 255
            brightness : (int) : set the brightness between 0 and 100 
            imageEffect : (str) : choose between: none (default), negative, solarize, sketch, denoise, emboss, oilpaint, hatch, gpen, pastel, watercolor, film, blur, saturation, colorswap, washedout, posterise, colorpoint, colorbalance, cartoon, deinterlace1
            exposure : (str) : choose between: off, auto (default), night, nightpreview, backlight, spotlight, sports, snow, beach, verylong, fixedfps, antishake
            whiteBalence : (str) : choose between: off, auto (default), sunlight, cloudy, shade, tungsten, fluorescent, incandescent, flash
        """
        if alpha:
            self.camera.start_preview(alpha=alpha)
        else:
            self.camera.start_preview()
        if brightness:
            self.camera.brightness = brightness
        self.camera.image_effect = imageEffect
        self.camera.exposure_mode = exposure
        self.camera.awb_mode = whiteBalance
        sleep(duration)
        self.camera.stop_preview()
        
    def setCameraRotation(self, angle: int):
        """
        Rotate the angle of the camera.
        
        Params:
            angle : (int) : angle between 0 and 360 in degree.
        """
        self.camera.rotation = angle
        
    def resetRotation(self):
        """
        Reset rotation to 0.
        """
        self.setCameraRotation(0)
        
    def getImage(self, name: str, directory: str = None, previewTime: int = 2, text: str = None, textSize: int = None, textBackgroundColor: str = None, textForegroundColor: str = None):
        """
        Take a picture.
        
        Params:
            name : (str) : name of the image
            directory : (str) : directory path 
            previewTime : (int) : time to preview the camera
            text : (str) : if text to display on the image
            textBackgroundColor : (str) : background color of the text
            textForegroundColor : (str) : foreground color of the text
            textSize : (int) : size of the text
        """
        filepath = name
        if directory:
            filepath = directory + name
        if not filepath.endswith(".jpg"):
            filepath += ".jpg"
        self.camera.start_preview()
        if text:
            if textBackgroundColor:
                self.camera.annotate_background = Color(textBackroundColor)
            if textForegroudColor:
                self.camera.annotate_foreground = Color(textForeroudColor)
            self.setText(text)
            if textSize:
                self.camera.annotate_text_size = textSize
        sleep(previewTime)
        self.camera.capture(filepath)
        self.camera.stop_preview()        

    def getImages(self, nb: int, name: str, directory: str = None, previewTime: int = 2, text: str = None, textSize: int = None, textBackgroundColor: str = None, textForegroundColor: str = None):
        """
        Take a set pf <nb> pictures.
        
        Params:
            nb : (int) : number of image(s) to take
            name : (str) : name of the image set
            directory : (str) : directory path 
            previewTime : (int) : time to preview the camera
            text : (str) : if text to display on the image
            textBackgroundColor : (str) : background color of the text
            textForegroundColor : (str) : foreground color of the text
            textSize : (int) : size of the text
        """
        for i in range(nb):
            self.getImage(name=name+"_"+str(i), directory=directory, previewTime=previewTime, text=text, textSize=textSize, textBackgroundColor=textBackground, textForegroudColor=textForeground)
    
    def getVideo(self, duration: int, name: str, directory : str = None):
        """
        Take a video.
        
        Params:
            duration : (int) : duration of the video
            name : (str) : name of the video
            directory : (str) : directory path 
        """
        filepath = name
        if directory:
            filepath = directory + name
        if not filepath.endswith(".h264"):
            filepath += ".h264"
        self.camera.start_preview()
        self.camera.start_recording(filepath)
        sleep(duration)
        self.camera.stop_recording()
        self.camera.stop_preview()
        
    def getVideos(self, nb : int, duration: int, name: str, directory : str = None):
        """
        Take a video.
        
        Params:
            nb : (int) : number of video(s) to take
            duration : (int) : duration of the video
            name : (str) : name of the video
            directory : (str) : directory path 
        """
        for i in range(nb):
            self.getImage(duration=duration, name=name+"_"+str(i), directory=directory)

    def setResolution(self, xResolution: int = 2592, yResolution: int = 1994):
        """
        Change the Resolution and take a picture.

        Params:
            xResolution : (int) : resolution in pixel alonf X axis
            yResolution : (int) : resolution in pixel alonf Y axis
        """
        self.camera.resolution = (xResolution, yResolution)
        self.framerate = 15
        self.camera.start_preview()
        sleep(5)
        self.camera.capture("max_tmp_image.jpg")
        self.camera.stop_preview()
        
    def setText(self, text : str):
        """
        Add text to the camera

        Params:
            text : (str) : text to add
        """
        self.camera.annotate_text = text
        
    def autoBrightness(self):
        """
        Auto explore the brightness and preview.
        """
        self.camera.start_preview()
        for i in range(100):
            self.camera.annotate_text = "Brightness: %s" % i
            self.camera.brightness = i
            sleep(0.1)
        self.camera.stop_preview()

    def autoContrast(self):
        """
        Auto explore the contrast and preview.
        """
        self.camera.start_preview()
        for i in range(100):
            self.camera.annotate_text = "Contrast: %s" % i
            self.camera.contrast = i
            sleep(0.1)
        self.camera.stop_preview()
        
if __name__ == "__main__":
    cam = piMoonCamera(doTest=True)
    #cam.preview(alpha=128)