from ink2canvas.svg.AbstractShape import AbstractShape
from pip._pkgutil import get_data

class Image(AbstractShape):

    def getData(self):
        x = self.attr("x")
        y = self.attr("y")
        width = self.attr("width")
        height = self.attr("height")
        href = self.attr("href","xlink")
        return x, y, width, height, href
    
    def draw(self, isClip=False):
        if self.hasTransform():
            transMatrix = self.getTransform()
            self.ctx.transform(*transMatrix) # unpacks argument list
        if not isClip:
            style = self.getStyle()
            self.setStyle(style)
            self.canvasContext.beginPath()

        x, y, width, height, href = self.getData()
        
        self.canvasContext.write("\n\tvar image = new Image();")
        self.canvasContext.write("\n\timage.src = '" + href +"';")
        self.canvasContext.write("\n\tctx.drawImage(image, %f,%f,%f,%f);" %(x,y,width, height))
        
        if not isClip: 
            self.canvasContext.closePath()
        
        


