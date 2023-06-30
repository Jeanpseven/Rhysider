from PIL import Image

# Define os caracteres ASCII para diferentes tons de cinza e vermelho
ascii_chars = "@%#*+=-:. "
gray_chars = ascii_chars[::-1]  # Caracteres em ordem reversa para efeito de sombreamento
red_chars = ascii_chars[:3] + ascii_chars[-1]

def convert_image_to_ascii(image_path, width):
    image = Image.open(image_path)
    image = image.convert("RGB")
    
    # Redimensiona a imagem para o número de colunas especificado
    aspect_ratio = image.height / image.width
    height = int(width * aspect_ratio)
    image = image.resize((width, height))
    
    ascii_art = ""
    
    # Converte cada pixel da imagem em um caractere ASCII correspondente
    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            
            if r < 50:  # Tons escuros de vermelho são substituídos por caracteres em vermelho
                char = red_chars[0]
            elif r < 150:  # Tons intermediários são substituídos por caracteres em cinza
                char = gray_chars[int(r / 50)]
            else:  # Tons claros são substituídos por caracteres em branco
                char = " "
            
            ascii_art += char
        
        ascii_art += "\n"
    
    return ascii_art

# Solicita o caminho da imagem ao usuário
image_path = input("Digite o caminho da imagem: ")

# Solicita a largura da imagem ASCII desejada
width = int(input("Digite a largura desejada (em colunas): "))

# Solicita o nome do arquivo de saída
output_filename = input("Digite o nome do arquivo de saída (sem extensão): ")

# Converte a imagem para arte ASCII
ascii_art = convert_image_to_ascii(image_path, width)

# Define o nome completo do arquivo de saída com a extensão .txt
output_path = output_filename + ".txt"

# Salva a arte ASCII no arquivo de saída
with open(output_path, "w") as file:
    file.write(ascii_art)

print("Arte ASCII salva com sucesso no arquivo:", output_path)
