from logging import exception
from parser_generic import MedicalDocParser
import re

class PatientDetailsParser(MedicalDocParser):
    def __init__(self, text) -> None:
        super().__init__(text)

    def parse(self):
        return {
            'patient_name':self.get_patient_name(),
            'patient_phone_number': self.get_phone_number(),
            'hepatitis_b_vaccination': self.get_heptatitis_b_vaccination(),
            'medical_problems': self.get_medical_problems()
        }

    def get_patient_name(self):
        pattern = r'Patient Information(.*?)\(\d{3}\)'
        match = re.findall(pattern, self.text, flags = re.DOTALL)
        name = ''
        if match:
            name = self.remove_noise_from_name(match[0])
        return name
    
    def remove_noise_from_name(self, name):
        name = name.replace('Birth Date', '').strip()
        date_pattern = r'((Jan|Feb|March|April|May|June|July|August|Sep|Oct|Nov|Dec)[ \d]+)'
        date_matches = re.findall(date_pattern, name)
    
        if date_matches:
            date = date_matches[0][0]
            name = name.replace(date, '').strip()
        return name

    def get_phone_number(self):
        pattern = r'Patient Information(.*?)(\(\d{3}\) \d{3}-\d{4})'
        match = re.findall(pattern, self.text, flags=re.DOTALL)
        phone_number = match[0][1]
        return phone_number
    
    def get_heptatitis_b_vaccination(self):
        pattern = r'Have you had the Hepatitis B vaccination\?.*(Yes|No|yes|no)'
        match = re.findall(pattern, self.text, flags = re.DOTALL)
        return match[0]

    def get_medical_problems(self):
        pattern = r'List any Medical Problems .*?:(.*)'
        match = re.findall(pattern, self.text, flags = re.DOTALL)
        medical_problems = match[0].strip()
        return medical_problems
if __name__ == '__main__':
 
    document_text = '''
17/12/2020

Patient Medical Record

Patient Information Birth Date

Kathy Crawford May 6 1972

(737) 988-0851 Weight’

9264 Ash Dr 95

New York City, 10005 '

United States Height:
190

In Case of Emergency
ee J
Simeone Crawford 9266 Ash Dr
New York City, New York, 10005
Home phone United States
(990) 375-4621
Work phone
Genera! Medical History
nn ee
Chicken Pox (Varicella): Measies:
IMMUNE

IMMUNE
Have you had the Hepatitis B vaccination?

No

List any Medical Problems (asthma, seizures, headaches}:

Migraine
    '''
    pp = PatientDetailsParser(document_text)
    print(pp.parse())