try:
    import hashlib
    import sys

    print("SHA1 CRACKER CREATED BY NUKE ")
    print("-"*50)
    def crack_sha1_hash(hash, wordlist_file):
        with open(wordlist_file, "r", encoding="utf-8", errors="ignore") as wordlist:
            for word in wordlist:
                word = word.strip()

                hashed_word = hashlib.sha1(word.encode()).hexdigest()

                if hashed_word == hash:
                    return word

        return "Kelime bulunamadı."

    veritabanindaki_hash = sys.argv[2]
    kelime_listesi = sys.argv[1]

    kelime = crack_sha1_hash(veritabanindaki_hash, kelime_listesi)
    print("BULUNDU ==>", kelime)
except:
    print("HATA TESPİT EDİLDİ ! WORDLİST YADA SHA1 HASH GİRDİ VERDİĞİNİZE EMİN OLUN")