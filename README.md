# 🔐 Sudip Cryptor

A powerful, military-grade file encryption tool that provides uncompromising security through multiple layers of AES-GCM encryption. Created with a focus on security, usability, and reliability.

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Security](https://img.shields.io/badge/security-AES--GCM-orange.svg)
![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Maintained](https://img.shields.io/badge/maintained-yes-green.svg)

<div align="center">
  <img src="/api/placeholder/800/400" alt="Sudip Cryptor Banner">
  <p><i>Secure your files with confidence using Sudip Cryptor</i></p>
</div>

## ✨ Key Features

- 🔒 **Military-Grade Security**: Implements AES-GCM (Galois/Counter Mode) encryption
- 🔄 **Multi-Layer Protection**: Customizable encryption iterations for enhanced security
- 📦 **Universal File Support**: Seamlessly handles any file type and size
- 🔑 **Advanced Key Management**: Utilizes PBKDF2 key derivation with SHA-256
- 🎯 **Simple Interface**: Easy-to-use command-line interface
- 📝 **Detailed Logging**: Comprehensive operation tracking
- 🛡️ **Robust Protection**: Built-in error handling and validation

## 🚀 Installation

1. Clone the Sudip Cryptor repository:
```bash
git clone https://github.com/KillThePython/Sudip-Cryptor.git
cd Sudip-Cryptor
```

2. Set up a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## 📋 Requirements

```
cryptography>=39.0.0
```

## 💻 Usage

### Encrypt Your Files

```bash
python main.py encrypt path/to/your/file -l 3
```
- `-l` sets the number of encryption layers (default: 3)
- A unique encryption key will be generated and displayed
- ⚠️ **Critical**: Store your encryption key securely!

### Decrypt Your Files

```bash
python main.py decrypt path/to/encrypted/file -l 3
```
- Use identical number of layers (-l) as encryption
- You'll need to enter your saved encryption key

### Available Commands

```
usage: main.py [-h] [-l ITERATIONS] {encrypt,decrypt} filepath

arguments:
  {encrypt,decrypt}      Choose operation: encrypt or decrypt
  filepath              Path to target file

optional arguments:
  -h, --help           Show help message
  -l, --iterations     Set encryption/decryption layers (default: 3)
```

## 🔒 Security Architecture

- **AES-GCM**: Authenticated encryption providing confidentiality and integrity
- **PBKDF2**: Military-grade key derivation using SHA-256
- **Layered Security**: Multiple encryption iterations
- **Nonce Generation**: Unique nonce for each encryption layer
- **Secure Processing**: Binary-safe operations supporting all file types

## ⚠️ Security Best Practices

1. **Key Management**: Store encryption keys in a secure, offline location
2. **Iteration Selection**: Higher iterations = stronger security + longer processing
3. **Backup Strategy**: Always maintain backups of important files
4. **Key Storage**: Never store encryption keys in plain text or share them online

## 📝 Example Workflow

```bash
# Encrypting a confidential document
python main.py encrypt documents/confidential.pdf -l 3

# The process will:
# 1. Apply multi-layer encryption
# 2. Save as documents/confidential.pdf.sudip
# 3. Generate and display your unique key
# 4. Offer to remove the original file

# Decrypting your document
python main.py decrypt documents/confidential.pdf.sudip -l 3

# The process will:
# 1. Request your encryption key
# 2. Verify and decrypt the file
# 3. Restore the original file
# 4. Offer to remove the encrypted version
```

## 🤝 Contributing

Want to make Sudip Cryptor even better? Contributions are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## 📜 License

Licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built using [Python Cryptography](https://cryptography.io/)
- Inspired by the need for accessible, strong encryption
- Thanks to all contributors and security researchers

## ⚡️ Pro Tips

1. Match iteration counts for encryption/decryption
2. Use offline key storage methods
3. Maintain current backups
4. Increase iterations for sensitive data

## 🐛 Troubleshooting Guide

### Common Issues & Solutions

1. **"Invalid key or corrupted file"**
   - Verify your encryption key
   - Confirm iteration count matches encryption settings
   - Check file integrity

2. **"File not found"**
   - Verify file path and permissions
   - Check working directory

3. **Performance Considerations**
   - Adjust iterations based on file size
   - Monitor system resources

## 📬 Contact & Support

Created by Priyanshu Bag

- GitHub: [@yourusername](https://github.com/KillThePython)
- Email: com33dom44@gmail.com
Report issues on [GitHub Issues](https://github.comKillThePython/Sudip-Cryptor/issues)

---

<div align="center">
  <p>Made with ❤️ by the Sudip Cryptor Team</p>
  <p>Give us a ⭐️ if you find this project useful!</p>
</div>
