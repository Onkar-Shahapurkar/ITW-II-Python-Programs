import os
import hashlib

def calculate_file_hash(file_path, block_size=65536):
    """Calculate the SHA256 hash of a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            hasher.update(block)
    return hasher.hexdigest()

def scan_file(file_path, known_hashes):
    """Scan a file for potential malware."""
    file_hash = calculate_file_hash(file_path)
    if file_hash in known_hashes:
        return False, f"File '{file_path}' is safe."

    # Add more sophisticated malware detection logic here

    # For simplicity, let's consider any file with a new hash as suspicious
    known_hashes.add(file_hash)
    return True, f"Potential malware detected in '{file_path}'."

def scan_directory(directory_path, known_hashes):
    """Scan all files in a directory for potential malware."""
    results = []
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            is_suspicious, result_message = scan_file(file_path, known_hashes)
            if is_suspicious:
                results.append(result_message)
    return results

if __name__ == "__main__":
    # Simulating a list of known safe file hashes
    known_hashes = set()

    # Specify the directory to scan
    target_directory = "/path/to/scan"

    # Scan the directory
    scan_results = scan_directory(target_directory, known_hashes)

    # Display the results
    if scan_results:
        print("Scan Results:")
        for result in scan_results:
            print(result)
    else:
        print("No threats detected. The system is clean.")