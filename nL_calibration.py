import csv

# ----------------------------------------------------------------------
# GETTING READINGS FROM XL-500 SENSOR
# ----------------------------------------------------------------------

nL_XL_readings = []

# read through the csv file
with open('XL500_data/XLdata1.csv') as nL_XL:
    reader = csv.reader(nL_XL, delimiter=',')
    row = 0
    for lst in reader:
        if row == 7:
            nL_XL_readings = lst[1:]
        row += 1
# convert data into float values and round to 13 decimal places
i = 0
while i < len(nL_XL_readings):
    rounded = round(float(nL_XL_readings[i]), 13)
    nL_XL_readings[i] = rounded
    i += 1
# print(nL_XL_readings)

# ----------------------------------------------------------------------
# GETTING READINGS FROM NSP32 SENSOR
# ----------------------------------------------------------------------

nL_NSP_readings = []

# read through the csv file
with open('NSP32_data/NSPdata1.csv') as nL_NSP:
    reader = csv.reader(nL_NSP, delimiter=',')
    row = 0
    for lst in reader:
        if row == 5:
            nL_NSP_readings = lst[:len(lst) - 1]
        row += 1
# convert data into float values and round to 13 decimal places
i = 0
while i < len(nL_NSP_readings):
    rounded = round(float(nL_NSP_readings[i]), 13)
    nL_NSP_readings[i] = rounded
    i += 1
# print(nL_NSP_readings)

# ----------------------------------------------------------------------
# CALCULATING THE CONSTANT OF PROPORTIONALITY (ASSUMING LINEAR RELATION)
# ----------------------------------------------------------------------

ratios = []

i = 0
while i < 135: # there are 135 data points
    if nL_XL_readings[i] == 0.0:
        ratios.append(0.0)
    else:
        ratio = nL_NSP_readings[i] / nL_XL_readings[i]
        ratios.append(ratio)
    i += 1
print(ratios)
print(len(ratios))