__author__ = "Heracles93"
"""
source:
https://projects.raspberrypi.org/en/projects/getting-started-with-picamera
"""
from picamera import PiCamera, Color
from time import sleep

class piMoonCamera:
    
    def __init__(self):
        """
        Init
        """
        self.camera = PiCamera()

    def preview(self, duration: int = 5, alpha: int = None, brightness: int = None, imageEffect : str = "none", exposure : str = "auto", whiteBalance : (str): "auto"):
        """Show the camera for <duration> secs.

        Params:
            duration : (int) : duration in seconds.
            alpha : (int) : set the alpha level between 0 and 255
            brightness
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
        
    def getImage(self, name: str, directory: str = None, previewTime: int = 2, text: str = None, textSize: int = None, textBackgroundColor: str = None, textForegroundColor: str = None): #@TODO
        """
        @TODO
        """
        filepath = "tmp_image.jpg"
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

    def getImages(self, nb: int, name: str, directory: str = None, previewTime: int = 2): #@TODO
        """
        @TODO
        """
        for i in range(nb):
            self.getImage(name=name+str(i), directory=directory, previewTime=previewTime)
    
    def getVideo(self, duration: int, name: str):
        """
        @TODO
        """
        filepath = "tmp_video.h264"
        self.camera.start_preview()
        self.camera.start_recording(filepath)
        sleep(duration)
        self.camera.stop_recording()
        self.camera.stop_preview()
        
    def setResolution(self, xResolution: int = 2592, yResolution: int = 1994):
        self.camera.resolution = (xResolution, yResolution)
        self.framerate = 15
        self.camera.start_preview()
        sleep(5)
        camera.capture("max_tmp_image.jpg")
        camera.stop_preview()
        
    def setText(self, text : str):
        self.camera.annotate_text = text
        
    def autoBrightbess(self):
        self.camera.start_preview()
        for i in range(100):
            self.camera.annotate_text = "Brightness: %s" % i
            self.camera.brightness = i
            sleep(0.1)
        self.camera.stop_preview()

    def autoContrast(self):
        self.camera.start_preview()
        for i in range(100):
            self.camera.annotate_text = "Contrast: %s" % i
            self.camera.contrast = i
            sleep(0.1)
        self.camera.stop_preview()
        
if __name__ == "__main__":
    print("Starting ...")
    cam = piMoonCamera()
    cam.preview()