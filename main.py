# main.py
from cryptograph import CryptographyManager, generate_key, read_file, write_file
import argparse
import os
import sys
from getpass import getpass
import logging


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


def parse_arguments():
    parser = argparse.ArgumentParser(description='File encryption/decryption tool')
    parser.add_argument('-l', '--iterations', type=int, default=3,
                        help='Number of encryption/decryption iterations')
    parser.add_argument('mode', choices=['encrypt', 'decrypt'],
                        help='Operation mode: encrypt or decrypt')
    parser.add_argument('filepath', help='Path to the file')
    return parser.parse_args()


def main():
    setup_logging()
    args = parse_arguments()

    try:
        if args.mode == 'encrypt':
            # Generate new key and create manager
            key = generate_key()
            manager = CryptographyManager(key, iterations=args.iterations)

            # Read and encrypt file
            data = read_file(args.filepath)
            encrypted_data = manager.encrypt(data)

            # Generate output filename
            output_path = f"{args.filepath}.sudip"
            write_file(output_path, encrypted_data)

            # Securely store or display the key
            logging.info(f"File encrypted successfully: {output_path}")
            logging.info("IMPORTANT: Store this key safely. You will need it to decrypt the file:")
            print(f"\nKEY: {key}\n")

            # Optionally remove original file
            if input("Delete original file? (y/n): ").lower() == 'y':
                os.remove(args.filepath)
                logging.info("Original file deleted")

        else:  # decrypt mode
            # Get key from user
            key = getpass("Enter decryption key: ")
            manager = CryptographyManager(key, iterations=args.iterations)

            # Read and decrypt file
            encrypted_data = read_file(args.filepath)
            try:
                decrypted_data = manager.decrypt(encrypted_data)
            except Exception as e:
                logging.error("Decryption failed. Invalid key or corrupted file.")
                sys.exit(1)

            # Generate output filename (remove .encrypted extension if present)
            output_path = args.filepath.replace('.sudip', '')
            if output_path == args.filepath:
                output_path = f"decrypted_{os.path.basename(args.filepath)}"

            write_file(output_path, decrypted_data)
            logging.info(f"File decrypted successfully: {output_path}")

            # Optionally remove encrypted file
            if input("Delete encrypted file? (y/n): ").lower() == 'y':
                os.remove(args.filepath)
                logging.info("Encrypted file deleted")

    except FileNotFoundError:
        logging.error(f"File not found: {args.filepath}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
