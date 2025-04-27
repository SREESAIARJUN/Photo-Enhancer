from PIL import Image, ImageFilter

class Enhancer:
    def __init__(self, method=None, background_enhancement=False, upscale=None):
        self.method = method or "Unspecified"
        self.background_enhancement = background_enhancement or False
        self.upscale = upscale or None

    def enhance(self, image):
        """Enhances the given image by sharpening it.

        Args:
            image (Image.Image): The input image to enhance.

        Returns:
            The sharpened image.
        """
        sharpened_image = image.filter(ImageFilter.UnsharpMask(radius=2, percent=150))
        return sharpened_image
