import csv
import json
import sys

filename = 'Partnership.tsv'

with open('answers.json', 'r', encoding='utf-8') as f:
    updates = json.load(f)

with open(filename, 'r', encoding='utf-8') as f:
    reader = list(csv.reader(f, delimiter='\t'))

header = reader[0]
ans_idx = header.index('Answer')
sol_idx = header.index('Basic Solution')

for row in reader[1:]:
    qnum = str(row[0]).strip()
    if qnum in updates:
        while len(row) <= max(ans_idx, sol_idx):
            row.append('')
        row[ans_idx] = updates[qnum]['Answer']
        row[sol_idx] = updates[qnum]['Basic Solution']

with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(reader)

print(f'Updated {len(updates)} questions.')
