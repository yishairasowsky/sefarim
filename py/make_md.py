from os import path

file_name = 'eicha' # changeable
input_file = path.join('txt',file_name + '.txt')

with open(input_file, 'r') as file:
    content = file.readlines()

output_lst = []
output_lst.append('|||')
output_lst.append('|-:|:-|')

section = []
for line in content:
    # if True:
    if line != '\n':
    # if section == []:
        section.append(line)
    if line == '\n':
        num_phrases = int(len(section)/2)
        hebrew_section = section[:num_phrases]
        english_section = section[num_phrases:]

        for phrase_tuple in zip(hebrew_section,english_section):
            phr_heb = phrase_tuple[0].strip()
            phr_eng = phrase_tuple[1].strip()
            curr_row = f'|{phr_heb}|{phr_eng}|'
            output_lst.append(curr_row)
            pass

        output_lst.append('\n')
        output_lst.append('|||')
        output_lst.append('|-:|:-|')
        section = []
        pass

output_str = '\n'.join(output_lst)

output_file = path.join('md',file_name + '_test.md')

with open(output_file, 'w') as file:
    file.write(output_str)
