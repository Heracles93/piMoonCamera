__author__ = "Heracles93"
from picamera import PiCamera
from time import sleep

class piMoonCamera:
    
    def __init__(self):
        """
        Init
        """
        self.camera = PiCamera()

    def preview(self, duration: int = 5, alpha: int = None):
        """Show the camera for <duration> secs.

        Params:
            duration : (int) : duration in seconds.
            alpha : (int) : set the alpha level between 0 and 255
        """
        if alpha:
            self.camera.start_preview(alpha=alpha)
        else:
            self.camera.start_preview()                
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
        
    def getImage(self, name: str, directory: str = None, previewTime: int = 2): #@TODO
        """
        @TODO
        """
        filepath = "tmp_image.jpg"
        self.camera.start_preview()
        sleep(previewTime)
        self.camera.capture(filepath)
        self.camera.stop_preview()        

    def getImages(self, nb: int, name: str, directory: str = None, previewTime: int = 2): #@TODO
        for i in range(nb):
            self.getImage(name=name+str(i), directory=directory, previewTime=previewTime)
    
if __name__ == "__main__":
    print("Starting ...")
    cam = piMoonCamera()
    cam.preview()