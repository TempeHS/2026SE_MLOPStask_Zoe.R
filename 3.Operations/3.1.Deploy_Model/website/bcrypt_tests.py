import bcrypt

password = "passwordabc"

bytes = password.encode("utf-8")

salt = bcrypt.gensalt()

hash = bcrypt.hashpw(bytes, salt)

userPassword = "passwordabc"

userBytes = userPassword.encode("utf-8")

result = bcrypt.checkpw(userBytes, hash)

print(result)
