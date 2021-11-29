import random

# to determine the greatest common divisor
def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return b

#test the prime numbers
def prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False

# generating the private key
def inverse(e,phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1*x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y
    if temp_phi == 1: 
        return d + phi

# # generating the public key 
def keypair(p,q):
    if not (prime(p) and prime(q)):
        print('Both numbers have to be prime numbers')
    elif p == q:
        print('p and q cannot be equal')
    
    n = p * q
    phi = (p - 1) * (q - 1)
   
    # choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)
    
    #use gcd to verify that e and phi are coprime
    f = gcd(e,phi)
    while f != 1:
        e = random.randrange (1, phi)
        f = gcd (e, phi)
    
    d = inverse(e, phi)

    # return public and private key pairs
    return ((e, n), (d, n))

def encrypt(k, plaintext):
    key, n = k
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

def decrypt(k, ciphertext):
    key,n = k
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain) #return the array of bites as a string

def main():
    print ('Encrypter & Decrypter')
    p = ("Enter a prime number: ")
    q = ("Enter another prime number: ")
    
    print ("Generating your private/public keypairs...")
    
    public, private = keypair(p,q)
    
    print ("Your public key is ",public ,"your private key is ",private)

    message = ('Enter your message: ')
    encrypted = encrypt(private, message)
    
    print ('Your encrypted message is: ', ''.join(map(lambda x: str(x), encrypted)))
    print ('Decrypt message with public key',public)
    print ('Your message is: ')
    print (decrypt(public, encrypted))
