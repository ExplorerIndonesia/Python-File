# Opening file with 'r' (read) mode
with open('file.txt', 'r') as file:
    # Reading file content
    content = file.read()
    print('File content:', content)

# Opening file with 'w' (write) mode
with open('file.txt', 'w') as file:
    # Writing text to file
    file.write('Hello, world!')
    print('Text has been written to file.')

# Opening file with 'a' (append) mode
with open('file.txt', 'a') as file:
    # Appending text to file
    file.write('\nAdditional text.')
    print('Additional text has been added to file.')

# Opening file with 'rb' (read binary) mode
with open('file.txt', 'rb') as file:
    # Reading file content in binary format
    content = file.read()
    print('File content in binary format:', content)

# Opening file with 'wb' (write binary) mode
with open('file.txt', 'wb') as file:
    # Writing binary data to file
    byte_data = b'Hello, world!'
    file.write(byte_data)
    print('Binary data has been written to file.')

# Opening file with 'ab' (append binary) mode
with open('file.txt', 'ab') as file:
    # Appending binary data to file
    byte_data = b'\nAdditional binary data.'
    file.write(byte_data)
    print('Additional binary data has been added to file.')
