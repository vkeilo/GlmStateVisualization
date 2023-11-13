def remove_duplicates_from_file(input_file_path, output_file_path):
    # This set will store the English sentences we have seen
    seen_english_sentences = set()
    unique_lines = []

    # Read the input file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Each line is expected to have an English sentence followed by its translation, separated by a tab
            if '\t' in line:
                english, _ = line.split('\t', 1)
                # Check if the English sentence has already been seen
                if english not in seen_english_sentences:
                    # If not, add it to the set of seen sentences and keep the line
                    seen_english_sentences.add(english)
                    unique_lines.append(line)
    
    # Write the unique lines to the output file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.writelines(unique_lines)

# Example file paths
input_file_path = 'datas/en_ch_trans_data'
output_file_path = 'datas/en_ch_trans_data_no_repeated'
remove_duplicates_from_file(input_file_path, output_file_path)
