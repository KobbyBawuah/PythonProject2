from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


from QuoteEngine.QuoteModel import QuoteModel


class generate_meme:
    def __init__(self, output_path):
        self.output_path = output_path + ".png"

    def make_meme(self, img_path, text, author, width=500) -> str:
        self.text = text
        self.author = author
        self.width = width

        self.img = Image.open(img_path)

        if width is not None:
            ratio = self.width / float(self.img.size[0])
            height = int(ratio * float(self.img.size[1]))
            self.img = self.img.resize((self.width, height), Image.NEAREST)

        font = ImageFont.truetype("arial.ttf", 20)
        draw = ImageDraw.Draw(self.img)
        body = self.text + " -> " + self.author
        draw.multiline_text((10, 10), body, font=font)
        self.img.save(self.output_path)

        return self.output_path
