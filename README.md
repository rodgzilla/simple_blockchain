# Simple blockchain PoC

A very simple implementation of a blockchain.

An example run of the `blockchain.py` program:

```
$ ./blockchain.py

data: b'Hey'
proof of work b'QAYQPEVPDE'
block hash b'bbede54cfad3ccb0ed9bb858849f629783fbbd4c0cacd8302cde8144fe3788bb54278196ca5de188e7d4a388d33ff1078633fa081666f8fbf0386bc277e00000'
data: b' everybody.'
proof of work b'OYYXWIWGMG'
block hash b'a5e4ec6069bf940bf0e5d1c6180d0b98803c53c5994e80b0383fe3f028896018baa85d0f0cb0961a01bd0eae06858cca4b2735706ec876a627a96dbec8100000'
data: b' How are you doing?'
proof of work b'FCLPWNKXZF'
block hash b'87ab2d9ea74b8e8b16317e8d1ad0bb38ba77a3b09bf69db451bca706ebf3d6386e6adc570eada9c70436e9b2ffc215134c0c9bfb7173188ac0b5f1de60500000'
Hey everybody. How are you doing?
```

The ```blockchain_multiminer.py``` contains a blockchain and miner
implementation in which the miners compete to identify transactions.

An example run of this program:

```
$ ./blockchain_multiminer.py

Transactions to identify:
	Dom gives 263 to Alfred
	Dom gives 82 to Edward
	Ben gives 152 to Caroline
	Edward gives 204 to Dom
	Fanny gives 124 to Edward
	Ben gives 210 to Caroline
	Caroline gives 199 to Fanny
	Ben gives 25 to Alfred
	Caroline gives 270 to Alfred
	Ben gives 11 to Caroline
	Edward gives 172 to Ben
	Alfred gives 249 to Caroline
	Edward gives 244 to Ben
	Dom gives 168 to Alfred
	Alfred gives 216 to Ben
	Fanny gives 210 to Caroline
	Edward gives 76 to Ben
	Caroline gives 123 to Ben
	Caroline gives 79 to Fanny
	Fanny gives 84 to Ben
	Dom gives 59 to Ben
	Alfred gives 203 to Fanny
	Alfred gives 294 to Edward
	Edward gives 61 to Caroline
	Edward gives 63 to Caroline
Miner 3 found proof of work: b'XPNOBQMYYN'
Transactions authentified:
	Caroline gives 123 to Ben
	Alfred gives 216 to Ben
	Alfred gives 249 to Caroline
	Caroline gives 79 to Fanny
Miner 2 found proof of work: b'RFDTXKAAJX'
Transactions authentified:
	Ben gives 152 to Caroline
	Dom gives 263 to Alfred
	Caroline gives 199 to Fanny
	Ben gives 25 to Alfred
Miner 8 found proof of work: b'EIMPQFUSSB'
Transactions authentified:
	Fanny gives 124 to Edward
	Edward gives 204 to Dom
	Alfred gives 294 to Edward
	Edward gives 76 to Ben
Miner 10 found proof of work: b'QVJIWIHYAX'
Transactions authentified:
	Fanny gives 84 to Ben
	Ben gives 11 to Caroline
	Edward gives 172 to Ben
	Caroline gives 270 to Alfred
Miner 9 found proof of work: b'ZJYVCGFWNC'
Transactions authentified:
	Fanny gives 210 to Caroline
	Edward gives 61 to Caroline
	Ben gives 210 to Caroline
	Edward gives 63 to Caroline
Miner 6 found proof of work: b'ZYTTCDGMRK'
Transactions authentified:
	Edward gives 244 to Ben
	Dom gives 168 to Alfred
	Alfred gives 203 to Fanny
	Dom gives 59 to Ben
Miner 1 found proof of work: b'HULCZSWOJE'
Transactions authentified:
	Dom gives 82 to Edward
[('Caroline', 'Ben', 123), ('Alfred', 'Ben', 216), ('Alfred', 'Caroline', 249), ('Caroline', 'Fanny', 79)][('Ben', 'Caroline', 152), ('Dom', 'Alfred', 263), ('Caroline', 'Fanny', 199), ('Ben', 'Alfred', 25)][('Fanny', 'Edward', 124), ('Edward', 'Dom', 204), ('Alfred', 'Edward', 294), ('Edward', 'Ben', 76)][('Fanny', 'Ben', 84), ('Ben', 'Caroline', 11), ('Edward', 'Ben', 172), ('Caroline', 'Alfred', 270)][('Fanny', 'Caroline', 210), ('Edward', 'Caroline', 61), ('Ben', 'Caroline', 210), ('Edward', 'Caroline', 63)][('Edward', 'Ben', 244), ('Dom', 'Alfred', 168), ('Alfred', 'Fanny', 203), ('Dom', 'Ben', 59)][('Dom', 'Edward', 82)]
```
