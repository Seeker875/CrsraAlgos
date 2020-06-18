# python3


def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))


def hash_func(s,hash_multiplier,hash_prime):
        ans = 0
        for c in reversed(s):
        	#ord c for ascii code
            ans = (ans * hash_multiplier + ord(c)) % hash_prime
        return ans 
#15,485,863
#31
def PreComputeHashes(pattern, text,hash_multiplier,hash_prime):
    
	# get h array for storing hash values
	lenDiff=len(text) - len(pattern)
	h = [0]*(lenDiff +1)
	#get string of up to pattern length 
	#python fix for not having -1
	subS = text[lenDiff: len(text)] 
	h[lenDiff] = hash_func(subS,hash_multiplier,hash_prime)
	y=1
	for i in range(1,len(pattern)+1):
		y=(y*hash_multiplier)%hash_prime
	#i to zero
	for i in range(lenDiff-1,-1,-1):
		h[i] = (hash_multiplier*h[i+1] +ord(text[i]) -y*ord(text[i+len(pattern)]))%hash_prime

	return h		


def get_occurrences(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]

def RabinKarp(pattern, text):
	hash_multiplier = 31
	hash_prime = 15485863#big prime
	lenDiff=len(text) - len(pattern)
	result=[]
	pHash=hash_func(pattern,hash_multiplier,hash_prime)
	H = PreComputeHashes(pattern, text,hash_multiplier,hash_prime)
	for i in range(0,lenDiff+1):
		if pHash!=H[i]:
			continue
         #i=4   
		if text[i: (i+len(pattern))]==pattern:
			result.append(i)
	return result			



if __name__ == '__main__':
    print_occurrences(RabinKarp(*read_input()))

