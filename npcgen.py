from random import randint
from russian_names import RussianNames
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder



temp = ["Флегма","Сангва","Меланха","Холера"]
aug = [["Протезирование","Порт для подключения к сетевым устройствам", "Железный кулак","Стабилизатор клинка","Баллистический стабилизатор","Скрытый клинок","Дополнительный огнестрел в руках","Мышечный стабилизатор","Мышечный парализатор","Проект «Восхождение»","Фонарь","Проект «Паук»","Разрыватель материи","Укротитель замков","Помощник хирурга"],
["Глазные импланты","Вероятностный компьютер","Проект «Альманах»","Тактический анализатор","Проект «Фрейд»","Гоночный сопроцессор","Церебральный ускоритель","Проект «Адреналин»","Проект «Смотритель»","Проект «Пацифист»","Проект «Блэкаут»" ,"Удаленный доступ" ,"Удаленный доступ v1.2" ,"Проект «Марионетка»" ,"Баллистический компьютер" ,"Локальный криптободборщик" ,"Проект «Фрейд» v1.2" ,"Проект «Просвет»" ,"Проект «Ночь»" ,"Проект «След»" ,"Змеиный укус","Проект «Змея»"],
["Протезирование ","Проект «Скороход» ","Попрыгунчик" ,"Падение ангела ","Проект «Мгновение»" ,"Проект «Тихоход» ","Сканер приближения ","Проект «Повелитель» ","Скрытый клинок","Проект «Шагоход» ","Проект «Восхождение» доп. модуль","Генератор феромонов" ],
["Проект «Искра»","Радиоактивный протектор","Молниеотвод","Огнетушитель","Высокий иммунитет","Проект «Второй шанс»","Проект «Защитник»","Адреналиновый контроллер","Проект «Икар» ","Функциональный расширитель","Проект «Перехват»","Второе дыхание","Проект «Хамелеон","Активный камуфляж ","Видеокамера ","Око за око","Проект «Кокон»"]]
characters=["Храбрый","Спокойствие","Целомудренный","Прилежный","Непостоянный","Прощение","Щедрый","Общительный","Честный","Скромный","Терпеливый","Умеренный","Ревностный","Сострадательный","Гневный","Похотливый","Честолюбивый","Ленивый","Упрямый","Жадный","Застенчивый","Лживый","Высокомерный","Произвольный","Нетерпеливый","Прожорливый","Параноик","Циничный","Бездушный","Садистский"]
navs=["Холодное оружие","Огнестрельное оружие","Ближний бой"]



# def rand_temp():
#     temp_i=randint(0, len(temp)-1)
#     print("Темпераменты: ",temp[temp_i])
#
# def rand_ch():
#     print("Характеристики:")
#     l=18
#     pw=randint(1,10)
#     print("  Мощь: ",pw)
#     l-=pw
#     if l>10:
#         itl=randint(1,10)
#     else:
#         itl=randint(1, l-1)
#     print("  Скепсис: ",itl)
#     l-=itl
#     ag=randint(1, l)
#     print("  Проворство: ",ag)

