import pyotp

def generate_secret_key():
    secret_key = pyotp.random_base32()
    return secret_key

# Generate an OTP for the user
def generate_otp(secret_key):
    # Create a TOTP object with the secret key
    totp = pyotp.TOTP(secret_key)

    # Generate the OTP
    otp = totp.now()
    return otp

# Verify the OTP entered by the user
def verify_otp(secret_key, entered_otp):
    totp = pyotp.TOTP(secret_key)

    return totp.verify(entered_otp)


secret_key = generate_secret_key()
otp = generate_otp(secret_key)


# Display the generated OTP
print("Generated OTP:", otp)
print()

# Prompt the user to enter the OTP
entered_otp = input("Enter the OTP: ")
print()
print(generate_secret_key())
if verify_otp(secret_key, entered_otp):
    print('OTP verification successful!')
else:
    print('OTP verification failed!')