#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <libusb-1.0/libusb.h>

#define VENDOR_ID 0x1234 // USB cihazının üretici kimliği (örneğin)
#define PRODUCT_ID 0x5678 // USB cihazının ürün kimliği (örneğin)

int main() {
    libusb_context *context = NULL;
    libusb_device_handle *dev_handle = NULL;

    // LibUSB'yi başlatın
    if (libusb_init(&context) != 0) {
        fprintf(stderr, "LibUSB başlatma hatası\n");
        return 1;
    }

    // USB cihazını açın (belirtilen VENDOR_ID ve PRODUCT_ID ile)
    dev_handle = libusb_open_device_with_vid_pid(context, VENDOR_ID, PRODUCT_ID);
    if (dev_handle == NULL) {
        fprintf(stderr, "USB cihazı bulunamadı veya açılamadı\n");
        libusb_exit(context);
        return 1;
    }

    // Veri gönderme
    unsigned char data[] = "Merhaba, USB!";
    int data_length = strlen((char *)data) + 1;
    int transferred;

    if (libusb_bulk_transfer(dev_handle, 0x02, data, data_length, &transferred, 0) != 0) {
        fprintf(stderr, "Veri gönderme hatası\n");
    } else {
        printf("USB cihazına veri gönderildi: %s\n", data);
    }

    // USB cihazını kapatın ve LibUSB'yi kapatın
    libusb_close(dev_handle);
    libusb_exit(context);

    return 0;
}
