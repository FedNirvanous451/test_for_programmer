# НЕ МЕНЯТЬ
from tkinter import *
window = Tk()
window.title("test for programmer")
window['bg'] = "DeepSkyBlue2"
way = ''
img1 = PhotoImage(file="python_logo.png")
img2 = PhotoImage(file="web_designer.png")
img3 = PhotoImage(file="sys_admin.png")
img4 = PhotoImage(file="anal_d.png")
img5 = PhotoImage(file="tester.png")


def one():
    def select_level():
        global way
        way += str(choice_1.get())
    global way
    choice_1 = IntVar()
    label_one = Label(text="Вопрос 1.\nБлизкие знают вас, как человека: ", font=("Arial", 18), bg="DeepSkyBlue2")
    label_one.place(x = 500, y = 100)
    radio_1_1 = Radiobutton(window, text="Творческого и разностороннего", variable=choice_1, command=select_level, value=1)
    radio_1_1.place(x = 500, y = 200)
    radio_1_2 = Radiobutton(window, text="Пунктуального и коммуникабельного", variable=choice_1, command=select_level, value=2)
    radio_1_2.place(x = 500, y = 250)
    radio_1_3 = Radiobutton(window, text="Терпеливого и логичного", variable=choice_1, command=select_level, value=3)
    radio_1_3.place(x = 500, y = 300)
    radio_1_4 = Radiobutton(window, text="Осмотрительного и внимательного", variable=choice_1, command=select_level, value=4)
    radio_1_4.place(x = 500, y = 350)
    def two():
        global way
        def select_level():
            global way
            way += str(choice_2.get())
        choice_2 = IntVar()
        label_two = Label(text="Вопрос 2.\nЧто для Вас программирование? ", font=("Arial", 18), bg="DeepSkyBlue2")
        label_two.place(x = 500, y = 100)
        radio_2_1 = Radiobutton(window, text="Возможность самовыражаться", variable=choice_2, command=select_level, value=1)
        radio_2_1.place(x = 500, y = 200)
        radio_2_2 = Radiobutton(window, text="Перспективная сфера деятельности", variable=choice_2, command=select_level, value=2)
        radio_2_2.place(x = 500, y = 250)
        radio_2_3 = Radiobutton(window, text="То, в чем я действительно хорош(а)", variable=choice_2, command=select_level, value=3)
        radio_2_3.place(x = 500, y = 300)
        radio_2_4 = Radiobutton(window, text="Возможность заниматься любимым делом", variable=choice_2, command=select_level, value=4)
        radio_2_4.place(x = 500, y = 350)
        def three():
            global way
            def select_level():
                global way
                way += str(choice_3.get())
            choice_3 = IntVar()
            label_three = Label(text="Вопрос 3.\nКакой предмет привлекает вас больше других? ", font=("Arial", 18), bg="DeepSkyBlue2")
            label_three.place(x = 500, y = 100)
            radio_3_1 = Radiobutton(window, text="Изобразительное искусство", variable=choice_3, command=select_level, value=1)
            radio_3_1.place(x = 500, y = 200)
            radio_3_2 = Radiobutton(window, text="Математика", variable=choice_3, command=select_level, value=2)
            radio_3_2.place(x = 500, y = 250)
            radio_3_3 = Radiobutton(window, text="Технология", variable=choice_3, command=select_level, value=3)
            radio_3_3.place(x = 500, y = 300)
            radio_3_4 = Radiobutton(window, text="Проектная деятельность", variable=choice_3, command=select_level, value=4)
            radio_3_4.place(x = 500, y = 350)
            def four():
                global way
                def select_level():
                    global way
                    way += str(choice_4.get())
                choice_4 = IntVar()
                label_four = Label(text="Вопрос 4.\nА как у вас с воображением? ", font=("Arial", 18), bg="DeepSkyBlue2")
                label_four.place(x = 500, y = 100)
                radio_4_1 = Radiobutton(window, text="Отлично!", variable=choice_4, command=select_level, value=1)
                radio_4_1.place(x = 500, y = 200)
                radio_4_2 = Radiobutton(window, text="Хорошо визуализирую, но редко могу придумать что-то сам(а)", variable=choice_4, command=select_level, value=2)
                radio_4_2.place(x = 500, y = 250)
                radio_4_3 = Radiobutton(window, text="Не очень, но мне это не мешает", variable=choice_4, command=select_level, value=3)
                radio_4_3.place(x = 500, y = 300)
                def five():
                    global way
                    
                    
                    dict_answers = {"1111": "Веб-дизайнер",
                    "1113": "Веб-дизайнер",
                    "1131": "Веб-дизайнер",
                    "1132": "Веб-дизайнер",
                    "1142": "Веб-дизайнер",
                    "1211": "Веб-дизайнер",
                    "1213": "Веб-дизайнер",
                    "1222": "Веб-дизайнер",
                    "1231": "Веб-дизайнер",
                    "1233": "Веб-дизайнер",
                    "1242": "Веб-дизайнер",
                    "1311": "Веб-дизайнер",
                    "1313": "Веб-дизайнер",
                    "1321": "Веб-дизайнер",
                    "1322": "Веб-дизайнер",
                    "1343": "Веб-дизайнер",
                    "1441": "Веб-дизайнер",
                    "1443": "Веб-дизайнер",
                    "1432": "Веб-дизайнер",
                    "1421": "Веб-дизайнер",
                    "1423": "Веб-дизайнер",
                    "1411": "Веб-дизайнер",
                    "1412": "Веб-дизайнер",
                    "1413": "Веб-дизайнер",
                    "2211": "Веб-дизайнер",
                    "2411": "Веб-дизайнер",
                    "4411": "Веб-дизайнер",
                    "4412": "Веб-дизайнер",
                    "4413": "Веб-дизайнер",
                    "4443": "Веб-дизайнер",
                    "4233": "Веб-дизайнер",
                    "1112": "Аналитик данных",
                    "1121": "Аналитик данных",
                    "1122": "Аналитик данных",
                    "1123": "Аналитик данных",
                    "1133": "Аналитик данных",
                    "1143": "Аналитик данных",
                    "1141": "Аналитик данных",
                    "1212": "Аналитик данных",
                    "1221": "Аналитик данных",
                    "1223": "Аналитик данных",
                    "1232": "Аналитик данных",
                    "1241": "Аналитик данных",
                    "1243": "Аналитик данных",
                    "1312": "Аналитик данных",
                    "1313": "Аналитик данных",
                    "1323": "Аналитик данных",
                    "1331": "Аналитик данных",
                    "1341": "Аналитик данных",
                    "1342": "Аналитик данных",
                    "1431": "Аналитик данных",
                    "1433": "Аналитик данных",
                    "1422": "Аналитик данных",
                    "2111": "Аналитик данных",
                    "2112": "Аналитик данных",
                    "2113": "Аналитик данных",
                    "2121": "Аналитик данных",
                    "2122": "Аналитик данных",
                    "2123": "Аналитик данных",
                    "2142": "Аналитик данных",
                    "2213": "Аналитик данных",
                    "2221": "Аналитик данных",
                    "2222": "Аналитик данных",
                    "2231": "Аналитик данных",
                    "2232": "Аналитик данных",
                    "2242": "Аналитик данных",
                    "2243": "Аналитик данных",
                    "2311": "Аналитик данных",
                    "2312": "Аналитик данных",
                    "2322": "Аналитик данных",
                    "2332": "Аналитик данных",
                    "2341": "Аналитик данных",
                    "2342": "Аналитик данных",
                    "2343": "Аналитик данных",
                    "2413": "Аналитик данных",
                    "2423": "Аналитик данных",
                    "2431": "Аналитик данных",
                    "2432": "Аналитик данных",
                    "2441": "Аналитик данных",
                    "2442": "Аналитик данных",
                    "2443": "Аналитик данных",
                    "1333": "Системный администратор",
                    "1332": "Системный администратор",
                    "2131": "Системный администратор",
                    "2132": "Системный администратор",
                    "2133": "Системный администратор",
                    "2141": "Системный администратор",
                    "2143": "Системный администратор",
                    "2223": "Системный администратор",
                    "2233": "Системный администратор",
                    "2241": "Системный администратор",
                    "2313": "Системный администратор",
                    "2321": "Системный администратор",
                    "2323": "Системный администратор",
                    "2331": "Системный администратор",
                    "2412": "Системный администратор",
                    "2421": "Системный администратор",
                    "2422": "Системный администратор",
                    "2433": "Системный администратор",
                    "3222": "Системный администратор",
                    "3112": "Системный администратор",
                    "3121": "Системный администратор",
                    "3122": "Системный администратор",
                    "3123": "Системный администратор",
                    "3131": "Системный администратор",
                    "3133": "Системный администратор",
                    "3141": "Системный администратор",
                    "3211": "Системный администратор",
                    "3212": "Системный администратор",
                    "3221": "Системный администратор",
                    "3223": "Системный администратор",
                    "3231": "Системный администратор",
                    "3311": "Системный администратор",
                    "3312": "Системный администратор",
                    "3313": "Системный администратор",
                    "3321": "Системный администратор",
                    "3322": "Системный администратор",
                    "3331": "Системный администратор",
                    "3333": "Системный администратор",
                    "3342": "Системный администратор",
                    "3343": "Системный администратор",
                    "3411": "Системный администратор",
                    "3412": "Системный администратор",
                    "3422": "Системный администратор",
                    "3423": "Системный администратор",
                    "3431": "Системный администратор",
                    "3443": "Системный администратор",
                    "4123": "Системный администратор",
                    "4132": "Системный администратор",
                    "4143": "Системный администратор",
                    "4212": "Системный администратор",
                    "4221": "Системный администратор",
                    "4313": "Системный администратор",
                    "4321": "Системный администратор",
                    "4323": "Системный администратор",
                    "4331": "Системный администратор",
                    "4332": "Системный администратор",
                    "4423": "Системный администратор",
                    "2333": "Тестировщик",
                    "3111": "Тестировщик",
                    "3113": "Тестировщик",
                    "3132": "Тестировщик",
                    "3143": "Тестировщик",
                    "3142": "Тестировщик",
                    "3213": "Тестировщик",
                    "3232": "Тестировщик",
                    "3233": "Тестировщик",
                    "3241": "Тестировщик",
                    "3242": "Тестировщик",
                    "3243": "Тестировщик",
                    "3323": "Тестировщик",
                    "3332": "Тестировщик",
                    "3341": "Тестировщик",
                    "3413": "Тестировщик",
                    "3432": "Тестировщик",
                    "3433": "Тестировщик",
                    "3441": "Тестировщик",
                    "3442": "Тестировщик",
                    "4111": "Тестировщик",
                    "4112": "Тестировщик",
                    "4113": "Тестировщик",
                    "4121": "Тестировщик",
                    "4122": "Тестировщик",
                    "4131": "Тестировщик",
                    "4133": "Тестировщик",
                    "4141": "Тестировщик",
                    "4143": "Тестировщик",
                    "4211": "Тестировщик",
                    "4213": "Тестировщик",
                    "4222": "Тестировщик",
                    "4223": "Тестировщик",
                    "4231": "Тестировщик",
                    "4232": "Тестировщик",
                    "4241": "Тестировщик",
                    "4242": "Тестировщик",
                    "4243": "Тестировщик",
                    "4311": "Тестировщик",
                    "4312": "Тестировщик",
                    "4322": "Тестировщик",
                    "4333": "Тестировщик",
                    "4341": "Тестировщик",
                    "4342": "Тестировщик",
                    "4343": "Тестировщик",
                    "4421": "Тестировщик",
                    "4422": "Тестировщик",
                    "4431": "Тестировщик",
                    "4432": "Тестировщик",
                    "4433": "Тестировщик",
                    "4441": "Тестировщик",
                    "4442": "Тестировщик"} 
                    for key in dict_answers:
                        if key == way: 
                            Label(window, text=f"По результатам теста: из вас выйдет отличный {dict_answers[key]}", font=("Arial", 20), bg="DeepSkyBlue2").place(x = 270, y = 500)
                            if dict_answers[key] == "Веб-дизайнер":
                                im2 = Label(window, image=img2)
                                im2.place(x = 517, y = 100)
                            elif dict_answers[key] == "Системный администратор":
                                im3 = Label(window, image=img3)
                                im3.place(x = 410, y = 70)
                            elif dict_answers[key] == "Аналитик данных":
                                im4 = Label(window, image=img4)
                                im4.place(x = 400, y = 80)
                            elif dict_answers[key] == "Тестировщик":
                                im5 = Label(window, image=img5)
                                im5.place(x = 380, y = 80)

                    # for destroy
                    label_four.destroy()
                    radio_4_1.destroy()
                    radio_4_2.destroy()
                    radio_4_3.destroy()
                    button_choise_four.destroy()
                    button_choise_three.destroy()
                    button_choise_two.destroy()
                    button_choise_one.destroy()
                    



                button_choise_four = Button(window, text="Выбрать", font=("Arial", 18), command=five)
                button_choise_four.place(x = 600, y = 500)

                # for destroy
                label_three.destroy()
                radio_3_1.destroy()
                radio_3_2.destroy()
                radio_3_3.destroy()
                radio_3_4.destroy()

            button_choise_three = Button(window, text="Выбрать", font=("Arial", 18), command=four)
            button_choise_three.place(x = 600, y = 500)

            # for destroy
            label_two.destroy()
            radio_2_1.destroy()
            radio_2_2.destroy()
            radio_2_3.destroy()
            radio_2_4.destroy()

        button_choise_two = Button(window, text="Выбрать", font=("Arial", 18), command=three)
        button_choise_two.place(x = 600, y = 500)

        # for destroy
        label_one.destroy()
        radio_1_1.destroy()
        radio_1_2.destroy()
        radio_1_3.destroy()
        radio_1_4.destroy()

    button_choise_one = Button(window, text="Выбрать", font=("Arial", 18), command=two)
    button_choise_one.place(x = 600, y = 500)

    # for destroy
    label_text.destroy()
    button_for_start.destroy()
    im1.destroy()

label_text = Label(window, text="Здравствуйте! Это тест на определения специальности в IT-сфере!\nНажимайте 'Начать тест' и переходите к выполнению!",
font=("Arial", 18), bg="DeepSkyBlue2")
label_text.place(x = 275, y = 70)

im1 = Label(window, image=img1)
im1.place(x = 500, y = 150)

button_for_start = Button(window, text="Начать тест!", font=("Arial", 18), command=one)
button_for_start.place(x = 540, y = 500)
window.mainloop()

