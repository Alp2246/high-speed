import time

# SPI Simülasyonu İçin Yardımcı Fonksiyonlar
def spi_select_device(device):
    print(f"SPI Cihazı Seçildi: {device}")

def spi_deselect_device(device):
    print(f"SPI Cihazı Kapatıldı: {device}")

def spi_transfer_byte(data):
    received_data = data + 1  # Simülasyon amaçlı, gönderilen veriye 1 ekleriz
    print(f"Gönderilen Veri: {data}, Alınan Veri: {received_data}")
    return received_data

# SPI Cihazına Veri Gönderme Fonksiyonu
def spi_send_data(device, data):
    spi_select_device(device)
    received_data = spi_transfer_byte(data)
    spi_deselect_device(device)
    return received_data

if __name__ == "__main__":
    # SPI cihazını seçin (örnek olarak 0x01)
    selected_device = 0x01

    # Gönderilecek veri
    data_to_send = 0x55

    # SPI Cihazına Veri Gönderme
    print(f"SPI Cihazına Veri Gönderiliyor ({hex(selected_device)}): {hex(data_to_send)}")
    received_data = spi_send_data(selected_device, data_to_send)
    print(f"SPI Cihazından Alınan Veri: {hex(received_data)}")
