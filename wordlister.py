import itertools

usage_banner = """
USAGE
python3 wordlister.py <absolute_file_input> <absolute_file_output>

Example:
python3 wordlister.py /mnt/e/words.txt /mnt/e/result.txt

HH
"""

def main():
	import sys, os
	argv = sys.argv[1:]

	wordlist = None
	generated = list()

	try:
		file_read = open(argv[0], 'r')
		file_write = open(argv[1], 'w')
		wordlist = file_read.read().split('\n')

		while '' in wordlist:
			wordlist.remove('')

		repeat = len(wordlist)

		try:
			for repeat in range(1, repeat):
				for generated_string in itertools.product(wordlist, repeat=repeat):
					print(f"[*] {''.join(generated_string)}", end='\r')
					generated.append(''.join(generated_string))
		except KeyboardInterrupt:
			file_read.close()

			print(f"\n[i] Writing to file {argv[1]}")
			file_write.write('\n'.join(generated))
			file_write.close()
		except Exception as e:
			print(f"\n[!] {e}")
		finally:
			file_read.close()

			print(f"\n[i] Writing to file {argv[1]}")
			file_write.write('\n'.join(generated))
			file_write.close()
	except Exception as e:
		print(e)
		print(usage_banner)

if __name__ == '__main__':
	main()
