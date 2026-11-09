import itertools
import string
import time

def brute_force_password(target, charset, panjang_maks=5):
    """
    saya coba ngedemonstrasikan brute force pada password simulasi.
    target nya harus didefinisikan sendiri di dalam program (bukan password asli/orang lain).
    """
    percobaan = 0
    waktu_mulai = time.time()

    # coba dari panjang 1 sampai panjang_maks
    for panjang in range(1, panjang_maks + 1):
        # itertools.product menghasilkan semua kombinasi sepanjang 'panjang'
        for kombinasi_tuple in itertools.product(charset, repeat=panjang):
            kombinasi = ''.join(kombinasi_tuple)
            percobaan += 1

            if kombinasi == target:
                waktu_selesai = time.time()
                return {
                    "ditemukan": True,
                    "password": kombinasi,
                    "jumlah_percobaan": percobaan,
                    "waktu": round(waktu_selesai - waktu_mulai, 4)
                }

    return {"ditemukan": False, "jumlah_percobaan": percobaan}


# conto simulasi nya
if __name__ == "__main__":
    # Password target didefinisikan sendiri untuk tujuan demonstrasi
    password_target = "abcd"          # contoh password 4 karakter
    charset = string.ascii_lowercase  # a-z

    hasil = brute_force_password(password_target, charset, panjang_maks=5)

    print(f"Password target   : {password_target}")
    print(f"Ditemukan         : {hasil['ditemukan']}")
    print(f"Password hasil    : {hasil.get('password')}")
    print(f"Jumlah percobaan  : {hasil['jumlah_percobaan']:,}")
    print(f"Waktu eksekusi    : {hasil.get('waktu')} detik")
