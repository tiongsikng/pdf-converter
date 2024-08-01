import cv2
import os, sys, glob, shutil
from fpdf import FPDF
from PIL import Image
from tqdm import tqdm
sys.path.insert(0, os.path.abspath('.'))

jpg_list = []

def make_pdf_folder(folder_nm='./pdfs'):
    if not os.path.exists(folder_nm):
        os.makedirs(folder_nm)

def jpg_pdf_convert(dir_root, jpg_path, output_pdf_path, a4_stretch=True, rotate_landscape=False):
    
    for names in (glob.glob(os.path.join(dir_root, jpg_path))):
        im1 = Image.open(names)                             # Open the image.
        width, height = im1.size
        width, height = float(width * 0.264583), float(height * 0.264583)

        pdf_size = {'P': {'w': 210, 'h': 297}, 'L': {'w': 297, 'h': 210}}
        orientation = 'P' if width <= height else 'L'  
        width = width if width < pdf_size[orientation]['w'] else pdf_size[orientation]['w']
        height = height if height < pdf_size[orientation]['h'] else pdf_size[orientation]['h']        

        if a4_stretch:
            width = pdf_size[orientation]['w']
            height = pdf_size[orientation]['h']
        
        # if rotate_landscape == True or orientation == 'L':
        #     im2 = im1.transpose(Image.ROTATE_270)
        #     os.remove(names)
        #     im2.save(names)
        #     print(names.split('\\')[-1].split('.jpg')[0] + ' rotated!')
        #     orientation = 'P'
        
        pdf = FPDF(unit='mm')
        pdf.add_page(orientation=orientation)
        pdf.image(names, 0, 0, width, height)

        pdf.output(os.path.join(dir_root, output_pdf_path) + names.split('\\')[-1].split('.jpg')[0] + '.pdf', "F")
        print('Converted: ' + names.split('\\')[-1] + ' -> ' + names.split('\\')[-1].split('.jpg')[0] + '.pdf')
        os.rename(os.path.join(dir_root, output_pdf_path) + names.split('\\')[-1].split('.jpg')[0] + '.pdf', os.path.join(dir_root, output_pdf_path) + names.split('\\')[-1].split('.jpg')[0] + '.pdf')


if __name__ == '__main__':
    dir_root='./'
    jpg_path='jpgs/*'
    pdf_output = 'pdfs/'

    make_pdf_folder(folder_nm=pdf_output)
    jpg_pdf_convert(dir_root=dir_root, jpg_path=jpg_path, output_pdf_path=pdf_output, a4_stretch=False, rotate_landscape=False)
