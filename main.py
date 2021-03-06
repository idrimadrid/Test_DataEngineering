from extract import *
from transform import *
from load import *


# Extracting  files
med, clt, pub, pub_json = read_files()

# transformation and processing
med = process_drugs(med)
pub = process_pub(pub, pub_json)
clt = process_cli(clt)

# generating Json file
gen_json(med, pub, clt)
