from blockchain import Blockchain
from uuid import uuid4
from utility.verification import Verification
from wallet import Wallet
verifier = Verification()
class Node:
	def __init__(self):
		self.wallet =Wallet()
		self.blockchain =Blockchain(self.wallet.public_Key)
	def get_transaction_value(self):

		tx_recipient = input('Enter the recipient of the transaction: ')
		tx_amount = float(input('Your transaction amount please: '))
		return tx_recipient, tx_amount


	def get_user_choice(self):
	
		user_input = input('Your choice: ')
		return user_input


	def print_blockchain_elements(self):
 
		for block in self.blockchain.chain:
			print('Outputting Block')
			print(block)
		 

	def get_data(self):

		waiting_for_input = True

		while waiting_for_input:
			print('Please choose')
			print('1: Add a new transaction value')
			print('2: Mine a new block')
			print('3: Output the blockchain blocks')
			print('4: Check transaction validity')
			print('5 .To generate the keys')
			print('6. To load the keys')
			print('q: Quit')
			user_choice = self.get_user_choice()
			if user_choice == '1':
				tx_data = self.get_transaction_value()
				recipient, amount = tx_data
			
				if self.blockchain.add_transaction(recipient,self.id, amount=amount):
					print('Added transaction!')
				else:
					print('Transaction failed!')
					print(self.blockchain.open_transactions)
			elif user_choice == '2':
				self.blockchain.mine_block()
					
			elif user_choice == '3':
				self.print_blockchain_elements()
				print('Balance of {}: {:6.2f}'.format(self.wallet.public_Key, self.blockchain.get_balance()))

			elif user_choice == '4':
				if verifier.verify_transactions(self.blockchain.open_transactions,self.blockchain.get_balance):
					print('All transactions are valid')
				else:
					print('There are invalid transactions')
			elif user_choice == '5':
				 
				self.wallet.create_keys()
			elif user_choice == 'q':
			 
				waiting_for_input = False
			else:
				print('Input was invalid, please pick a value from the list!')
			if not verifier.verify_chain(self.blockchain.chain):
				self.print_blockchain_elements()
				print('Invalid blockchain!')
				break
				
			 


	
if __name__ == '__main__':
	node =Node()
	node.get_data()