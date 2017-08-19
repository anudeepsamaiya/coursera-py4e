import re

filename = 'regex_sum_20223.txt'

handle = open(filename, 'r')
# numbers = []
# for line in handle:
#     matches = re.findall('[0-9]+', line)
#     if not len(matches) > 0: continue
#     for x in matches:
#         numbers.append(int(x))
#
# print(sum(numbers))
test = handle.read()
print(sum(int(x) for x in re.findall('[0-9]+', test)))
