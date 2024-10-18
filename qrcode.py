import qrcode

def generate_qr_code(table_number):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add table number data to the QR code
    qr.add_data(f"Table {table_number}")
    qr.make(fit=True)
    
    # Create an image of the QR code
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the image to a file
    img.save(f"table_{table_number}_qr.png")
    print(f"Generated QR code for Table {table_number}: saved as table_{table_number}_qr.png")

# Generate QR codes for tables 1 to 5
for table_number in range(1, 6):
    generate_qr_code(table_number)
