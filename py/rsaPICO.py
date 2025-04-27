q = 2 
p = 10502777974083015098550155967722755460043406571368148399148141794335271603649940234324769286480063618943979875387264596053808302401992600346064916122762159
e = 65537
ct = 10382026118703909851481900839401709731010469344503351968828906871801429941617722415336958916285256156655801895280988617431125102155961034094501379518602805
N = 21005555948166030197100311935445510920086813142736296798296283588670543207299880468649538572960127237887959750774529192107616604803985200692129832245524318

tot = (p-1)*(q-1)

# Calculate d, the private key
d = pow(e, -1, tot)

# Decrypt the message
m = pow(ct, d, N)

# Convert the decrypted integer m to bytes
# You need to know how many bytes to use. We typically use the number of bytes in N.
byte_length = (N.bit_length() + 7) // 8  # The number of bytes needed to represent N

# Convert to bytes
message_bytes = m.to_bytes(byte_length, byteorder='big')

# If it's text (assuming UTF-8 encoding):
try:
    message_text = message_bytes.decode('utf-8')
    print("Decrypted Message (Text):", message_text)
except UnicodeDecodeError:
    print("Decrypted Message (Bytes):", message_bytes)
