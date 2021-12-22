# Copyright [2021] [mohamedSulaiman]

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
	A simple Module to encrypt data with a dictionary in a fast and safe encryption algorithm.
	
	Crediting is not required, But Thank you if you did, To credit me, Just link to my github repo.
		
"""
from cryptography.fernet import Fernet
import pickle

# A function to create a key and return it, Please store this somewhere safe, This getting lost means no decryption for encrypted data.
def create_key():
    return Fernet.generate_key()


class Data_manager(object):
    def __init__(self, key, filename):
        """
        params

        key: byte, A key taken from the create_key() Function.
        You can take that returned output and pass it to the class instance in the __init__() Call, Please note, Keep the key to use somewhere safe, If you lost the key, Data encrypted by this is undecryptable.

        filename: str, A filename to store encrypted data in, If a file with the same name doesn't exists, It will create one, If a file, However, Exists with the same name, Content inside will be overwritten.

        """
        self.key = key
        self.filename = filename
        self.f = Fernet(self.key)
        self.d = {}

    def encrypt(self, text):
        """
        Params

        Text, byte, Data to encrypt

        returns

        Encrypted data, In bytes.

        """
        return self.f.encrypt(text)

    def decrypt(self, text):
        """
        params

        text: byte, Encrypted data to get decrypted.

        returns

        decrypted data, as str.
        """
        return self.f.decrypt(text)

    def exists(self, item):
        """
        Params

        item: anyType, Searches if the item exists inside of the dictionary.

        returns

        True if the item was found, False otherwise.
        """

        if item in self.d:
            return True
        return False

    def add(self, initial_name, content):
        """
        Params

        item, AnyType, Adds the item to the dictionary, If an item with the same name already exists, It will get overwritten.

        Content, AnyType, The content of the item.
        """

        self.d[initial_name] = content

    def get(self, name):
        """
        params
        name, AnyType, The name of the item to return.

        returns

        The item if it was found.
        """
        if name in self.d:
            return self.d.get(name)
        return False

    def save(self):
        """
        Saves The dictionary in a file and encrypts it, Returns true If the file was saved, False otherwise.
        """
        try:
            with open(self.filename, "wb") as fn:
                fn.write(self.encrypt(pickle.dumps(self.d)))
        except:
            return False
        return True

    def load(self):
        """
        Open the file the data is stored in, Decrypts it and reforms it back into a dictionary and returns true, False, If the process didn't complete.
        """
        try:
            with open(self.filename, "rb") as fn:
                self.d = dict(pickle.loads(self.decrypt(fn.read())))
        except:
            return False
        return True
