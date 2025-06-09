def read_raw_file(filepath):
    with open(filepath, 'rb') as file:  # 'rb' means "read binary"
        data = file.read()
    return data

# Example usage:
filepath = 'example.png'  # Change to your file
raw_data = read_raw_file(filepath)

# Show first 100 bytes in hexadecimal
for byte in raw_data:
    print(format(byte, '08b'))
