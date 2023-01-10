import os
import sys
import shutil
import subprocess

print(os.getcwd())
print(os.path)

#Functions
def make_directory():
    file_name = input("Введите название папки: ")
    os.mkdir(file_name)

def delete():
    choice = input("Что вы хотите удалить?\n 1. Папку\n 2. Файл\nВыберите опцию: ")
    file_name = input("Введите название: ")
    if choice == "1":
        os.rmdir(file_name)
    elif choice == "2":
        os.remove(file_name)
    else:
        print("Такого я вам не предлагал:")
        delete()

def copy():
    choice = input("Что вы хотите копировать?\n 1. Папку\n 2. Файл\nВыберите опцию: ")
    file_name = input("Введите название папки или файла: ")
    file_copy_name = input("Введите название для копии: ")
    if choice == "1":
        shutil.copytree(file_name, file_copy_name)
    elif choice == "2":
        shutil.copy(file_name, file_copy_name)
    else:
        print("Такого я вам не предлагал:")
        copy()

def check_directory():
    print("\nДиректория:")
    [print(stuff) for stuff in os.listdir()]

def check_directory_foulders():
    print("\nВсе папки в директории:")
    [print(foulder) for foulder in os.listdir() if os.path.isdir(foulder) == True]
    
def check_directory_files():
    print("\nВсе файлы в директории:")
    [print(file) for file in os.listdir() if os.path.isfile(file) == True]

def get_operating_system():
    print(f"OS: {sys.platform} ({os.name})")

def get_creator_info():
    print("Информация о создателе программы:")
    print("Алёша\n 20 годиков ")
    print("Простите пожалуйста, я не понял что тут надо выводить...")

def play_victory():
    """Оставлю коменты чтоб вы видели как я мучался. В любом случае, буду признателен если напишете ещё варианты реализации.
    UPD: Не знаю как именно вы будете проверять что это работает, учитывая что у вас нет этой директории (а оно работает) , но я решил не копировать сюда модули с прошлых уроков, оборачивать их в функции и обращаться через импорт."""
    #os.system("cd D:\Courses\Python lessons AI U\\3 | python -m cd D:\Courses\Python lessons AI U\\3\\victory")
    #os.system("cd D:\Courses\Python lessons AI U\\3 python -m victory")
    #os.system("python -m D:/Courses/Python lessons AI U/3/victory.py")
    #os.startfile("D:/Courses/Python lessons AI U/3/victory.py")
    print("\nВикторина: ")
    subprocess.call(["python", "D:\\Courses\\Python lessons AI U\\3\\victory.py"])
    #os.system("python -m victory")

def mybank_acc():
    print("\nМММ: ")
    subprocess.call(["python", "D:\\Courses\\Python lessons AI U\\4\\lesson4-functions-dz\\use_functions.py"])

def change_directory():
    """Здесь вроде все ровно получилос... Не понял почему это 'усложненное задание'."""
    try:
        text = input("Введите название новой директории: ")
        os.chdir(text)
    except Exception as ex:
        print("Упс, кто-то ошибся в синтаксисе")
        print(ex)
        change_directory()

def save_dirs():
    with open("listdir.txt", "w") as file:
        files = []
        dirs = []
        for stuff in os.listdir():
            files.append(stuff) if os.path.isfile(stuff) == True else dirs.append(stuff)
        with open("listdir.txt", "w") as file:
            file.write(f"files: {', '.join(files)}\ndirs: {', '.join(dirs)}")

def exit_func():
    global polling
    polling = False

dict_with_functions = {
    "1": make_directory, "2": delete, "3": copy,
    "4": check_directory, "5": check_directory_foulders,
    "6": check_directory_files, "7": get_operating_system,
    "8": get_creator_info, "9": play_victory, 
    "10": mybank_acc, "11": change_directory, "12": save_dirs, "13": exit_func
}

polling = True
while polling == True:
    print(
        """
        КОНСОЛЬНЫЙ ФАЙЛОВЫЙ МЕНЕДЖЕР 
        Главное меню:

        1 - создать папку;
        2 - удалить (файл/папку);
        3 - копировать (файл/папку);
        4 - просмотр содержимого рабочей директории;
        5 - посмотреть только папки;
        6 - посмотреть только файлы;
        7 - просмотр информации об операционной системе;
        8 - создатель программы;
        9 - играть в викторину;
        10 - мой банковский счет;
        11 - смена рабочей директории (*необязательный пункт);
        12 - сохранить содержимое рабочей директории в файл
        13 - выход
        """
    )

    choice = input("Выберите действие: ")
    if 1> int(choice) >12:
        print("Такой команды не существует!")


    dict_with_functions[choice]()
