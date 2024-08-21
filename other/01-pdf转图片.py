
import os
from pdf2image import convert_from_path
 
def convert_pdf_to_image(pdf_path, output_dir, first_page=None, last_page=None):
    # 将PDF文件转换成图片列表
    images = convert_from_path(pdf_path, first_page=first_page, last_page=last_page)
    
    for i, image in enumerate(images):
        # 将图片保存到指定目录
        image.save('{}/page_{}.png'.format(output_dir, i), 'PNG')
    print('PDF转换完成！')
 

# 调用函数进行转换
pwd = os.getcwd()
pdf_file_path = os.path.join(pwd, '管志辉.pdf')
output_directory = os.path.join(pwd, 'images')  # 输出图片的目录
convert_pdf_to_image(pdf_file_path, output_directory)
