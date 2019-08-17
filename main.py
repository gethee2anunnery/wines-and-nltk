import nltk
import csv
from constants import DESCRIPTORS, ATTRS_TO_CAPTURE

def main():
	with open("winemag-data-130k-v2.csv", 'r') as file_data:
		csv_reader = csv.DictReader(file_data)
		for row in csv_reader:
			row_attrs = dict()
			counts = get_word_counts_from_description(row['description'])
			row_attrs['word_counts'] = counts
			for k, v in row.items():
				if k in ATTRS_TO_CAPTURE:
					row_attrs[k] = row[k]
			print row_attrs


def get_word_counts_from_description(row_description):
	word_counts = dict()
	words = row_description.split(' ')
	freq = nltk.FreqDist(words)
	for k, v in freq.items():
		if k in DESCRIPTORS:
			word_counts[k] = v
	return word_counts




if __name__ == "__main__":
    main()