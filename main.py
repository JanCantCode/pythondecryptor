alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ,.-;:_#'+*~´`?=)(/&%$§!²³{[]}}^° "


def makeLonger(string, length):
    i = 0
    while len(string) != length:
        string += string[i]
        i += 1
        if i > len(string):
            i = 0
    return string


def numify(string):
    nums = []
    for i in string:
        if len(str(alphabet.index(i))) == 2:
            nums.append(int(alphabet.index(i)))
        else:
            nums.append(int("0" + str(alphabet.index(i))))
    return nums


def decrypt(message, password):
    password = makeLonger(password, len(message))
    password = numify(password)
    message = numify(message)
    decrypted = ""
    for i in range(len(message)):
        decrypted += alphabet[add(message[i], password[i])]
    return decrypted


def encrypt(message, password):
    password = makeLonger(password, len(message))
    password = numify(password)
    message = numify(message)
    encrypted = ""
    for i in range(len(message)):
        encrypted += alphabet[subtract(password[i], message[i])]
    return encrypted


def add(a, b):
    return int((a - b) % len(alphabet))


def subtract(a, b):
    return int((a + b) % len(alphabet))


def encryptionTest(message, password):
    print(f"decrypting '{message}' with '{password}'..")
    decrypted = decrypt(message, password)
    encrypted = encrypt(decrypted, password)
    if encrypted == message:
        print(f"sucessfully encrypted into '{encrypted}'")
    else:
        print(f"oops, something seems to have went wrong! encrypted into '{encrypted}'")


encryptionTest("abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ,.-;:_#'+*~´`?=)(/&%$§!²³{[]}}^° ", "password")
