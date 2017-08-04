#!/usr/bin/env python

import hashlib
import string
import random

difficulty = 5
block_size = 4
try_number = 20

class Block():
    def __init__(self, transactions, previous_block = None):
        """Creates the data block. It does not get mined by default. The
        default value of None for the previous_block parameter is used
        to create the genesis block of the chain.
        """
        self.transactions   = transactions
        self.previous_block = previous_block
        self.proof_of_work  = None
        self.hash           = None
        self.data           = str(self.transactions).encode('utf-8')

    def get_transactions(self):
        """Returns the list of transactions contained in this block."""
        return self.transactions

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

    def get_proof_of_work(self):
        """Returns the proof of work authentifying this block. If the block
        has not been mined yet, returns None.
        """
        return self.proof_of_work

    def is_valid(self, guess):
        """Returns True if guess is a correct proof of work for this block.
        """
        result = self.hash_block(guess)

        return result[-difficulty:] == '0' * difficulty

    def authentify(self, proof_of_work):
        """Sets the block proof of work and fills the hash field to allow the
        next block to be mined using the hash of this one.
        """
        self.proof_of_work = proof_of_work
        self.hash          = self.hash_block(proof_of_work).encode('utf-8')

    def is_authentified(self):
        """Check whether the proof of work of the block is indeed valid and
        other miners are not trying to dupe this miner into accepting
        their blocks.
        """
        return self.is_valid(self.proof_of_work)

class Miner():
    def __init__(self, id, transaction_set, head_block):
        self.id              = id
        self.transaction_set = transaction_set.copy()
        self.head_block      = head_block

    def try_to_prove_work(self):
        """This function creates a block storing some transactions and then
        try to find a proof of work for it. Finding the proof of work
        consists in generating random strings, appending them to the
        block data and testing if the hash of the result has
        `difficulty` 0 at the end.
        """
        def generate_random_string():
            """Generates a random string of 10 uppercase characters that will be
            added at the end of the block as proof of work.
            """
            return ''.join(random.choice(string.ascii_uppercase) for _ in range(10)).encode('utf-8')
        number_of_transactions = min(block_size, len(self.transaction_set))
        block_transactions     = random.sample(self.transaction_set, number_of_transactions)
        new_block              = Block(block_transactions, self.head_block)

        for _ in range(try_number):
            guess = generate_random_string()
            if new_block.is_valid(guess):
                new_block.authentify(guess)
                self.head_block = new_block

                return True

        return False

    def update_blockchain(self, new_head_block):
        """This method updates the copy of the blockchain stored in this
        miner. Before accepting the block, this method test if the
        block is indeed identified (the proof of work gives the
        correct amount of 0 at the end of the hash). The set of
        transactions left to be identified is also updated by removing
        the transactions contained in the new head block.
        """
        if not new_head_block.is_authentified():
            return False

        for transaction in new_head_block.get_transactions():
            self.transaction_set.remove(transaction)
        self.head_block = new_head_block

        return True

    def get_head_block(self):
        """Returns the head block of this miner copy of the blockchain.
        """
        return self.head_block

    def name(self):
        """Returns the name of the current miner. This method is used for
        printing purposes.
        """
        return 'Miner %d' % self.id


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

def create_transation_set(transaction_number):
    """Creates a set of transactions that we will store into the
    blockchain. The actual size of the result might be lower than
    transaction_number because the set does not store duplicate
    transactions.
    """
    account_owners = [
        'Alfred',
        'Ben',
        'Caroline',
        'Dom',
        'Edward',
        'Fanny'
    ]

    transactions = set()
    for _ in range(transaction_number):
        emitter, receiver = random.sample(account_owners, 2)
        amount = random.randint(1, 300)
        transactions.add((emitter, receiver, amount))

    return transactions

def print_transactions(transactions):
    for emitter, receiver, amount in transactions:
        print('\t%s gives %d to %s' % (emitter, amount, receiver))

if __name__ == '__main__':
    transactions_set = create_transation_set(25)
    head_block       = None
    miners           = [Miner(i, transactions_set, head_block) for i in range(1, 11)]

    print('Transactions to identify:')
    print_transactions(transactions_set)

    transactions_authentified = 0
    while transactions_authentified < len(transactions_set):
        for miner in miners:
            if miner.try_to_prove_work():
                head_block = miner.get_head_block()
                print(miner.name(), 'found proof of work:', head_block.get_proof_of_work())
                print('Transactions authentified:')
                print_transactions(head_block.get_transactions())
                for miner in miners:
                    miner.update_blockchain(head_block)
                transactions_authentified += len(head_block.transactions)

    print_blockchain(head_block)
