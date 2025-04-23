from rembg import remove
from PIL import Image
input_path = 'linda.png'
output_path = 'linda.png'
inp=Image.open(input_path)
output=remove(inp)
output.save(output_path)
Image.open(output_path)
