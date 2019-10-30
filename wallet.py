from Crypto.PublicKey import RSA
import Crypto.Random
import binascii
class Wallet:
	def __init__(self):
		
		self.private_Key=None
		self.public_Key =None

	def create_keys(self):
		private_Key,public_Key = self.generate_keys()
		self.private_Key=private_Key
		self.public_Key =public_Key
	def load_keys():
		pass

	def generate_keys(self):
		private_key = RSA.generate(1024, Crypto.Random.new().read)
		public_key = private_key.publickey()
		return (binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'), binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii'))


 


