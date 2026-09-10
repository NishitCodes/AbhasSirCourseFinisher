import csv

filename = 'Partnership.tsv'
with open(filename, 'r', encoding='utf-8') as f:
    reader = list(csv.reader(f, delimiter='\t'))

header = reader[0]
ans_idx = header.index('Answer')

with open('next_q.txt', 'w', encoding='utf-8') as out:
    count = 0
    for row in reader[1:]:
        if len(row) <= ans_idx or not row[ans_idx].strip():
            out.write(f"QNum: {row[0]}\n")
            out.write(f"Question: {row[1]}\n")
            out.write(f"Options: {row[3].replace(chr(10), ' ')}\n")
            out.write('---\n')
            count += 1
            if count >= 4:
                break
