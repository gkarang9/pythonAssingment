def main():
	infile=open('philosopher.txt','r')
	line= infile.readline()
	while line !="" :
		#amount=float(line)
		print(line)
		line=infile.readline()
		
	infile.close()

main()		