import csv as csv
import numpy as np

csv_file_object = csv.reader(open('train.csv','rU'))
header = next(csv_file_object)

data = []

for row in csv_file_object:
	data.append(row)

data = np.array(data)

fare_ceiling = 40

data[data[0::,9].astype(np.float) >= fare_ceiling, 9] = fare_ceiling - 1.0

fare_bracket_size = 10

number_of_price_buckets = fare_ceiling / fare_bracket_size

number_of_classes = len(np.unique(data[0::,2]))

survival_table = np.zeros((2, number_of_classes, number_of_price_buckets))

for i in range(number_of_classes):
	for j in range(int(number_of_price_buckets)):
		women_only_stats = data[(data[0::,4] == 'female') 
								& (data[0::,2].astype(np.float) == i+1) \
								& (data[0::,9].astype(np.float) >= j*fare_bracket_size) \
								& (data[0::,9].astype(np.float) < (j+1) * fare_bracket_size), 1]

		men_only_stats = data[(data[0::,4] != 'female')
								& (data[0::,2].astype(np.float) == i+1) \
								& (data[0::,9].astype(np.float) >= j*fare_bracket_size) \
								& (data[0::,9].astype(np.float) < (j+1) * fare_bracket_size),1]

survival_table[0,i,j] = np.mean(women_only_stats.astype(np.float))
survival_table[1,i,j] = np.mean(men_only_stats.astype(np.float))

survival_table[survival_table != survival_table] = 0

survival_table[survival_table >= .5] = 1
survival_table[survival_table < .5] = 0

test_file = open('test.csv','rU')
test_file_object = csv.reader(test_file)
header = next(test_file_object)

precition_file = open('classgendermodel1.csv','w')
p = csv.writer(precition_file)
p.writerow(['PassengerId', 'Survived'])


for row in test_file_object:
	for j in range(int(number_of_price_buckets)):
		try:
			row[8] = float(row[8])

		except:
			bin_fare = 3 - float(row[1])
			break

		if row[8] > fare_ceiling:
			bin_fare = number_of_price_buckets - 1
			break

		if row[8] >= j * fare_bracket_size \
		and row[8] < (j+1) * fare_bracket_size:
			bin_fare = j
			break

if row[3] == 'female':
	p.writerow([row[0], '%d' % int(survival_table[0, float(row[1])-1, bin_fare])])

else:
	p.writerow([row[0], '%d' % int(survival_table[1, float(row[1])-1, bin_fare])])


test_file.close()
precition_file.close()
