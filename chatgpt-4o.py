# https://chatgpt.com/share/67e1a2b2-1dec-8013-93f1-a11e530e9ed3


import requests
import hashlib
import json

def fetch_instructions():
    url = "https://api.close.com/buildwithus/"
    response = requests.get(url)
    
    if response.status_code == 200:
        try:
            data = response.json()
            print("Instructions received:", data)
            return data
        except requests.exceptions.JSONDecodeError:
            print("Failed to parse JSON response.")
    else:
        print(f"Request failed with status code {response.status_code}")

def generate_hashes(traits, key):
    hashes = []
    for trait in traits:
        hasher = hashlib.blake2b(key=key.encode("utf-8"), digest_size=64)  # Correct key handling
        hasher.update(trait.encode("utf-8"))
        hash_hex = hasher.hexdigest()
        print(f"Hash for {trait}: {hash_hex}")  # Debugging output
        hashes.append(hash_hex)
    return hashes

def submit_hashes(hashes):
    url = "https://api.close.com/buildwithus/"
    response = requests.post(url, json=hashes)

    if response.status_code == 200:
        print("Verification ID received:", response.text)  # Use response.text instead of response.json()
    else:
        print(f"Request failed with status code {response.status_code}", response.text)

if __name__ == "__main__":
    instructions = fetch_instructions()
    if instructions:
        traits = instructions.get("traits", [])
        key = instructions.get("key", "")
        if traits and key:
            hashes = generate_hashes(traits, key)
            submit_hashes(hashes)
