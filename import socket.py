import socket

# Hedef IP adresi ve port numarası
target_ip = "192.168.1.100"
target_port = 12345

# Veri gönderilecek metin
data_to_send = "Merhaba, Ethernet!"

# Ethernet ile veri gönderme fonksiyonu
def send_ethernet_data(ip, port, data):
    try:
        # Soket oluşturma
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Hedef IP adresi ve port numarasına bağlanma
        client_socket.connect((ip, port))

        # Veriyi gönderme
        client_socket.send(data.encode())

        # Soketi kapatma
        client_socket.close()
        print("Veri Ethernet ile başarıyla gönderildi.")
    except Exception as e:
        print(f"Hata: {str(e)}")

if __name__ == "__main__":
    print(f"Hedef IP Adresi: {target_ip}")
    print(f"Hedef Port Numarası: {target_port}")
    print(f"Gönderilen Veri: {data_to_send}")

    # Ethernet ile veri gönderme işlemi
    send_ethernet_data(target_ip, target_port, data_to_send)
