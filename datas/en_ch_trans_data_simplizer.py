# Read the file
with open('datas/en_ch_trans_data', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Process each line and extract the original text and its translation
processed_lines = []
for line in lines:
    parts = line.strip().split('\t')
    if len(parts) == 4:
        original_text = parts[1]  # The original text
        translation = parts[3]    # The translated text
        processed_lines.append(f"{original_text}\t{translation}")

# Write the processed lines to a new file
with open('datas/simplized_trans_data.txt', 'w', encoding='utf-8') as outfile:
    for processed_line in processed_lines:
        outfile.write(processed_line + '\n')
