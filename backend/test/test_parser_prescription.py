
from backend.src.parser_prescription import PrescriptionParser


def test_get_name():
    pp = PrescriptionParser(document_text_1)
    assert pp.get_field('patient_name') == 'Marta Sharapova'
    
    # pp = PrescriptionParser(document_text_2)
    # assert pp.get_field('patient_name') == '9 tennis court, new Russia, DC'


document_text_1 = '''
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222


Name: Marta Sharapova Date: 5/11/2022


Address: 9 tennis court, new Russia, DC


Prednisone 20 mg
Lialda 2.4 gram

Directions:

Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month

Refill: 2 times
'''


document_text_2 = '''
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222


Name: Kirat Mike Date: 5/11/2022


Address: 9 tennis court, new Russia, DC


Prednisone 20 mg
Lialda 2.4 gram

Directions:

Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month

Refill: 2 times
'''