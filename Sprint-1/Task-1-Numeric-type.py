# Система учёта рабочего времени сохраняет на сервере время, которое сотрудники провели в социальных сетях за месяц. 
# HR решил узнать, сколько времени тестировщик Антон листал ленту с мемами, но сервер вернул непонятное число 424562. 

# HR прочитал мануалы к системе и выяснил, что сервер сохраняет время в секундах. 
# HR обратился к вам с просьбой написать приложение, которое посредством арифметических операций переводило бы полученное число секунд в формат дни часы минуты секунды.

response = 424562

sec_in_days = 60 * 60 * 24
sec_in_hours = 60 * 60
sec_in_minutes = 60

days = response//sec_in_days
response = response % sec_in_days
hours = response//sec_in_hours
response = response % sec_in_hours
minutes = response//sec_in_minutes
response %= sec_in_minutes
seconds = response

print(days, hours, minutes, seconds)