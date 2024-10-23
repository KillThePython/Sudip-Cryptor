from cryptograph import *
import sys, os


try:
    key = generate_key()
    manager = CryptographyManager(key.encode(), layers=int(sys.argv[2]))

    if sys.argv[3] == "-e":
        data = read_from_file(sys.argv[4])
        os.remove(sys.argv[4])
        encrypted_data = manager.encrypt(data)
        write_to_file(sys.argv[4] + '.sudip', encrypted_data)

        print("Encrypted file saved as:", sys.argv[4] + '.sudip')
        print("You will need this key to decrypt the file:", key)

    elif sys.argv[3] == "-d":
        key = input("Enter the key: ")
        manager = CryptographyManager(key.encode(), layers=int(sys.argv[2]))

        data = read_from_file(sys.argv[4]).encode()
        os.remove(sys.argv[4])
        decrypted_data = manager.decrypt(data)
        write_to_file(sys.argv[4].replace('.sudip', ''), decrypted_data)

        print("Decrypted file saved as:", sys.argv[4].replace('.sudip', ''))

    else:
        print("Usage: python3 main.py -l <layers> -e/-d '<filepath>'")
        sys.exit(1)

    input("Press enter to exit...")

except IndexError:
    print("Usage: python3 main.py -l <layers> -e/-d '<filepath>'")
    sys.exit(1)
    
except FileNotFoundError:
    print("File not found")
    sys.exit(1)