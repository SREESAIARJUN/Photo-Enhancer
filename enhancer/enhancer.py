from PIL import Image, ImageFilter

class Enhancer:
    def __init__(self, method, background_enhancement, upscale):
        self.method = method
        self.background_enhancement = background_enhancement
        self.upscale = upscale

    def enhance(self, image: Image.Image) -> Image.Image:
        """Enhances the given image by sharpening it.

        Args:
            image: The input image to enhance.

        Returns:
            The sharpened image.
        """
        sharpened_image = image.filter(ImageFilter.UnsharpMask(radius=2, percent=150))
        return sharpened_image
