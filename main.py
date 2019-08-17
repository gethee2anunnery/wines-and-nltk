import nltk
import csv
from constants import DESCRIPTORS, ATTRS_TO_CAPTURE


def write_data_from_csv_to_dict():
	data = list()
	with open("winemag-data-130k-v2.csv", 'r') as file_data:
		csv_reader = csv.DictReader(file_data)
		for row in csv_reader:
			row_attrs = dict()
			counts = get_word_counts_from_description(row['description'])
			row_attrs['word_counts'] = counts
			for k, v in row.items():
				if k in ATTRS_TO_CAPTURE:
					row_attrs[k] = row[k]
			data.append(row_attrs)
	return data


def get_word_counts_from_description(row_description):
	word_counts = dict()
	words = row_description.split(' ')
	freq = nltk.FreqDist(words)
	for k, v in freq.items():
		if k in DESCRIPTORS:
			word_counts[k] = v
	return word_counts


def get_data():
	return write_data_from_csv_to_dict()


if __name__ == "__main__":
    get_data()
