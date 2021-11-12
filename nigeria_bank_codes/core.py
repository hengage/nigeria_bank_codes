from nigeria_bank_codes.database.db import bankdb

def cbn_code(num):
    num_str = str(num)
    db = bankdb()
    for i in db:
        if i['cbn_code'] == num_str:
            data =  {
                "bank_code": i["bank_code"],
                "cbn_code": i["cbn_code"],
                "name": i["name"],
                "bank_short_name": i["bank_short_name"],
                "disabled_for_vnuban": i["disabled_for_vnuban"]
            }

            

            return data
        




