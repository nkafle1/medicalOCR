
from parser_prescription import PrescriptionParser
import pytest

@pytest.fixture()
def doc_1_maria():
    document_text = '''
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
    return PrescriptionParser(document_text)

@pytest.fixture()
def doc_2_kirat():
    document_text = '''
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
    return PrescriptionParser(document_text)

@pytest.fixture()
def doc_3_empty():
    return PrescriptionParser('')



def test_get_name(doc_1_maria, doc_2_kirat, doc_3_empty):
    assert doc_1_maria.get_field('patient_name') == 'Marta Sharapova'
    assert doc_2_kirat.get_field('patient_name') == 'Kirat Mike'
    assert doc_3_empty.get_field('patient_name') == None

def test_get_address(doc_1_maria, doc_2_kirat, doc_3_empty):
    assert doc_1_maria.get_field('patient_address') ==  '9 tennis court, new Russia, DC'
    assert doc_2_kirat.get_field('patient_address') ==  '9 tennis court, new Russia, DC'
    assert doc_3_empty.get_field('patient_address') == None

def test_get_medicines(doc_1_maria, doc_2_kirat, doc_3_empty):
    assert doc_1_maria.get_field('prescription') ==     '''Prednisone 20 mg
    Lialda 2.4 gram'''
    assert doc_2_kirat.get_field('prescription') ==  '''Prednisone 20 mg
    Lialda 2.4 gram'''
    assert doc_3_empty.get_field('prescription') == None

def test_get_directions(doc_1_maria, doc_2_kirat, doc_3_empty):
    assert doc_1_maria.get_field('directions') ==     '''Prednisone, Taper 5 mg every 3 days,
    Finish in 2.5 weeks a
    Lialda - take 2 pill everyday for 1 month'''
    assert doc_2_kirat.get_field('directions') ==  '''Prednisone, Taper 5 mg every 3 days,
    Finish in 2.5 weeks a
    Lialda - take 2 pill everyday for 1 month'''
    assert doc_3_empty.get_field('directions') == None

def test_get_refill(doc_1_maria, doc_2_kirat, doc_3_empty):
    assert doc_1_maria.get_field('refills') ==  '2'
    assert doc_2_kirat.get_field('refills') ==  '2'
    assert doc_3_empty.get_field('refills') == None

def test_parse(doc_1_maria, doc_3_empty):
    record_maria = doc_1_maria.parse()
    assert record_maria == {
            'patient_name' : 'Marta Sharapova',
            'patient_address' : '9 tennis court, new Russia, DC',
            'prescriptions'  : '''Prednisone 20 mg
    Lialda 2.4 gram''',
            'directions'  : "Prednisone, Taper 5 mg every 3 days,\n    Finish in 2.5 weeks a\n    Lialda - take 2 pill everyday for 1 month",
            'refill'  : '2'
    }

    record_empty = doc_3_empty.parse()
    assert record_empty == {
            'patient_name' : None,
            'patient_address' : None,
            'prescriptions'  : None,
            'directions'  : None,
            'refill'  : None
    }