'''import hashlib
hash = hashlib.sha256("secret message".encode()).hexdigest()
print('Testing hash',hash)

class Block:
    def _init_(self,previous_hash,transaction):
        self.transactions = transaction
        self.previous_hash = previous_hash
        string_to_hash = "".join(transaction) + previous_hash
        self.block_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()


genesis_block = Block()
genesis_block._init_("First Block",["Transaction 1","Transaction 2","Transaction 3"])
print("First Block",genesis_block.block_hash)

second_block = Block()
second_block._init_(genesis_block.block_hash,["Transaction 1","Transaction2","Transaction 3"])
print("Second Block",second_block.block_hash)

third_block = Block()
third_block._init_(second_block.block_hash,["Transaction 1","Transaction 2","Transaction 3"])
print("Third Block",third_block.block_hash)

fourth_block = Block()
fourth_block._init_(third_block.block_hash,["Transaction 1","Transaction 2","Transaction 3"])
print("Fourth Block",fourth_block.block_hash)'''
import pickle
ch="t"
fin=open("book.dat","w")
while (ch=="t"):
    bk_no=int((input("enter book no"))
    bk_name=input("enter book name")
    author=input("enter book's author name")
    bk_price=int((input("enter books price"))
    record=[bk_no,bk_name,author,bk_price]
    pickle.dump(record,fin)
    ch=input("enter t or f")
fin.close()
fin=open("book.dat","rb")
c=0
try:
    while True:
        data=pickle.load(fin)
        if data[2]==author:
            c=c+1
except EOFError:
    pass
print(c)
fin.close()
