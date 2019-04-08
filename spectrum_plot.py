import matplotlib.pyplot as plt
from data_processing_for_chart import *

# ======================================
line_style = ('-', '--', '-.')
# ======================================

file_name = "./content/405_r.csv"
x, y, header = parsing_csv(file_name, 550, 650)

print(header)

y2 = []
y2.append(y[2])
y2.append(y[3])
y.pop(3)
y.pop(2)


y = delete_const(y)
y = normalize_all_to_one(y)


ff = find_cross(x, y[1], 0.5)
print(ff)
print(ff[1]-ff[0])
print(ff[3]-ff[2])

plt.subplot(1, 1, 1)
plt.plot(x, y[1], 'k'+line_style[0], label="150 "+chr(176)+"C", linewidth=1)
plt.plot(x, y[0], 'k'+line_style[1], label="70 "+chr(176)+"C", linewidth=1)
plt.axvline(589, color='k', linewidth=0.5)
plt.text(589.01, 1.03, r"$D_2$", fontsize=11)
plt.axvline(589.6, color='k', linewidth=0.5)
plt.text(589.61, 1.03, r"$D_1$", fontsize=11)
plt.legend()
plt.xlim(588, 590.5)
plt.ylim(0, 1.1)
plt.xlabel(chr(955)+", нм")
plt.ylabel("H, от. ед.")
plt.grid()
# plt.savefig(file_name[0:-4]+'_1.png')
plt.show()

y2 = delete_const(y2)
y2 = normalize_all_to_one(y2)

ff = find_cross(x, y2[0], 0.4)
print(ff)
print(ff[1]-ff[0])
print(ff[3]-ff[2])

plt.subplot(1, 1, 1)
plt.plot(x, y2[0], 'k'+line_style[0], label="150 "+chr(176)+"C", linewidth=1)
plt.plot(x, y2[1], 'k'+line_style[1], label="80 "+chr(176)+"C", linewidth=1)
plt.axvline(589, color='k', linewidth=0.5)
plt.text(589.01, 1.03, r"$D_2$", fontsize=11)
plt.axvline(589.6, color='k', linewidth=0.5)
plt.text(589.61, 1.03, r"$D_1$", fontsize=11)
plt.legend()
plt.xlim(588, 590.5)
plt.ylim(0, 1.1)
plt.xlabel(chr(955)+", нм")
plt.ylabel("H, от. ед.")
plt.grid()
# plt.savefig(file_name[0:-4]+'_2.png')
plt.show()

