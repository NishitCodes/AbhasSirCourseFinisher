file_path = r'd:\Nishit\Softwares\Gemini\AbhasSirCourseFinisher\Profit_Loss_Discount.tsv'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

count = 0
for i, line in enumerate(lines):
    if line.startswith('177.'):
        parts = line.strip('\n').split('\t')
        if not (len(parts) > 1 and parts[1].strip()):
            if '15. The marked price' in line:
                q = parts[0]
                lines[i] = f"{q}\t(c) 5%\tCP = 750 * 0.8 = 600. SP = 750 * (1 - x/100)^2 = 634.80. (1 - x/100)^2 = 0.8464 => x = 8. Disc = 16%. New SP = 750 * 0.84 = 630. Gain = 30 => Gain% = 5%.\t750(1-x)^2 = 634.8 => x=8%. SP = 750(0.84) = 630. CP=600. Gain = 5%.\t40\tSource::AbhasSaini\n"
                count += 1
            elif 'A shopkeeper allows' in line:
                q = parts[0]
                lines[i] = f"{q}\t(d) 18.29\tMP = 1800. SP1 = 1800 * 0.84 = 1512. CP = 1512 / 1.08 = 1400. SP2 = 1800 * 0.92 = 1656. Profit = 256. Profit% = 256 / 1400 = 18.285%.\tCP = 1800*0.84/1.08 = 1400. SP2 = 1800*0.92 = 1656. P% = 256/1400 = 18.29%.\t40\tSource::AbhasSaini\n"
                count += 1

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print(f'Fixed {count} questions.')
