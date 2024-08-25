from werkzeug.security import generate_password_hash, check_password_hash

# Test hashing
hashed_password = generate_password_hash('testpass')
print("Hashed password:", hashed_password)

# Test verification
print("Password match:", check_password_hash(hashed_password, 'testpass'))
