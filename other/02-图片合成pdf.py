import os
import img2pdf

def images_to_pdf(image_paths, output_path):
    # 将图片路径列表转换为PDF
    with open(output_path, "wb") as f:
        f.write(img2pdf.convert(image_paths))
        print("图片合成为pdf成功！")

# 示例使用
pwd = os.getcwd()
image_path = os.path.join(pwd, 'images')

image_files = []
for file in os.listdir(image_path):
    if os.path.isfile(os.path.join(image_path, file)):
        image_files.append(os.path.join(image_path, file))
# print(image_files)

output_pdf_path = os.path.join(pwd, "output.pdf")

images_to_pdf(image_files, output_pdf_path)