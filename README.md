##this script is for cracking vignere ciphers.


the intention was to crack the key for the puzzle [here](http://www.recruitahacker.net/Puzzle)


The key size for the solution seems to be larger than 5. With the key size approaching the length of the cipher text, I realized that there are many possible decryptions of the cipher text that result in real english words. 


So the puzzle probably requires a better approach, possibly using a little NLP to determine if the result is a real sentence, not just real words, or maybe it's a diversion and the test is actually passed with a timing attack.


The script is certainly not optimal. The next things I would do to improve it are firstly eliminating duplicate checks when increasing the key size by ignoring keys with a repeating pattern shorter than the full length of the key (ie abcabc is the same key as abc) and multithreading.
