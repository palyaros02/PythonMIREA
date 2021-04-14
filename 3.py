# 31
"""import struct
test1 = (b'WTGY\xa0Tpi\xbf\xc5\xea?u\naQ\x00@\xedFs=\xb6\xe4\xbf|\x00\x00'
         b'\x00\x88\x00\x00\x00\x94\x00\x00\x00\xfc\x93$O\x8b$\xe0\xbf\x02\x00\xa0'
         b'\x00\x00\x00v\xa2\xa5\xb0\x9e8X\x1c12\xc5\x8bIe\xc1iA\xc2\x81\xb7qs\xde\x1fj'
         b'C,\xa0\xa6\xb5G\x1a\xc8&\xd7\xd4\xc8\x9f\xfcD\x8a\x84\xf7\x84\xfd_<9\x84'
         b'TT\x03\x00\x00\x00N\x00\x1c\x1d\xd8)l\xab\xdf\xa1\x90\x8d1\x9c'
         b'\xba\xc4\xb3\xbf\xb8X\x80/\xb4\x97Vm\x07\xb1\t\xe57\x12y\x1a-S\x11\xf0'
         b'3]&\x89\x83G\xc5?\xe5]\x18-\xe2\xa3o}\xc8\xe2\xd2\x19#,\xc3\xbf\x88P\xea\xf7'
         b'/X\xcf\xbf')

ans1 = {'A1': 0.8366391238547699,
        'A2': {'B1': 2677,
               'B2': 97,
               'B3': {'C1': 650648135,
                      'C2': 215,
                      'C3': -611211620514805548,
                      'C4': {'D1': 6076627178590567812,
                             'D2': [160, 166, 181],
                             'D3': 11664230040959720732},
                      'C5': -0.0772205954868268},
               'B4': -0.6472460986619026,
               'B5': [{'E1': 796940472, 'E2': 16503916954933172148},
                      {'E1': 444142135, 'E2': 9882688909963514669},
                      {'E1': 1069893507, 'E2': 9038623168970382821}],
               'B6': -0.5044609590300975,
               'B7': {'F1': [-0.1497844577877656, -0.24487876515616258],
                      'F2': 2042444685232153206,
                      'F3': 7620483411039564337,
                      'F4': [65, 194, 129, 183],
                      'F5': 113,
                      'F6': -8589}},
        'A3': 742615583}

test2 = (b'WTGYH\x9a\x9d\x13\xf6\xdd\xc9\xbfo"\xdeP\x00\xd8O\x81 ^\xc1\xca?{\x00\x00'
         b'\x00\x87\x00\x00\x00\x93\x00\x00\x00\x90\xca\xc4\xb6u\x0e\xed'
         b'\xbf\x02\x00\x9f\x00\x00\x00\xd9%\x83+\xa1_\x8b\x87D\xfc\x82\xf6\xe4'
         b'\x08\xd8\xf6\xb2\xc1\x83\x8fp)\x87\xf2\x1aA\xb6\x97\xec^\xb1\x8a\xc8=\t\x946'
         b'\xa1\x82\x10\xde\xd8q\x10\x8b.a\x04p\xbd\x02\x00\x00\x00N\x00\xea'
         b'F\xf1\x8c\xc9=\xc1~\xe8\xe2QUz\x0c\xec?\xc6\x8ch?L\xb7o6\xcb\xb2c\xbf\xa6'
         b'7\xca\xdb\xear\xed\xca\x10\x8b\xa3\xdd\xeaj\xef\x86\x13\xc7\x19\x90*'
         b'&\xe9V\xc0^\xe9\xbc\x85\x04\xbe\xbf\xe8\x82\xf1\xf2E\x1c\xc6\xbf')

ans2 = {'A1': -0.20208621938509652,
        'A2': {'B1': 8815,
               'B2': -34,
               'B3': {'C1': -930434722,
                      'C2': 61,
                      'C3': -2819798163450850295,
                      'C4': {'D1': -4796328787710373775,
                             'D2': [151, 236],
                             'D3': 9133649455146419946},
                      'C5': 0.8765231768039401},
               'B4': 0.20902611338772092,
               'B5': [{'E1': 1063816390, 'E2': 13791063069799987020},
                      {'E1': 3687462822, 'E2': 15970761607826207466},
                      {'E1': 2263837418, 'E2': 6262578721083475731}],
               'B6': -0.9080151147557718,
               'B7': {'F1': [-0.11725650655841502, -0.17273783075781712],
                      'F2': 9767005362707441113,
                      'F3': 17786976507781119044,
                      'F4': [178, 193, 131, 143],
                      'F5': 112,
                      'F6': -30935}},
        'A3': -1237247246}"""

#32
class C32:
    def __init__(self):
        self.cur_node = "A"
    def add(self):
        if self.cur_node == "A":
            self.cur_node = "D"
            return 1
        elif self.cur_node == "B":
            self.cur_node = "C"
            return 2
        elif self.cur_node == "C":
            self.cur_node = "D"
            return 1
        elif self.cur_node == "A":
            self.cur_node = "D"
            return 1
        elif self.cur_node == "A":
            self.cur_node = "D"
            return 1
        else:
            raise RuntimeError