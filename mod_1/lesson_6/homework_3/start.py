import input_values
import calculations.calc

initial_value = input_values.input_value("Podaj inicjalną wartość lokaty ")
percentage = input_values.input_percentage("Podaj oprocentowanie ")
years = input_values.input_years("Podaj okres w latach ")

final_value = calculations.calc.locate_value(initial_value, percentage, years)

print(f"Wartość lokaty po {years} latach, będzie wynosić {final_value:.2f}")