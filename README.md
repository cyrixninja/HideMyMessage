# Hide My Message

Hide My Message is a web application that allows users to send and receive messages in a unique way. The application uses steganography, a method of hiding information within non-secret data, to hide messages within image files. This provides an additional layer of security for the messages, as they are not visible without the correct key.

## Features

### To Encrypt a Message

Users can send a message by selecting an image file and entering their message. The application will then hide the message within the image file and provide a download link for the new image file. The original image file is not modified.

To send a message:

1. Click on the "Select an image" button and choose an image file from your device.
2. Enter your message in the "Enter a message" field.
3. Click on the "Submit" button. The application will hide your message within the image file and provide a download link for the new image file.

### To Decrypt a Message

Users can receive a message by uploading the image file that contains the hidden message. The application will extract the message from the image file and display it.

To receive a message:

1. Click on the "Image" button and choose the image file that contains the hidden message.
2. Enter the key in the "Key" field.
3. Click on the "Submit" button. The application will extract the message from the image file and display it.

## Technology

Hide My Message is built with HTML, CSS, and JavaScript on the front-end, and Python on the back-end. It uses the Flask web framework and the Bootstrap CSS framework.

## Security

Hide My Message uses steganography to hide messages within image files. This provides an additional layer of security for the messages, as they are not visible without the correct key. However, it is still important to use strong, unique keys to ensure the security of your messages.


# Mathematical Concepts in Hide My Message

Hide My Message uses a combination of steganography and encryption to hide messages within image files. Both of these techniques involve mathematical concepts.

## Steganography

Steganography is the practice of concealing a message within another message or a physical object. In computing, steganography often involves hiding data within digital images, audio tracks, video clips, or other files.

The mathematical concept behind steganography is quite simple. Digital images are made up of pixels, and each pixel is represented by three color values (red, green, and blue). Each color value is an 8-bit number, meaning it can range from 0 to 255.

When hiding a message within an image, the least significant bit (LSB) of each color value can be changed to a bit from the message. This change is so small that it's virtually undetectable to the human eye, but it allows for a large amount of data to be hidden within the image.

## Encryption

Encryption is the process of encoding a message so that only authorized parties can read it. This is typically done using an encryption algorithm and a key.

There are many different encryption algorithms, but most of them involve some form of mathematical operation, such as addition, multiplication, or modular arithmetic. For example, the Caesar cipher is a simple encryption algorithm that involves shifting each letter in the message by a certain number of places.

More complex encryption algorithms, such as AES (Advanced Encryption Standard), involve multiple rounds of substitution, permutation, and mixing to transform the plaintext message into ciphertext.

In the context of Hide My Message, the encryption key is used both to encrypt the message before it's hidden within the image, and to decrypt the message after it's extracted from the image. This ensures that even if someone discovers the hidden message, they won't be able to read it without the key.

# AES Encryption

![AES](/static/image/2.jpg)

AES, or Advanced Encryption Standard, is a symmetric encryption algorithm that was established by the U.S. National Institute of Standards and Technology (NIST) in 2001. It is widely regarded as the most secure symmetric encryption algorithm available today and is used worldwide by governments, cybersecurity experts, and organizations to protect sensitive data.

## How AES Works

![AES](/static/image/1.jpg)

AES operates on blocks of data and uses a series of transformations, including substitution, permutation, and mixing, to convert plaintext into ciphertext. The same key is used for both encryption and decryption, making it a symmetric encryption algorithm.

Here's a brief overview of the steps involved in AES encryption:

1. **SubBytes**: Each byte in the block is replaced with its entry in a fixed substitution table, the Rijndael S-box.

2. **ShiftRows**: The bytes in each row of the block are shifted cyclically to the left. The number of places each byte is shifted differs for each row.

3. **MixColumns**: Each column of the block is mixed using a transformation function. This function takes four bytes as input and outputs four bytes, where each input byte affects all four output bytes.

4. **AddRoundKey**: The result is combined with a round key using bitwise exclusive OR (XOR).

These steps are repeated for a number of rounds. The number of rounds depends on the key size: 10 rounds for a 128-bit key, 12 rounds for a 192-bit key, and 14 rounds for a 256-bit key.

## Security of AES

AES is considered to be very secure. The largest successful brute-force attack against AES encryption was against a 128-bit key and required over a billion years of computing time. AES-256, with its larger key size, is even more secure.

However, like all encryption algorithms, AES is not impervious to all attacks. Side-channel attacks, which exploit information gained from the physical implementation of the cryptosystem, can be effective against AES. Proper implementation and key management are crucial for maintaining the security of an AES-encrypted system.


# LSB Steganography

![AES](/static/image/3.png)

LSB Steganography is a common method of hiding data within digital media files. The term "Least Significant Bit" refers to the bit in a binary representation of a number that has the smallest value. In the context of digital images, each pixel is represented by three color values (red, green, and blue), and each color value is an 8-bit number.

In LSB Steganography, the least significant bit of each color value can be changed to a bit from the hidden message. This change is so small that it's virtually undetectable to the human eye, but it allows for a large amount of data to be hidden within the image.

Here's a step-by-step process of how LSB Steganography works:

1. Convert the hidden message into a binary format.
2. For each bit in the binary message:
    - Find a pixel with three color values (red, green, blue).
    - Replace the least significant bit of each color value with a bit from the message.

The hidden message can then be retrieved by reversing this process. LSB Steganography is a simple yet effective method of steganography, and it's widely used due to its simplicity and the difficulty in detecting the hidden message.