from parser_generic import MedicalDocParser
import re

class PrescriptionParser(MedicalDocParser):
    def __init__(self, text) -> None:
        super().__init__(text)
    
    def parse(self):
        return {
            'patient_name' : self.get_field('patient_name'),
            'patient_address' : self.get_field('patient_address'),
            'prescriptions'  : self.get_field('prescription'),
            'directions'  : self.get_field('directions'),
            'refill'  : self.get_field('refills')
        }

    def get_field(self, field_name):
        pattern = ''
        
        pattern_dict = {
            'patient_name': {'pattern': 'Name:(.*)Date', 'flag': 0},
            'patient_address': {'pattern':'Address:(.*)\n', 'flag': 0},
            'prescription': {'pattern':'Address[^\n]*(.*)Directions', 'flag': re.DOTALL},
            'directions': {'pattern':'Directions:(.*)Refill', 'flag': re.DOTALL},
            'refills': {'pattern':'Refill:(.*) times', 'flag': 0}
        }

        pattern_object = pattern_dict.get(field_name)

        if pattern_dict:
            matches = re.findall(pattern_object['pattern'], self.text, flags = pattern_object['flag'])
            if len(matches) > 0:
                return matches[0].strip()

if __name__ == '__main__':
    document_text = '''Dr John Smith, M.D
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

    pp = PrescriptionParser(document_text)
    print(pp.parse())
