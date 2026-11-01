"""
UTS Dasar Komputer dan Pemrograman
Kelompok E - Embedded/IoT
Monitoring Kelembapan Tanah & Aksi Pompa
"""

# 15 data inti dari soal + tepat 5 data tambahan (dalam persen)
data_kelembapan = [
    22, 28, 34, 41, 55, 63, 72, 78, 31, 47,
    66, 81, 19, 58, 69,
    0, 35, 70, 71, 100
]


def status_sensor(nilai):
    """Menentukan status kelembapan berdasarkan nilai sensor."""
    if nilai < 35:
        return "KERING"
    elif nilai <= 70:
        return "NORMAL"
    else:
        return "BASAH"


def aksi_pompa(status):
    """Menentukan aksi pompa berdasarkan status kelembapan."""
    if status == "KERING":
        return "POMPA ON"
    else:
        return "POMPA OFF"


def rata_rata(data):
    """Menghitung rata-rata sekumpulan data."""
    return sum(data) / len(data)


def hitung_kategori(data):
    """Menghitung jumlah data pada setiap kategori."""
    jumlah = {"KERING": 0, "NORMAL": 0, "BASAH": 0}

    for nilai in data:
        status = status_sensor(nilai)
        jumlah[status] += 1

    return jumlah


def tampilkan_monitoring(data):
    """Menampilkan hasil pembacaan sensor dan aksi pompa untuk setiap data."""
    print("=" * 58)
    print(" MONITORING KELEMBAPAN TANAH & AKSI POMPA - KELOMPOK E")
    print("=" * 58)

    for nomor, nilai in enumerate(data, start=1):
        status = status_sensor(nilai)
        pompa = aksi_pompa(status)
        print(f"{nomor:02d}. Kelembapan: {nilai:>3}% | Status: {status:<6} | Aksi: {pompa}")


def tampilkan_ringkasan(data):
    """Menampilkan total, jumlah kategori, dan statistik kelembapan."""
    jumlah = hitung_kategori(data)

    print("\n" + "=" * 25 + " RINGKASAN " + "=" * 22)
    print(f"Total data       : {len(data)}")
    print(f"Jumlah KERING   : {jumlah['KERING']}")
    print(f"Jumlah NORMAL   : {jumlah['NORMAL']}")
    print(f"Jumlah BASAH    : {jumlah['BASAH']}")
    print(f"Rata-rata       : {rata_rata(data):.2f}%")
    print(f"Maksimum        : {max(data)}%")
    print(f"Minimum         : {min(data)}%")
    print("=" * 58)


def main():
    tampilkan_monitoring(data_kelembapan)
    tampilkan_ringkasan(data_kelembapan)


if __name__ == "__main__":
    main()
    tabel_2 = [
    (34, "KERING", "POMPA ON"),    # sedikit di bawah batas bawah
    (35, "NORMAL", "POMPA OFF"),   # tepat pada batas bawah
    (36, "NORMAL", "POMPA OFF"),   # sedikit di atas batas bawah
    (69, "NORMAL", "POMPA OFF"),   # sedikit di bawah batas atas
    (70, "NORMAL", "POMPA OFF"),   # tepat pada batas atas
    (71, "BASAH", "POMPA OFF"),    # sedikit di atas batas atas
    (5, "KERING", "POMPA ON"),     # nilai rendah realistis
    (95, "BASAH", "POMPA OFF"),    # nilai tinggi realistis
]
 
 
def jalankan(judul, kasus_uji):
    lulus = 0
    print(judul)
    print(f"{'No':<3} {'Input':>6}  {'Expected':<24} {'Actual':<24} Hasil")
    for no, (nilai, exp_status, exp_aksi) in enumerate(kasus_uji, start=1):
        status = status_sensor(nilai)
        aksi = aksi_pompa(status)
        expected = f"{exp_status} / {exp_aksi}"
        actual = f"{status} / {aksi}"
        hasil = "PASS" if actual == expected else "FAIL"
        lulus += hasil == "PASS"
        print(f"{no:<3} {nilai:>5} %  {expected:<24} {actual:<24} {hasil}")
    print(f"Total: {lulus}/{len(kasus_uji)} test PASS\n")
 
 
jalankan("=== TABEL 2 (8 test case) ===", tabel_2)
