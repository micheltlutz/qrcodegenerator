import qrcode

def generate_qr_code(link, output_file):
    # Cria a instância do QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Adiciona o link ao QRCode
    qr.add_data(link)
    qr.make(fit=True)

    # Cria a imagem do QRCode
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Salva a imagem no arquivo especificado
    img.save(output_file)

if __name__ == "__main__":
    link = "https://compasso.ninja/pls/interno/whsprogramacertificacao"
    output_file = "certificaçao.png"
    generate_qr_code(link, output_file)
    print(f"QR Code gerado e salvo como {output_file}")
