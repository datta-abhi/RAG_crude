# file to fetch and put all info as python dict
import glob

# initialising context 
context = {}

# adding employees and product info to context dict
for i in ['employees','products']:
    entities = glob.glob(f"knowledge-base/{i}/*")

    for entity in entities:
        name = entity.split("\\")[-1].split('.md')[0]
        doc = ""
        with open(entity,'r',encoding='utf-8') as f:
            doc = f.read()
        context[name] = doc
        