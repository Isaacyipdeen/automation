

if __name__ == "__main__":
    # Read data from the text file (modify the file path accordingly)
    file_path = "data.txt"
    
    data_list = []

with open('data.txt', 'r') as file:
    lines = file.read().split('\n\n')  # Assumes paragraphs are separated by two newlines
    
    for paragraph in lines:
        paragraph_dict = {}
        for i, line in enumerate(paragraph.split('\n'), 1):
            paragraph_dict[f'key{i}'] = line.strip()
        data_list.append(paragraph_dict)

# Print the resulting list of dictionaries
#print(data_list)


for paragraph_dict in data_list:
    for key, value in paragraph_dict.items():
        print(f'{key}: {value}')

    # Add a newline for better readability between paragraphs
    print()
    

x = (type(data_list[2].get('key3')))

print (x)

if x is type(None):
    print ("NO")
else:
    print ("Yes")


for a in range((len(data_list))):
    print (a)