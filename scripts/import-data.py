import json, sys
from pathlib import Path
import openpyxl
source = Path(sys.argv[1])
sheet = openpyxl.load_workbook(source, read_only=True, data_only=True)['Form Responses 1']
values = list(sheet.values)
keys = ['date', 'status', 'research', 'information', 'channel', 'importance', 'barrier', 'content', 'feedback']
records = []
for index, row in enumerate(values[1:], 2):
    if not row[0]: continue
    record = {'id': index}
    for i, key in enumerate(keys):
        value = row[i]
        if key == 'date': value = value.isoformat()
        elif key in ['information', 'channel', 'barrier']: value = list(dict.fromkeys(v.strip() for v in str(value or '').split(',') if v.strip()))
        elif key == 'importance': value = int(value) if value is not None else None
        else: value = str(value or '').strip()
        record[key] = value
    records.append(record)
output = Path(__file__).resolve().parents[1] / 'data' / 'survey.json'
output.write_text(json.dumps({'source': source.name, 'sheet': sheet.title, 'questions': [str(v).strip() for v in values[0][:9]], 'records': records}, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'Imported {len(records)} responses into {output.name}')
