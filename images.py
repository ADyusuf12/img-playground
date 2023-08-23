from PIL import Image, ImageFilter
img = Image.open('./Pokedex/favicon.png')
# img.thumbnail((400, 400))
filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save('favicon.png', 'png')

