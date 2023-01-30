import mysql.connector as a
con=a.connect(host="localhost",user="root",passwd="Manish#51",database="rms")

def checkin():
	d=input("Checkin Days : ")
	g=input("Checkin Names : ")
	a=input("Checkin Aadhaar : ")
	dt=input("Checkin Date : ")
	b=input("Checkin Type & Number : ")

	data=(d,g,a,dt,b)				# tuples datatype

	sql='Insert into checkin values(%s,%s,%s,%s,%s)'
	c=con.cursor()
	c.execute(sql,data)
	con.commit()

	print("Data Entered Successfully")
	main()

def checkout():
	b=input("Checkout Type & Number :")
	tg=int(input("Checkout Guests : "))
	f=int(input("Checkout Fare :"))
	d=int(input("Checkout Days :"))
	bl=f*d*tg

	cod=input("Checkout Date :")

	data=(b,tg,f,d,bl,cod)			#tuple datatype

	sql='Insert into checkout values(%s,%s,%s,%s,%s,%s)'
	c=con.cursor()
	c.execute(sql,data)
	con.commit()

	print("Data Entered Successfully")
	main()

def rooms():
	print("Executive – 5000/d/g")
	print("""Facilities – Wifi, TV, AC, Bathroom with Tub and Geyser, Breakfast, lunch, dinner""")
	print(" ")
	print("Deluxe – 2500/d/g")
	print(""" Facilities – Wifi, TV, AC, Bathroom with Tub and Geyser""")
	print(" ")
	print("Simple – 1000/d/g")
	print(""" Facilities – Wifi, TV , Bathroom with Geyser """)
	main()

def main():
	print("1. Check In")
	print("2. Check Out")
	print("3. Fare and Amenities")
	c=int(input("Choice : "))
	
	if c==1:
		checkin()
	elif c==2:
		checkout()
	elif c==3:
		rooms()
	else:
		print("Enter Correct Choice")
	main()
main()