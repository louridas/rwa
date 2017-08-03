from collections import Counter

import pickle
import argparse

def create_pq():
    return []

def add_last(pq, c):
    pq.append(c)

def root(pq):
    return 0

def set_root(pq, c):
    if len(pq) == 0:
        pq = [c]
    else:
        pq[0] = c

def get_data(pq, c):
    return pq[c]

def children(pq, c):
    if 2*c + 2 < len(pq):
        return [2*c + 1, 2*c + 2]
    else:
        return [2*c + 1]

def parent(c):
    return (c - 1) // 2

def exchange(pq, c, p):
    pq[c], pq[p] = pq[p], pq[c]

def insert_in_pq(pq, c):
    add_last(pq, c)
    i = len(pq) - 1
    while i != root(pq) and get_data(pq, i) < get_data(pq, parent(i)):
        p = parent(i)
        exchange(pq, i, p)
        i = p

def extract_last_from_pq(pq):
    return pq.pop()

def has_children(pq, c):
    return 2*c + 1 < len(pq)

def extract_min_from_pq(pq):
    c = pq[root(pq)]
    set_root(pq, extract_last_from_pq(pq))
    i = root(pq)
    while has_children(pq, i):
        # Use the data stored at each child as the comparison key
        # for finding the minimum.
        j = min(children(pq, i), key=lambda x: get_data(pq, x))
        if get_data(pq, i) < get_data(pq, j):
            return c        
        exchange(pq, i, j)
        i = j
    return c

def create_huffman_code(pq):
    while len(pq) > 1:
        # Extract the two minimum items from the priority queue.
        x = extract_min_from_pq(pq)
        y = extract_min_from_pq(pq)
        # Get all the [character, encoding] items associated with x;
        # as x is the left child of the new node, prepend '0'
        # to their encodings.
        for pair in x[1:]:
            pair[1] = '0' + pair[1]
        # Do the same for y; as y is the right child of the 
        # new node, prepend '1' to their encodings.
        for pair in y[1:]:
            pair[1] = '1' + pair[1]
        # Insert a new node with the sum of the occurrences
        # of the two extracted nodes and the updated 
        # [character, encoding] sequences.
        insert_in_pq(pq, [x[0] + y[0]] + x[1:] + y[1:])
    return extract_min_from_pq(pq)

def huffman_compress(input_file, output_file):
    pq = create_pq()
    # First pass: count character occurrences.
    symb2freq = Counter()
    with open(input_file) as uncompressed_file:
        for line in uncompressed_file:
            symb2freq += Counter(line)
    # Put the occurrences in a priority queue.
    pq = create_pq()
    for key, value in symb2freq.items():
        insert_in_pq(pq, [value, [key, '']])
    # Create the Huffman code.
    hc = create_huffman_code(pq)
    # Turn the code to a dictionary for easier lookup.
    hc_table = { character: encoding for [character, encoding] in  hc[1:]}
    # Second pass: we'll read again the uncompressed file,
    # we'll compress the contents and save them to the
    # compressed file as we go.
    with open(input_file) as uncompressed_file, \
        open(output_file, 'wb') as compressed_file:
        # First save the Huffman encoding.
        pickle.dump(hc_table, compressed_file)
        # Then save the total number of characters in the input file.
        pickle.dump(sum(symb2freq.values()), compressed_file)
        # Use a buffer in which we will be adding the encoded characters;
        # when the buffer has 8 bits or more we will output a byte and
        # keep the remaining bits.
        buffer = ''
        for line in uncompressed_file:
            for c in line:
                # For each character, add the encoding to the buffer.
                buffer += hc_table[c]
                # Have we got enough stuff in the buffer to output a byte?
                while len(buffer) >= 8:
                    # Yes, output a byte
                    byte = int(buffer[:8], base=2).to_bytes(1, byteorder='big')
                    compressed_file.write(byte)
                    # Keep any remaining stuff in the buffer; that will go out
                    # with the next byte.
                    buffer = buffer[8:]
        if len(buffer) > 0:
            # If we have still remaining stuff, it means that part of the last 
            # character encoding was put in the previous byte, and part of it
            # will go in the last byte; we'll pad zeroes to the end of it.
            buffer = buffer.ljust(8, '0')
            byte = int(buffer[:8], base=2).to_bytes(1, byteorder='big')
            compressed_file.write(byte)

def huffman_decompress(input_file, output_file):
    with open(input_file, 'rb') as compressed_file,\
        open(output_file, 'w') as decompressed_file:
        # Read the Huffman table.
        hc_table = pickle.load(compressed_file)
        # Read the total number of uncompressed characters.
        num_chars = pickle.load(compressed_file)
        # Construct an inverse, Huffman decoding table.
        hc_decoding_table = { v: k for (k, v) in hc_table.items() }
        # Set a counter for the decompressed characters.
        num_decompressed = 0
        # Keep the Huffman code that we want to decode.
        encoding = ''
        # Read the file byte-by-byte.
        byte = compressed_file.read(1)
        while byte:
            # For each byte, get its bit representation.
            bit_repr = format(int.from_bytes(byte, byteorder='big'), '08b')
            # Then read it bit-by-bit, extending the current encoding
            # that we are trying to decode.
            for bit in bit_repr:
                encoding += bit
                # Is this a valid Huffman encoding?
                if encoding in hc_decoding_table:
                    # Yes, decompress it.
                    decompressed_file.write(hc_decoding_table[encoding])
                    num_decompressed += 1
                    # If we have decompressed the expected amount of
                    # characters, we are done; any leftover is just the
                    # padding of the last byte of the file.
                    if num_decompressed == num_chars:
                        break
                    encoding = ''
            byte = compressed_file.read(1)

parser = argparse.ArgumentParser(description=
                                 'Huffman compression/decompression')

parser.add_argument('input_file', help='Input file')
parser.add_argument('output_file', help='Output file')
parser.add_argument('-d', '--decompress',
                    action='store_true',
                    help='Decompress',
                    default=False)

args = parser.parse_args()

if args.decompress:
    huffman_decompress(args.input_file, args.output_file)
else:
    huffman_compress(args.input_file, args.output_file)
