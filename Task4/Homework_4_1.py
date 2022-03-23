from PIL import Image

# Проверка установленного пакета Pillow
image01 = Image.open('01.png')

# Установка последнего пакета Pillow
image02 = Image.open('02.png')

# Переключение на новое виртуальное окружение и проверка установленных пакетов
image03 = Image.open('03.png')

# Установка пакета Pillow, отличного от последней версии
# Версия 7.1.1 не установилась, так как не поддерживает Python версии 3.10
image04 = Image.open('04.png')

image01.show()
image02.show()
image03.show()
image04.show()