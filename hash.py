import hashlib

def hash_string(text, algorithm='sha256'):
   
    return hashlib.new(algorithm)(text.encode()).hexdigest()

def hash_file(filepath, algorithm='sha256'):
    hasher = hashlib.new(algorithm)
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

# Example usage
if __name__ == "__main__":
    text = "Hello, World!"
    print(f"SHA256: {hash_string(text)}")
    print(f"MD5: {hash_string(text, 'md5')}")