import os
import argparse
from PIL import Image, ImageDraw, ImageFont

def get_file(image_dir):
	image_list = []
	for root, dirs, files in os.walk(image_dir):
		if not files:
			continue
		for file in files:
			if file.endswith(".jpg") or file.endswith(".JPG"):
				image_list.append(os.path.join(root, file))
	return image_list

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--images', help="the dir of input file", default="./jiafang")
	options = parser.parse_args()
	image_file = get_file(options.images)
	#图片分辨率
	width, height = 300,300
	#设置图片有3x3共九张图片组成，可更改
	col_max, row_max = 4, 4
	save_image = Image.new('RGBA', (width*col_max, height*row_max))
	for i, image_name in enumerate(image_file):
		image = Image.open(image_name)
		img_size = image.size
		draw = ImageDraw.Draw(image)
		re_image = image.resize((300, 300))
		#选择行或列来填充
		#loc = (int(i/col_max)*width,  int(i%row_max)*height)
		loc = (int(i%col_max)*width, int(i/row_max)*height)
		save_image.paste(re_image, loc)
	#png为rgba，存为jpg更改Image构造时的格式即可
	save_image.save("flower.png")
if __name__ == "__main__":
	main()
