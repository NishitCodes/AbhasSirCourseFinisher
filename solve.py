import sys

file_path = r'D:\Nishit\Softwares\Gemini\AbhasSirCourseFinisher\Profit_Loss_Discount.tsv'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

ans_1 = "(a) 36%"
basic_1 = "CP = 65500, SP = 89080.<br>Profit = 89080 - 65500 = 23580.<br>Profit % = (23580 / 65500) * 100 = 36%."
short_1 = "SP/CP = 89080 / 65500 = 8908 / 6550.<br>Profit% = (23580/65500)*100 = 36%"
lines[1] = lines[1].replace('\t\t\t\t40\t', f'\t{ans_1}\t{basic_1}\t{short_1}\t40\t')

ans_2 = "(d) 8.69%"
basic_2 = "Let SP = 100, then CP = 92.<br>Profit = SP - CP = 100 - 92 = 8.<br>Profit % = (Profit / CP) * 100 = (8 / 92) * 100 = 8.695% ≈ 8.69%."
short_2 = "CP = 92% of SP => CP/SP = 92/100 = 23/25.<br>Profit = 2 units on CP of 23.<br>Profit % = 2/23 * 100 ≈ 8.69%"
lines[2] = lines[2].replace('\t\t\t\t40\t', f'\t{ans_2}\t{basic_2}\t{short_2}\t40\t')

ans_3 = "(c) 53.2%"
basic_3 = "Let MP = 100.<br>SP = 100 * 0.90 * 0.80 * 0.65 = 46.8.<br>Total discount = 100 - 46.8 = 53.2%."
short_3 = "Successive discount formula: a + b - ab/100.<br>10% & 20% => 10 + 20 - 2 = 28%.<br>28% & 35% => 28 + 35 - (28 * 35)/100 = 63 - 9.8 = 53.2%."
lines[3] = lines[3].replace('\t\t\t\t40\t', f'\t{ans_3}\t{basic_3}\t{short_3}\t40\t')

ans_4 = "(b) 46%"
basic_4 = "Let MP = 100.<br>SP = 100 * 0.90 * 0.80 * 0.75 = 54.<br>Total discount = 100 - 54 = 46%."
short_4 = "10% & 20% => 28%.<br>28% & 25% => 28 + 25 - (28 * 25)/100 = 53 - 7 = 46%."
lines[4] = lines[4].replace('\t\t\t\t40\t', f'\t{ans_4}\t{basic_4}\t{short_4}\t40\t')

ans_5 = "(d) 16 2/3%"
basic_5 = "Let CP of 1 orange = x.<br>CP of 28 oranges = 28x.<br>SP of 24 oranges = 28x => SP of 1 orange = 28x / 24 = 7x/6.<br>Profit = 7x/6 - x = x/6.<br>Profit % = (x/6) / x * 100 = 100/6% = 16 2/3%."
short_5 = "28 CP = 24 SP => SP/CP = 28/24 = 7/6.<br>Profit = 1 unit on CP of 6.<br>Profit % = 1/6 * 100 = 16 2/3%."
lines[5] = lines[5].replace('\t\t\t\t40\t', f'\t{ans_5}\t{basic_5}\t{short_5}\t40\t')

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)
