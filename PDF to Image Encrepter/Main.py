# import pdf2image
import numpy as np


# def pdf_to_image(pdf_file):
#     """
#     Converts a PDF file to an image.

#     Args:
#       pdf_file: The path to the PDF file.

#     Returns:
#       The image as a numpy array.
#     """

#     images = pdf2image.convert_from_path(pdf_file)
#     image = images[0]

#     return image


def f5_encode(image, secret):
    """
    Encodes the secret message into the image using the F5 algorithm.

    Args:
      image: The image as a numpy array.
      secret: The secret message as a string.

    Returns:
      The stego image as a numpy array.
    """

    secret_len = len(secret)
    row_len = image.shape[0]
    col_len = image.shape[1]

    # Create a matrix to store the secret message.
    secret_matrix = np.zeros((row_len, col_len), dtype=int)

    # Embed the secret message into the image.
    for i in range(row_len):
        for j in range(col_len):
            secret_matrix[i][j] = secret[i * col_len + j]

    # Convert the secret matrix to a numpy array.
    stego = secret_matrix.astype(np.uint8)

    return stego


def f5_decode(stego):
    """
    Decodes the secret message from the stego image using the F5 algorithm.

    Args:
      stego: The stego image as a numpy array.

    Returns:
      The secret message as a string.
    """

    row_len = stego.shape[0]
    col_len = stego.shape[1]

    # Create a matrix to store the secret message.
    secret_matrix = np.zeros((row_len, col_len), dtype=int)

    # Extract the secret message from the stego image.
    for i in range(row_len):
        for j in range(col_len):
            secret_matrix[i][j] = stego[i * col_len + j]

    # Convert the secret matrix to a string.
    secret = ''.join([chr(i) for i in secret_matrix.flatten()])

    return secret


def main():
    # Convert the PDF file to an image.
    # image = pdf_to_image('secret.pdf')

    # Encode the secret message into the image.
    stego = f5_encode(image, 'This is a secret message.')

    # Save the stego image.
    imageio.imsave('stego.png', stego)


if __name__ == '__main__':
    main()
