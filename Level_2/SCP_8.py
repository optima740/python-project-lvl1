# ЗАЛАНИЕ 16.

"""
Оружие - сущность способная наносить урон.
Танк - является оружием, которое способно передвигаться. Мы могли бы наследовать класс «танк» от базового
класса «оружие». Но, если рассмотреть с точки зрения того, что танк – содержит оружие, то получается, что по сути,
танк - это платформа с размещенным на ней оружием (башня, пулемет). Поэтому, мы можем взять класс
«гусеничная платформа», и включить в него другой полиморфный объект - «оружие», в нашем случае – пушка.

Телефон – сущность которая способна предоставлять связь между объектами в пространстве.
Смартфон – является телефоном с рядом других функций. Мы могли бы наследовать класс «смартфон» от класса «телефон»,
расширив родительский функционал. Но также, мы можем использовать класс «мобильное электронное устройство», и включить
в него функционал класса «телефон».
"""
# ЗАДАНИЕ 17.
"""
Устройство чтения внешних накопителей – это наш General класс. Класс “DVD-ROM” является наследником нашего 
базового класса. Т. о. класс “DVD-ROM”  переопределит родительские методы, и можно утверждать, что DVD-ROM – 
это устройство чтения внешних накопителей. (отношение “is-a”) 

Также можно привести еще пример. Базовый класс “Пользователь”. От него наследуются классы “Менеджер” и “Водитель”. 
Даные классы наследники спкциализируют функционал родительского класса.
Т. о. для системы самообслуживания сотрудников предприятия, эти два класса-потомка будут являться пользователями.  
(отношение “is-a”)
"""