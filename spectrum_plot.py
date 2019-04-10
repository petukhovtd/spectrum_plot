import matplotlib.pyplot as plt
from data_processing_for_chart import *

# ======================================
line_style = ('-', '--', '-.', ':')
# ======================================

file_name = "./content/405_r.csv"
x, y, header = parsing_csv(file_name, 300, 1000)

print("Header:\n", header)

y = delete_const(y)
# y = normalize_all_to_one(y)
y = normalize_all_by_self(y)

# ff = find_cross(x, y[0], 0.5)
# print_cross(ff)


plt.subplot(1, 1, 1)
for i in range(len(y)):
	plt.plot(x, y[i], label=header[i+1])
# plt.plot(x, y[0], 'k'+line_style[0], label="70 "+chr(176)+"C", linewidth=1)
# plt.axvline(589, color='k', linewidth=0.5)
# plt.text(589.01, 1.03, r"$D_2$", fontsize=11)
# plt.axvline(589.6, color='k', linewidth=0.5)
# plt.text(589.61, 1.03, r"$D_1$", fontsize=11)
plt.legend()
# plt.xlim(588, 590.5)
plt.ylim(0, 1.1)
plt.xlabel(chr(955)+", нм")
plt.ylabel("H, от. ед.")
plt.grid()
# plt.savefig(file_name[0:-4]+'_1.png')
plt.show()

