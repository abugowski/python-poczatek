
# Importujemy moduł hello - jest on dostępny w tym pliku
import hello

# za pomocą kropiki możemy się odwołać do funkcji i zimiennych dostępnych w hello
hello.say_hello()
name = input("Jak się nazywasz? ")
hello.say_hello_with_name(name)