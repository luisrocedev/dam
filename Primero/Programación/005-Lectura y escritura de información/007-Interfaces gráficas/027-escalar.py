from PIL import Image

imagencargada = Image.open('marcas.jpg')

escalada = imagencargada.resize((1920,1080))

width, height = 1920, 1080

imagen = Image.new(
    'RGB',
    (width, height),
    color=(255, 0, 0)
    )

imagen.paste(
    escalada,
    (0,0)
    )

ruta = 'imagenes/imagen.jpg'

imagen.save(ruta)
