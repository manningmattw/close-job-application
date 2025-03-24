import hashlib
import requests


def main():
    response = requests.get("https://api.close.com/buildwithus/")

    data = response.json()

    print(f"INSTRUCTIONS:\n{data['meta']['description']}\n\n")

    key = data['key'].encode('utf-8')
    traits_digested = []

    for trait in data['traits']:
        digest = hashlib.blake2b(key=key, digest_size=64)
        digest.update(trait.encode('utf-8'))

        traits_digested.append(digest.hexdigest())

    response = requests.post("https://api.close.com/buildwithus/", json=traits_digested)

    print(f"RESULTS:\nHTTP Status: {response.status_code}\n{response.text}")


if __name__ == "__main__":
    main()
