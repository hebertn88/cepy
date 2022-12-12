DATABASE_FILE = 'data.db'

CEP_MIN = 16300001
CEP_MAX = 16309999

SLEEP_MIN = 5
SLEEP_MAX = 25

if __name__ == '__main__':
    from models import *
    from utils import print_body, print_title  
    
    print_title('SETTINGS', sleep_time=1)
    
    print_title('BATABASE NAME')
    print_body(f"DATABASE_FILE = {DATABASE_FILE}")
    
    print_title('CEP RANGE')
    cep_range = CepRange.get()
    print_body(
        f"CepRange.min_cep = {cep_range.min_cep}",
        f"CepRange.max_cep = {cep_range.max_cep}",
        f"CepRange.last_cep = {cep_range.last_cep}"
        )
    
    print_title('LAST CEP IN DATABASE')
    last_cep = Cep.select().order_by(Cep.cep.desc()).limit(1)[0]
    print_body(f"Cep.last_cep = {last_cep.cep}")

    print_title('API QUERY DELAY')
    print_body(
        f"SLEEP_MIN = {SLEEP_MIN}",
        f"SLEEP_MAX = {SLEEP_MAX}"
    )