import argparse

def lzw_compress(input_file, output_file, nb, n):
    """ 
    Perform LZW compression.
    
    Parameters
    ----------
    message : str
        the message to compress
    nb : int
        the number of bits used for each encoding
    n : int
        the size of the alphabet
        
    Returns
    -------
    compressed : list
       The encoded message
    """

    uncompressed_file = open(input_file)
    compressed_file = open(output_file, 'wb')
    
    max_code = 2**nb - 1 # size of the encoding table
    # Initialize table with encodings for each character
    # in the alphabet.
    table = { chr(i): i for i in range(n) }
    code = n # this is the encoding for the next unencoded ngram
    # The necessary bytes to store nb bits nb // 8 rounded up to
    # next integer; to do that, we add 7 to nb.
    num_bytes = (nb + 7) // 8 
    
    w = "" # current ngram
    for line in uncompressed_file:
        for c in line:
            wc = w + c # form new ngram
            # If we have already encountered the new ngram
            # prepare to add another character to it.
            if wc in table:
                w = wc
            else:
                # Otherwise we must put out the encoding of the
                # existing ngram.
                compressed_file.write(table[w].to_bytes(num_bytes,
                                                        byteorder='big'))
                # Start an ngram from the current character.
                w = c            
                # Check if we can add the non-found ngram
                # in the table and add it if possible.
                if code <= max_code:
                    table[wc] = code
                    code += 1
    # If we have finished the input file, output the encoding of the
    # current ngram.
    if w:
        compressed_file.write(table[w].to_bytes(num_bytes, byteorder='big'))
    
    uncompressed_file.close()
    compressed_file.close()


def lzw_decompress(input_file, output_file, nb, n):
    """ 
    Perform LZW decompression.
    
    Parameters
    ----------
    compressed : list
        the message to decompress
    nb : int
        the number of bits used for each encoding
    n : int
        the size of the alphabet
        
    Returns
    -------
    result : str
        The decompressed message
    """
   
    max_code = 2**nb - 1 # size of the decoding table
    # Initialize the decoding table with reverse encodings 
    # for each character in the alphabet.
    table = { i : chr(i) for i in range(n) }
    code = n # this is the encoding for the next unencoded ngram
    # The necessary bytes to store nb bits nb // 8 rounded up to
    # next integer; to do that, we add 7 to nb.
    num_bytes = (nb + 7) // 8
    
    compressed_file = open(input_file, 'rb')
    decompressed_file = open(output_file, 'w')
    # Output the first character.
    bytes = compressed_file.read(num_bytes)
    c = int.from_bytes(bytes, byteorder='big')
    v = table[c]
    decompressed_file.write(v)
    pv = v # previous
    
    # For each encoded value in the compressed message:
    bytes = compressed_file.read(num_bytes)
    while bytes:
        c = int.from_bytes(bytes, byteorder='big')
        # If we know the corresponding ngram, get it.
        if c in table:
            v = table[c]
        # If we do not know it, the corresponding ngram
        # is really the previous ngram with its first
        # character appended to its end.
        else:
            v = pv + pv[0]

        decompressed_file.write(v)

        # If there is room in the decoding table:
        if code <= max_code:
            # add the new mapping to it.
            table[code] = pv + v[0]
            code += 1
            
        pv = v
        bytes = compressed_file.read(num_bytes)

    decompressed_file.close()
    compressed_file.close()

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description=
                                     "LZW compression/decompression")

    parser.add_argument('input_file', help='Input file')
    parser.add_argument('output_file', help='Output file')
    parser.add_argument("-d", "--decompress", help="decompress",
                        default=False,
                        action="store_true")
    parser.add_argument("-n", "--nb", help="number of bits of each table entry",
                        type=int, default=16)
    parser.add_argument("-s", "--size", help="size of alphabet",
                        type=int, default=2**8)

    args = parser.parse_args()

    if (args.decompress):
        lzw_decompress(args.input_file, args.output_file, args.nb, args.size)
    else:
        lzw_compress(args.input_file, args.output_file, args.nb, args.size)
