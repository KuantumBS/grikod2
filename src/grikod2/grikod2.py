class InvalidBinaryError(ValueError):
    """Geçersiz ikili girişler için özel hata sınıfı."""
    pass


def ikili_2_gri_kod(i2grik: str) -> str:
    """İkili bir string'i ilgili Gri Koduna dönüştürür."""
    if not i2grik:
        raise InvalidBinaryError("Hata: Giriş boş olamaz.")
    if not all(c in '01' for c in i2grik):
        raise InvalidBinaryError("Hata: Lütfen geçerli bir ikili sayı girin (sadece '0' ve '1' içermeli).")
    if len(i2grik) > 64:
        raise InvalidBinaryError("Hata: İkili sayı çok uzun (maksimum 64 bit).")
    try:
        i2grikod = int(i2grik, 2)
    except ValueError:
        raise InvalidBinaryError("Hata: İkili sayıya dönüştürme sırasında beklenmedik bir hata.")
    i2grikod ^= (i2grikod >> 1)
    return bin(i2grikod)[2:].zfill(len(i2grik))


def grikod2ikili(grik2i: str) -> str:
    """
    Gri Kod string'ini ikili (binary) string'e dönüştürür.
    
    Algoritma:
        - İlk bit aynen alınır.
        - Sonraki her bit için: yeni_ikili_bit = önceki_ikili_bit XOR mevcut_gri_bit
    """
    # --- Girdi kontrolleri ---
    if not grik2i:
        raise InvalidBinaryError("Hata: Giriş boş olamaz.")
    if not all(c in '01' for c in grik2i):
        raise InvalidBinaryError("Hata: Lütfen geçerli bir Gri Kod girin (sadece '0' ve '1' içermeli).")
    if len(grik2i) > 64:
        raise InvalidBinaryError("Hata: Gri Kod çok uzun (maksimum 64 bit).")

    # --- Dönüşüm ---
    binary = []                     # Sonuç bitlerini toplayacağımız liste
    prev_bit = int(grik2i[0])       # İlk bit aynen alınır
    binary.append(str(prev_bit))

    for bit in grik2i[1:]:          # İkinci bitten itibaren
        current_gray = int(bit)
        new_bit = prev_bit ^ current_gray   # XOR işlemi
        binary.append(str(new_bit))
        prev_bit = new_bit          # Bir sonraki adım için önceki ikili biti güncelle

    return ''.join(binary)


# --- İnteraktif Mod Fonksiyonu ---
def run_interactive_converter():
    """İnteraktif Gri Kod dönüştürücü konsolunu başlatır."""
    print("GriKod2 Dönüştürücü - İnteraktif Mod")
    print("Çıkmak için 'q' girin.")
    print("İkili -> Gri Kod  için ikili sayı girin (örnek: 1010)")
    print("Gri Kod -> İkili için 'gri:' öneki ile girin (örnek: gri:1111)")

    while True:
        user_input = input("Dönüştürmek istediğiniz değeri girin: ")
        if user_input.lower() == 'q':
            print("Çıkılıyor...")
            break

        # Kullanıcı hem ikili hem gri girdi girebilsin diye:
        if user_input.lower().startswith('gri:'):
            gray_code = user_input[4:].strip()   # 'gri:' önekini at
            try:
                binary_result = grikod2ikili(gray_code)
                print("İkili karşılığı:", binary_result)
            except InvalidBinaryError as e:
                print(e)
            except Exception as e:
                print(f"Beklenmeyen bir hata: {e}")
        else:
            # Normal ikili giriş
            try:
                gri_result = ikili_2_gri_kod(user_input)
                print("Gri Kod:", gri_result)
            except InvalidBinaryError as e:
                print(e)
            except Exception as e:
                print(f"Beklenmeyen bir hata: {e}")


# --- Doğrudan Çalıştırma Bloğu ---
if __name__ == "__main__":
    run_interactive_converter()
