from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

font_name = '/usr/share/fonts/truetype/freefont/FreeMono.ttf'
font_size = 20
font_color = (3, 8, 12)
 
def watermark_text(input_image_path,
                   output_image_path,
                   text, pos):
    photo = Image.open(input_image_path)
    # make the image editable
    drawing = ImageDraw.Draw(photo)
    font = ImageFont.truetype(font_name, font_size)
    drawing.text(pos, text, fill=font_color, font=font)
    photo.show()
    photo.save(output_image_path)
 
if __name__ == '__main__':
    watermark_text('./apple.png', './apple_watermark.png',
                   text='Created by Steve & Steve.',
                   pos=(0, 0))
