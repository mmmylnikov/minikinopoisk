# minikinopoisk
LPA 5, Django, week 4

## Описание задания
В качестве второго мини-проекта я предлагаю сделать свой Кинопоиск на минималках. В нём должны быть следующие возможности:

- посмотреть страницу фильма (с обложкой, названием, годом, описанием, рейтингом и жанром);
- посмотреть все фильмы с возможностью фильтровать по жанрам, рейтингу и годам;
- искать фильмы по поиковому запросу;
- добавлять новый фильм.

Несколько важных моментов.  
Во-первых, вы ещё не работали с изображениями в БД. Чтобы понакомиться с азами работы с медиа-файлами, начните [с этой страницы](https://geteml.com/ru/mail_link_tracker?hash=6rwwgeeesbgf9nzomua9p7n3szrmnntskygdnbbkgo5hrot9xfbt4j96xn5jm4zb8frcn4wkcz45snj39prieemyzfxz5fr51idy6pfo&url=aHR0cHM6Ly9kb2NzLmRqYW5nb3Byb2plY3QuY29tL2VuLzQuMi90b3BpY3MvZmlsZXMv&uid=NDgxMzEyNQ~~&ucs=d508e4aa3c7dd5f9913ecc14fb03e479) документации.  
Во-вторых, в рамках этого проекта вам придётся ещё больше верстать. Старайтесь делать фронтенд максимально простым. Наша с вами цель – познакомиться с тем, как правильно использовать Django для типичных задач веб-разработки, а не научиться дизайнить и верстать красивые фильтры.  
В-третьих, для этого мини-проекта я не готовил кода, с которого вам нужно начать. Я предлагаю вам самостоятельно начать с нуля проект на django. С этим вам поможет команда startproject. Только не забудьте удалить всё лишнее.  

## TODO
+ создать проект
+ создать апку киносервис
+ создать модель жанр
+ создать модель фильма (обложкой, названием, годом, описанием, рейтингом и жанром)
+ создать вьюху - добавить фильм (при необходимости создать форму)
+ наполнить тестовыми данными
+ создать вьюху - фильм
+ создать вьюху фильмы (фильтр по жанру, рейтингу, году)
+ создать вьюху поиск фильма
