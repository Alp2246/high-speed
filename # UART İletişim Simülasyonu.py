# UART İletişim Simülasyonu

# Bu projede, Python dilini kullanarak basit bir UART iletişim simülasyonu oluşturuyoruz. UART, veri iletişimi için sıkça kullanılan bir seri iletişim protokolüdür ve birçok gömülü sistemde kullanılır. Proje, UART gönderme ve alma işlemlerini simüle eder ve iletişim hatası algılama yeteneği içerir.

# Gerekli kütüphaneleri içe aktarın
import random
import time

# UART Gönderme Fonksiyonu
def uart_send(data):
    # Başlangıç biti gönderme
    print("Başlangıç Biti: 0", end=' ')

    # Veriyi karakterlere ayırma ve gönderme
    for char in data:
        char_code = ord(char)
        print(f'Karakter: {char}, ASCII: {char_code}', end=' ')
        for i in range(8):
            bit = (char_code >> i) & 1
            print(bit, end=' ')
        time.sleep(0.1)  # Bitler arası zaman gecikmesi
        print(f'Stop Biti: 1', end=' ')
        time.sleep(0.1)  # Karakterler arası zaman gecikmesi
    print()

# UART Alım Fonksiyonu
def uart_receive(data):
    received_data = ""
    i = 0
    while i < len(data):
        # Başlangıç biti kontrolü
        if data[i] == 0:
            i += 1
            received_char = 0
            for j in range(8):
                received_char |= (data[i] << j)
                i += 1
            # Stop bit kontrolü
            if data[i] == 1:
                received_data += chr(received_char)
                i += 1
            else:
                print("Hata: Geçersiz Stop Biti")
        else:
            print("Hata: Geçersiz Başlangıç Biti")
    return received_data

# Ana Program
if __name__ == "__main__":
    # Gönderilecek veriyi oluşturun
    sent_data = "Hello, UART!"

    # Veriyi rastgele hatalara karşı değiştirin (simülasyon amacıyla)
    received_data = list(sent_data)
    error_index = random.randint(0, len(received_data) - 1)
    received_data[error_index] = chr(ord(received_data[error_index]) ^ 1)

    # UART Gönderme
    print("Gönderilen Veri:", sent_data)
    print("UART Gönderme:")
    uart_send(sent_data)

    # UART Alım
    print("\nUART Alım:")
    received_message = uart_receive(received_data)
    print("Alınan Veri:", received_message)
