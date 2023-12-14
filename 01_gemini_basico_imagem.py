import google.generativeai as genai
import PIL.Image

genai.configure(api_key="sua-api-key")

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel('gemini-pro-vision')

img = PIL.Image.open('bob_img.png')

response = model.generate_content(img)

print("Resposta 1:", response.text)

response = model.generate_content(["Descreva a imagem e depois diga quantos animais tem nessa imagem?", img])
response.resolve()

print("Resposta da pergunta", response.text)
