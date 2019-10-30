import os
from pdf2image import convert_from_path


def pdf_to_img(pdf_path, to_dir_path):
    images = convert_from_path(pdf_path)
    pdf_name = os.path.basename(os.path.splitext(pdf_path)[0])
    pdf_anotated_dir = '{}/{}'.format( to_dir_path, pdf_name )
    
    if not os.path.exists(pdf_anotated_dir):
        print(pdf_anotated_dir)
        os.makedirs(pdf_anotated_dir)
    if not os.path.exists(to_dir_path):
        os.makedirs(to_dir_path)

    i = 0
    for image in images:
        print('  pdf_name  :  ', pdf_name)
        image.save('{}/{}_{}.png'.format(to_dir_path, pdf_name, i), 'png')
        i += 1
