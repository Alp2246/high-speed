import time

# I2C Simülasyonu İçin Yardımcı Fonksiyonlar
def i2c_start_condition():
    print("I2C Start Şartı Oluşturuldu")

def i2c_stop_condition():
    print("I2C Stop Şartı Oluşturuldu")

def i2c_send_byte(data):
    print(f"Gönderilen Veri: {data}")

def i2c_receive_byte():
    received_data = 0xAA  # Simülasyon amaçlı sabit bir değer döndürdük
    print(f"Alınan Veri: {received_data}")
    return received_data

# I2C Cihazına Veri Gönderme Fonksiyonu
def i2c_send_data(device_address, data):
    i2c_start_condition()
    i2c_send_byte(device_address << 1)  # Cihaz adresini 7 bit sola kaydırıp yazma bitini ekleriz
    i2c_send_byte(data)
    i2c_stop_condition()

# I2C Cihazından Veri Alma Fonksiyonu
def i2c_receive_data(device_address):
    i2c_start_condition()
    i2c_send_byte((device_address << 1) | 0x01)  # Cihaz adresini 7 bit sola kaydırıp okuma bitini ekleriz
    received_data = i2c_receive_byte()
    i2c_stop_condition()
    return received_data

if __name__ == "__main__":
    # I2C cihazının adresi (örnek olarak 0x50)
    device_address = 0x50

    # Gönderilecek veri
    data_to_send = 0x12

    # I2C Cihazına Veri Gönderme
    print(f"I2C Cihazına Veri Gönderiliyor ({hex(device_address)}): {hex(data_to_send)}")
    i2c_send_data(device_address, data_to_send)

    # I2C Cihazından Veri Alma
    print(f"I2C Cihazından Veri Alınıyor ({hex(device_address)})")
    received_data = i2c_receive_data(device_address)
    print(f"Alınan Veri: {hex(received_data)}")
