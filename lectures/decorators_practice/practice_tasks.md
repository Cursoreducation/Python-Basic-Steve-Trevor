Decorators:

1. Для того щоб подолати шлях від New Jersey до New York, потрібно проїхатися по платному мосту, 
   який автоматично списує кошти з людини яка має відповідну мітку. Створіть декоратор Fare, та 
   застосуйте його до функції bridge, по якій їздять люди Person. За проїзд мостом в них віднімаються 
   кошти, якщо їх достатньо та якщо в них присутня мітка. Якщо мітки немає, але грошей достатньо для 
   оплати проїзду та покупки мітки, зробіть це, в іншому випадку PassageProhibited exception не дасть 
   людині переїхати міст!

2. Створіть декоратор (Timer), який засікає час роботу функції. 
   Для створення декоратора використайте class, а не function.
   
   def __init__(self, func): self.function = func
   def __call__(self, *args, **kwargs):

# adding a decorator to the function

```
@Timer
def some_function(delay): 
    from time import sleep 

    # Introducing some time delay to  
    # simulate a time taking function. 
    sleep(delay) 

some_function(3)
```

3. recursion + factorial Напишіть функцію, яка рекурсивно рахує факторіал, 
   а заодно декоратор, який перевіряє чи вхідне значення ціле та позитивне число:

```
def argument_test_natural_number(f):
    # check is arg to f is int and > 0, raise error otherwise
```

4. Напишіть програму, яка виводить частину послідовності 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 .... 
   На вхід приймається значення n - кількість елементів послідовності, які мають бути виведенні

    Наприклад, якщо n = 7, то програма має вивести 1 2 2 3 3 3 4. Sample Input:
    7 Sample Output:
    1 2 2 3 3 3 4
   
   Напишіть декоратор який виведе результат як str.

5. Напишіть декоратор logger який буде зберігати логи у файлі, шлях до файлу можна 
   вказувати як аргумент до декоратора.  
      @logger()
      def myfunc1():
          pass
   
      myfunc1()
   
      # Output: myfunc1 finished
      # File out.log created and contain the output
      
      @logger(logfile='func2.log')
      def myfunc2():
          pass
   
      myfunc2()
   
      # Output: myfunc1 finished
      # File func2.log created and contain the output

6. Напишіть декоратор який буде перейменовувавти вихідний файл функції яка створює цей файл.
    @rename('test1.txt')
    def create_file():
        file_name = "copy.txt"
        file = open(file_name, "w")
        file.write("Your text goes here")
        file.close()
        return file_name
