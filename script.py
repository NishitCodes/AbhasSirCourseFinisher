import sys

file_path = r'd:\Nishit\Softwares\Gemini\AbhasSirCourseFinisher\Profit_Loss_Discount.tsv'
out_path = r'd:\Nishit\Softwares\Gemini\AbhasSirCourseFinisher\Profit_Loss_Discount_Updated.tsv'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

q_start = -1
for i, line in enumerate(lines):
    if line.startswith('208. A tailor'):
        q_start = i
        break

if q_start != -1:
    lines[q_start] = lines[q_start].replace('\t\t\t\t40\tSource::AbhasSaini', '\t(d) 10 10/19%\tBuys 105cm for 100 units. Sells 95cm for 100 units. CP of 1cm = 100/105. SP of 1cm = 100/95. Profit = 100/95 - 100/105. Profit% = ((100/95 - 100/105) / (100/105)) * 100 = 200/19 = 10 10/19%.\tSP/CP = 105/95 = 21/19. Profit = 2/19 = 200/19 % = 10 10/19%.\t40\tSource::AbhasSaini')
    lines[q_start+1] = lines[q_start+1].replace('\t\t\t\t40\tSource::AbhasSaini', '\t(b) ₹45,000\tNo of people = 2700 / 4.5 = 600. Actual rice given = 600 * 3.75 = 2250 kg. Accumulated rice = 2700 - 2250 = 450 kg. Black market price = 2 * 40 = 80 Rs/kg. Earned = 450 * 80 = 36000. Fine = 125% of 36000 = 45000.\tSaved per person = 4.5 - 3.75 = 0.75 kg. Total saved = (2700/4.5) * 0.75 = 450 kg. Black market earning = 450 * 80 = 36000. Fine = 1.25 * 36000 = 45000.\t40\tSource::AbhasSaini')
    lines[q_start+2] = lines[q_start+2].replace('\t\t\t\t40\tSource::AbhasSaini', '\t(d) 11.2\tActual weight given = 3 - 0.1 = 2.9 kg. Total CP = 2.9 * 12 = 34.8. SP = 46. Profit = 46 - 34.8 = 11.2.\tActual weight = 2.9 kg. CP = 2.9 * 12 = 34.8. Profit = 46 - 34.8 = 11.2.\t40\tSource::AbhasSaini')
    lines[q_start+3] = lines[q_start+3].replace('\t\t\t\t40\tSource::AbhasSaini', '\t(a) 15.5%\tCP of 105 cm = 100. CP per cm = 100/105. SP for 100 cm = 110. Discount = 5% => discounted SP = 104.5 for 100 cm. But gives 95 cm, so SP of 95 cm = 104.5. SP per cm = 104.5/95 = 1.1. SP/CP = 1.1 / (100/105) = 1.1 * 1.05 = 1.155. Profit = 15.5%.\tNet SP/CP multiplier = (105/100) * (110/100) * 0.95 * (100/95) = 1.05 * 1.1 = 1.155 = 15.5%.\t40\tSource::AbhasSaini')
    lines[q_start+4] = lines[q_start+4].replace('\t\t\t\t40\tSource::AbhasSaini', '\t(a) 27.16\tAfter raid: SP = 90% of CP. 0.9 * CP = 20 => CP = 200/9 per kg. Before raid: MP = 1.1 * CP = 220/9 per kg (according to machine). Machine reads 1000g for 900g actual. To get 1kg actual, machine reading = 1000/900 * 1kg = 10/9 kg. Amount paid = (220/9) * (10/9) = 2200/81 = 27.16.\tNew SP = 0.9 CP = 20. Old SP for 1kg actual = 1.1 CP * (1000/900) = 1.1 * (20/0.9) * 10/9 = 2200/81 = 27.16.\t40\tSource::AbhasSaini')

with open(out_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Done')

