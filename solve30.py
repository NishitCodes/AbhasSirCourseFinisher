import sys

file_path = r'D:\Nishit\Softwares\Gemini\AbhasSirCourseFinisher\Profit_Loss_Discount.tsv'

sols = [
    # 6: 5.1
    ("d) 16 2/3%", "SP = 7/6 CP.<br>Profit = SP - CP = 1/6 CP.<br>Profit % = (1/6) * 100 = 16 2/3%.", "SP/CP = 7/6. Profit 1 on 6 => 1/6 * 100 = 16 2/3%."),
    # 7: 5.2
    ("b) 25", "30 * CP = x * SP.<br>SP = (30/x) * CP.<br>Profit = 20%, so SP = 1.2 * CP.<br>30/x = 1.2 => x = 30 / 1.2 = 25.", "CP * 30 = SP * x.<br>Profit 20% = 1/5 => SP/CP = 6/5.<br>So 30/x = 6/5 => x = 25."),
    # 8: 5.3
    ("(a) 18.75%", "95 * CP = 80 * SP.<br>SP / CP = 95 / 80 = 19 / 16.<br>Profit = 3 on 16 => (3/16)*100 = 18.75%.", "SP/CP = 95/80 = 19/16.<br>Profit = 3/16 = 18.75%."),
    # 9: 5.4
    ("25", "20 * SP = 25 * CP.<br>SP / CP = 25 / 20 = 5 / 4.<br>Profit = 1 on 4 => (1/4)*100 = 25%.", "SP/CP = 25/20 = 5/4.<br>Profit = 1/4 = 25%."),
    # 10: 5.5
    ("(b) 11%", "Loss = CP - SP.<br>10 * SP = 80 * CP - 80 * SP.<br>90 * SP = 80 * CP => SP / CP = 8 / 9.<br>Loss = 1 on 9 => 1/9 * 100 = 11.11% ≈ 11%.", "Loss = 10 SP, total SP = 80.<br>CP = 80 + 10 = 90 SP units.<br>Loss% = 10/90 = 1/9 ≈ 11%."),
    # 11: 5.6
    ("150", "Profit = SP - CP.<br>Profit on 2 = 2*SP - 2*CP.<br>Given Profit = 3*CP.<br>So 2*SP - 2*CP = 3*CP => 2*SP = 5*CP.<br>SP / CP = 5 / 2.<br>Profit = 3 on 2 => (3/2)*100 = 150%.", "Profit = 3 CP on sale of 2 CP.<br>Profit% = 3/2 * 100 = 150%."),
    # 12: 5.7
    ("37.5", "Profit = CP of 30 kg.<br>Base (Total CP) = CP of 80 kg.<br>Profit % = (30 / 80) * 100 = 3/8 * 100 = 37.5%.", "Profit / Total CP = 30 / 80 = 3/8 = 37.5%."),
    # 13: 5.8
    ("35.96%", "Profit = CP of 32 kg.<br>Base = CP of 89 kg.<br>Profit % = (32 / 89) * 100 = 35.955% ≈ 35.96%.", "Profit% = 32/89 * 100 ≈ 35.96%."),
    # 14: 5.9
    ("(a) ₹130", "CP of 80 = 11180.<br>Loss = CP - SP => 80*CP - 80*SP = 6*SP => 80*CP = 86*SP.<br>So 86*SP = 11180.<br>SP of 1 article = 11180 / 86 = 130.", "80 CP = 86 SP = 11180.<br>SP(1) = 11180 / 86 = 130."),
    # 15: 5.10
    ("C. Rs.130", "Profit = 36*SP - 36*CP.<br>Given Profit = 10*SP => 36*CP = 26*SP.<br>36*SP = 1080 => 1*SP = 30.<br>36*CP = 26 * 30 = 780 => 6*CP = 780/6 = 130.", "36 SP = 1080 => 1 SP = 30.<br>36 CP = 26 SP = 26 * 30 = 780.<br>6 CP = 780 / 6 = 130."),
    # 16: 5.11
    ("(d) 400", "Let CP = x, Profit% = x.<br>SP = CP(1 + Profit%/100) => x(1 + x/100) = 2000.<br>x^2 + 100x - 200000 = 0 => (x+500)(x-400) = 0.<br>x = 400.", "Check options:<br>If CP=400, Profit=400%.<br>SP = 400 + 400% of 400 = 400 + 1600 = 2000. Correct."),
    # 17: 5.12
    ("(d) 36", "Let CP = x, Profit% = x.<br>x(1 + x/100) = 96 => x^2 + 100x - 9600 = 0.<br>(x+160)(x-60) = 0 => CP = 60.<br>The options are for Profit amount. If CP=60, Profit = 36.", "Check options for Profit:<br>If Profit=36, CP=60. Profit% = 36/60 = 60%. CP=Profit%. Correct."),
    # 18: 5.13
    ("(b) 25", "Let CP = x, Profit% = x.<br>x(1 + x/100) = 31.25 => x^2 + 100x - 3125 = 0.<br>(x+125)(x-25) = 0 => CP = 25. Profit = 6.25.<br>The options likely represent CP, so 25 is the answer.", "Check options for CP:<br>If CP=25, Profit=25%.<br>SP = 25 + 25% of 25 = 25 + 6.25 = 31.25. Correct."),
    # 19: 5.14
    ("(c) 80", "Let CP = x, Profit% = x.<br>x(1 + x/100) = 144 => x^2 + 100x - 14400 = 0.<br>(x+180)(x-80) = 0 => CP = 80.<br>The options represent CP, so 80 is the answer.", "Check options for CP:<br>If CP=80, Profit=80%.<br>SP = 80 + 80% of 80 = 80 + 64 = 144. Correct."),
    # 20: 6
    ("(a) 8% Loss", "Let inv1 = 200, inv2 = 300.<br>Profit1 = 10% of 200 = 20.<br>Loss2 = 20% of 300 = -60.<br>Net = -40 on 500.<br>Net % = (-40 / 500) * 100 = -8%.", "Weighted average:<br>(2*10 + 3*(-20)) / (2+3) = (20 - 60)/5 = -40/5 = -8%."),
    # 21: 7
    ("(b) Rs.12,000", "Let total value = x.<br>(3/4)x * 8% + (1/4)x * (-4%) = 600.<br>x * (24% - 4%)/4 = 600 => x * (20%/4) = 600 => x * 5% = 600.<br>x = 600 / 0.05 = 12000.", "Weighted avg% = (3*8 - 1*4)/4 = 5%.<br>5% of Total = 600 => Total = 12000."),
    # 22: 8
    ("(c) 8 7/8", "Total CP = 4600 + 1800 = 6400.<br>Total Profit = 10% of 4600 + 6% of 1800 = 460 + 108 = 568.<br>Net Profit % = (568 / 6400) * 100 = 568 / 64 = 71/8 = 8 7/8 %.", "Profit = 460 + 108 = 568.<br>Profit% = 568 / 6400 = 71/8 = 8 7/8 %."),
    # 23: 9
    ("(d) 14.5", "Total CP = 9000 + 4000 = 13000.<br>Total desired profit = 10% of 13000 = 1300.<br>Profit on comp = 8% of 9000 = 720.<br>Required profit on center table = 1300 - 720 = 580.<br>Profit % = (580 / 4000) * 100 = 14.5%.", "Weighted avg:<br>(9*8 + 4*x) / 13 = 10 => 72 + 4x = 130 => 4x = 58 => x = 14.5."),
    # 24: 10
    ("(c) 36.1% Profit", "CP of 42 bananas = 6 * 6 = 36.<br>SP of 42 bananas = 7 * 7 = 49.<br>Profit = 49 - 36 = 13.<br>Profit % = (13 / 36) * 100 = 36.11%.", "Cross multiply:<br>CP: 7 for 6<br>SP: 6 for 7<br>CP = 6*6=36, SP = 7*7=49.<br>Profit% = 13/36 * 100 = 36.1%."),
    # 25: 11
    ("(c) 77.7% Profit", "CP of 12 bananas = 3 * 3 = 9.<br>SP of 12 bananas = 4 * 4 = 16.<br>Profit = 16 - 9 = 7.<br>Profit % = (7 / 9) * 100 = 77.77%.", "Cross multiply:<br>CP = 3*3=9. SP = 4*4=16.<br>Profit% = 7/9 * 100 = 77.7%."),
    # 26: 12
    ("(b) 1% Loss", "CP of 99 = 9*100 = 900. CP of 99 = 11*100 = 1100.<br>Total CP of 198 = 2000 => CP per fruit = 2000/198.<br>SP per fruit = 100/10 = 10.<br>Total SP of 198 = 1980. Loss = 20 on 2000 = 1%.", "Buy 11 for 100, 9 for 100. Mix = 198. CP = 2000.<br>SP = 1980 for 198. Loss 1%."),
    # 27: 13
    ("(b) 1080", "CP of 20 = 4, CP of 20 = 5. Total CP of 40 = 9. CP/pen = 9/40.<br>SP/pen = 2/9. Loss/pen = 9/40 - 2/9 = 1/360.<br>Total Loss = 3 => Total pens = 3 / (1/360) = 1080.", "Net loss per pen = 1/360.<br>Total pens = Total loss / loss per pen = 3 * 360 = 1080."),
    # 28: 9.1
    ("(a) 4:3", "SP = 72, Profit = 20% => CP = 72 / 1.2 = 60.<br>By Alligation on CP: Type1=45, Type2=80, Mean=60.<br>Ratio = (80-60) : (60-45) = 20 : 15 = 4 : 3.", "Mean CP = 72/1.2 = 60.<br>Alligation: (80-60)/(60-45) = 20/15 = 4:3."),
    # 29: 9.2
    ("(b) 5", "Total CP = 26*20 + 30*36 = 520 + 1080 = 1600.<br>Total SP = (26+30) * 30 = 56 * 30 = 1680.<br>Profit = 80.<br>Profit % = (80 / 1600) * 100 = 5%.", "CP = 1600. SP = 1680.<br>Profit% = 80/1600 = 5%."),
    # 30: 9.3
    ("(d) 27 7/9%", "Total CP = 300 * (18/12) = 450.<br>SP1 = 200 * (24/12) = 400. SP2 = 100 * (21/12) = 175.<br>Total SP = 575.<br>Profit = 125. Profit % = (125/450)*100 = 250/9 = 27 7/9%.", "Profit = 125 on 450.<br>Profit% = 125/450 = 27.77%."),
    # 31: 9.4
    ("(b) 25", "Let costlier wheat price = x.<br>5 * 18 + 2 * x = 7 * 20.<br>90 + 2x = 140 => 2x = 50 => x = 25.", "Alligation: (x - 20)/(20 - 18) = 5/2.<br>x - 20 = 5 => x = 25."),
    # 32: 9.5
    ("22.55", "Let costlier price = x.<br>2.5*18.75 + 2.75*x = 5.25*20.75.<br>46.875 + 2.75x = 108.9375 => 2.75x = 62.0625.<br>x = 22.568. Closest option is 22.55.", "Alligation: (x - 20.75)/(20.75 - 18.75) = 2.5 / 2.75 = 10/11.<br>x - 20.75 = 20/11 = 1.81. x ≈ 22.56."),
    # 33: 9.6
    ("(a) 12.32%", "CP_A = 4290 / 1.1 = 3900. Profit A = 390.<br>CP_B = 6156 / 1.14 = 5400. Profit B = 756.<br>Total CP = 9300. Total Profit = 1146.<br>Profit % = 1146 / 9300 * 100 = 12.32%.", "Total CP = 9300. Total Profit = 1146.<br>Profit% = 1146/9300 * 100 ≈ 12.32%."),
    # 34: 9.7
    ("c) 13 1/3%", "Parts: 2/3, 20% of 1/3 = 1/15, Remaining = 4/15.<br>Net Profit = (10/15)*26% + (1/15)*40% + (4/15)*(-25%).<br>= (260 + 40 - 100) / 15 = 200 / 15 = 40/3 = 13 1/3%.", "Net% = (10*26 + 1*40 - 4*25)/15 = 200/15 = 13 1/3%."),
    # 35: 9.8
    ("b) 20.6", "Profit currently = 45*12% + 75*25% = 5.4 + 18.75 = 24.15 CP units.<br>If 15% uniform, Profit = 120*15% = 18 CP units.<br>Diff = 6.15 * CP = 126.69 => CP = 126.69 / 6.15 = 20.6.", "Diff in profit% = 24.15x - 18x = 6.15x = 126.69 => x = 20.6.")
]

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, sol in enumerate(sols):
    idx = i + 6
    parts = lines[idx].split('\t')
    parts[1] = sol[0]
    parts[2] = sol[1]
    parts[3] = sol[2]
    lines[idx] = '\t'.join(parts)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)
