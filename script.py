import json

file_path = r'd:\Nishit\Softwares\Gemini\AbhasSirCourseFinisher\Profit_Loss_Discount.tsv'

unsolved = []
with open(file_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i == 0: continue
        parts = line.strip('\n').split('\t')
        if len(parts) >= 6:
            if not parts[1].strip() and not parts[2].strip() and not parts[3].strip():
                unsolved.append({'line': i, 'q': parts[0]})
        elif len(parts) >= 2 and '\t\t' in line:
             unsolved.append({'line': i, 'q': parts[0]})

print(json.dumps(unsolved, ensure_ascii=False, indent=2))

