from PIL import ImageFont, Image, ImageDraw
import os
import sys

try:

    '''путь сохранения введенный во время запуска скрипта'''
    output_dirname = str(sys.argv[1]) + '/'

except:

    '''путь сохранения по умолчанию'''
    output_dirname = 'output-images/'

'''полный путь истинных данных'''
input_dirname = os.path.dirname(os.path.abspath(__file__))

try:
    '''создание папки сохранения'''
    os.mkdir(output_dirname)

except FileExistsError:
    print("Directory ", output_dirname, " already exists")

'''массив исходных файлов'''
files_list = os.listdir(input_dirname + "/source-images")

for file in files_list:
    '''определение формата файла'''
    if file.endswith(".jpg"):

        '''загрузка изображения'''
        img = Image.open(input_dirname + "/source-images/" + file)

        '''определение размеров изображения'''
        width,height=img.size


        '''определения объекта рисования'''
        draw = ImageDraw.Draw(img)

        '''подпись на изображении'''
        text ='©' + file.title().split('.')[0].replace('-',' ')


        '''определение шрифта'''
        font = ImageFont.truetype('Pacifico-Regular.ttf', 30)

        '''определение размеров текста'''
        text_w, text_h = draw.textsize(text, font)

        '''определяете положение текста на картинке'''
        text_position = (width-text_w, height-text_h)

        '''цвет текста, RGB'''
        text_color = (255, 255, 255)





        '''добавление текста'''
        draw.text(text_position, text, text_color, font)

        '''сохранение нового изображения'''
        img.save(output_dirname + file)