class InsPanel(TabbedPanel):
    def chp(self):
        ch=""
        l=18
        pw=randint(1,10)
        ch="Мощь: "+ str(pw)
        l-=pw
        if l>10:
            itl=randint(1,10)
        else:
            itl=randint(1, l-1)
        ch+="\n  Скепсис: "+ str(itl)
        l-=itl
        ag=randint(1, l)
        ch+="\n  Проворство: "+ str(ag)
        return ch

    def navs(self,hr):
        nav=""
        if hr<3:
            for i in range(len(navs)):
                nav+="  " + navs[i]
                x=randint(1,2)
                nav+=":"+ str(x) + "\n"
        elif hr==3:
            for i in range(len(navs)):
                nav+="  " + navs[i]
                x=randint(1,3)
                nav+=": "+ str(x) + "\n"
        elif hr>3:
            for i in range(len(navs)):
                nav+="  " + navs[i]
                x=randint(1,5)
                nav+=":"+ str(x) + "\n"
        return nav


    def aug(self,hr):
        augp="  Аугментации:"
        if hr<3:
            numb=randint(0,1)
        elif hr==3:
            numb=randint(1,2)
        elif hr>3:
            numb=randint(2,4)

        if numb == 0:
            augp+="Не найдены"
        else:

            for i in range(numb):
                part=randint(0, len(aug)-1)
                if part == 0:
                    name = "\n   Руки: "
                elif part == 1:
                    name="\n   Голова: "
                elif part == 2:
                    name="\n   Ноги: "
                elif part == 3:
                    name="\n   Тело: "
                aug_i=randint(0, len(aug[part])-1)
                augp+= str(name) + str(aug[part][aug_i])
        return augp

    def ez(self):
        numb=randint(1,2)
        for i in range(numb):
            ch=self.chp()
            nav=self.navs(1)
            augp=self.aug(1)
            if i==0:
                self.pr.text= str(i+1)+ ". " + str(ch) + "\n --------------------------\n" + str(nav) + "--------------------------\n" + str(augp) + "\n\n =========================="
            else:
                self.pr.text+= "\n" + "\n" + str(i+1) + ". " + str(ch) + "\n --------------------------\n" + str(nav) + "--------------------------\n" + str(augp) + "\n\n =========================="

    def light(self):
        numb=randint(1,3)
        for i in range(numb):
            ch=self.chp()
            nav=self.navs(2)
            augp=self.aug(2)
            if i==0:
                self.pr.text= str(i+1)+ ". " + str(ch) + "\n --------------------------\n" + str(nav) + "--------------------------\n" + str(augp) + "\n\n =========================="
            else:
                self.pr.text+= "\n" + "\n" + str(i+1) + ". " + str(ch) + "\n --------------------------\n" + str(nav) + "--------------------------\n" + str(augp) + "\n\n =========================="

    def norm(self):
        numb=randint(1,4)
        for i in range(numb):
            ch=self.chp()
            nav=self.navs(3)
            augp=self.aug(3)
            if i==0:
                self.pr.text= str(i+1)+ ". " + str(ch) + "\n --------------------------\n" + str(nav) + "--------------------------\n" + str(augp) + "\n\n =========================="
            else:
                self.pr.text+= "\n" + "\n" + str(i+1) + ". " + str(ch) + "\n --------------------------\n" + str(nav) + "--------------------------\n" + str(augp) + "\n\n =========================="

    def hard(self):
        numb=randint(1,4)
        for i in range(numb):
            ch=self.chp()
            nav=self.navs(4)
            augp=self.aug(4)
            if i==0:
                self.pr.text= str(i+1)+ ". " + str(ch) + "\n --------------------------\n" + str(nav) + "--------------------------\n" + str(augp) + "\n\n =========================="
            else:
                self.pr.text+= "\n" + "\n" + str(i+1) + ". " + str(ch) + "\n --------------------------\n" + str(nav) + "--------------------------\n" + str(augp) + "\n\n =========================="


    def imp(self):
        numb=randint(1,5)
        for i in range(numb):
            ch=self.chp()
            nav=self.navs(5)
            augp=self.aug(5)
            if i==0:
                self.pr.text= str(i+1)+ ". " + str(ch) + "\n --------------------------\n" + str(nav) + "--------------------------\n" + str(augp) + "\n\n =========================="
            else:
                self.pr.text+= "\n" + "\n" + str(i+1) + ". " + str(ch) + "\n --------------------------\n" + str(nav) + "--------------------------\n" + str(augp) + "\n\n =========================="






    def genp(self, l):
        if l==1:
            self.ez()
        elif l==2:
            self.light()
        elif l==3:
            self.norm()
        elif l==4:
            self.hard()
        elif l==5:
            self.imp()




















class Container(TabbedPanel):
    def rand_character(self):
        numb=randint(2,4)
        for i in range(numb):
            ch=randint(0, len(characters)-1)
            if i==0:
                self.char.text=str(characters[ch])
            else:
                self.char.text+="\n" + str(characters[ch])
    def rand_aug(self):
        numb=randint(0,3)
        if numb == 0:
            self.aug.text ="Имплантов не обнаружено"
        else:
            for i in range(numb):
                part=randint(0, len(aug)-1)
                if part == 0:
                    name = "Руки: "
                elif part == 1:
                    name="Голова: "
                elif part == 2:
                    name="Ноги: "
                elif part == 3:
                    name="Тело: "
                aug_i=randint(0, len(aug[part])-1)
                if i==0:
                    self.aug.text= str(name) + str(aug[part][aug_i])
                else:
                    self.aug.text+= "\n" + str(name) + str(aug[part][aug_i])
    def rand_ch(self):
        l=18
        pw=randint(1,10)
        self.ch.text="Мощь: "+ str(pw)
        l-=pw
        if l>10:
            itl=randint(1,10)
        else:
            itl=randint(1, l-1)
        self.ch.text+="\nСкепсис: "+ str(itl)
        l-=itl
        ag=randint(1, l)
        self.ch.text+="\nПроворство: "+ str(ag)
    def rand_temp(self):
        temp_i=randint(0, len(temp)-1)
        self.temp.text = str(temp[temp_i])
    def rand_name(self):
        rn = RussianNames(count=1, patronymic=False).get_person()
        self.name.text = str(rn)
    def gen(self, *args):
        self.rand_name()
        self.rand_temp()
        self.rand_ch()
        self.rand_character()
        self.rand_aug()

class MyApp(App):
    def build(self):
        return Container()


if __name__ == "__main__":
	MyApp().run()
