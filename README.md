-------------------------------------------------------ED TEMA_1 ----------------------------------------

Nume Chelu Madalina-Lavinia
initialaNume = C
codAscii = 67 (67 % 4 = 3)
circuitStudiat = 3 ( Circuit RC serie cu intrare pe rezistenta, iesire pe condensator legat la Vcc

---------------------------------------------------------------------------------------------------------



-------------------------------------------------------OBS-----------------------------------------------



Pentru functia Euler am folosit functia math.exp() din biblioteca math.
In plus, am importat si pyplot din biblioteca matplotlib pentru a
putea realiza graficele folosind direct Python.


Functia main primeste ca parametru cazul pe care sa il execute (1 sau 2).
Pentru ambele cazuri am folosit o functie care primeste ca parametrii R, C
si un sufix pentru numele fisierului in care vor fi scrise valorile obtinute.
In acest fel voi obtine fisiere diferite pentru cele doua cazuri.

Functia calculeazaVout este partea principala din proiect, fiind cea fiecare
calculeaza tensiunea in timp pentru circuitul RC.

Am ales ca timp, T = 1000 milisecunde, iar tensiunea E de 5V.
Vectorul t contine 1000 de elemente din intervalul [0.001, 1.0] secunde.
Astfel, la fiecare timp din vectorul t este calculata tensiunea de iesire (Vo).

Pentru a putea simula o perioada de timp din care jumatate Vi = E V, iar
iar cealalta jumatate Vi = 0V, am ales sa folosesc modulo 300. Astfel,
fiecare 300 de elemente din vectorul t reprezinta o perioada in fiecare
semnalul creste si descreste. Mai departe, pentru a sti daca sunt
pe front crescator sau descrescator, verific daca rezultatul modului
este mai mic decat 150 (front crescator) sau mai are decat 150 (front descrescator).

Toate valorile pentru Vo calculate sunt scrise in vectorul v.

In final, atat vectorul t, cat si vectorul v sunt scrise in fisiere separate.

***Ploatarea a fost facuta folosind Python

----------------------------------------------------------------------------------------------------------
