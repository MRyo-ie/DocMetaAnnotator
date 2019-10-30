import argparse
import glob
from to_img_convertors import pdf2img

parser = argparse.ArgumentParser(description='document file to img')
parser.add_argument('--source_type', default='pdf', type=str, choices=['pdf', 'PDF', 'xml'], help='text confidence threshold')
parser.add_argument('--source_dir', default='datas/pdf', type=str, help='souruce files dir')
parser.add_argument('--out_dir', default='datas/out', type=str, help='souruce files dir')


if __name__ == "__main__":
    args = parser.parse_args()

    s_files = None
    if args.source_type in ['pdf', 'PDF']:
        s_files = glob.glob(args.source_dir + '/*.pdf')
        for pdf_p in s_files:
            pdf2img.pdf_to_img(pdf_p, args.out_dir)

