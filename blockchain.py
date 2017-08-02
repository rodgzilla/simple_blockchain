#!/usr/bin/env python

import hashlib
import string
import random

difficulty = 5

class Block():
    def __init__(self, data, previous_block = None):
        """Creates the data block. It does not get mined by default. The
        default value of None for the previous_block parameter is used
        to create the genesis block of the chain.
        """
        self.data = data
        self.previous_block = previous_block
        self.proof_of_work = None
        self.hash = None

    def is_verified(self):
        return self.hash is not None

    def _generate_random_string(self):
        """Generates a random string of 10 uppercase characters that will be
        added at the end of the block as proof of work.
        """
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(10)).encode('utf-8')

    def hash_block(self, proof_of_work = None):
        """Produce the hash value of the current block using the proof_of_work
        parameter. If this parameter is None, the proof_of_work value
        stored in the class is used.
        """
        if not proof_of_work:
            proof_of_work = self.proof_of_work

        sha512 = hashlib.sha512()
        sha512.update(self.previous_block.hash if self.previous_block else ''.encode('utf-8'))
        sha512.update(self.data)
        sha512.update(proof_of_work)

        return sha512.hexdigest()

    def mine(self):
        """This method mine the current block i.e. finds a 10 characters
        uppercase string to add at the end of the block in order to
        get the correct number of 0 at the end of the hash value of
        the block.
        """
        def is_valid(guess):
            result = self.hash_block(guess)

            return result[-difficulty:] == '0' * difficulty

        guess = self._generate_random_string()
        while not is_valid(guess):
            guess = self._generate_random_string()
        self.proof_of_work = guess
        self.hash = self.hash_block().encode('utf-8')

def print_blockchain(head_block):
    """This function print the content of the blockchain. The data has to
    be reversed in order to get the values in the input order because
    the access point to the blockchain is the head.
    """
    data = []

    while head_block is not None:
        data.append(head_block.data.decode())
        head_block = head_block.previous_block

    print(''.join(data[::-1]))

def print_block_info(block):
    print('data:', block.data)
    print('proof of work', block.proof_of_work)
    print('block hash', block.hash)

if __name__ == '__main__':
    genesis_block = Block('Hey'.encode('utf-8'))
    genesis_block.mine()
    print_block_info(genesis_block)

    block = Block(' everybody.'.encode('utf-8'), genesis_block)
    block.mine()
    print_block_info(block)

    block = Block(' How are you doing?'.encode('utf-8'), block)
    block.mine()
    print_block_info(block)

    print_blockchain(block)
