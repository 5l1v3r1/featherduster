import cryptanalib as ca
import feathermodules

ecb_cpa_decrypt_attack_script_skeleton = """# Generated by FeatherDuster
import cryptanalib as ca

def encryption_oracle(text):
   # TODO: Write a function to interact with the ECB encryption oracle
   # Pseudocode:
   # Send text to the encryption oracle
   # Retrieve ciphertext from encryption oracle response
   # Decode ciphertext if encoded
   # return ciphertext

ca.ecb_cpa_decrypt(encryption_oracle=encryption_oracle, block_size=%r, verbose=True, hollywood=%r)

"""

def generate_ecb_cpa_decrypt_attack_script(ciphertexts):
   options = dict(feathermodules.current_options)
   options = process_options(options, ciphertexts)
   if options == False:
      print '[*] Options could not be validated, please try again.'
      return False
   try:
      print '[+] Attempting to write script...'
      fh = open(options['filename'], 'w')
      fh.write(ecb_cpa_decrypt_attack_script_skeleton % (options['blocksize'], options['hollywood']))
      fh.close()
   except:
      print '[*] Couldn\'t write to the file with the name provided. Please try again.'
      return False
   print '[+] Done! Your script is available at %s' % options['filename']


def process_options(options, ciphertexts):
   if options['blocksize'] == 'auto':
      print '[+] Analyzing samples to discover block size...'
      analysis_results = ca.analyze_ciphertext(ciphertexts)
      blocksize = analysis_results['blocksize']
      if blocksize == 0:
         print '[*] No common block size could be discovered.'
      else:
         options['blocksize'] = blocksize
   else:
      try:
         print '[+] Checking block size...'
         options['blocksize'] = int(options['blocksize'])
      except:
         return False
   options['hollywood'] = (options['hollywood'].lower() not in ['','n','no','no i am lame'])
 
   return options


feathermodules.module_list['ecb_cpa_decrypt'] = {
   'attack_function':generate_ecb_cpa_decrypt_attack_script,
   'type':'block',
   'keywords':['ecb'],
   'description':'Generate an attack script to decrypt a secret suffix added to data by an ECB mode encryption oracle.',
   'options':{
      'blocksize': 'auto',
      'filename': 'ecb_cpa_decrypt.py',
      'hollywood': 'no',
   }
}
