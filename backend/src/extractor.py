# this script is responsible to exctract the data from pdf file


from xml.dom.expatbuilder import DOCUMENT_NODE
from pdf2image import convert_from_path
import pytesseract
import util
from PIL import Image
from parser_prescription import PrescriptionParser
from paser_patient_details import PatientDetailsParser

import os

def extract(file_path, file_format):
    pages = convert_from_path(file_path)
    document_text = ''
    # if len(pages) > 0:
    page = pages[0]
    processed_image = util.preprocess_image(page)
    text = pytesseract.image_to_string(processed_image, lang = 'eng')
    document_text = '\n'+ text


    if file_format == 'prescription':
        extracted_data = PrescriptionParser(document_text).parse()
        pass # extract data from prescription
    elif file_format == 'patient_details':
         extracted_data = PatientDetailsParser(document_text).parse()
    else:
        raise Exception(f'Invalid document format: {file_format}')
    return extracted_data

if __name__ == '__main__':
    # data = extract('../resources/prescription/pre_1.pdf', 'prescription')
    data = extract('../resources/patient_details/pd_2.pdf', 'patient_details')
    print(data)
