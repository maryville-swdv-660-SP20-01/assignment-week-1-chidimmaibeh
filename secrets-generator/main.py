import arrow
import secrets

# Generates secret key for user
secret_key = secrets.token_hex(25)

#Today's Date 
time = arrow.utcnow().format('MM/DD/YYYY')
print("The Date of Today is: " + time)
print("Your secret key is ==>> " + secret_key)

input("Press ENTER to quit!")
