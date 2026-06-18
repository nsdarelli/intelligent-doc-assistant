import hashlib

class HashService:

    @staticmethod
    def calculate_file_hash(file_path: str):
        sha256 = hashlib.sha256()

        with open(file_path, "rb") as file:
            while chunk := file.read(8192):
                sha256.update(chunk)

        return sha256.hexdigest()