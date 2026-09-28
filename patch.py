import json
import sys

file_path = r'd:\Nishit\Softwares\Gemini\AbhasSirCourseFinisher\Profit_Loss_Discount.tsv'

with open('solutions.json', 'r', encoding='utf-8') as f:
    sols = json.load(f)

sol_map = {str(s['q_num']): s for s in sols}

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

patched = 0
for i, line in enumerate(lines):
    if i == 0: continue
    parts = line.strip('\n').split('\t')
    if len(parts) > 0 and parts[0]:
        q_num = parts[0].split('. ')[0]
        if q_num in sol_map:
            s = sol_map[q_num]
            q = parts[0]
            # Handle cases where existing lines have fewer tabs
            time = parts[4] if len(parts) > 4 and parts[4].strip() else '40'
            tags = parts[5] if len(parts) > 5 and parts[5].strip() else 'Source::AbhasSaini'
            
            new_line = f"{q}\t{s['ans']}\t{s['basic']}\t{s['short']}\t{time}\t{tags}\n"
            lines[i] = new_line
            patched += 1

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print(f'Patched {patched} questions.')
