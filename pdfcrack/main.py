import pikepdf
from tqdm import tqdm

passwords = [line.strip() for line in open("word.txt")]
for password in tqdm(passwords, "Decrypting PDF"):
    try:
        with pikepdf.open("mai.pdf", password=password)as pdf:
            print("\n[+] Password found:", password)
            break
    except pikepdf._qpdf.PasswordError as e:
        # wrong password, just continue in the loop
        continue
#hii my name is maithil deore i m a software dev if you want something for you than you can mail me on maithildeore12@gmail.com