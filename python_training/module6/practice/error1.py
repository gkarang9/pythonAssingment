def main():
	try:
		hours=int(input("how many hours did you work"))
		pay_rate=int(input("Enter the hourly pay rate:"))
	except Exception as err:
		print("exception is",err)

main()		
	