from PIL import Image, ImageDraw, ImageFont


# Original Size is 2448 * 2448 pixels.
# Image taken from Apple iPhone5s with Square mode.

# Instgram recommendation is 1080 * 1080 pixels.
# https://www.facebook.com/business/help/430958953753149

recommended_size = 1080, 1080

input = Image.open('sample_image.jpg').convert('RGBA').resize(recommended_size)
text = Image.new('RGBA', input.size, (255, 255, 255, 0))

font = ImageFont.truetype('Consolas.ttf', size=100)
drawing = ImageDraw.Draw(text)

drawing.text(
    (100, 100),
    '#dailycoding',
    font=font,
    fill=(255, 255, 255, 255),
)

output = Image.alpha_composite(input, text)
output.save('sample_image_processed.jpg', 'JPEG')
output.show()
