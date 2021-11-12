📦 nigeria_bank_codes 
=======================

The Nigeria bank code is a basic python package that returns details of particular bank in Nigeria.

## Installation

You can install Nigeria bank codes from [PyPI](https://pypi.org/project/nigeria_bank_codes/):

    pip install nigeria-bank-codes



## How to use

    $ from nigeria_bank_codes import core
     bank = core.cbn_code("322")
     print(bank)
     ## {'bank_code': '100018', 'cbn_code': '322', 'name': 'Zenith Mobile', 'bank_short_name': 'zenith-mobile', 'disabled_for_vnuban': None}
     
     print(bank['bank_short_name'])
     ## zenith-mobile

     

